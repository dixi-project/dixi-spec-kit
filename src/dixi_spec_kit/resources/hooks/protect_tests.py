"""DIXI control: an agent never edits a committed test (PreToolUse on edit tools and Bash).

Committed test = a test path that exists in HEAD. Tests not yet committed can be written (tests first).
The person may allow edits by launching the agent with DIXI_ALLOW_TEST_EDITS=1.
Reads Claude Code input (Edit, Write, MultiEdit, NotebookEdit), Codex input (apply_patch) and shell
commands from both (Bash): redirections, sed/perl -i, tee, cp, mv, rm, truncate, dd and git rm/mv,
also inside env, sudo, bash -c, eval, command chains and after cd; and inline interpreter code
(python -c, heredocs, node -e, ruby/perl -e, php -r) that writes and names a committed test in quotes.
Scripts run from a file and paths built at run time are not detected: a hook is a second layer,
never the last one.
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

TEST = re.compile(r"(^|/)(tests?|__tests__|spec)/|(^|/)test_[^/]*$|_test\.[^/]+$|\.(test|spec)\.[^/]+$|\.feature$")
PATCH = re.compile(r"^\*\*\* (?:Add File|Update File|Delete File|Move to): (.+?)\s*$", re.MULTILINE)
OPERATORS = {"&&", "||", ";", "|", "&", "\n", "|&"}
SHELLS = {"bash", "sh", "zsh", "dash"}
WRAPPERS = {"env", "sudo", "command", "exec", "nohup", "time", "nice"}
IN_PLACE = {"sed", "gsed", "perl"}
REMOVERS = {"rm", "unlink", "shred", "truncate"}
COPIERS = {"cp", "mv", "install", "ln", "rsync"}
INTERPRETER = re.compile(r"(^|[\s;&|(])(python[0-9.]*|node|nodejs|deno|bun|ruby|perl|php)(?=[\s;&|)]|$)")
WRITE_CODE = re.compile(
    r"""open\([^)]*,\s*['"][^'"]*[wax+]|\.write_(text|bytes)\(|\bos\.(remove|unlink|rename|replace|truncate)\("""
    r"""|\bshutil\.(copy\w*|move|rmtree)\(|\.(unlink|rename|rmdir)\(|\b(writeFile|appendFile|rm|unlink|rename|copyFile"""
    r"""|truncate|cp)(Sync)?\(|\bFile\.(write|delete|rename|open\([^)]*['"][wa])|\bFileUtils\.|\bunlink\b|\brename\b"""
    r"""|file_put_contents|fopen\([^)]*['"][wax]""")


def block(reason):
    print(f"DIXI protect_tests: {reason}", file=sys.stderr)
    sys.exit(2)


def load():
    try:
        data = json.load(sys.stdin)
    except (ValueError, UnicodeDecodeError):
        return None
    return data if isinstance(data, dict) else None


def lex(command):
    lexer = shlex.shlex(command, posix=True, punctuation_chars=True)
    lexer.whitespace_split = True
    try:
        return list(lexer)
    except ValueError:
        return command.split()


def segments(command):
    current = []
    for word in lex(command):
        if word in OPERATORS or (word and set(word) <= set("&|;")):
            if current:
                yield current
            current = []
        else:
            current.append(word)
    if current:
        yield current


def strip_redirections(words):
    """Split a simple command into its words and the files its output redirections write."""
    plain, written = [], []
    index = 0
    while index < len(words):
        word = words[index]
        if word and set(word) <= set("<>&|") and ">" in word:
            if plain and plain[-1].isdigit():
                plain.pop()
            if index + 1 < len(words) and not words[index + 1].lstrip("&").isdigit():
                written.append(words[index + 1])
            index += 2
            continue
        if word and set(word) <= set("<"):
            index += 2
            continue
        plain.append(word)
        index += 1
    return plain, written


def operands(words):
    return [w for w in words if not w.startswith("-") or w == "-"]


def written_by(words):
    """Files that a simple command writes, moves or deletes (after wrappers are removed)."""
    if not words:
        return []
    program, rest = Path(words[0]).name, words[1:]
    if program in IN_PLACE:
        if any(w.startswith("-i") or w == "--in-place" or w.startswith("--in-place=")
               or (program == "perl" and re.fullmatch(r"-[a-zA-Z]*i\S*", w)) for w in rest):
            return operands(rest)
        return []
    if program == "tee":
        return operands(rest)
    if program in REMOVERS:
        return [w for w in operands(rest) if not (program == "truncate" and w.isdigit())]
    if program == "dd":
        return [w.split("=", 1)[1] for w in rest if w.startswith("of=")]
    if program in COPIERS:
        names = operands(rest)
        target = next((rest[i + 1] for i, w in enumerate(rest) if w in ("-t", "--target-directory")
                       and i + 1 < len(rest)), None)
        if target:
            sources = [n for n in names if n != target]
            return ([*sources] if program == "mv" else []) + [os.path.join(target, Path(s).name) for s in sources]
        if len(names) < 2:
            return []
        sources, destination = names[:-1], names[-1]
        moved = sources if program == "mv" else []
        return moved + [destination] + [os.path.join(destination, Path(s).name) for s in sources]
    if program == "git" and rest and rest[0] in ("rm", "mv"):
        return operands(rest[1:])
    return []


