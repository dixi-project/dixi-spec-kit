"""DIXI control: an agent never signs, attests, approves or merges for a person (PreToolUse on Bash).

Blocks Signed-off-by (commit -s/--signoff, --trailer, a trailer in -m or in the -F file, rebase/am/
cherry-pick/revert/format-patch with --signoff), `gh pr review --approve`, `gh pr merge` and ticking an
attestation checkbox through `gh pr create/edit` or `gh api`, also inside env, sudo, bash -c, eval or
command chains. The agent may commit without a sign-off; the person signs with `git rebase --signoff`.
Exit 0 allows; exit 2 blocks with the reason on stderr. Unreadable input blocks.
Standard library only; installed by `dixi init --controls`.
"""
import json
import os
from pathlib import Path
import re
import shlex
import sys

OPERATORS = {"&&", "||", ";", "|", "&", "\n"}
SHELLS = {"bash", "sh", "zsh", "dash"}
SIGNOFF = re.compile(r"signed-off-by\s*:", re.IGNORECASE)
ATTEST = re.compile(r"\[\s*[xX]\s*\].*(attest|atest)", re.IGNORECASE | re.DOTALL)


def block(reason):
    print(f"DIXI guard_attestation: {reason}", file=sys.stderr)
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
        while words and (words[0] in ("env", "sudo", "command", "exec", "nohup")
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


def option_values(words, names):
    values = []
    for index, word in enumerate(words):
        for name in names:
            if word == name and index + 1 < len(words):
                values.append(words[index + 1])
            elif word.startswith(name + "="):
                values.append(word.split("=", 1)[1])
    return values


def read_file(root, name):
    path = Path(name) if Path(name).is_absolute() else root / name
    try:
        return path.read_text(encoding="utf-8", errors="replace")[:65536]
    except OSError:
        return ""


def reason(words, root):
    program, rest = words[0], words[1:]
    sub = rest[0] if rest else ""
    if program == "git":
        if sub == "commit":
            if any(w == "--signoff" or w.startswith("--signoff=") or re.fullmatch(r"-[a-zA-Z]*s[a-zA-Z]*", w)
                   for w in rest[1:] if not w.startswith("--") or w.startswith("--signoff")):
                return "git commit with a sign-off"
            if any(SIGNOFF.search(value) for value in option_values(rest, ("--trailer",))):
                return "git commit with a Signed-off-by trailer"
            if any(SIGNOFF.search(w) for w in rest):
                return "a Signed-off-by line in the commit message"
            if any(SIGNOFF.search(read_file(root, f)) for f in option_values(rest, ("-F", "--file"))):
                return "a Signed-off-by line in the commit message file"
        if sub in ("rebase", "am", "cherry-pick", "revert", "format-patch") and (
                "--signoff" in rest or (sub != "rebase" and "-s" in rest)):
            return f"git {sub} with a sign-off"
    if program == "gh" and len(rest) >= 2:
        if rest[:2] == ["pr", "merge"]:
            return "merging a pull request"
        if rest[:2] == ["pr", "review"] and ("--approve" in rest or "-a" in rest):
            return "approving a pull request"
        if rest[:2] in (["pr", "create"], ["pr", "edit"]):
            bodies = option_values(rest, ("--body", "-b"))
            bodies += [read_file(root, f) for f in option_values(rest, ("--body-file", "-F"))]
            if any(ATTEST.search(body) for body in bodies):
                return "ticking the human attestation in a pull request"
    if program == "gh" and sub == "api" and any(ATTEST.search(w) for w in rest):
        return "ticking the human attestation through the API"
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
    for words in simple_commands(command):
        found = reason(words, root)
        if found:
            block(f"{found} is reserved to a person. Agents do not sign, attest, approve or merge. Commit without "
                  "a sign-off and ask the person to sign (git rebase --signoff) and to review and merge.")


if __name__ == "__main__":
    main()
