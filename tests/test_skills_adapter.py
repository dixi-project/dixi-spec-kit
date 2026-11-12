"""ADR-108 phase D: `--agent skills` installs every operation as an Agent Skill (agentskills.io) in .agents/skills/."""
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from dixi_spec_kit.core import CLAUDE_COMMANDS  # noqa: E402

NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


class SkillsAdapterTests(unittest.TestCase):
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

    def init(self, name, language="en", *extra):
        project = self.base / name
        result = self.cli("--lang", language, "init", str(project), "--agent", "skills", *extra)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return project

    def frontmatter(self, text):
        self.assertTrue(text.startswith("---\n"))
        header, body = text[4:].split("\n---\n", 1)
        fields = dict(line.split(": ", 1) for line in header.splitlines())
        return fields, body

    def test_installs_every_operation_as_a_conforming_skill(self):
        for language in ("en", "es"):
            with self.subTest(language=language):
                project = self.init(f"p-{language}", language)
                skills = sorted(p.name for p in (project / ".agents/skills").iterdir())
                self.assertEqual(skills, sorted(f"dixi-{op}" for op in CLAUDE_COMMANDS))
                for folder in skills:
                    text = (project / ".agents/skills" / folder / "SKILL.md").read_text(encoding="utf-8")
                    fields, body = self.frontmatter(text)
                    self.assertEqual(fields["name"], folder, "name must match the parent folder")
                    self.assertRegex(fields["name"], NAME)
                    self.assertLessEqual(len(fields["name"]), 64)
                    description = fields["description"].strip('"')
                    self.assertTrue(1 <= len(description) <= 1024)
                    self.assertEqual(fields["disable-model-invocation"], "true")
                    for foreign in ("$ARGUMENTS", "$dixi-", "/dixi."):
                        self.assertNotIn(foreign, body, f"{folder}: {foreign}")
                    self.assertTrue((project / ".agents/skills" / folder / "agents/openai.yaml").is_file())

    def test_installs_no_agent_specific_folders(self):
        project = self.init("plain")
        for absent in (".claude", ".codex", ".cursor", ".github", ".gemini", ".opencode", "CLAUDE.md"):
            self.assertFalse((project / absent).exists(), absent)
        self.assertTrue((project / "AGENTS.md").is_file())

    def test_check_doctor_and_upgrade_recognise_the_adapter(self):
        project = self.init("checked")
        self.assertEqual(self.cli("check", cwd=project).returncode, 0)
        doctor = json.loads(self.cli("--json", "doctor", cwd=project).stdout)
        self.assertIn("agent_skills", [m["key"] for m in doctor["messages"]])
        plan = json.loads(self.cli("--json", "upgrade", "--dry-run", cwd=project).stdout)["upgrade"]["files"]
        for status in ("updatable", "conflict", "new", "missing", "obsolete"):
            self.assertEqual(plan[status], [], status)

    def test_controls_are_not_available_for_generic_skills(self):
        result = self.cli("init", str(self.base / "ctl"), "--agent", "skills", "--controls")
        self.assertEqual(result.returncode, 2)
        self.assertFalse((self.base / "ctl").exists())

    def test_messages_in_both_languages(self):
        for lang in ("en", "es"):
            catalog = json.loads((ROOT / f"src/dixi_spec_kit/locales/{lang}.json").read_text(encoding="utf-8"))
            self.assertIn("agent_skills", catalog)


if __name__ == "__main__":
    unittest.main()
