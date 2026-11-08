import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class DefaultLanguageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()

    def cli(self, *args, cwd=None):
        env = dict(os.environ, PYTHONPATH=str(ROOT / "src"), PYTHONDONTWRITEBYTECODE="1")
        return subprocess.run([sys.executable, "-m", "dixi_spec_kit"] + list(args), cwd=cwd or self.base,
                              env=env, text=True, capture_output=True, timeout=10)

    def test_help_defaults_to_english(self):
        result = self.cli("--help")
        self.assertEqual(result.returncode, 0)
        self.assertIn("Show this help.", result.stdout)

    def test_init_defaults_to_english(self):
        project = self.base / "project"
        self.assertEqual(self.cli("init", str(project)).returncode, 0)
        self.assertEqual(json.loads((project / ".dixi/project.json").read_text())["language"], "en")
        self.assertIn("## Purpose", (project / "README.md").read_text())

    def test_errors_default_to_english(self):
        result = self.cli("check")
        self.assertEqual(result.returncode, 2)
        self.assertIn("Project metadata is missing", result.stderr)

    def test_messages_follow_project_language(self):
        project = self.base / "proyecto"
        self.assertEqual(self.cli("--lang", "es", "init", str(project)).returncode, 0)
        check = self.cli("check", cwd=project)
        self.assertEqual(check.returncode, 0, check.stderr)
        self.assertIn("Alcance: estructura documental", check.stdout)
        forced = self.cli("--lang", "en", "check", cwd=project)
        self.assertIn("Scope: documentary structure", forced.stdout)

    def test_unreadable_project_falls_back_to_english(self):
        project = self.base / "broken"
        (project / ".dixi").mkdir(parents=True)
        (project / ".dixi/project.json").write_text("{not json")
        result = self.cli("check", cwd=project)
        self.assertEqual(result.returncode, 1)
        self.assertIn("Invalid", result.stderr)


if __name__ == "__main__":
    unittest.main()
