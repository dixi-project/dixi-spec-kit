"""ADR-109: local, data-only presets override kit operation texts and templates (threat T15)."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
PLAN_EN = '---\ndescription: "Plan with our checklist"\nargument-hint: "[feature]"\n---\n\n# /dixi.plan\n\nOur plan for `$ARGUMENTS`.\n'
PLAN_ES = '---\ndescription: "Planificar con nuestra lista"\nargument-hint: "[feature]"\n---\n\n# /dixi.plan\n\nNuestro plan para `$ARGUMENTS`.\n'
GUIDE = {"en": "# Team guide\n\nOur way of working.\n", "es": "# Guía del equipo\n\nNuestra forma de trabajar.\n"}


def digest(data):
    return hashlib.sha256(data).hexdigest()


class PresetTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()

    def cli(self, *args, cwd=None):
        env = dict(os.environ, PYTHONPATH=str(ROOT / "src"), PYTHONDONTWRITEBYTECODE="1")
        command = [sys.executable, "-c", "import socket, runpy; "
                   "socket.socket=lambda *a, **k: (_ for _ in ()).throw(AssertionError('network')); "
                   "runpy.run_module('dixi_spec_kit', run_name='__main__')"]
        return subprocess.run(command + list(args), cwd=cwd or self.base, env=env,
                              text=True, capture_output=True, timeout=20)

    def project(self, agent="claude", language="en", name="project"):
        path = self.base / name
        self.assertEqual(self.cli("--lang", language, "init", str(path), "--agent", agent).returncode, 0)
        return path

    def preset(self, name="team", preset_id="team", priority=50, operations=True, templates=True):
        folder = self.base / name
        folder.mkdir()
        (folder / "preset.json").write_text(json.dumps({"id": preset_id, "version": "1.0.0", "priority": priority}))
        for lang, plan in (("en", PLAN_EN), ("es", PLAN_ES)):
            if operations:
                (folder / f"operations/{lang}").mkdir(parents=True)
                (folder / f"operations/{lang}/plan.md").write_text(plan)
            if templates:
                (folder / f"templates/{lang}/docs").mkdir(parents=True)
                (folder / f"templates/{lang}/docs/guide.md").write_text(GUIDE[lang])
        return folder

    def snapshot(self, path):
        return {str(p.relative_to(path)): digest(p.read_bytes()) for p in path.rglob("*") if p.is_file()}

    def add(self, project, folder):
        return self.cli("--json", "preset", "add", str(folder), cwd=project)

    def test_overrides_unedited_kit_files(self):
        project = self.project("claude")
        kit_plan = (project / ".claude/commands/dixi.plan.md").read_text()
        result = self.add(project, self.preset())
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual((project / ".claude/commands/dixi.plan.md").read_text(), PLAN_EN)
        self.assertEqual((project / "docs/guide.md").read_text(), GUIDE["en"])
        data = json.loads((project / ".dixi/project.json").read_text())
        self.assertIn("team", data["presets"])
        self.assertEqual(data["managed_files"][".claude/commands/dixi.plan.md"], digest(kit_plan.encode()),
                         "the kit inventory keeps the kit hash, so upgrade never overwrites the preset")
        self.assertEqual(self.cli("check", cwd=project).returncode, 0)
        plan = json.loads(self.cli("--json", "upgrade", "--dry-run", cwd=project).stdout)["upgrade"]["files"]
        self.assertNotIn(".claude/commands/dixi.plan.md", plan["updatable"])

    def test_skills_get_the_converted_text(self):
        project = self.project("skills")
        self.assertEqual(self.add(project, self.preset()).returncode, 0)
        text = (project / ".agents/skills/dixi-plan/SKILL.md").read_text()
        self.assertTrue(text.startswith("---\nname: dixi-plan\n"))
        self.assertIn("disable-model-invocation: true", text)
        self.assertNotIn("$ARGUMENTS", text)

    def test_edited_files_and_project_overrides_win(self):
        project = self.project("claude")
        (project / "docs/guide.md").write_text("# Mine\n")
        (project / ".dixi/overrides/operations/en").mkdir(parents=True)
        (project / ".dixi/overrides/operations/en/plan.md").write_text(PLAN_EN.replace("Our", "My"))
        result = json.loads(self.add(project, self.preset()).stdout)["preset"]
        self.assertEqual((project / "docs/guide.md").read_text(), "# Mine\n")
        self.assertIn("docs/guide.md", result["kept"])
        self.assertIn(".claude/commands/dixi.plan.md", result["kept"])

    def test_higher_priority_preset_wins(self):
        project = self.project("claude")
        self.assertEqual(self.add(project, self.preset("high", "high", priority=90, templates=False)).returncode, 0)
        low = self.preset("low", "low", priority=10, templates=False)
        (low / "operations/en/plan.md").write_text(PLAN_EN.replace("Our", "Low"))
        result = json.loads(self.add(project, low).stdout)["preset"]
        self.assertIn(".claude/commands/dixi.plan.md", result["kept"])
        self.assertEqual((project / ".claude/commands/dixi.plan.md").read_text(), PLAN_EN)

    def test_crafted_presets_are_refused_without_writing(self):
        project = self.project("claude")
        before = self.snapshot(project)
        unknown_op = self.preset("unknown-op", "unknown-op", templates=False)
        (unknown_op / "operations/en/deploy.md").write_text(PLAN_EN)
        (unknown_op / "operations/es/deploy.md").write_text(PLAN_ES)
        unknown_tpl = self.preset("unknown-tpl", "unknown-tpl", operations=False)
        (unknown_tpl / "templates/en/evil.md").write_text("# x\n")
        (unknown_tpl / "templates/es/evil.md").write_text("# x\n")
        script = self.preset("script", "script")
        (script / "run.sh").write_text("echo\n")
        link = self.preset("link", "link")
        (link / "templates/en/docs/guide.md").unlink()
        (link / "templates/en/docs/guide.md").symlink_to(self.base / "script/run.sh")
        bad_priority = self.base / "bad-priority"
        bad_priority.mkdir()
        (bad_priority / "preset.json").write_text(json.dumps({"id": "bp", "version": "1.0.0", "priority": 500}))
        for folder in (unknown_op, unknown_tpl, script, link, bad_priority):
            with self.subTest(folder=folder.name):
                self.assertEqual(self.add(project, folder).returncode, 2, folder.name)
                self.assertEqual(self.snapshot(project), before)

    def test_remove_restores_kit_text_and_keeps_edits(self):
        project = self.project("claude")
        kit_plan = (project / ".claude/commands/dixi.plan.md").read_bytes()
        self.assertEqual(self.add(project, self.preset()).returncode, 0)
        (project / "docs/guide.md").write_text("# Edited after the preset\n")
        result = self.cli("--json", "preset", "remove", "team", cwd=project)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual((project / ".claude/commands/dixi.plan.md").read_bytes(), kit_plan)
        self.assertEqual((project / "docs/guide.md").read_text(), "# Edited after the preset\n")
        self.assertIn("docs/guide.md", json.loads(result.stdout)["preset"]["kept"])
        self.assertNotIn("presets", json.loads((project / ".dixi/project.json").read_text()))

    def test_messages_in_both_languages(self):
        for lang in ("en", "es"):
            catalog = json.loads((ROOT / f"src/dixi_spec_kit/locales/{lang}.json").read_text(encoding="utf-8"))
            for key in ("preset", "preset_add", "preset_list", "preset_remove", "preset_added", "preset_removed",
                        "invalid_preset", "preset_missing"):
                self.assertIn(key, catalog)


if __name__ == "__main__":
    unittest.main()