def shell_targets(command, cwd, depth=0):
    """Pairs (directory, path) for every file the command would write, move or delete."""
    found = []
    for words in segments(command):
        words, redirected = strip_redirections(words)
        found += [(cwd, target) for target in redirected]
        while words and (Path(words[0]).name in WRAPPERS or re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*=.*", words[0])):
            words = words[1:]
        if not words:
            continue
        program = Path(words[0]).name
        if program == "cd":
            destination = words[1] if len(words) > 1 else os.path.expanduser("~")
            cwd = Path(os.path.expanduser(destination)) if Path(os.path.expanduser(destination)).is_absolute() \
                else cwd / destination
            continue
        if depth < 3 and program in SHELLS and "-c" in words[:-1]:
            found += shell_targets(words[words.index("-c") + 1], cwd, depth + 1)
        elif depth < 3 and program == "eval":
            found += shell_targets(" ".join(words[1:]), cwd, depth + 1)
        else:
            found += [(cwd, target) for target in written_by(words)]
    return found


def interpreter_targets(command, cwd):
    """Quoted names in inline interpreter code that writes, moves or deletes files."""
    if not INTERPRETER.search(command) or not WRITE_CODE.search(command):
        return []
    names = re.findall(r"'([^'\n]{1,500})'", command) + re.findall(r'"([^"\n]{1,500})"', command)
    return [(cwd, name) for name in names if "/" in name or TEST.search(name) or name in ("tests", "test", "spec")]


def tool_targets(data, root):
    tool_input = data.get("tool_input")
    if not isinstance(tool_input, dict):
        return None
    tool = data.get("tool_name")
    if tool == "Bash":
        command = tool_input.get("command")
        if not isinstance(command, str):
            return None
        cwd = Path(data["cwd"]) if isinstance(data.get("cwd"), str) and data["cwd"] else root
        return shell_targets(command, cwd) + interpreter_targets(command, cwd)
    if tool == "apply_patch":
        patch = tool_input.get("command") or tool_input.get("input") or tool_input.get("patch")
        return [(root, p) for p in PATCH.findall(patch)] if isinstance(patch, str) else None
    path = tool_input.get("file_path") or tool_input.get("notebook_path") or tool_input.get("path")
    return [(root, path)] if isinstance(path, str) and path else None


def expand(pattern):
    """Expand shell wildcards with pathlib (absolute pattern in, existing absolute paths out)."""
    if not any(c in pattern for c in "*?["):
        return []
    path = Path(pattern)
    anchor = Path(path.anchor)
    try:
        return [str(p) for p in anchor.glob(str(path.relative_to(anchor)))]
    except (ValueError, OSError):
        return []


def relative_paths(root, cwd, raw):
    """Project-relative paths for a target, expanding ~ and wildcards; empty when outside the project."""
    raw = os.path.expanduser(raw)
    if "$" in raw:
        return []
    base = os.path.normpath(raw if os.path.isabs(raw) else os.path.join(str(cwd), raw))
    result = []
    for candidate in expand(base) or [base]:
        try:
            relative = Path(candidate).relative_to(root)
        except ValueError:
            try:
                relative = Path(candidate).resolve().relative_to(root)
            except ValueError:
                continue
        result.append(relative.as_posix())
    return result


def committed_tests(root, relative):
    """Committed test files at this path, or under it when it is a folder."""
    try:
        listing = subprocess.run(["git", "ls-tree", "-r", "--name-only", "HEAD", "--", relative], cwd=root,
                                 capture_output=True, text=True, timeout=20)
    except (OSError, subprocess.SubprocessError):
        return []
    return [n for n in listing.stdout.splitlines() if TEST.search(n)] if listing.returncode == 0 else []


def main():
    if os.environ.get("DIXI_ALLOW_TEST_EDITS") == "1":
        return
    data = load()
    if data is None:
        block("cannot read the hook input; refusing the edit to be safe.")
    root = Path(os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd") or os.getcwd()).resolve()
    if not os.environ.get("CLAUDE_PROJECT_DIR"):
        try:
            top = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=root, capture_output=True, text=True,
                                 timeout=20)
            if top.returncode == 0 and top.stdout.strip():
                root = Path(top.stdout.strip()).resolve()
        except (OSError, subprocess.SubprocessError):
            pass
    targets = tool_targets(data, root)
    if targets is None:
        block("the hook input has no file path or command; refusing the edit to be safe.")
    for cwd, raw in targets:
        for relative in relative_paths(root, cwd, raw):
            frozen = committed_tests(root, relative)
            if frozen:
                block(f"{frozen[0]} is a committed test. Committed tests are frozen: change the code, not the test. "
                      "If the test itself is wrong, stop and explain it to the person; only they can allow the edit "
                      "(DIXI_ALLOW_TEST_EDITS=1).")


if __name__ == "__main__":
    main()
