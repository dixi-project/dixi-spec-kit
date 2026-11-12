"""TASK-018: every operation shows a realistic example for the three adapters."""
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / "docs/commands"
EXAMPLES = ROOT / "scripts/site/command-examples.json"
OPERATIONS = sorted(path.name[5:-3] for path in
                    (ROOT / "src/dixi_spec_kit/resources/claude/en").glob("dixi.*.md"))
SUFFIX = {"en": ".md", "es": ".es.md"}
HEADING = {"en": "## Example", "es": "## Ejemplo"}
BEFORE = {"en": "## Invocation", "es": "## Invocación"}
AFTER = {"en": "## When to use it", "es": "## Cuándo usarlo"}
SKILL = {"en": "Use the `dixi-{operation}` skill: {example}", "es": "Usa la skill `dixi-{operation}`: {example}"}


def section(text, heading):
    return text.split(f"\n{heading}\n", 1)[1].split("\n## ", 1)[0].strip()


class CommandExamplesTests(unittest.TestCase):
    def setUp(self):
        self.examples = json.loads(EXAMPLES.read_text(encoding="utf-8"))

    def test_catalog_has_an_example_per_operation_and_language(self):
        self.assertEqual(sorted(self.examples), OPERATIONS)
        for operation, texts in self.examples.items():
            with self.subTest(operation=operation):
                self.assertEqual(sorted(texts), ["en", "es"])
                for text in texts.values():
                    self.assertGreaterEqual(len(text), 3)
                    self.assertEqual(text, text.strip())
                    self.assertNotIn("`", text)
                    self.assertNotRegex(text, r"[<>\[\]]")

    def test_examples_are_written_in_each_language(self):
        same = [operation for operation, texts in self.examples.items() if texts["en"] == texts["es"]]
        identifiers = {"clarify", "plan", "tasks", "build", "verify", "review", "release", "architecture", "contract",
                       "threat-model", "data", "quality", "finops", "risk-review", "compliance", "converge", "issues",
                       "status", "interview", "onboard", "operate"}
        self.assertLessEqual(set(same), identifiers)

    def test_every_page_shows_the_example_for_the_three_adapters(self):
        for lang, suffix in SUFFIX.items():
            for operation in OPERATIONS:
                with self.subTest(lang=lang, operation=operation):
                    text = (PAGES / f"{operation}{suffix}").read_text(encoding="utf-8")
                    self.assertLess(text.index(f"\n{BEFORE[lang]}\n"), text.index(f"\n{HEADING[lang]}\n"))
                    self.assertLess(text.index(f"\n{HEADING[lang]}\n"), text.index(f"\n{AFTER[lang]}\n"))
                    example = self.examples[operation][lang]
                    shown = section(text, HEADING[lang])
                    self.assertIn(f"- Claude Code: `/dixi.{operation} {example}`", shown)
                    self.assertIn(f"- Codex: `$dixi-{operation} {example}`", shown)
                    self.assertIn("- Agent Skills: " + SKILL[lang].format(operation=operation, example=example), shown)

    def test_spanish_readme_and_guides_mention_interview_and_risk_review(self):
        for path in ("README.md", "README.es.md", "docs/command-catalog.md", "docs/command-catalog.es.md"):
            text = (ROOT / path).read_text(encoding="utf-8")
            for operation in ("interview", "risk-review"):
                with self.subTest(path=path, operation=operation):
                    self.assertIn(f"`/dixi.{operation}`", text)


if __name__ == "__main__":
    unittest.main()
