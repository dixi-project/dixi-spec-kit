from pathlib import Path
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from dixi_spec_kit.core import check_project, initialize


class LinkDestinationsTests(unittest.TestCase):
    def test_empty_and_spaced_destinations(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory).resolve() / "project"
            initialize(project, "es")
            (project / "docs/user guide.md").write_text("# Guide\n")
            (project / "README.md").write_text(
                "# Draft\n[Self](   )\n[Anchor](#draft)\n"
                "[Guide](<docs/user guide.md>)\n[Reference][guide]\n\n"
                '[guide]: <docs/user guide.md> "User guide"\n')
            self.assertEqual(check_project(project)[0], 0)
