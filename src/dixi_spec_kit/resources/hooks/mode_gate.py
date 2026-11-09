"""DIXI control: destructive commands are blocked while MODE is prod (PreToolUse on Bash).

With MODE = prod: rm -rf outside temporary folders, forced pushes, git reset --hard on main/master,
infrastructure apply/destroy (terraform, tofu, pulumi, cdk), kubectl delete/apply/replace and
SQL DROP/TRUNCATE through database clients. With any other MODE, everything is allowed.
Exit 0 allows; exit 2 blocks with the reason on stderr. Unreadable input blocks.
Standard library only; installed by `dixi init --controls`.
"""
import json
import os
from pathlib import Path
import re
import shlex
import subprocess
import sys

OPERATORS = {"&&", "||", ";", "|", "&", "\n"}
SHELLS = {"bash", "sh", "zsh", "dash"}
TEMPORARY = {"tmp", ".tmp", "build", "dist", ".cache", "node_modules", "__pycache__", "coverage", "target"}
DATABASES = {"psql", "mysql", "mariadb", "sqlite3", "sqlcmd", "mongosh", "cockroach", "clickhouse-client"}
SQL = re.compile(r"\b(drop|truncate)\b", re.IGNORECASE)
INFRA = {"terraform": {"apply", "destroy"}, "tofu": {"apply", "destroy"}, "pulumi": {"up", "destroy"},
         "cdk": {"deploy", "destroy"}}


def block(reason):
    print(f"DIXI mode_gate: {reason}", file=sys.stderr)
    sys.exit(2)


def load():
    try:
        data = json.load(sys.stdin)
    except (ValueError, UnicodeDecodeError):
        return None
    return data if isinstance(data, dict) else None


def split(command):
    lexer = shlex.shlex(command, posix=True, punctuation_chars=True)
    lexer.whitespace_split = True
    try:
        words = list(lexer)
    except ValueError:
        words = command.split()
    segments, current = [], []
    for word in words:
        if word in OPERATORS or (word and set(word) <= set("&|;")):
            if current:
                segments.append(current)
            current = []
        else:
            current.append(word)
    if current:
        segments.append(current)
    return segments


def simple_commands(command, depth=0):
    for words in split(command):
        while words and (words[0] in ("env", "sudo", "command", "exec", "nohup", "time")
                         or re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*=.*", words[0])):
            words = words[1:]
        if not words:
            continue
        if depth < 3 and words[0] in SHELLS and "-c" in words[:-1]:
            yield from simple_commands(words[words.index("-c") + 1], depth + 1)
        elif depth < 3 and words[0] == "eval":
            yield from simple_commands(" ".join(words[1:]), depth + 1)
        else:
            yield words


def temporary(target):
    if target.startswith(("/", "~")) or ".." in Path(target).parts:
        return False
    parts = [p for p in Path(target).parts if p not in (".", "")]
    return bool(parts) and parts[0] in TEMPORARY


def current_branch(root):
    try:
        result = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=root,
                                capture_output=True, text=True, timeout=20)
    except (OSError, subprocess.SubprocessError):
        return None
    return result.stdout.strip() if result.returncode == 0 else None


def reason(words, root):
    program, rest = Path(words[0]).name, words[1:]
    sub = rest[0] if rest else ""
    if program == "rm":
        flags = "".join(w.lstrip("-") for w in rest if w.startswith("-") and not w.startswith("--"))
        recursive = "r" in flags.lower() or "--recursive" in rest
        force = "f" in flags or "--force" in rest
        targets = [w for w in rest if not w.startswith("-")]
        if recursive and force and not all(temporary(t) for t in targets):
            return "rm -rf outside temporary folders"
    if program == "git" and sub == "push" and any(
            w in ("-f", "--force", "--force-with-lease") or w.startswith(("--force", "+")) for w in rest[1:]):
        return "a forced push"
    if program == "git" and sub == "reset" and "--hard" in rest and current_branch(root) in ("main", "master", None):
        return "git reset --hard on a shared branch"
    if program in INFRA and sub in INFRA[program]:
        return f"{program} {sub}"
    if program == "kubectl" and sub in ("delete", "apply", "replace"):
        return f"kubectl {sub}"
    if program in DATABASES and SQL.search(" ".join(rest)):
        return "SQL DROP or TRUNCATE"
    return None


def main():
    data = load()
    if data is None:
        block("cannot read the hook input; refusing to be safe.")
    if data.get("tool_name") != "Bash":
        return
    tool_input = data.get("tool_input")
    command = tool_input.get("command") if isinstance(tool_input, dict) else None
    if not isinstance(command, str):
        block("the hook input has no command; refusing to be safe.")
    root = Path(os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd") or os.getcwd())
    try:
        mode = (root / "MODE").read_text(encoding="utf-8").strip()
    except OSError:
        mode = ""
    if mode != "prod":
        return
    for words in simple_commands(command):
        found = reason(words, root)
        if found:
            block(f"{found} is blocked while MODE is prod. Ask the person for explicit confirmation; "
                  "they run it themselves if it is intended.")


if __name__ == "__main__":
    main()
