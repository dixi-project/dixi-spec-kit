"""TASK-016: one reference page per operation, generated from the packaged command texts."""
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/build-command-reference.py"
COMMANDS = ROOT / "src/dixi_spec_kit/resources/claude"
PAGES = ROOT / "docs/commands"
OPERATIONS = sorted(path.name[5:-3] for path in (COMMANDS / "en").glob("dixi.*.md"))
SUFFIX = {"en": ".md", "es": ".es.md"}
HEADINGS = {
    "en": ("## Purpose", "## Invocation", "## When to use it", "## Steps", "## Files read and written",
           "## Stops and human gates", "## Closing", "## Next step", "## Related"),
    "es": ("## Propósito", "## Invocación", "## Cuándo usarlo", "## Pasos", "## Archivos que lee y escribe",
           "## Paradas y controles humanos", "## Cierre", "## Siguiente paso", "## Relacionado"),
}


def run(*arguments):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    return subprocess.run([sys.executable, str(SCRIPT), *arguments], cwd=ROOT, env=env, text=True,
                          capture_output=True, timeout=60)


def section(text, heading):
    return text.split(f"\n{heading}\n", 1)[1].split("\n## ", 1)[0].strip()


class CommandReferenceTests(unittest.TestCase):
    def test_there_are_thirty_three_operations(self):
        self.assertEqual(len(OPERATIONS), 33)

    def test_every_operation_has_a_page_in_both_languages(self):
        for lang, suffix in SUFFIX.items():
            self.assertTrue((PAGES / f"index{suffix}").is_file(), f"index{suffix}")
            for operation in OPERATIONS:
                with self.subTest(lang=lang, operation=operation):
                    self.assertTrue((PAGES / f"{operation}{suffix}").is_file())
        expected = {f"{name}{suffix}" for name in [*OPERATIONS, "index"] for suffix in SUFFIX.values()}
        self.assertEqual({path.name for path in PAGES.iterdir()}, expected)

    def test_pages_have_every_section_and_the_three_invocations(self):
        for lang, suffix in SUFFIX.items():
            for operation in OPERATIONS:
                with self.subTest(lang=lang, operation=operation):
                    text = (PAGES / f"{operation}{suffix}").read_text(encoding="utf-8")
                    self.assertTrue(text.startswith(f"# /dixi.{operation}\n"))
                    positions = [text.index(f"\n{heading}\n") for heading in HEADINGS[lang]]
                    self.assertEqual(positions, sorted(positions))
                    invocation = section(text, HEADINGS[lang][1])
                    for command in (f"`/dixi.{operation}", f"`$dixi-{operation}", f"`dixi-{operation}`"):
                        self.assertIn(command, invocation)

    def test_pages_carry_the_command_text(self):
        names = {"en": ("Goal", "Steps", "Limits", "Closing"), "es": ("Objetivo", "Pasos", "Límites", "Cierre")}
        for lang, suffix in SUFFIX.items():
            purpose, invocation, _, steps, _, stops, closing = HEADINGS[lang][:7]
            for operation in OPERATIONS:
                with self.subTest(lang=lang, operation=operation):
                    source = (COMMANDS / lang / f"dixi.{operation}.md").read_text(encoding="utf-8")
                    page = (PAGES / f"{operation}{suffix}").read_text(encoding="utf-8")
                    goal, source_steps, limits, source_closing = (section(source, f"## {name}") for name in names[lang])
                    description = re.search(r'^description: "(.*)"$', source, re.M).group(1)
                    hint = re.search(r'^argument-hint: "(.*)"$', source, re.M).group(1)
                    self.assertIn(description, section(page, purpose))
                    self.assertIn(goal, section(page, purpose))
                    self.assertIn(hint, section(page, invocation))
                    self.assertEqual(section(page, steps), source_steps)
                    self.assertEqual(section(page, stops), limits)
                    self.assertEqual(section(page, closing), source_closing)

    def test_files_section_lists_the_paths_named_by_the_steps(self):
        text = (PAGES / "specify.md").read_text(encoding="utf-8")
        files = section(text, "## Files read and written")
        self.assertIn("- `05-features/<slug>/feature-spec.md`", files)
        self.assertIn("- `.dixi/traceability.json`", files)
        self.assertNotIn("dixi workflow prepare", files)
        self.assertNotIn("/dixi.clarify", files)

    def test_next_step_and_when_follow_the_workflow_graph(self):
        text = (PAGES / "specify.md").read_text(encoding="utf-8")
        following = section(text, "## Next step")
        for operation in ("clarify", "contract", "plan"):
            self.assertIn(f"[`/dixi.{operation}`]({operation}.md)", following)
        self.assertIn("[`/dixi.discover`](discover.md)", section((PAGES / "domain.md").read_text(encoding="utf-8"),
                                                                 "## When to use it"))
        spanish = section((PAGES / "specify.es.md").read_text(encoding="utf-8"), "## Siguiente paso")
        self.assertIn("[`/dixi.plan`](plan.es.md)", spanish)

    def test_index_lists_every_operation_with_its_description(self):
        for lang, suffix in SUFFIX.items():
            text = (PAGES / f"index{suffix}").read_text(encoding="utf-8")
            for operation in OPERATIONS:
                with self.subTest(lang=lang, operation=operation):
                    source = (COMMANDS / lang / f"dixi.{operation}.md").read_text(encoding="utf-8")
                    description = re.search(r'^description: "(.*)"$', source, re.M).group(1)
                    self.assertIn(f"- [`/dixi.{operation}`]({operation}{suffix}) — {description}", text)

    def test_check_passes_on_the_committed_pages(self):
        result = run("--check")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_check_fails_when_a_page_is_missing_or_out_of_date(self):
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder).resolve() / "commands"
            self.assertEqual(run("--check", "--output", str(output)).returncode, 1)
            self.assertEqual(run("--output", str(output)).returncode, 0)
            self.assertEqual(run("--check", "--output", str(output)).returncode, 0)
            page = output / "build.md"
            page.write_text(page.read_text(encoding="utf-8").replace("## Steps", "## Steps\n\nEdited by hand."),
                            encoding="utf-8")
            stale = run("--check", "--output", str(output))
            self.assertEqual(stale.returncode, 1)
            self.assertIn("build.md", stale.stdout + stale.stderr)
            page.unlink()
            self.assertEqual(run("--check", "--output", str(output)).returncode, 1)
            (output / "left-over.md").write_text("# Old\n", encoding="utf-8")
            shutil.copyfile(output / "plan.md", page)
            self.assertEqual(run("--check", "--output", str(output)).returncode, 1)

    def test_generator_uses_only_the_standard_library(self):
        text = SCRIPT.read_text(encoding="utf-8")
        modules = set(re.findall(r"^(?:import|from) ([\w.]+)", text, re.M))
        self.assertLessEqual(modules, {"argparse", "json", "pathlib", "re", "sys"})


if __name__ == "__main__":
    unittest.main()
