"""TASK-019: a CLI reference generated from the argparse parser, in English and Spanish."""
import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from dixi_spec_kit.cli import parser_for  # noqa: E402

SCRIPT = ROOT / "scripts/build-cli-reference.py"
PAGES = ROOT / "docs/cli"
SUFFIX = {"en": ".md", "es": ".es.md"}
HEADINGS = {"en": ("## Purpose", "## Usage", "## Related"), "es": ("## Propósito", "## Uso", "## Relacionado")}


def catalog(lang):
    return json.loads((ROOT / "src/dixi_spec_kit/locales" / f"{lang}.json").read_text(encoding="utf-8"))


def children(parser):
    for action in parser._actions:
        if isinstance(action, argparse._SubParsersAction):
            return action.choices
    return {}


def walk(parser, path=("dixi",)):
    yield path, parser
    for name, child in children(parser).items():
        yield from walk(child, (*path, name))


def run(*arguments):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    return subprocess.run([sys.executable, str(SCRIPT), *arguments], cwd=ROOT, env=env, text=True,
                          capture_output=True, timeout=60)


class CliReferenceTests(unittest.TestCase):
    def test_one_page_per_command_in_both_languages(self):
        commands = list(children(parser_for(catalog("en"))))
        self.assertEqual(commands, ["init", "doctor", "check", "workflow", "upgrade", "extension", "preset",
                                    "placeholders", "pr-size", "mode"])
        expected = {f"{name}{suffix}" for name in [*commands, "index"] for suffix in SUFFIX.values()}
        self.assertEqual({path.name for path in PAGES.iterdir()}, expected)

    def test_every_command_subcommand_and_option_is_documented(self):
        for lang, suffix in SUFFIX.items():
            for path, parser in walk(parser_for(catalog(lang))):
                page = PAGES / f"{path[1] if len(path) > 1 else 'index'}{suffix}"
                text = page.read_text(encoding="utf-8")
                with self.subTest(lang=lang, command=" ".join(path)):
                    self.assertIn(f"`{' '.join(path)}", text)
                    if len(path) > 1:
                        self.assertIn(parser.description, text)
                    for action in parser._actions:
                        if isinstance(action, argparse._SubParsersAction):
                            continue
                        for flag in action.option_strings or [action.dest]:
                            self.assertRegex(text, rf"`{re.escape(flag)}[ `]")
                        if action.help:
                            self.assertIn(action.help.replace("%(prog)s", "dixi"), text)
                        if action.choices and action.dest != "operation":
                            self.assertIn("{" + ",".join(map(str, action.choices)) + "}", text)

    def test_pages_have_the_sections_and_a_usage_line(self):
        for lang, suffix in SUFFIX.items():
            for command in children(parser_for(catalog(lang))):
                with self.subTest(lang=lang, command=command):
                    text = (PAGES / f"{command}{suffix}").read_text(encoding="utf-8")
                    self.assertTrue(text.startswith(f"# dixi {command}\n"))
                    positions = [text.index(f"\n{heading}\n") for heading in HEADINGS[lang]]
                    self.assertEqual(positions, sorted(positions))
                    self.assertRegex(text, rf"(?m)^dixi {re.escape(command)}( |$)")
        usage = (PAGES / "init.md").read_text(encoding="utf-8")
        self.assertIn("dixi init <directory> [--agent {none,claude,codex,skills}]", usage)
        self.assertIn("dixi workflow prepare <operation> --target <target> --request <request>",
                      (PAGES / "workflow.md").read_text(encoding="utf-8"))
        self.assertIn("`--max <limit>`", (PAGES / "pr-size.md").read_text(encoding="utf-8"))
        self.assertIn("1500", (PAGES / "pr-size.md").read_text(encoding="utf-8"))

    def test_index_lists_commands_global_options_and_exit_codes(self):
        # 0 is success and 1 the default code of an Issue; the others are passed explicitly.
        codes = {"0", "1"} | set(re.findall(r'Issue\("\w+", (\d)', "".join(
            path.read_text(encoding="utf-8") for path in (ROOT / "src/dixi_spec_kit").glob("*.py"))))
        self.assertEqual(codes, {"0", "1", "2", "3", "4", "5"})
        for lang, suffix in SUFFIX.items():
            text = (PAGES / f"index{suffix}").read_text(encoding="utf-8")
            texts = catalog(lang)
            with self.subTest(lang=lang):
                for command in children(parser_for(texts)):
                    self.assertIn(f"- [`dixi {command}`]({command}{suffix}) — {texts[command]}", text)
                for option in ("--help", "--version", "--lang {es,en}", "--json"):
                    self.assertIn(f"`{option}", text)
                for code in sorted(codes):
                    self.assertRegex(text, rf"(?m)^\| {code} \| \S.+ \|$")

    def test_check_passes_and_detects_missing_or_stale_pages(self):
        self.assertEqual(run("--check").returncode, 0, run("--check").stderr)
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder).resolve() / "cli"
            self.assertEqual(run("--check", "--output", str(output)).returncode, 1)
            self.assertEqual(run("--output", str(output)).returncode, 0)
            self.assertEqual(run("--check", "--output", str(output)).returncode, 0)
            page = output / "init.md"
            page.write_text(page.read_text(encoding="utf-8").replace("--existing", "--exists"), encoding="utf-8")
            stale = run("--check", "--output", str(output))
            self.assertEqual(stale.returncode, 1)
            self.assertIn("init.md", stale.stdout + stale.stderr)

    def test_generator_uses_only_the_standard_library_and_the_package(self):
        modules = set(re.findall(r"^(?:import|from) ([\w.]+)", SCRIPT.read_text(encoding="utf-8"), re.M))
        self.assertLessEqual(modules, {"argparse", "json", "pathlib", "sys", "dixi_spec_kit.cli"})

    def test_site_and_readmes_link_the_cli_reference(self):
        self.assertIn("](docs/cli/index.md)", (ROOT / "README.md").read_text(encoding="utf-8"))
        self.assertIn("](docs/cli/index.es.md)", (ROOT / "README.es.md").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as folder:
            out = Path(folder).resolve() / "site"
            env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
            result = subprocess.run([sys.executable, str(ROOT / "scripts/build-site.py"), str(out)], cwd=ROOT,
                                    env=env, text=True, capture_output=True, timeout=60)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            for lang, word in (("en", "Options"), ("es", "Opciones")):
                with self.subTest(lang=lang):
                    page = (out / lang / "cli/init.html").read_text(encoding="utf-8")
                    self.assertIn(f">{word}</h2>", page)
                    self.assertIn(f'/{lang}/cli/init.html"', page)
                    home = (out / lang / "index.html").read_text(encoding="utf-8")
                    self.assertIn('href="cli/index.html"', home)
                    self.assertIn('href="cli/pr-size.html"', home)
                    self.assertTrue((out / lang / "cli/workflow.html").is_file())


if __name__ == "__main__":
    unittest.main()
