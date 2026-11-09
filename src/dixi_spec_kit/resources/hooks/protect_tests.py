"""DIXI control: an agent never edits a committed test (PreToolUse on edit tools).

Committed test = the path exists in HEAD. Tests not yet committed can be written (tests first).
The person may allow edits by launching the agent with DIXI_ALLOW_TEST_EDITS=1.
Reads Claude Code input (Edit, Write, MultiEdit, NotebookEdit) and Codex input (apply_patch).
Exit 0 allows; exit 2 blocks with the reason on stderr. Unreadable input blocks.
Standard library only; installed by `dixi init --controls`.
"""
import json
import os
from pathlib import Path
import re
import subprocess
import sys

TEST = re.compile(r"(^|/)(tests?|__tests__|spec)/|(^|/)test_[^/]*$|_test\.[^/]+$|\.(test|spec)\.[^/]+$|\.feature$")
PATCH = re.compile(r"^\*\*\* (?:Add File|Update File|Delete File|Move to): (.+?)\s*$", re.MULTILINE)


def block(reason):
    print(f"DIXI protect_tests: {reason}", file=sys.stderr)
    sys.exit(2)


def load():
    try:
        data = json.load(sys.stdin)
    except (ValueError, UnicodeDecodeError):
        return None
    return data if isinstance(data, dict) else None


def targets(data):
    tool_input = data.get("tool_input")
    if not isinstance(tool_input, dict):
        return None
    if data.get("tool_name") == "apply_patch":
        patch = tool_input.get("command") or tool_input.get("input") or tool_input.get("patch")
        return PATCH.findall(patch) if isinstance(patch, str) else None
    path = tool_input.get("file_path") or tool_input.get("notebook_path") or tool_input.get("path")
    return [path] if isinstance(path, str) and path else None


def committed(root, relative):
    try:
        result = subprocess.run(["git", "cat-file", "-e", f"HEAD:{relative}"], cwd=root,
                                capture_output=True, timeout=20)
    except (OSError, subprocess.SubprocessError):
        return False
    return result.returncode == 0


def main():
    if os.environ.get("DIXI_ALLOW_TEST_EDITS") == "1":
        return
    data = load()
    if data is None:
        block("cannot read the hook input; refusing the edit to be safe.")
    paths = targets(data)
    if paths is None:
        block("the hook input has no file path; refusing the edit to be safe.")
    root = Path(os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd") or os.getcwd()).resolve()
    for raw in paths:
        path = Path(raw)
        if path.is_absolute():
            try:
                path = path.resolve().relative_to(root)
            except ValueError:
                continue
        relative = path.as_posix()
        if TEST.search(relative) and committed(root, relative):
            block(f"{relative} is a committed test. Committed tests are frozen: change the code, not the test. "
                  "If the test itself is wrong, stop and explain it to the person; only they can allow the edit "
                  "(DIXI_ALLOW_TEST_EDITS=1).")


if __name__ == "__main__":
    main()
