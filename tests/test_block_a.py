import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
V1_COMMANDS = ("discover", "specify", "clarify", "plan", "tasks", "build", "verify", "review", "analyze", "status")
NEW_COMMANDS = ("domain", "architecture", "contract", "threat-model", "handoff", "change",
                "data", "quality", "ai", "release", "promote", "operate", "finops", "compliance", "duediligence",
                "interview", "risk-review")


def digest(data):
    return hashlib.sha256(data).hexdigest()


class BlockATests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.project = self.base / "project"

    def cli(self, *args, cwd=None):
        env = dict(os.environ, PYTHONPATH=str(ROOT / "src"), PYTHONDONTWRITEBYTECODE="1")
        command = [sys.executable, "-c", "import socket, runpy; "
                   "socket.socket=lambda *a, **k: (_ for _ in ()).throw(AssertionError('network')); "
                   "runpy.run_module('dixi_spec_kit', run_name='__main__')"]
        return subprocess.run(command + list(args), cwd=cwd or self.project, env=env,
                              text=True, capture_output=True, timeout=10)

    def init(self, language="en", agent="claude"):
        result = self.cli("--lang", language, "init", str(self.project), "--agent", agent, cwd=self.base)
        self.assertEqual(result.returncode, 0, result.stderr)

    def metadata(self):
        return json.loads((self.project / ".dixi/project.json").read_text())

    def write_metadata(self, data):
        (self.project / ".dixi/project.json").write_text(json.dumps(data))

    def snapshot(self):
        return {str(p.relative_to(self.project)): digest(p.read_bytes())
                for p in self.project.rglob("*") if p.is_file()}

    def as_v1_project(self):
        data = self.metadata()
        for name in NEW_COMMANDS:
            path = f".claude/commands/dixi.{name}.md"
            del data["managed_files"][path]
            (self.project / path).unlink()
        data["kit_version"] = "1.0.0"
        self.write_metadata(data)

    def plan(self):
        result = self.cli("--json", "upgrade", "--dry-run")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return json.loads(result.stdout)["upgrade"]

    def test_design_commands_start_from_workflows(self):
        for language in ("es", "en"):
            with self.subTest(language=language):
                self.project = self.base / language
                self.init(language)
                for name in ("domain", "architecture", "contract", "threat-model"):
                    text = (self.project / f".claude/commands/dixi.{name}.md").read_text()
                    self.assertIn(f"dixi workflow prepare {name}", text)

    def test_handoff_and_change_targets(self):
        for language in ("es", "en"):
            with self.subTest(language=language):
                self.project = self.base / language
                self.init(language)
                handoff = (self.project / ".claude/commands/dixi.handoff.md").read_text()
                change = (self.project / ".claude/commands/dixi.change.md").read_text()
                self.assertIn(".context/handoff.md", handoff)
                self.assertIn("CHANGE-NNN", change)
                self.assertIn(".context/", (self.project / ".gitignore").read_text())

    def test_v1_project_still_passes(self):
        self.init()
        self.as_v1_project()
        check = self.cli("--json", "check")
        self.assertEqual(check.returncode, 0, check.stdout)
        doctor = self.cli("--json", "doctor")
        self.assertEqual(doctor.returncode, 0, doctor.stdout)
        messages = json.loads(doctor.stdout)["messages"]
        claude = next(m for m in messages if m["key"] == "agent_claude")
        self.assertEqual(claude["params"]["commands"], len(V1_COMMANDS))
        self.assertEqual(claude["params"]["available"], len(V1_COMMANDS) + len(NEW_COMMANDS))
        self.assertTrue(any(m["key"] == "upgrade_hint" for m in messages), messages)

    def test_fresh_project_plan_is_unchanged(self):
        self.init()
        before = self.snapshot()
        plan = self.plan()
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(plan["to"], plan["from"])
        files = plan["files"]
        self.assertEqual(sorted(files["unchanged"]), sorted(self.metadata()["managed_files"]))
        for status in ("updatable", "conflict", "new", "missing", "obsolete"):
            self.assertEqual(files[status], [], status)

    def test_plan_classifies_every_status(self):
        self.init()
        self.as_v1_project()
        data = self.metadata()
        old = b"# Old original\n"
        for name in ("README.md", "docs/guide.md", "AGENTS.md"):
            data["managed_files"][name] = digest(old)
        (self.project / "README.md").write_bytes(old)
        (self.project / "docs/guide.md").write_text("# My own edits\n")
        (self.project / "AGENTS.md").unlink()
        data["managed_files"]["docs/retired.md"] = digest(b"gone\n")
        (self.project / "docs/retired.md").write_text("gone\n")
        (self.project / ".claude/commands/dixi.change.md").write_text("my own command\n")
        self.write_metadata(data)
        before = self.snapshot()
        plan = self.plan()
        self.assertEqual(self.snapshot(), before)
        files = plan["files"]
        self.assertEqual(plan["from"], "1.0.0")
        self.assertEqual(files["updatable"], ["README.md"])
        self.assertEqual(files["conflict"], [".claude/commands/dixi.change.md", "docs/guide.md"])
        self.assertEqual(files["missing"], ["AGENTS.md"])
        self.assertEqual(files["obsolete"], ["docs/retired.md"])
        self.assertEqual(files["new"], sorted(f".claude/commands/dixi.{n}.md" for n in NEW_COMMANDS
                                              if n != "change"))

    def test_human_output_lists_statuses(self):
        self.init()
        self.as_v1_project()
        result = self.cli("upgrade", "--dry-run")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(".claude/commands/dixi.domain.md", result.stdout)
        self.assertIn("No files were changed", result.stdout)

    def test_upgrade_requires_dry_run(self):
        self.init()
        before = self.snapshot()
        self.assertEqual(self.cli("upgrade").returncode, 2)
        self.assertEqual(self.snapshot(), before)

    def test_upgrade_requires_project(self):
        self.project.mkdir()
        self.assertEqual(self.cli("upgrade", "--dry-run").returncode, 2)

    def test_newer_project_is_rejected(self):
        self.init()
        data = self.metadata()
        data["kit_version"] = "1.99.0"
        self.write_metadata(data)
        self.assertEqual(self.cli("upgrade", "--dry-run").returncode, 4)

    def test_none_agent_plan(self):
        self.init(agent="none")
        files = self.plan()["files"]
        self.assertFalse(any(p.startswith(".claude/") for status in files.values() for p in status))

    def test_help_announces_upgrade(self):
        result = self.cli("--help", cwd=self.base)
        self.assertEqual(result.returncode, 0)
        self.assertIn("upgrade", result.stdout)


if __name__ == "__main__":
    unittest.main()
