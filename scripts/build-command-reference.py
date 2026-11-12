"""Generate the command reference: `python3 scripts/build-command-reference.py [--check] [--output <folder>]`.

Standard library only. Writes one page per operation in English (`<operation>.md`) and Spanish
(`<operation>.es.md`), plus an index per language, under `docs/commands/`. Everything comes from the packaged
Claude Code command texts and the workflow graph, so the reference cannot drift: `--check` exits with 1 when a
page is missing, out of date or left over. Interface strings come from `scripts/site/<lang>.json` and the example
of each operation from `scripts/site/command-examples.json`.
"""
import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
RESOURCES = ROOT / "src/dixi_spec_kit/resources"
OUTPUT = ROOT / "docs/commands"
LANGUAGES = {"en": ".md", "es": ".es.md"}
SECTIONS = {"en": ("Goal", "Steps", "Limits", "Closing"), "es": ("Objetivo", "Pasos", "Límites", "Cierre")}
PATH = re.compile(r"(\.?[\w<>*-]+/)+[\w<>*.-]*|[\w<>*-]+\.(md|json|ya?ml)")


def read_command(lang, operation):
    text = (RESOURCES / "claude" / lang / f"dixi.{operation}.md").read_text(encoding="utf-8")
    front, _, body = text.removeprefix("---\n").partition("\n---\n")
    fields = dict(re.findall(r'^([\w-]+): "(.*)"$', front, re.M))
    parts = re.split(r"^## (.+)\n", body, flags=re.M)
    sections = {parts[i]: parts[i + 1].strip() for i in range(1, len(parts), 2)}
    goal, steps, limits, closing = (sections[name] for name in SECTIONS[lang])
    return {"description": fields["description"], "hint": fields["argument-hint"], "goal": goal, "steps": steps,
            "limits": limits, "closing": closing}


def named_paths(command):
    """Code spans that are file or folder paths, in order of appearance."""
    found = []
    for part in ("goal", "steps", "limits", "closing"):
        for span in re.findall(r"`([^`]+)`", command[part]):
            if PATH.fullmatch(span) and span not in found:
                found.append(span)
    return found


def links(operations, suffix):
    return ", ".join(f"[`/dixi.{name}`]({name}{suffix})" for name in operations)


def page(lang, operation, graph, strings, example):
    suffix, command = LANGUAGES[lang], read_command(lang, operation)
    hint = command["hint"]
    when = [f"- {strings['works_on']}: " + ", ".join(f"`{kind}`" for kind in graph[operation]["target_kinds"])]
    before = [name for name in graph if operation in graph[name]["next_operations"]]
    when.append(f"- {strings['after']}: {links(before, suffix)}" if before else f"- {strings['any_time']}")
    following = graph[operation]["next_operations"]
    files = named_paths(command)
    lines = [
        f"# /dixi.{operation}", "",
        f"## {strings['purpose']}", "",
        f"{command['description']}.", "", command["goal"], "", strings["generated"], "",
        f"## {strings['invocation']}", "",
        f"- Claude Code: `/dixi.{operation} {hint}`",
        f"- Codex: `$dixi-{operation} {hint}`",
        f"- Agent Skills: `dixi-{operation}` — {strings['skills']}", "",
        strings["arguments"].format(hint=hint), "",
        f"## {strings['example']}", "",
        f"- Claude Code: `/dixi.{operation} {example}`",
        f"- Codex: `$dixi-{operation} {example}`",
        "- Agent Skills: " + strings["example_skill"].format(operation=operation, example=example), "",
        strings["example_note"], "",
        f"## {strings['when']}", "", *when, "",
        f"## {strings['steps']}", "", command["steps"], "",
        f"## {strings['files']}", "",
        *([strings["files_intro"], "", *(f"- `{path}`" for path in files)] if files else [strings["no_files"]]), "",
        f"## {strings['stops']}", "", command["limits"], "",
        f"## {strings['closing']}", "", command["closing"], "",
        f"## {strings['next']}", "",
        *([f"- [`/dixi.{name}`]({name}{suffix})" for name in following] if following else [strings["no_next"]]), "",
        f"## {strings['related']}", "",
        f"- [{strings['index_title']}](index{suffix})",
        f"- [README](../../{'README.md' if lang == 'en' else 'README.es.md'})",
    ]
    return "\n".join(lines) + "\n"


def index(lang, graph, strings):
    suffix = LANGUAGES[lang]
    lines = [f"# {strings['index_title']}", "", f"## {strings['purpose']}", "", strings["index_purpose"], "",
             strings["generated"], "", f"## {strings['commands']}", ""]
    for operation in graph:
        lines.append(f"- [`/dixi.{operation}`]({operation}{suffix}) — {read_command(lang, operation)['description']}")
    lines += ["", f"## {strings['related']}", "", f"- [README](../../{'README.md' if lang == 'en' else 'README.es.md'})"]
    return "\n".join(lines) + "\n"


def pages():
    graph = json.loads((RESOURCES / "workflows.json").read_text(encoding="utf-8"))["operations"]
    examples = json.loads((ROOT / "scripts/site/command-examples.json").read_text(encoding="utf-8"))
    result = {}
    for lang, suffix in LANGUAGES.items():
        strings = json.loads((ROOT / "scripts/site" / f"{lang}.json").read_text(encoding="utf-8"))["reference"]
        result[f"index{suffix}"] = index(lang, graph, strings)
        for operation in graph:
            result[f"{operation}{suffix}"] = page(lang, operation, graph, strings, examples[operation][lang])
    return result


def main():
    parser = argparse.ArgumentParser(description="Generate docs/commands/ from the packaged command texts.")
    parser.add_argument("--check", action="store_true", help="do not write; exit with 1 when a page is not current")
    parser.add_argument("--output", type=Path, default=OUTPUT, help="folder to write or check (default: docs/commands)")
    arguments = parser.parse_args()
    expected, output = pages(), arguments.output.resolve()
    if arguments.check:
        present = {path.name for path in output.iterdir()} if output.is_dir() else set()
        problems = [f"missing: {name}" for name in sorted(set(expected) - present)]
        problems += [f"left over: {name}" for name in sorted(present - set(expected))]
        problems += [f"out of date: {name}" for name in sorted(set(expected) & present)
                     if (output / name).read_text(encoding="utf-8") != expected[name]]
        for problem in problems:
            print(problem, file=sys.stderr)
        if problems:
            print("Run: python3 scripts/build-command-reference.py", file=sys.stderr)
            return 1
        print(f"Command reference is current ({len(expected)} pages)")
        return 0
    output.mkdir(parents=True, exist_ok=True)
    for path in output.iterdir():
        if path.name not in expected:
            path.unlink()
    for name, text in expected.items():
        (output / name).write_text(text, encoding="utf-8")
    print(f"Command reference written: {len(expected)} pages in {arguments.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
