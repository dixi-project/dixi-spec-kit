"""Generate the CLI reference: `python3 scripts/build-cli-reference.py [--check] [--output <folder>]`.

Standard library and the package itself only. Walks the real argparse parser of `dixi` with the English and the
Spanish message catalogs and writes one page per command (`<command>.md`, `<command>.es.md`) plus an index per
language under `docs/cli/`: usage, arguments, options, subcommands and the exit codes. It reads the parser instead
of copying `--help`, whose layout changes between Python versions. `--check` exits with 1 when a page is missing,
out of date or left over. Headings and the exit-code table come from `scripts/site/<lang>.json`.
"""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from dixi_spec_kit.cli import parser_for  # noqa: E402

OUTPUT = ROOT / "docs/cli"
LANGUAGES = {"en": ".md", "es": ".es.md"}


def subcommands(parser):
    for action in parser._actions:
        if isinstance(action, argparse._SubParsersAction):
            return action.choices
    return {}


def arguments_of(parser):
    plain = [action for action in parser._actions if not isinstance(action, argparse._SubParsersAction)]
    return ([action for action in plain if not action.option_strings],
            [action for action in plain if action.option_strings])


def value(action):
    """How an option's value is written: nothing for a flag, the choices, or a placeholder."""
    if action.nargs == 0:
        return ""
    return " {" + ",".join(map(str, action.choices)) + "}" if action.choices else f" <{action.dest}>"


def usage(path, parser):
    positionals, options = arguments_of(parser)
    parts = [" ".join(path), *(f"<{action.dest}>" for action in positionals)]
    for action in options:
        if action.dest in ("help", "version"):
            continue
        text = action.option_strings[0] + value(action)
        parts.append(text if action.required else f"[{text}]")
    if subcommands(parser):
        parts.append("<command>")
    return " ".join(parts)


def describe(parser, strings):
    """Arguments and options of one parser as Markdown lines, each list under its own label."""
    positionals, options = arguments_of(parser)
    lines = []
    if positionals:
        lines += [f"**{strings['arguments']}**", ""]
        for action in positionals:
            note = f" {strings['operation_values']}" if action.dest == "operation" else ""
            lines.append(f"- `{action.dest}` — {action.help}{note}")
        lines.append("")
    lines += [f"**{strings['options']}**", ""]
    for action in options:
        names = ", ".join(f"`{name}{value(action)}`" for name in action.option_strings)
        notes = ""
        if action.required:
            notes += f" {strings['required']}"
        if action.nargs != 0 and action.default not in (None, argparse.SUPPRESS) and str(action.default) not in action.help:
            notes += f" {strings['default']}: `{action.default}`."
        lines.append(f"- {names} — {action.help}{notes}")
    return lines + [""]


def sections(parser, strings):
    """The same lists as `describe`, as second-level sections for a page's own command."""
    return [f"## {line.strip('*')}" if line.startswith("**") else line for line in describe(parser, strings)]


def command_page(lang, name, parser, strings):
    suffix, path = LANGUAGES[lang], ("dixi", name)
    lines = [f"# dixi {name}", "", f"## {strings['purpose']}", "", f"`dixi {name}`: {parser.description}", "",
             strings["generated"], "", f"## {strings['usage']}", "", "```text", usage(path, parser)]
    for child_name, child in subcommands(parser).items():
        lines.append(usage((*path, child_name), child))
    lines += ["```", "", strings["global_note"].format(suffix=suffix), ""]
    lines += sections(parser, strings)
    if subcommands(parser):
        lines += [f"## {strings['subcommands']}", ""]
        for child_name, child in subcommands(parser).items():
            lines += [f"### `{' '.join((*path, child_name))}`", "", child.description, ""]
            lines += describe(child, strings)
    lines += [f"## {strings['related']}", "", f"- [{strings['index_title']}](index{suffix})",
              f"- [README](../../{'README.md' if lang == 'en' else 'README.es.md'})"]
    return "\n".join(lines) + "\n"


def index_page(lang, parser, strings):
    suffix = LANGUAGES[lang]
    lines = [f"# {strings['index_title']}", "", f"## {strings['purpose']}", "", strings["index_purpose"], "",
             strings["generated"], "", f"## {strings['usage']}", "", "```text",
             "dixi [--lang {es,en}] [--json] <command>", "```", "", f"## {strings['global_options']}", "",
             strings["global_intro"], ""]
    lines += [line for line in describe(parser, strings) if not line.startswith("**")][1:]
    lines += [f"## {strings['commands']}", ""]
    for name, child in subcommands(parser).items():
        lines.append(f"- [`dixi {name}`]({name}{suffix}) — {child.description}")
    lines += ["", f"## {strings['exit_codes']}", "", f"| {strings['code']} | {strings['meaning']} |", "|---|---|"]
    lines += [f"| {code} | {meaning} |" for code, meaning in strings["codes"].items()]
    lines += ["", f"## {strings['related']}", "",
              f"- [{strings['commands_reference']}](../commands/index{suffix})",
              f"- [README](../../{'README.md' if lang == 'en' else 'README.es.md'})"]
    return "\n".join(lines) + "\n"


def pages():
    result = {}
    for lang, suffix in LANGUAGES.items():
        catalog = json.loads((ROOT / "src/dixi_spec_kit/locales" / f"{lang}.json").read_text(encoding="utf-8"))
        strings = json.loads((ROOT / "scripts/site" / f"{lang}.json").read_text(encoding="utf-8"))["cli"]
        parser = parser_for(catalog)
        result[f"index{suffix}"] = index_page(lang, parser, strings)
        for name, child in subcommands(parser).items():
            result[f"{name}{suffix}"] = command_page(lang, name, child, strings)
    return result


def main():
    parser = argparse.ArgumentParser(description="Generate docs/cli/ from the dixi argument parser.")
    parser.add_argument("--check", action="store_true", help="do not write; exit with 1 when a page is not current")
    parser.add_argument("--output", type=Path, default=OUTPUT, help="folder to write or check (default: docs/cli)")
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
            print("Run: python3 scripts/build-cli-reference.py", file=sys.stderr)
            return 1
        print(f"CLI reference is current ({len(expected)} pages)")
        return 0
    output.mkdir(parents=True, exist_ok=True)
    for path in output.iterdir():
        if path.name not in expected:
            path.unlink()
    for name, text in expected.items():
        (output / name).write_text(text, encoding="utf-8")
    print(f"CLI reference written: {len(expected)} pages in {arguments.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
