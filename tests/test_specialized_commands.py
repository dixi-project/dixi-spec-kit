from pathlib import Path
import unittest


RESOURCES = Path(__file__).resolve().parents[1] / "src/dixi_spec_kit/resources"
AREAS = {"data": "08-data/", "quality": "11-quality/", "ai": "21-ai/", "release": "docs/releases/",
         "promote": "docs/promotion/", "operate": "15-operations/", "finops": "22-finops/",
         "compliance": "23-compliance/", "duediligence": "28-due-diligence/"}


class SpecializedCommandsTests(unittest.TestCase):
    def texts(self, operation):
        for language in ("es", "en"):
            yield f"claude/{language}", (RESOURCES / "claude" / language / f"dixi.{operation}.md").read_text()
            yield f"codex/{language}", (RESOURCES / "codex" / language / f"dixi-{operation}.md").read_text()

    def test_each_operation_writes_in_its_area(self):
        for operation, area in AREAS.items():
            for source, text in self.texts(operation):
                with self.subTest(operation=operation, source=source):
                    self.assertIn(area, text)

    def test_promote_never_edits_mode(self):
        for source, text in self.texts("promote"):
            with self.subTest(source=source):
                self.assertIn("`MODE`", text)
                self.assertNotIn("echo prod", text)


if __name__ == "__main__":
    unittest.main()
