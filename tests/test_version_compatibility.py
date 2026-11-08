import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class VersionCompatibilityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.project = Path(self.temp.name).resolve() / "project"
        self.assertEqual(self.cli("init", str(self.project), cwd=self.project.parent).returncode, 0)

    def cli(self, *args, cwd=None):
        env = dict(os.environ, PYTHONPATH=str(ROOT / "src"), PYTHONDONTWRITEBYTECODE="1")
        return subprocess.run([sys.executable, "-m", "dixi_spec_kit"] + list(args), cwd=cwd or self.project,
                              env=env, text=True, capture_output=True, timeout=10)

    def with_kit_version(self, version):
        path = self.project / ".dixi/project.json"
        data = json.loads(path.read_text())
        data["kit_version"] = version
        path.write_text(json.dumps(data))

    def test_same_major_versions_are_accepted(self):
        for version in ("1.0.0", "1.0.7", "1.4.2", "1.0.0.dev0"):
            with self.subTest(version=version):
                self.with_kit_version(version)
                result = self.cli("check")
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_other_major_versions_are_unsupported(self):
        for version in ("0.9.0", "2.0.0", "10.1.0"):
            with self.subTest(version=version):
                self.with_kit_version(version)
                self.assertEqual(self.cli("check").returncode, 4)

    def test_malformed_versions_are_invalid(self):
        for version in ("", "uno", "1", "1.x.0", "1.0.0; rm"):
            with self.subTest(version=version):
                self.with_kit_version(version)
                self.assertEqual(self.cli("check").returncode, 1)


if __name__ == "__main__":
    unittest.main()
