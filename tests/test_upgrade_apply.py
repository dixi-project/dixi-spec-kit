"""ADR-108 phase C: `dixi upgrade --apply` writes only updatable and new kit files (contract: block A, T09-T12)."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from dixi_spec_kit import __version__  # noqa: E402
from dixi_spec_kit import upgrade  # noqa: E402

OLD = b"# Old original\n"
REMOVED = ("constitution", "checklist", "converge")


def digest(data):
    return hashlib.sha256(data).hexdigest()


class UpgradeApplyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.project = self.base / "project"
        self.reference = self.base / "reference"

    def cli(self, *args, cwd=None):
        env = dict(os.environ, PYTHONPATH=str(ROOT / "src"), PYTHONDONTWRITEBYTECODE="1")
        command = [sys.executable, "-c", "import socket, runpy; "
                   "socket.socket=lambda *a, **k: (_ for _ in ()).throw(AssertionError('network')); "
                   "runpy.run_module('dixi_spec_kit', run_name='__main__')"]
        return subprocess.run(command + list(args), cwd=cwd or self.project, env=env,
                              text=True, capture_output=True, timeout=20)

    def init(self, path):
        result = self.cli("--lang", "en", "init", str(path), "--agent", "claude", cwd=self.base)
        self.assertEqual(result.returncode, 0, result.stderr)

    def metadata(self):
        return json.loads((self.project / ".dixi/project.json").read_text())

    def write_metadata(self, data):
        (self.project / ".dixi/project.json").write_text(json.dumps(data))

    def snapshot(self):
        return {str(p.relative_to(self.project)): digest(p.read_bytes())
                for p in self.project.rglob("*") if p.is_file() and not p.is_symlink()}

    def older_project(self):
        """A project from an older kit: three commands missing, every status present."""
        self.init(self.project)
        self.init(self.reference)
        data = self.metadata()
        for name in REMOVED:
            path = f".claude/commands/dixi.{name}.md"
            del data["managed_files"][path]
            (self.project / path).unlink()
        for name in ("README.md", "docs/guide.md", "AGENTS.md"):
            data["managed_files"][name] = digest(OLD)
        (self.project / "README.md").write_bytes(OLD)
        (self.project / "docs/guide.md").write_text("# My own edits\n")
        (self.project / "AGENTS.md").unlink()
        data["managed_files"]["docs/retired.md"] = digest(b"gone\n")
        (self.project / "docs/retired.md").write_text("gone\n")
        data["kit_version"] = "1.0.0"
        self.write_metadata(data)

    def apply(self):
        result = self.cli("--json", "upgrade", "--apply")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return json.loads(result.stdout)["upgrade"]

    def test_apply_writes_only_updatable_and_new(self):
        self.older_project()
        result = self.apply()
        new = sorted(f".claude/commands/dixi.{n}.md" for n in REMOVED)
        self.assertEqual(result["applied"], sorted(["README.md"] + new))
        self.assertEqual(result["skipped"], [])
        for name in ["README.md"] + new:
            self.assertEqual((self.project / name).read_bytes(), (self.reference / name).read_bytes(), name)
        self.assertEqual((self.project / "docs/guide.md").read_text(), "# My own edits\n")
        self.assertFalse((self.project / "AGENTS.md").exists(), "missing files are not recreated")
        self.assertEqual((self.project / "docs/retired.md").read_text(), "gone\n", "obsolete files are kept")
        data = self.metadata()
        self.assertEqual(data["kit_version"], __version__)
        for name in ["README.md"] + new:
            self.assertEqual(data["managed_files"][name], digest((self.reference / name).read_bytes()), name)
        self.assertEqual(data["managed_files"]["docs/guide.md"], digest(OLD), "conflicts keep their record")
        self.assertIn("docs/retired.md", data["managed_files"])
        self.assertFalse((self.project / ".dixi-upgrade.lock").exists())

    def test_dry_run_predicts_apply(self):
        self.older_project()
        plan = json.loads(self.cli("--json", "upgrade", "--dry-run").stdout)["upgrade"]["files"]
        self.assertEqual(self.apply()["applied"], sorted(plan["updatable"] + plan["new"]))

    def test_apply_is_idempotent(self):
        self.older_project()
        self.apply()
        before = self.snapshot()
        second = self.apply()
        self.assertEqual(second["applied"], [])
        self.assertEqual(self.snapshot(), before)

    def test_recovers_after_interruption(self):
        self.older_project()
        (self.project / "README.md").write_bytes((self.reference / "README.md").read_bytes())
        plan = json.loads(self.cli("--json", "upgrade", "--dry-run").stdout)["upgrade"]["files"]
        self.assertIn("README.md", plan["updatable"])
        self.assertIn("README.md", self.apply()["applied"])
        self.assertEqual(self.metadata()["managed_files"]["README.md"],
                         digest((self.reference / "README.md").read_bytes()))

    def test_changed_after_plan_is_skipped(self):
        self.older_project()
        planned = upgrade.plan(self.project)
        (self.project / "README.md").write_text("# Edited after the plan\n")
        result = upgrade.apply(self.project, planned=planned)
        self.assertIn("README.md", result["skipped"])
        self.assertNotIn("README.md", result["applied"])
        self.assertEqual((self.project / "README.md").read_text(), "# Edited after the plan\n")
        self.assertEqual(self.metadata()["managed_files"]["README.md"], digest(OLD))

    def test_symlink_target_is_never_written(self):
        self.older_project()
        outside = self.base / "outside.md"
        outside.write_bytes(OLD)
        (self.project / "README.md").unlink()
        (self.project / "README.md").symlink_to(outside)
        result = self.apply()
        self.assertNotIn("README.md", result["applied"])
        self.assertIn("README.md", result["files"]["conflict"])
        self.assertTrue((self.project / "README.md").is_symlink())
        self.assertEqual(outside.read_bytes(), OLD)

    def test_requires_exactly_one_mode(self):
        self.older_project()
        before = self.snapshot()
        for args in (("upgrade",), ("upgrade", "--dry-run", "--apply")):
            with self.subTest(args=args):
                self.assertEqual(self.cli(*args).returncode, 2)
                self.assertEqual(self.snapshot(), before)

    def test_lock_refuses_concurrent_apply(self):
        self.older_project()
        (self.project / ".dixi-upgrade.lock").write_bytes(b"")
        before = self.snapshot()
        result = self.cli("--json", "upgrade", "--apply")
        self.assertEqual(result.returncode, 3, result.stdout)
        self.assertEqual(self.snapshot(), before)

    def test_newer_project_is_rejected(self):
        self.older_project()
        data = self.metadata()
        data["kit_version"] = "1.99.0"
        self.write_metadata(data)
        before = self.snapshot()
        self.assertEqual(self.cli("upgrade", "--apply").returncode, 4)
        self.assertEqual(self.snapshot(), before)

    def test_messages_in_both_languages(self):
        self.older_project()
        result = self.cli("upgrade", "--apply")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("README.md", result.stdout)
        catalogs = [json.loads((ROOT / f"src/dixi_spec_kit/locales/{lang}.json").read_text(encoding="utf-8"))
                    for lang in ("en", "es")]
        for catalog in catalogs:
            for key in ("upgrade_apply", "upgrade_applied", "upgrade_locked", "upgrade_requires_mode"):
                self.assertIn(key, catalog)


if __name__ == "__main__":
    unittest.main()
