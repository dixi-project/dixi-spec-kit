"""Generate the subagent reference: `python3 scripts/build-subagent-reference.py [--check] [--output <folder>]`.

Standard library only. Writes `docs/subagents.md` (English) and `docs/subagents.es.md` (Spanish) from the packaged
Claude Code subagent files, so the page cannot drift: what each subagent is for, what it does, what it delivers
and its limits are copied from the file the kit installs. `--check` exits with 1 when a page is missing or out of
date. Headings and the introduction come from `scripts/site/<lang>.json`.
"""
import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
AGENTS = ROOT / "src/dixi_spec_kit/resources/claude"
OUTPUT = ROOT / "docs"
LANGUAGES = {"en": ".md", "es": ".es.md"}
SECTIONS = {"en": ("What you do", "What you deliver", "Limits"), "es": ("Qué haces", "Qué entregas", "Límites")}
# The order in which a task goes through them; a subagent added later is listed after these.
ORDER = ("dixi-architect", "dixi-tester", "dixi-developer", "dixi-reviewer")


def names():
    found = sorted(path.stem for path in (AGENTS / "en/agents").glob("*.md"))
    return [name for name in ORDER if name in found] + [name for name in found if name not in ORDER]


def read_agent(lang, name):
    text = (AGENTS / lang / "agents" / f"{name}.md").read_text(encoding="utf-8")
    front, _, body = text.removeprefix("---\n").partition("\n---\n")
    description = re.search(r'^description: "(.*)"$', front, re.MULTILINE).group(1)
    parts = re.split(r"^## (.+)\n", body, flags=re.MULTILINE)
    sections = {parts[i]: parts[i + 1].strip() for i in range(1, len(parts), 2)}
    return description, [sections[heading] for heading in SECTIONS[lang]]


def page(lang, strings):
    suffix = LANGUAGES[lang]
    lines = [f"# {strings['title']}", "", f"## {strings['purpose']}", "", strings["purpose_text"], "",
             strings["generated"], "", f"## {strings['how']}", "", *strings["how_text"], ""]
    for name in names():
        description, (does, delivers, limits) = read_agent(lang, name)
        lines += [f"## `{name}`", "", description, "", strings["file"].format(name=name), "",
                  f"### {strings['does']}", "", does, "",
                  f"### {strings['delivers']}", "", delivers, "",
                  f"### {strings['limits']}", "", limits, ""]
    lines += [f"## {strings['related']}", "",
              f"- [{strings['documentation']}](documentation{suffix})",
              f"- [{strings['commands']}](commands/index{suffix})",
              f"- [{strings['controls']}](controls{suffix})"]
    return "\n".join(lines) + "\n"


def pages():
    result = {}
    for lang, suffix in LANGUAGES.items():
        strings = json.loads((ROOT / "scripts/site" / f"{lang}.json").read_text(encoding="utf-8"))["subagents"]
        result[f"subagents{suffix}"] = page(lang, strings)
    return result


def main():
    parser = argparse.ArgumentParser(description="Generate docs/subagents*.md from the packaged subagent files.")
    parser.add_argument("--check", action="store_true", help="do not write; exit with 1 when a page is not current")
    parser.add_argument("--output", type=Path, default=OUTPUT, help="folder to write or check (default: docs)")
    arguments = parser.parse_args()
    expected, output = pages(), arguments.output.resolve()
    if arguments.check:
        problems = []
        for name, text in expected.items():
            path = output / name
            if not path.is_file():
                problems.append(f"missing: {name}")
            elif path.read_text(encoding="utf-8") != text:
                problems.append(f"out of date: {name}")
        for problem in problems:
            print(problem, file=sys.stderr)
        if problems:
            print("Run: python3 scripts/build-subagent-reference.py", file=sys.stderr)
            return 1
        print(f"Subagent reference is current ({len(expected)} pages)")
        return 0
    output.mkdir(parents=True, exist_ok=True)
    for name, text in expected.items():
        (output / name).write_text(text, encoding="utf-8")
    print(f"Subagent reference written: {len(expected)} pages in {arguments.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
