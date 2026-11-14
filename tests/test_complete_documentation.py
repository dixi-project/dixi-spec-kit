"""TASK-030: guides for what surrounds the commands, and a documentation index."""
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
RESOURCES = ROOT / "src/dixi_spec_kit/resources"
SUFFIX = {"en": ".md", "es": ".es.md"}
AGENTS = sorted(path.stem for path in (RESOURCES / "claude/en/agents").glob("*.md"))
HOOKS = sorted(path.name for path in (RESOURCES / "hooks").glob("*.py"))
PAGES = ("documentation", "subagents", "controls", "extensions-and-presets", "workflow-quickstart")
INTENTS = {
    "en": ("## Start", "## Choose a command", "## Look up a command or an option", "## Extend the kit",
           "## Migrate", "## Contribute"),
    "es": ("## Empezar", "## Elegir un comando", "## Consultar un comando o una opción", "## Extender el kit",
           "## Migrar", "## Contribuir"),
}


def read(name):
    return (ROOT / name).read_text(encoding="utf-8")


def section(text, heading):
    return text.split(f"\n{heading}\n", 1)[1].split("\n## ", 1)[0]


def cli(*args, cwd):
    env = dict(os.environ, PYTHONPATH=str(ROOT / "src"), PYTHONDONTWRITEBYTECODE="1")
    return subprocess.run([sys.executable, "-m", "dixi_spec_kit", *args], cwd=cwd, env=env, text=True,
                          capture_output=True, timeout=30)


def script(name, *args):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    return subprocess.run([sys.executable, str(ROOT / "scripts" / name), *args], cwd=ROOT, env=env, text=True,
                          capture_output=True, timeout=60)


class DocumentationIndexTests(unittest.TestCase):
    def test_every_page_exists_in_both_languages(self):
        for page in PAGES:
            for lang, suffix in SUFFIX.items():
                with self.subTest(page=page, lang=lang):
                    text = (DOCS / f"{page}{suffix}").read_text(encoding="utf-8")
                    self.assertTrue(text.startswith("# "))
                    self.assertIn("\n## Purpose\n" if lang == "en" else "\n## Propósito\n", text)

    def test_index_is_organized_by_what_the_person_wants_to_do(self):
        targets = ("command-catalog", "commands/index", "cli/index", "subagents", "controls",
                   "extensions-and-presets", "workflow-quickstart", "coming-from-spec-kit")
        for lang, suffix in SUFFIX.items():
            text = (DOCS / f"documentation{suffix}").read_text(encoding="utf-8")
            with self.subTest(lang=lang):
                positions = [text.index(f"\n{heading}\n") for heading in INTENTS[lang]]
                self.assertEqual(positions, sorted(positions))
                for target in targets:
                    self.assertIn(f"]({target}{suffix})", text)
                for other in ("support-matrix.md", "local-development.md", "../CONTRIBUTING.md"):
                    self.assertIn(f"]({other})", text)
                for href in re.findall(r"\]\(([^)\s#]+)\)", text):
                    if not href.startswith("http"):
                        self.assertTrue((DOCS / href).resolve().exists(), href)

    def test_readmes_link_the_index_in_a_section_of_its_own_near_the_top(self):
        for name, heading, before, link in (
                ("README.md", "## Documentation", "## Installation", "](docs/documentation.md)"),
                ("README.es.md", "## Documentación", "## Instalación", "](docs/documentation.es.md)")):
            with self.subTest(readme=name):
                text = read(name)
                self.assertLess(text.index(f"\n{heading}\n"), text.index(f"\n{before}\n"))
                self.assertIn(link, section(text, heading))


