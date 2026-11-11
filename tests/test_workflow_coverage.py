"""ADR-108 phase B: every installed operation has a complete `dixi workflow` recipe."""
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
RESOURCES = ROOT / "src/dixi_spec_kit/resources"
sys.path.insert(0, str(ROOT / "src"))
from dixi_spec_kit.core import CLAUDE_COMMANDS


def load(name):
    return json.loads((RESOURCES / name).read_text(encoding="utf-8"))["operations"]


class WorkflowCoverageTests(unittest.TestCase):
    def test_every_command_has_a_recipe(self):
        self.assertEqual(set(load("workflows.json")), set(CLAUDE_COMMANDS))

    def test_localized_recipes_are_complete(self):
        for language in ("en", "es"):
            operations = load(f"workflows.{language}.json")
            self.assertEqual(set(operations), set(CLAUDE_COMMANDS), language)
            for operation in CLAUDE_COMMANDS:
                with self.subTest(language=language, operation=operation):
                    text = operations[operation]
                    for key in ("title", "purpose"):
                        self.assertIsInstance(text[key], str)
                        self.assertTrue(text[key].strip(), key)
                    for key in ("inputs", "steps", "outputs", "gates", "checks"):
                        self.assertIsInstance(text[key], list)
                        self.assertTrue(text[key], key)
                        for item in text[key]:
                            self.assertIsInstance(item, str)
                            self.assertTrue(item.strip(), key)

    def test_quickstart_names_every_operation(self):
        text = (ROOT / "docs/workflow-quickstart.md").read_text(encoding="utf-8")
        self.assertEqual(len(CLAUDE_COMMANDS), 30)
        for operation in CLAUDE_COMMANDS:
            with self.subTest(operation=operation):
                self.assertIn(f"`{operation}`", text)


if __name__ == "__main__":
    unittest.main()
