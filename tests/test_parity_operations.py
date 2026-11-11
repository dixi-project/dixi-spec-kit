"""ADR-108 phase A: constitution, checklist and converge, in both languages and both adapters."""
from pathlib import Path
import json
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
RESOURCES = ROOT / "src/dixi_spec_kit/resources"
NEW = ("constitution", "checklist", "converge")
LANGUAGES = ("en", "es")
PRINCIPLES = "00-governance/principles.md"


def adapter_texts(operation):
    for language in LANGUAGES:
        yield language, "claude", (RESOURCES / f"claude/{language}/dixi.{operation}.md").read_text(encoding="utf-8")
        yield language, "codex", (RESOURCES / f"codex/{language}/dixi-{operation}.md").read_text(encoding="utf-8")


class ParityOperationTests(unittest.TestCase):
    def test_files_exist_with_frontmatter(self):
        for operation in NEW:
            for language, adapter, text in adapter_texts(operation):
                with self.subTest(operation=operation, language=language, adapter=adapter):
                    self.assertTrue(text.startswith("---\n"))
                    header = text.split("---\n", 2)[1]
                    self.assertIn("description:", header)
                    if adapter == "claude":
                        self.assertIn("argument-hint:", header)
                        self.assertIn(f"# /dixi.{operation}", text)
                    else:
                        self.assertIn(f"name: dixi-{operation}", header)
                        self.assertIn(f"# $dixi-{operation}", text)
                        self.assertNotIn("$ARGUMENTS", text)

    def test_constitution_versions_principles_and_never_touches_code(self):
        for language, adapter, text in adapter_texts("constitution"):
            with self.subTest(language=language, adapter=adapter):
                self.assertIn(PRINCIPLES, text)
                self.assertRegex(text, r"MAJOR.*MINOR.*PATCH")
                self.assertIn("ADR", text)
                self.assertIn("{{pending:", text)
                self.assertIn("/dixi.analyze" if adapter == "claude" else "$dixi-analyze", text)

    def test_checklist_writes_unchecked_traced_items_only(self):
        for language, adapter, text in adapter_texts("checklist"):
            with self.subTest(language=language, adapter=adapter):
                self.assertIn("05-features/<slug>/checklists/", text)
                self.assertIn("CHK-", text)
                self.assertIn("- [ ]", text)
                self.assertIn(PRINCIPLES, text)

    def test_converge_appends_typed_traced_tasks(self):
        for language, adapter, text in adapter_texts("converge"):
            with self.subTest(language=language, adapter=adapter):
                self.assertIn("05-features/<slug>/tasks.md", text)
                for kind in ("missing", "partial", "contradicts", "unrequested"):
                    self.assertIn(f"`{kind}`", text)
                self.assertIn("T-NNN", text)
                self.assertIn(PRINCIPLES, text)

    def test_build_stops_on_open_checklist_items(self):
        for language in LANGUAGES:
            for path in (RESOURCES / f"claude/{language}/dixi.build.md", RESOURCES / f"codex/{language}/dixi-build.md"):
                with self.subTest(path=path.name, language=language):
                    text = path.read_text(encoding="utf-8")
                    self.assertIn("checklists/", text)
                    self.assertIn("- [ ]", text)

    def test_every_operation_reads_the_constitution(self):
        for folder in ("claude/en", "claude/es", "codex/en", "codex/es"):
            for path in sorted((RESOURCES / folder).glob("dixi[.-]*.md")):
                with self.subTest(file=f"{folder}/{path.name}"):
                    self.assertIn(PRINCIPLES, path.read_text(encoding="utf-8"))

    def test_workflow_recipes_in_both_languages(self):
        recipes = json.loads((RESOURCES / "workflows.json").read_text(encoding="utf-8"))["operations"]
        self.assertEqual(recipes["constitution"]["target_kinds"], ["goal"])
        self.assertEqual(recipes["checklist"]["target_kinds"], ["feature"])
        self.assertEqual(recipes["converge"]["target_kinds"], ["feature"])
        for language in LANGUAGES:
            texts = json.loads((RESOURCES / f"workflows.{language}.json").read_text(encoding="utf-8"))["operations"]
            for operation in NEW:
                with self.subTest(language=language, operation=operation):
                    for key in ("title", "purpose", "inputs", "steps", "outputs", "gates", "checks"):
                        self.assertTrue(texts[operation][key], key)

    def test_resources_are_declared_for_packaging(self):
        pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
        for operation in NEW:
            self.assertIn(f'"resources/claude/*/dixi.{operation}.md"', pyproject)
            self.assertIn(f'"resources/codex/*/dixi-{operation}.md"', pyproject)


class ParityDocsTests(unittest.TestCase):
    def test_migration_guide_maps_every_spec_kit_command(self):
        guide = (ROOT / "docs/coming-from-spec-kit.md").read_text(encoding="utf-8")
        for command in ("constitution", "specify", "clarify", "plan", "checklist", "tasks", "analyze", "implement",
                        "converge"):
            self.assertRegex(guide, rf"`/speckit\.{command}`.*`/dixi\.")
        self.assertIn("/dixi.build", guide)

    def test_comparison_is_dated_and_sourced(self):
        text = (ROOT / "docs/spec-kit-comparison.md").read_text(encoding="utf-8")
        self.assertIn("2026-11-11", text)
        self.assertIn("v1.4.0", text)
        self.assertIn("https://github.com/github/spec-kit", text)
        self.assertNotRegex(text, r"(?i)\b(better|worse|superior|inferior)\b")

    def test_catalog_and_readmes_list_the_new_operations(self):
        for path in ("docs/command-catalog.md", "README.md", "README.es.md", "packaging/README.md"):
            text = (ROOT / path).read_text(encoding="utf-8")
            for operation in NEW:
                with self.subTest(path=path, operation=operation):
                    self.assertIn(f"/dixi.{operation}", text)


if __name__ == "__main__":
    unittest.main()
