import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class InitCurrentDirectoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.project = Path(self.temp.name).resolve() / "project"
        self.project.mkdir()

    def cli(self, *args):
        env = dict(os.environ, PYTHONPATH=str(ROOT / "src"), PYTHONDONTWRITEBYTECODE="1")
        return subprocess.run([sys.executable, "-m", "dixi_spec_kit", *args], cwd=self.project, env=env,
                              text=True, capture_output=True, timeout=10)

    def listing(self):
        return sorted(str(p.relative_to(self.project)) for p in self.project.rglob("*"))

    def test_dot_initializes_empty_current_directory(self):
        for spelling, agent in ((".", "codex"), ("./", "claude")):
            with self.subTest(spelling=spelling):
                for item in sorted(self.project.rglob("*"), reverse=True):
                    item.rmdir() if item.is_dir() else item.unlink()
                result = self.cli("init", spelling, "--agent", agent)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn(str(self.project), result.stdout)
                metadata = json.loads((self.project / ".dixi/project.json").read_text())
                self.assertEqual(metadata["agent"], agent)
                self.assertEqual(self.cli("check").returncode, 0)

    def test_dot_refuses_non_empty_current_directory(self):
        (self.project / "notes.txt").write_text("mine")
        before = self.listing()
        result = self.cli("--json", "init", ".")
        self.assertEqual(result.returncode, 3)
        self.assertEqual(json.loads(result.stdout)["messages"][0]["key"], "destination_conflict")
        self.assertEqual(self.listing(), before)
        self.assertEqual((self.project / "notes.txt").read_text(), "mine")

    def test_unsafe_destination_explains_how_to_fix(self):
        for destination in ("..", "../sibling", ""):
            with self.subTest(destination=destination):
                result = self.cli("--json", "init", destination)
                self.assertEqual(result.returncode, 3, result.stdout + result.stderr)
                self.assertEqual(json.loads(result.stdout)["messages"][0]["key"], "unsafe_destination")
                self.assertEqual(self.listing(), [])
        for language in ("en", "es"):
            with self.subTest(language=language):
                result = self.cli("--lang", language, "init", "../sibling")
                self.assertIn("dixi init .", result.stderr)


if __name__ == "__main__":
    unittest.main()
