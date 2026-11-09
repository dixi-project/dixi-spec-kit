import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
import zipfile


ROOT = Path(__file__).resolve().parents[1]
OPERATIONS = ("discover", "specify", "clarify", "plan", "tasks", "build", "verify", "review", "analyze", "status",
              "domain", "architecture", "contract", "threat-model", "handoff", "change",
              "data", "quality", "ai", "release", "promote", "operate", "finops", "compliance", "duediligence",
              "interview", "risk-review")
V1 = OPERATIONS[:10]
NAME = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*")
LIMITS = {
    "es": ("pruebas congeladas", "no firmes, no apruebes ni integres", "dixi check"),
    "en": ("frozen tests", "do not sign, approve or merge", "dixi check"),
}


class CodexAdapterTests(unittest.TestCase):
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
        return subprocess.run(command + list(args), cwd=cwd or self.base, env=env,
                              text=True, capture_output=True, timeout=10)

    def init(self, language="en"):
        self.project = self.base / language
        result = self.cli("--lang", language, "init", str(self.project), "--agent", "codex")
        self.assertEqual(result.returncode, 0, result.stderr)

    def skill(self, operation):
        return (self.project / f".agents/skills/dixi-{operation}/SKILL.md").read_text(encoding="utf-8")

    def metadata(self):
        return json.loads((self.project / ".dixi/project.json").read_text())

    def test_init_help_announces_codex(self):
        result = self.cli("init", "--help")
        self.assertIn("codex", result.stdout)

    def test_installs_only_skills(self):
        self.init()
        installed = sorted(str(p.relative_to(self.project)) for p in (self.project / ".agents").rglob("*")
                           if p.is_file())
        expected = sorted([f".agents/skills/dixi-{op}/SKILL.md" for op in OPERATIONS] +
                          [f".agents/skills/dixi-{op}/agents/openai.yaml" for op in OPERATIONS])
        self.assertEqual(installed, expected)
        for absent in (".codex", ".claude", "CLAUDE.md", ".mcp.json", ".git"):
            self.assertFalse((self.project / absent).exists(), absent)
        metadata = self.metadata()
        self.assertEqual(metadata["agent"], "codex")
        for name in expected:
            self.assertEqual(hashlib.sha256((self.project / name).read_bytes()).hexdigest(),
                             metadata["managed_files"][name])

    def test_frontmatter_follows_agent_skills_spec(self):
        for language in ("es", "en"):
            with self.subTest(language=language):
                self.init(language)
                for op in OPERATIONS:
                    text = self.skill(op)
                    match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
                    self.assertIsNotNone(match, op)
                    fields = dict(line.split(": ", 1) for line in match.group(1).splitlines())
                    self.assertEqual(set(fields), {"name", "description"}, op)
                    self.assertEqual(fields["name"], f"dixi-{op}")
                    self.assertTrue(NAME.fullmatch(fields["name"]) and len(fields["name"]) <= 64)
                    self.assertTrue(1 <= len(fields["description"]) <= 1024, op)

    def test_implicit_invocation_disabled(self):
        self.init()
        for op in OPERATIONS:
            policy = (self.project / f".agents/skills/dixi-{op}/agents/openai.yaml").read_text()
            self.assertEqual(policy, "policy:\n  allow_implicit_invocation: false\n")

    def test_bodies_keep_limits_and_use_codex_syntax(self):
        for language in ("es", "en"):
            with self.subTest(language=language):
                self.init(language)
                for op in OPERATIONS:
                    text = self.skill(op)
                    lowered = text.casefold()
                    for phrase in LIMITS[language]:
                        self.assertIn(phrase.casefold(), lowered, f"{language}/{op}: {phrase}")
                    for forbidden in ("$ARGUMENTS", "/dixi.", "argument-hint", "allowed-tools", "git push",
                                      "--no-verify", "https://", "http://"):
                        self.assertNotIn(forbidden, text, f"{language}/{op}: {forbidden}")
                    for other in re.findall(r"\$dixi-([a-z-]+)", text):
                        self.assertIn(other, OPERATIONS, f"{language}/{op}: $dixi-{other}")
                self.assertIn("make verify", self.skill("build"))
                self.assertIn("dixi workflow prepare domain", self.skill("domain"))

    def test_generated_codex_project_passes(self):
        self.init()
        check = self.cli("--json", "check", cwd=self.project)
        self.assertEqual(check.returncode, 0, check.stdout)
        doctor = self.cli("--json", "doctor", cwd=self.project)
        self.assertEqual(doctor.returncode, 0, doctor.stdout)
        messages = json.loads(doctor.stdout)["messages"]
        codex = [m for m in messages if m["key"] == "agent_codex"]
        self.assertEqual(len(codex), 1, messages)
        self.assertEqual(codex[0]["params"]["skills"], len(OPERATIONS))
        self.assertEqual(codex[0]["params"]["available"], len(OPERATIONS))

    def test_required_skills_are_checked(self):
        self.init()
        (self.project / ".agents/skills/dixi-build/SKILL.md").unlink()
        self.assertEqual(self.cli("check", cwd=self.project).returncode, 1)
        data = self.metadata()
        del data["managed_files"][".agents/skills/dixi-review/agents/openai.yaml"]
        (self.project / ".dixi/project.json").write_text(json.dumps(data))
        self.assertEqual(self.cli("check", cwd=self.project).returncode, 1)

    def test_newer_skills_are_optional(self):
        self.init()
        data = self.metadata()
        for op in OPERATIONS[10:]:
            for suffix in ("SKILL.md", "agents/openai.yaml"):
                name = f".agents/skills/dixi-{op}/{suffix}"
                del data["managed_files"][name]
                (self.project / name).unlink()
        (self.project / ".dixi/project.json").write_text(json.dumps(data))
        self.assertEqual(self.cli("check", cwd=self.project).returncode, 0)
        plan = self.cli("--json", "upgrade", "--dry-run", cwd=self.project)
        self.assertEqual(plan.returncode, 0, plan.stdout)
        new = json.loads(plan.stdout)["upgrade"]["files"]["new"]
        self.assertEqual(len(new), 2 * len(OPERATIONS[10:]))

    def test_existing_agents_dir_untouched(self):
        own = self.project / ".agents/skills/mine/SKILL.md"
        own.parent.mkdir(parents=True)
        own.write_text("mine")
        self.assertEqual(self.cli("init", str(self.project), "--agent", "codex").returncode, 3)
        self.assertEqual(own.read_text(), "mine")
        self.assertFalse((self.project / ".dixi").exists())

    def test_wheel_contains_codex_resources(self):
        wheels = list((ROOT / "dist").glob("dixi_spec_kit-*.whl"))
        self.assertEqual(len(wheels), 1, "Build exactly one wheel before verification")
        with zipfile.ZipFile(wheels[0]) as archive:
            names = set(archive.namelist())
        for language in ("es", "en"):
            for op in OPERATIONS:
                self.assertIn(f"dixi_spec_kit/resources/codex/{language}/dixi-{op}.md", names)


if __name__ == "__main__":
    unittest.main()