class SubagentReferenceTests(unittest.TestCase):
    def test_there_are_four_subagents(self):
        self.assertEqual(AGENTS, ["dixi-architect", "dixi-developer", "dixi-reviewer", "dixi-tester"])

    def test_page_has_every_subagent_with_its_packaged_text(self):
        names = {"en": ("What you do", "What you deliver", "Limits"), "es": ("Qué haces", "Qué entregas", "Límites")}
        for lang, suffix in SUFFIX.items():
            page = (DOCS / f"subagents{suffix}").read_text(encoding="utf-8")
            for agent in AGENTS:
                with self.subTest(lang=lang, agent=agent):
                    source = (RESOURCES / "claude" / lang / "agents" / f"{agent}.md").read_text(encoding="utf-8")
                    entry = section(page, f"## `{agent}`")
                    description = re.search(r'^description: "(.*)"$', source, re.M).group(1)
                    self.assertIn(description, entry)
                    for name in names[lang]:
                        self.assertIn(section(source, f"## {name}").strip(), entry)
                    self.assertIn(f"`.claude/agents/{agent}.md`", entry)
            self.assertIn("`--agent claude`", page)

    def test_check_passes_and_detects_a_stale_page(self):
        self.assertEqual(script("build-subagent-reference.py", "--check").returncode, 0)
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder).resolve()
            self.assertEqual(script("build-subagent-reference.py", "--check", "--output", str(output)).returncode, 1)
            self.assertEqual(script("build-subagent-reference.py", "--output", str(output)).returncode, 0)
            self.assertEqual(sorted(path.name for path in output.iterdir()), ["subagents.es.md", "subagents.md"])
            page = output / "subagents.md"
            page.write_text(page.read_text(encoding="utf-8") + "\nEdited by hand.\n", encoding="utf-8")
            stale = script("build-subagent-reference.py", "--check", "--output", str(output))
            self.assertEqual(stale.returncode, 1)
            self.assertIn("subagents.md", stale.stdout + stale.stderr)

    def test_generator_uses_only_the_standard_library(self):
        modules = set(re.findall(r"^(?:import|from) ([\w.]+)", read("scripts/build-subagent-reference.py"), re.M))
        self.assertLessEqual(modules, {"argparse", "json", "pathlib", "re", "sys"})


class ControlsGuideTests(unittest.TestCase):
    def test_there_are_five_hooks(self):
        self.assertEqual(HOOKS, ["guard_attestation.py", "guard_secrets.py", "mode_gate.py", "protect_tests.py",
                                 "verify_on_stop.py"])

    def test_guide_covers_every_hook_and_its_limits(self):
        headings = {"en": ("## What each control blocks", "## How to see that they are active",
                           "## What the controls do not cover"),
                    "es": ("## Qué bloquea cada control", "## Cómo ver que están activos",
                           "## Qué no cubren los controles")}
        for lang, suffix in SUFFIX.items():
            text = (DOCS / f"controls{suffix}").read_text(encoding="utf-8")
            with self.subTest(lang=lang):
                positions = [text.index(f"\n{heading}\n") for heading in headings[lang]]
                self.assertEqual(positions, sorted(positions))
                table = section(text, headings[lang][0])
                for hook in HOOKS:
                    self.assertEqual(len(re.findall(rf"(?m)^\| `{re.escape(hook)}` \|", table)), 1, hook)
                for piece in ("`--controls`", "`.dixi/hooks/`", "Claude Code", "Codex", "`.claude/settings.json`",
                              "`.codex/hooks.json`", "`--agent skills`", "`DIXI_ALLOW_TEST_EDITS=1`",
                              "`DIXI_VERIFY_TIMEOUT`"):
                    self.assertIn(piece, text)

    def test_guide_does_not_announce_controls_where_they_are_not_supported(self):
        english = (DOCS / "controls.md").read_text(encoding="utf-8")
        self.assertRegex(english, r"`--agent skills`[^.\n]*\bnot available\b|not available[^.\n]*`--agent skills`")
        self.assertIn("second layer", english)
        refused = None
        with tempfile.TemporaryDirectory() as folder:
            refused = cli("init", "project", "--agent", "skills", "--controls", cwd=folder)
        self.assertNotEqual(refused.returncode, 0)


class ExtensionAndPresetGuideTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        result = cli("init", "project", "--agent", "claude", cwd=self.base)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.project = self.base / "project"

    def test_the_minimal_extension_installs(self):
        result = cli("--json", "extension", "add", str(ROOT / "examples/extension-minimal"), cwd=self.project)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(json.loads(result.stdout)["extension"]["id"], "acme")
        installed = self.project / ".claude/commands/dixi-acme-deploy-check.md"
        self.assertEqual(installed.read_text(encoding="utf-8"),
                         read("examples/extension-minimal/operations/en/deploy-check.md"))
        self.assertEqual(cli("check", cwd=self.project).returncode, 0)
        self.assertEqual(cli("extension", "remove", "acme", cwd=self.project).returncode, 0)
        self.assertFalse(installed.exists())

    def test_the_minimal_preset_installs_and_is_removed(self):
        target = self.project / ".claude/commands/dixi.handoff.md"
        kit = target.read_text(encoding="utf-8")
        result = cli("--json", "preset", "add", str(ROOT / "examples/preset-minimal"), cwd=self.project)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(json.loads(result.stdout)["preset"]["id"], "team")
        self.assertEqual(target.read_text(encoding="utf-8"), read("examples/preset-minimal/operations/en/handoff.md"))
        self.assertEqual(cli("preset", "remove", "team", cwd=self.project).returncode, 0)
        self.assertEqual(target.read_text(encoding="utf-8"), kit)

    def test_examples_hold_only_what_the_formats_accept(self):
        files = {"extension-minimal": ["extension.json", "operations/en/deploy-check.md", "operations/es/deploy-check.md"],
                 "preset-minimal": ["operations/en/handoff.md", "operations/es/handoff.md", "preset.json"]}
        for example, expected in files.items():
            folder = ROOT / "examples" / example
            found = sorted(path.relative_to(folder).as_posix() for path in folder.rglob("*") if path.is_file())
            self.assertEqual(found, sorted(expected), example)

    def test_guide_shows_the_examples_as_they_are(self):
        for lang, suffix in SUFFIX.items():
            text = (DOCS / f"extensions-and-presets{suffix}").read_text(encoding="utf-8")
            with self.subTest(lang=lang):
                for manifest in ("examples/extension-minimal/extension.json", "examples/preset-minimal/preset.json"):
                    self.assertIn(read(manifest).strip(), text)
                for piece in ("dixi extension add", "dixi extension remove", "dixi preset add", "dixi preset remove",
                              "`.dixi/overrides/`", "`dixi-acme-deploy-check`", "`priority`", "`--agent none`",
                              "../examples/extension-minimal", "../examples/preset-minimal"):
                    self.assertIn(piece, text)


class SiteAndTranslationsTests(unittest.TestCase):
    def test_site_publishes_every_new_page_in_both_trees(self):
        notice = json.loads(read("scripts/site/es.json"))["english_only"]
        with tempfile.TemporaryDirectory() as folder:
            out = Path(folder).resolve() / "site"
            result = script("build-site.py", str(out))
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            for page in PAGES:
                with self.subTest(page=page):
                    self.assertTrue((out / "en" / f"{page}.html").is_file())
                    spanish = (out / "es" / f"{page}.html").read_text(encoding="utf-8")
                    self.assertNotIn(notice, spanish)
            for lang in SUFFIX:
                home = (out / lang / "index.html").read_text(encoding="utf-8")
                self.assertIn('href="documentation.html"', home)
            self.assertFalse((out / "en/documentation.es.html").exists())

    def test_recipes_guide_keeps_its_table_of_operations_in_spanish(self):
        english, spanish = (read(f"docs/workflow-quickstart{suffix}") for suffix in SUFFIX.values())
        rows = lambda text: re.findall(r"(?m)^\| `([a-z-]+)` \|", text)  # noqa: E731
        self.assertEqual(len(rows(english)), 33)
        self.assertEqual(rows(spanish), rows(english))
        self.assertIn("dixi --lang es workflow list", spanish)


if __name__ == "__main__":
    unittest.main()
