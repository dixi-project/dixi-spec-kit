"""TASK-022: `dixi mode` shows MODE and the promotion evidence that is missing; it never writes."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
ITEMS = ["tests", "threats", "data", "operations", "release", "owners"]


class ModeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.project = self.base / "project"
        result = self.cli("init", str(self.project), cwd=self.base)
        self.assertEqual(result.returncode, 0, result.stderr)

    def cli(self, *args, cwd=None):
        env = dict(os.environ, PYTHONPATH=str(ROOT / "src"), PYTHONDONTWRITEBYTECODE="1")
        command = [sys.executable, "-c", "import socket, runpy; "
                   "socket.socket=lambda *a, **k: (_ for _ in ()).throw(AssertionError('network')); "
                   "runpy.run_module('dixi_spec_kit', run_name='__main__')"]
        return subprocess.run(command + list(args), cwd=cwd or self.project, env=env,
                              text=True, capture_output=True, timeout=10)

    def report(self):
        result = self.cli("--json", "mode")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return json.loads(result.stdout)

    def write(self, name, text="# Document\n\nDecided and reviewed.\n"):
        path = self.project / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def snapshot(self):
        return {str(path.relative_to(self.project)): hashlib.sha256(path.read_bytes()).hexdigest()
                for path in self.project.rglob("*") if path.is_file()}

    def status(self):
        return {entry["item"]: entry["status"] for entry in self.report()["mode"]["evidence"]}

    def test_new_project_is_mvp_and_lists_the_six_items_as_missing(self):
        output = self.report()
        self.assertEqual(output["status"], "completed")
        self.assertEqual(output["mode"]["mode"], "mvp")
        self.assertEqual([entry["item"] for entry in output["mode"]["evidence"]], ITEMS)
        self.assertEqual(set(self.status().values()), {"missing"})
        self.assertEqual(output["mode"]["missing"], 6)
        for entry in output["mode"]["evidence"]:
            self.assertTrue(entry["expected"])
            self.assertEqual(entry["found"], [])
        text = self.cli("mode")
        self.assertEqual(text.returncode, 0, text.stderr)
        self.assertIn("mvp", text.stdout)
        self.assertIn("11-quality/strategy.md", text.stdout)
        self.assertIn("/dixi.promote", text.stdout)
        self.assertEqual(len(text.stdout.strip().splitlines()), 8)

    def test_a_document_without_blanks_is_evidence(self):
        self.write("11-quality/strategy.md")
        self.write("13-security/notes-threat-model.md")
        self.write("08-data/notes.md")
        self.write("15-operations/notes-api.md")
        self.write("docs/releases/0.1.0.md")
        self.write(".github/CODEOWNERS", "* @owner\n")
        output = self.report()
        self.assertEqual(set(self.status().values()), {"present"})
        self.assertEqual(output["mode"]["missing"], 0)
        found = {entry["item"]: entry["found"] for entry in output["mode"]["evidence"]}
        self.assertEqual(found["threats"], ["13-security/notes-threat-model.md"])
        self.assertEqual(found["owners"], [".github/CODEOWNERS"])
        self.assertEqual(len(self.cli("mode").stdout.strip().splitlines()), 2)

    def test_a_document_with_blanks_or_empty_is_not_evidence(self):
        self.write("11-quality/strategy.md", "# Strategy\n\n{{pending: test levels}}\n")
        self.write("08-data/README.md")
        self.write("13-security/checklist.md")
        self.write("CODEOWNERS", "")
        status = self.status()
        for item in ("tests", "data", "threats", "owners"):
            self.assertEqual(status[item], "missing", item)
        self.write("11-quality/strategy.md", "# Strategy\n\nUse `{{pending: …}}` for open questions.\n")
        self.assertEqual(self.status()["tests"], "present")

    def test_prod_has_nothing_to_report(self):
        (self.project / "MODE").write_text("prod\n", encoding="utf-8")
        output = self.report()
        self.assertEqual(output["mode"], {"mode": "prod", "evidence": [], "missing": 0})
        text = self.cli("mode").stdout
        self.assertIn("prod", text)
        self.assertEqual(len(text.strip().splitlines()), 1)

    def test_it_never_writes_and_cannot_change_the_mode(self):
        before = self.snapshot()
        for arguments in (("mode",), ("--json", "mode"), ("--lang", "es", "mode")):
            self.assertEqual(self.cli(*arguments).returncode, 0)
        self.assertEqual(self.snapshot(), before)
        for arguments in (("mode", "prod"), ("mode", "--set", "prod"), ("mode", "--prod")):
            self.assertEqual(self.cli(*arguments).returncode, 2, arguments)
        self.assertEqual((self.project / "MODE").read_text(encoding="utf-8"), "mvp\n")
        self.assertEqual(self.snapshot(), before)

    def test_invalid_mode_and_missing_project(self):
        (self.project / "MODE").write_text("production\n", encoding="utf-8")
        invalid = self.cli("--json", "mode")
        self.assertEqual(invalid.returncode, 1)
        self.assertEqual(json.loads(invalid.stdout)["messages"][0]["key"], "mode_invalid")
        (self.project / "MODE").unlink()
        self.assertEqual(self.cli("mode").returncode, 1)
        empty = self.base / "empty"
        empty.mkdir()
        self.assertEqual(self.cli("mode", cwd=empty).returncode, 2)

    def test_a_symlinked_document_is_not_evidence(self):
        outside = self.base / "outside.md"
        outside.write_text("# Strategy\n", encoding="utf-8")
        (self.project / "11-quality").mkdir(exist_ok=True)
        (self.project / "11-quality/strategy.md").symlink_to(outside)
        self.assertEqual(self.status()["tests"], "missing")

    def test_messages_in_both_languages(self):
        catalogs = {lang: json.loads((ROOT / "src/dixi_spec_kit/locales" / f"{lang}.json").read_text(encoding="utf-8"))
                    for lang in ("en", "es")}
        keys = ["mode", "mode_current", "mode_prod", "mode_invalid", "mode_summary", "mode_complete",
                *(f"mode_item_{item}" for item in ITEMS)]
        for lang, catalog in catalogs.items():
            for key in keys:
                with self.subTest(lang=lang, key=key):
                    self.assertTrue(catalog[key])
        self.assertNotEqual(catalogs["en"]["mode_summary"], catalogs["es"]["mode_summary"])
        spanish = self.cli("--lang", "es", "mode").stdout
        self.assertIn("evidencia", spanish)
        self.assertNotIn("evidence", spanish)

    def test_documents_describe_the_command(self):
        for path, command in (("README.md", "| `dixi mode` |"), ("README.es.md", "| `dixi mode` |")):
            self.assertIn(command, (ROOT / path).read_text(encoding="utf-8"), path)
        contract = (ROOT / "07-contracts/commands/automated-controls-contract.md").read_text(encoding="utf-8")
        self.assertIn("\n### `dixi mode`\n", contract)
        self.assertNotIn("There is no `mode` operation", contract)
        for item in ("11-quality/strategy.md", "13-security/", "08-data/", "15-operations/", "docs/releases/", "CODEOWNERS"):
            self.assertIn(item, contract.split("\n### `dixi mode`\n", 1)[1].split("\n## ", 1)[0])
        for suffix in (".md", ".es.md"):
            self.assertTrue((ROOT / "docs/cli" / f"mode{suffix}").is_file())
        promote = (ROOT / "src/dixi_spec_kit/resources/claude/en/dixi.promote.md").read_text(encoding="utf-8")
        self.assertIn("Never edit `MODE` yourself", promote)


if __name__ == "__main__":
    unittest.main()
