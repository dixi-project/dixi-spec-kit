import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class LocalCoreTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.project = self.base / "project"

    def cli(self, *args, cwd=None, network_guard=False):
        env = dict(os.environ, PYTHONPATH=str(ROOT / "src"), PYTHONDONTWRITEBYTECODE="1")
        command = [sys.executable, "-m", "dixi_spec_kit"]
        if network_guard:
            command = [sys.executable, "-c", "import socket, runpy; "
                       "socket.socket=lambda *a, **k: (_ for _ in ()).throw(AssertionError('network')); "
                       "runpy.run_module('dixi_spec_kit', run_name='__main__')"]
        return subprocess.run(command + list(args), cwd=cwd or self.base, env=env,
                              text=True, capture_output=True, timeout=10)

    def init(self, language="es"):
        result = self.cli("--lang", language, "init", str(self.project), "--agent", "none")
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        return self.project

    def metadata(self):
        return json.loads((self.project / ".dixi/project.json").read_text())

    def write_metadata(self, data):
        (self.project / ".dixi/project.json").write_text(json.dumps(data))

    def snapshot(self):
        return {str(p.relative_to(self.project)): hashlib.sha256(p.read_bytes()).hexdigest()
                for p in self.project.rglob("*") if p.is_file() and not p.is_symlink()}

    def test_help_only_available_commands(self):
        result = self.cli("--help")
        self.assertEqual(result.returncode, 0)
        for command in ("init", "doctor", "check"):
            self.assertIn(command, result.stdout)
        for absent in ("--agent codex", "--agent claude"):
            self.assertNotIn(absent, result.stdout)

    def test_version_is_release(self):
        result = self.cli("--version")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "dixi 1.3.0")

    def test_unknown_command(self):
        self.assertEqual(self.cli("not-a-command").returncode, 2)

    def test_initial_inventory(self):
        self.init()
        metadata = self.metadata()
        self.assertEqual(metadata["schema_version"], 1)
        self.assertEqual(metadata["agent"], "none")
        self.assertEqual(metadata["policy"], "portable")
        self.assertGreaterEqual(len(metadata["managed_files"]), 10)
        for name, digest in metadata["managed_files"].items():
            self.assertEqual(hashlib.sha256((self.project / name).read_bytes()).hexdigest(), digest)
        self.assertFalse((self.project / ".git").exists())
        self.assertFalse((self.project / ".claude").exists())
        self.assertFalse((self.project / ".codex").exists())
        self.assertIn(".context/", (self.project / ".gitignore").read_text())

    def test_empty_destination(self):
        self.project.mkdir()
        self.init()

    def test_default_agent_is_none(self):
        result = self.cli("init", str(self.project))
        self.assertEqual(result.returncode, 0)
        self.assertEqual(self.metadata()["agent"], "none")

    def test_unknown_agent_no_write(self):
        result = self.cli("init", str(self.project), "--agent", "cursor")
        self.assertEqual(result.returncode, 2)
        self.assertFalse(self.project.exists())

    def test_nonempty_unchanged(self):
        self.project.mkdir()
        (self.project / "important.txt").write_text("keep")
        before = self.snapshot()
        self.assertEqual(self.cli("init", str(self.project)).returncode, 3)
        self.assertEqual(self.snapshot(), before)

    def test_repeated_init(self):
        self.init()
        (self.project / "README.md").write_text("local edit")
        before = self.snapshot()
        self.assertEqual(self.cli("init", str(self.project)).returncode, 3)
        self.assertEqual(self.snapshot(), before)

    def test_traversal_destination(self):
        result = self.cli("init", "../escape")
        self.assertEqual(result.returncode, 3)

    def test_symlink_destination(self):
        outside = self.base / "outside"
        outside.mkdir()
        self.project.symlink_to(outside, target_is_directory=True)
        self.assertEqual(self.cli("init", str(self.project)).returncode, 3)
        self.assertEqual(list(outside.iterdir()), [])

    def test_symlink_parent(self):
        outside = self.base / "outside"
        outside.mkdir()
        link = self.base / "link"
        link.symlink_to(outside, target_is_directory=True)
        self.assertEqual(self.cli("init", str(link / "project")).returncode, 3)
        self.assertEqual(list(outside.iterdir()), [])

    def test_languages(self):
        es = self.cli("--lang", "es", "--help")
        en = self.cli("--lang", "en", "--help")
        self.assertEqual(es.returncode, 0)
        self.assertEqual(en.returncode, 0)
        self.assertNotEqual(es.stdout, en.stdout)
        self.init("en")
        self.assertEqual(self.metadata()["language"], "en")
        self.assertIn("Purpose", (self.project / "README.md").read_text())

    def test_generated_project_passes(self):
        self.init()
        result = self.cli("--json", "check", cwd=self.project)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        data = json.loads(result.stdout)
        self.assertTrue(any(m["key"] == "structure_only" for m in data["messages"]))

    def test_doctor_without_agent_or_project(self):
        result = self.cli("--json", "doctor")
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertEqual(json.loads(result.stdout)["code"], 0)

    def test_check_read_only(self):
        self.init()
        before = self.snapshot()
        self.assertEqual(self.cli("check", cwd=self.project).returncode, 0)
        self.assertEqual(self.cli("doctor", cwd=self.project).returncode, 0)
        self.assertEqual(self.snapshot(), before)

    def test_missing_project(self):
        self.assertEqual(self.cli("check").returncode, 2)

    def test_missing_required_file(self):
        self.init()
        (self.project / "README.md").unlink()
        self.assertEqual(self.cli("check", cwd=self.project).returncode, 1)

    def test_incomplete_inventory(self):
        self.init()
        metadata = self.metadata()
        metadata["managed_files"].pop("README.md")
        self.write_metadata(metadata)
        self.assertEqual(self.cli("check", cwd=self.project).returncode, 1)

    def test_invalid_metadata(self):
        self.init()
        target = self.project / ".dixi/project.json"
        for invalid in ("{", "[]", "null", '{"schema_version":true}', '{"schema_version":1,"agent":[]}'):
            with self.subTest(invalid=invalid):
                target.write_text(invalid)
                result = self.cli("check", cwd=self.project)
                self.assertEqual(result.returncode, 1)
                self.assertNotIn("Traceback", result.stderr)

    def test_unsupported_schema(self):
        self.init()
        metadata = self.metadata()
        metadata["schema_version"] = 99
        self.write_metadata(metadata)
        self.assertEqual(self.cli("check", cwd=self.project).returncode, 4)

    def test_duplicate_json_keys(self):
        self.init()
        path = self.project / ".dixi/project.json"
        original = path.read_text()
        path.write_text('{"schema_version":1,' + original.lstrip()[1:])
        self.assertEqual(self.cli("check", cwd=self.project).returncode, 1)

    def test_oversized_metadata(self):
        self.init()
        (self.project / ".dixi/project.json").write_text(" " * (1024 * 1024 + 1))
        self.assertEqual(self.cli("check", cwd=self.project).returncode, 1)

    def test_external_metadata_path(self):
        self.init()
        metadata = self.metadata()
        metadata["managed_files"]["../outside"] = "0" * 64
        self.write_metadata(metadata)
        self.assertEqual(self.cli("check", cwd=self.project).returncode, 1)

    def test_symlink_metadata(self):
        self.init()
        path = self.project / ".dixi/project.json"
        outside = self.base / "outside.json"
        outside.write_text(path.read_text())
        path.unlink()
        path.symlink_to(outside)
        self.assertEqual(self.cli("check", cwd=self.project).returncode, 1)

    def test_symlink_document(self):
        self.init()
        outside = self.base / "outside.md"
        outside.write_text("private")
        path = self.project / "README.md"
        path.unlink()
        path.symlink_to(outside)
        result = self.cli("check", cwd=self.project)
        self.assertEqual(result.returncode, 1)
        self.assertNotIn("private", result.stdout)

    def test_fifo_document(self):
        self.init()
        path = self.project / "README.md"
        path.unlink()
        os.mkfifo(path)
        self.assertEqual(self.cli("check", cwd=self.project).returncode, 1)

    def test_broken_link(self):
        self.init()
        (self.project / "README.md").write_text("# Draft\n[missing](missing.md)\n")
        self.assertEqual(self.cli("check", cwd=self.project).returncode, 1)

    def test_external_link(self):
        self.init()
        (self.project / "README.md").write_text("# Draft\n[external](../../outside.md)\n")
        self.assertEqual(self.cli("check", cwd=self.project).returncode, 1)

    def test_broken_parent(self):
        self.init()
        path = self.project / ".dixi/traceability.json"
        data = json.loads(path.read_text())
        item = next(i for i in data["items"] if i["kind"] == "module")
        item["parents"] = ["MISSING"]
        path.write_text(json.dumps(data))
        self.assertEqual(self.cli("check", cwd=self.project).returncode, 1)

    def test_duplicate_ids(self):
        self.init()
        path = self.project / ".dixi/traceability.json"
        data = json.loads(path.read_text())
        data["items"].append(data["items"][0])
        path.write_text(json.dumps(data))
        self.assertEqual(self.cli("check", cwd=self.project).returncode, 1)

    def test_check_does_not_execute(self):
        self.init()
        (self.project / "Makefile").write_text("verify:\n\ttouch executed\n")
        self.assertEqual(self.cli("check", cwd=self.project).returncode, 0)
        self.assertFalse((self.project / "executed").exists())

    def test_no_network(self):
        self.assertEqual(self.cli("init", str(self.project), network_guard=True).returncode, 0)
        for command in ("check", "doctor"):
            self.assertEqual(self.cli(command, cwd=self.project, network_guard=True).returncode, 0)


if __name__ == "__main__":
    unittest.main()
