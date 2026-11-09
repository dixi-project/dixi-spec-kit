"""DIXI control: an agent does not read secrets (PreToolUse on Bash, Read, Grep).

Blocks .env* files (except .env.example, .env.sample, .env.template, .env.dist), private keys,
.aws/ and .ssh/ folders and credential files, also when reached through shell commands.
A hook can be evaded: it is a second layer, never the last one.
Exit 0 allows; exit 2 blocks with the reason on stderr. Unreadable input blocks.
Standard library only; installed by `dixi init --controls`.
"""
import json
import re
import shlex
import sys

SAFE = {".env.example", ".env.sample", ".env.template", ".env.dist"}
KEYS = {"id_rsa", "id_ed25519", "id_ecdsa", "id_dsa", "credentials"}
EXTENSIONS = (".pem", ".key", ".p12", ".pfx")
SHELLS = {"bash", "sh", "zsh", "dash"}


def block(reason):
    print(f"DIXI guard_secrets: {reason}", file=sys.stderr)
    sys.exit(2)


def load():
    try:
        data = json.load(sys.stdin)
    except (ValueError, UnicodeDecodeError):
        return None
    return data if isinstance(data, dict) else None


def sensitive(token):
    name = token.strip("'\"<>|&;()")
    if not name:
        return False
    parts = [part.lower() for part in re.split(r"[\\/]", name) if part]
    if not parts:
        return False
    base = parts[-1]
    if base in SAFE:
        return False
    return (base.startswith(".env") or base in KEYS or base.endswith(EXTENSIONS)
            or ".aws" in parts or ".ssh" in parts)


def tokens(command, depth=0):
    try:
        words = shlex.split(command)
    except ValueError:
        words = command.split()
    found = []
    for index, word in enumerate(words):
        found.append(word)
        if depth < 3 and (" " in word or ";" in word) and index and (
                words[index - 1] == "-c" or words[0] in SHELLS or words[0] == "eval"):
            found.extend(tokens(word, depth + 1))
    return found


def main():
    data = load()
    if data is None:
        block("cannot read the hook input; refusing to be safe.")
    tool = data.get("tool_name")
    tool_input = data.get("tool_input")
    if tool not in ("Bash", "Read", "Grep"):
        return
    if not isinstance(tool_input, dict):
        block("the hook input has no tool input; refusing to be safe.")
    if tool == "Bash":
        command = tool_input.get("command")
        if not isinstance(command, str):
            block("the hook input has no command; refusing to be safe.")
        candidates = tokens(command)
    elif tool == "Read":
        path = tool_input.get("file_path")
        if not isinstance(path, str):
            block("the hook input has no file path; refusing to be safe.")
        candidates = [path]
    else:
        candidates = [value for value in (tool_input.get("path"), tool_input.get("glob")) if isinstance(value, str)]
    for candidate in candidates:
        if sensitive(candidate):
            block(f"{candidate.strip()} looks like a secret (.env, key or credentials). Agents do not read secrets; "
                  "ask the person for the non-secret value you need, or use a template such as .env.example.")


if __name__ == "__main__":
    main()
