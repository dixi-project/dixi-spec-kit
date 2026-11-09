"""DIXI control: an agent does not finish with `make verify` in red (Stop and SubagentStop).

Runs only when the working tree changed and the Makefile has a `verify` target. After one forced
continuation (stop_hook_active) it lets the agent stop and tells the person: a red ladder is resolved
by a human, never by trapping the agent in a loop. Unreadable input allows, for the same reason.
Timeout in seconds: DIXI_VERIFY_TIMEOUT (default 240).
Exit 0 allows; exit 2 asks the agent to keep working, with the reason on stderr.
Standard library only; installed by `dixi init --controls`.
"""
import json
import os
from pathlib import Path
import re
import subprocess
import sys


def load():
    try:
        data = json.load(sys.stdin)
    except (ValueError, UnicodeDecodeError):
        return None
    return data if isinstance(data, dict) else None


def notify(message):
    print(json.dumps({"systemMessage": f"DIXI verify_on_stop: {message}"}))


def changed(root):
    try:
        result = subprocess.run(["git", "status", "--porcelain"], cwd=root, capture_output=True, text=True,
                                timeout=30)
    except (OSError, subprocess.SubprocessError):
        return False
    return result.returncode == 0 and bool(result.stdout.strip())


def main():
    data = load()
    if data is None:
        return
    root = Path(os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd") or os.getcwd())
    try:
        makefile = (root / "Makefile").read_text(encoding="utf-8", errors="replace")
    except OSError:
        return
    if not re.search(r"^verify:", makefile, re.MULTILINE) or not changed(root):
        return
    if data.get("stop_hook_active"):
        notify("make verify was still red after one more attempt; the agent stopped. A person should look at it.")
        return
    try:
        timeout = max(1, int(os.environ.get("DIXI_VERIFY_TIMEOUT", "240")))
    except ValueError:
        timeout = 240
    try:
        result = subprocess.run(["make", "verify"], cwd=root, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        print(f"DIXI verify_on_stop: make verify did not finish in {timeout} s. Do not report the work as done; "
              "explain the situation to the person.", file=sys.stderr)
        sys.exit(2)
    except OSError:
        notify("make is not available; verification was not run.")
        return
    if result.returncode != 0:
        tail = "\n".join((result.stdout + result.stderr).strip().splitlines()[-30:])
        print("DIXI verify_on_stop: make verify is red, so the work is not done. Fix the cause (never by editing "
              f"committed tests) or explain the failure to the person.\n{tail}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
