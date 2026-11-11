"""ADR-108 phase C: DIXI's own operations onboard, bugfix and issues, in both languages and both adapters."""
from pathlib import Path
import json
import unittest


ROOT = Path(__file__).resolve().parents[1]
RESOURCES = ROOT / "src/dixi_spec_kit/resources"
NEW = ("onboard", "bugfix", "issues")


def texts(operation):
    for language in ("en", "es"):
        yield language, "claude", (RESOURCES / f"claude/{language}/dixi.{operation}.md").read_text(encoding="utf-8")
        yield language, "codex", (RESOURCES / f"codex/{language}/dixi-{operation}.md").read_text(encoding="utf-8")


class OwnOperationTests(unittest.TestCase):
    def test_onboard_writes_drafts_only_after_the_person_validates_modules(self):
        for language, adapter, text in texts("onboard"):
            with self.subTest(language=language, adapter=adapter):
                for marker in ("04-modules/", "05-features/", ".dixi/traceability.json", "{{pending:"):
                    self.assertIn(marker, text)
                self.assertIn("Status: draft", text)
                self.assertIn("file:line", text)
                self.assertIn("/dixi.converge" if adapter == "claude" else "$dixi-converge", text)

    def test_bugfix_records_a_failing_test_before_the_fix(self):
        for language, adapter, text in texts("bugfix"):
            with self.subTest(language=language, adapter=adapter):
                self.assertIn("05-features/<slug>/bugs/BUG-NNN.md", text)
                self.assertIn("Signed-off-by", text)
                self.assertIn("make verify", text)
                self.assertIn("/dixi.clarify" if adapter == "claude" else "$dixi-clarify", text)

    def test_issues_previews_and_needs_confirmation(self):
        for language, adapter, text in texts("issues"):
            with self.subTest(language=language, adapter=adapter):
                self.assertIn("gh issue create", text)
                self.assertIn("gh auth status", text)
                self.assertIn("05-features/<slug>/issues.md", text)
                self.assertNotIn("gh issue close", text.replace("`gh issue close`", ""))

    def test_recipes_and_packaging(self):
        recipes = json.loads((RESOURCES / "workflows.json").read_text(encoding="utf-8"))["operations"]
        self.assertEqual(recipes["onboard"]["target_kinds"], ["goal"])
        self.assertEqual(recipes["bugfix"]["target_kinds"], ["feature"])
        self.assertEqual(recipes["issues"]["target_kinds"], ["feature"])
        pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
        for operation in NEW:
            self.assertIn(f'"resources/claude/*/dixi.{operation}.md"', pyproject)
            self.assertIn(f'"resources/codex/*/dixi-{operation}.md"', pyproject)

    def test_docs_list_the_new_operations(self):
        for path in ("docs/command-catalog.md", "README.md", "README.es.md", "packaging/README.md",
                     "docs/spec-kit-comparison.md"):
            text = (ROOT / path).read_text(encoding="utf-8")
            for operation in NEW:
                with self.subTest(path=path, operation=operation):
                    self.assertIn(f"/dixi.{operation}", text)
        contract = (ROOT / "07-contracts/commands/own-commands-contract.md").read_text(encoding="utf-8")
        for operation in NEW:
            self.assertIn(f"`{operation}`", contract)


if __name__ == "__main__":
    unittest.main()
