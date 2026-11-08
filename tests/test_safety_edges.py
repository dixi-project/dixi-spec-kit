import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from dixi_spec_kit import core
from dixi_spec_kit.filesystem import safe_path


class SafetyEdgesTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.project = self.base / "project"

    def cli(self, *args, cwd=None):
        return subprocess.run([sys.executable, "-m", "dixi_spec_kit", *args],
                              cwd=cwd or self.base,
                              env=dict(os.environ, PYTHONPATH=str(ROOT / "src")),
                              capture_output=True, text=True, timeout=10)

    def init(self):
        self.assertEqual(self.cli("init", str(self.project)).returncode, 0)

    def test_invalid_unicode_metadata(self):
        self.init()
        path = self.project / ".dixi/project.json"
        data = json.loads(path.read_text())
        data["managed_files"]["\ud800.md"] = "0" * 64
        path.write_text(json.dumps(data))
        result = self.cli("check", cwd=self.project)
        self.assertEqual(result.returncode, 1)
        self.assertNotIn("Traceback", result.stderr)

    def test_many_links_limit(self):
        self.init()
        (self.project / "README.md").write_text("# Draft\n" + "[guide](docs/guide.md)\n" * 501)
        result = self.cli("--json", "check", cwd=self.project)
        self.assertEqual(result.returncode, 1)
        self.assertTrue(any(m["key"] == "invalid_file" for m in json.loads(result.stdout)["messages"]))

    def test_broken_reference_link(self):
        self.init()
        (self.project / "README.md").write_text("# Draft\nSee [a draft][missing].\n\n[missing]: missing.md\n")
        self.assertEqual(self.cli("check", cwd=self.project).returncode, 1)

    def test_reference_links_with_valid_destinations(self):
        self.init()
        (self.project / "README.md").write_text(
            '# Draft\n[Guide][guide] and [guide][] and [guide].\n\n'
            '[guide]: <docs/guide.md> "User guide"\n')
        self.assertEqual(self.cli("check", cwd=self.project).returncode, 0)

    def test_unsafe_path_spellings(self):
        for name in (".ENV", ".Aws/config", ".Context/private.md", "cert.PEM",
                     "ID_RSA", "line\nbreak.md", "escape\x1b.md", "\ud800.md"):
            with self.subTest(name=repr(name)):
                self.assertFalse(safe_path(name))
        self.assertTrue(safe_path("docs/visión del producto.md"))

    def test_unclosed_markdown_is_bounded(self):
        self.init()
        (self.project / "README.md").write_text("# Draft\n" + "[" * 100_000)
        self.assertEqual(self.cli("check", cwd=self.project).returncode, 0)

    def test_interrupted_initialization_preserves_partial_files(self):
        original = core.write_file
        calls = 0

        def fail_later(root, name, data):
            nonlocal calls
            calls += 1
            if calls == 3:
                raise OSError("simulated write failure")
            return original(root, name, data)

        with patch.object(core, "write_file", side_effect=fail_later):
            with self.assertRaises(OSError):
                core.initialize(str(self.project), "es")
        self.assertTrue((self.project / ".dixi-init.lock").exists())
        self.assertFalse((self.project / ".dixi/project.json").exists())
        before = {p.relative_to(self.project): p.read_bytes() for p in self.project.rglob("*") if p.is_file()}
        self.assertEqual(self.cli("init", str(self.project)).returncode, 3)
        self.assertEqual(before, {p.relative_to(self.project): p.read_bytes()
                                  for p in self.project.rglob("*") if p.is_file()})
