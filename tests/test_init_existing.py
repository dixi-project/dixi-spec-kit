"""`dixi init --existing` adds DIXI to a folder that already has files, never overwriting them (T13)."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
MINE = b"# My project\n\nOur own readme.\n"


def digest(data):
    return hashlib.sha256(data).hexdigest()


class InitExistingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.project = self.base / "repo"
        self.project.mkdir()
        (self.project / "src").mkdir()
        (self.project / "src/app.py").write_text("print('hello')\n")
        self.reference = self.base / "reference"

    def cli(self, *args, cwd=None):
        env = dict(os.environ, PYTHONPATH=str(ROOT / "src"), PYTHONDONTWRITEBYTECODE="1")
        command = [sys.executable, "-c", "import socket, runpy; "
                   "socket.socket=lambda *a, **k: (_ for _ in ()).throw(AssertionError('network')); "
                   "runpy.run_module('dixi_spec_kit', run_name='__main__')"]
        return subprocess.run(command + list(args), cwd=cwd or self.base, env=env,
                              text=True, capture_output=True, timeout=20)

    def init_existing(self, *extra):
        result = self.cli("--json", "--lang", "en", "init", str(self.project), "--agent", "claude", "--existing", *extra)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return json.loads(result.stdout)

    def snapshot(self, path=None):
        path = path or self.project
        return {str(p.relative_to(path)): digest(p.read_bytes())
                for p in path.rglob("*") if p.is_file() and not p.is_symlink()}

    def metadata(self):
        return json.loads((self.project / ".dixi/project.json").read_text())

    def reference_file(self, name):
        if not self.reference.exists():
            self.assertEqual(self.cli("--lang", "en", "init", str(self.reference), "--agent", "claude").returncode, 0)
        return (self.reference / name).read_bytes()

    def test_adds_dixi_without_touching_existing_code(self):
        self.init_existing()
        self.assertEqual((self.project / "src/app.py").read_text(), "print('hello')\n")
        self.assertTrue((self.project / ".dixi/project.json").is_file())
        self.assertTrue((self.project / ".claude/commands/dixi.plan.md").is_file())
        self.assertFalse((self.project / ".dixi-init.lock").exists())
        self.assertEqual(self.cli("check", cwd=self.project).returncode, 0)

    def test_existing_file_is_kept_and_reported(self):
        (self.project / "README.md").write_bytes(MINE)
        result = self.init_existing()
        self.assertEqual((self.project / "README.md").read_bytes(), MINE)
        self.assertIn("README.md", result["init"]["conflicts"])
        recorded = self.metadata()["managed_files"]["README.md"]
        self.assertEqual(recorded, digest(self.reference_file("README.md")),
                         "a kept file is recorded with the kit hash, so upgrade never sees it as updatable")
        plan = json.loads(self.cli("--json", "upgrade", "--dry-run", cwd=self.project).stdout)["upgrade"]["files"]
        self.assertNotIn("README.md", plan["updatable"])
        self.assertEqual(self.cli("upgrade", "--apply", cwd=self.project).returncode, 0)
        self.assertEqual((self.project / "README.md").read_bytes(), MINE)

    def test_identical_file_is_adopted(self):
        (self.project / "MODE").write_bytes(self.reference_file("MODE"))
        result = self.init_existing()
        self.assertNotIn("MODE", result["init"]["conflicts"])
        self.assertIn("MODE", result["init"]["adopted"])

    def test_existing_dixi_project_is_refused(self):
        self.init_existing()
        before = self.snapshot()
        result = self.cli("init", str(self.project), "--agent", "claude", "--existing")
        self.assertEqual(result.returncode, 3, result.stdout + result.stderr)
        self.assertEqual(self.snapshot(), before)

    def test_without_flag_a_non_empty_folder_is_refused(self):
        before = self.snapshot()
        result = self.cli("init", str(self.project), "--agent", "claude")
        self.assertEqual(result.returncode, 3)
        self.assertIn("--existing", result.stdout + result.stderr)
        self.assertEqual(self.snapshot(), before)

    def test_symlinked_file_is_never_followed(self):
        outside = self.base / "outside.md"
        outside.write_bytes(MINE)
        (self.project / "README.md").symlink_to(outside)
        result = self.init_existing()
        self.assertIn("README.md", result["init"]["conflicts"])
        self.assertEqual(outside.read_bytes(), MINE)
        self.assertTrue((self.project / "README.md").is_symlink())

    def test_symlinked_directory_is_never_written_through(self):
        outside = self.base / "outside-docs"
        outside.mkdir()
        (self.project / "docs").symlink_to(outside, target_is_directory=True)
        result = self.init_existing()
        self.assertEqual(list(outside.iterdir()), [])
        self.assertIn("docs/guide.md", result["init"]["conflicts"])

    def test_lock_refuses_concurrent_init(self):
        (self.project / ".dixi-init.lock").write_bytes(b"")
        before = self.snapshot()
        self.assertEqual(self.cli("init", str(self.project), "--existing").returncode, 3)
        self.assertEqual(self.snapshot(), before)

    def test_messages_in_both_languages(self):
        catalogs = [json.loads((ROOT / f"src/dixi_spec_kit/locales/{lang}.json").read_text(encoding="utf-8"))
                    for lang in ("en", "es")]
        for catalog in catalogs:
            for key in ("existing_option", "initialized_existing", "already_initialized"):
                self.assertIn(key, catalog)
            self.assertIn("--existing", catalog["destination_conflict"])


if __name__ == "__main__":
    unittest.main()
