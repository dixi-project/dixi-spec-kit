import hashlib
import json
import os
from pathlib import Path
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile


ROOT = Path(__file__).resolve().parents[1]
COMMANDS = ("discover", "specify", "clarify", "plan", "tasks", "build", "verify", "review", "analyze", "status",
            "domain", "architecture", "contract", "threat-model", "handoff", "change",
            "data", "quality", "ai", "release", "promote", "operate", "finops", "compliance", "duediligence",
            "interview", "risk-review", "constitution", "checklist", "converge")
SUBAGENTS = ("architect", "tester", "developer", "reviewer")
WORKFLOW_OPERATIONS = {"discover", "specify", "clarify", "domain", "architecture", "contract", "threat-model", "plan",
                       "constitution", "checklist", "converge"}
CLI_COMMANDS = {"init", "doctor", "check", "workflow", "placeholders", "pr-size",
                "--help", "--version", "--lang", "--json"}
LIMITS = {
    "es": ("pruebas congeladas", "no firmes, no apruebes ni integres", "$ARGUMENTS", "dixi check"),
    "en": ("frozen tests", "do not sign, approve or merge", "$ARGUMENTS", "dixi check"),
}


class ClaudeAdapterTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.project = self.base / "project"

    def env(self):
        return dict(os.environ, PYTHONPATH=str(ROOT / "src"), PYTHONDONTWRITEBYTECODE="1")

    def cli(self, *args, cwd=None, network_guard=False):
        command = [sys.executable, "-m", "dixi_spec_kit"]
        if network_guard:
            command = [sys.executable, "-c", "import socket, runpy; "
                       "socket.socket=lambda *a, **k: (_ for _ in ()).throw(AssertionError('network')); "
                       "runpy.run_module('dixi_spec_kit', run_name='__main__')"]
        return subprocess.run(command + list(args), cwd=cwd or self.base, env=self.env(),
                              text=True, capture_output=True, timeout=10)

    def init(self, language="es"):
        result = self.cli("--lang", language, "init", str(self.project), "--agent", "claude", network_guard=True)
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        return self.project

    def metadata(self):
        return json.loads((self.project / ".dixi/project.json").read_text())

    def snapshot(self):
        return {str(p.relative_to(self.project)): hashlib.sha256(p.read_bytes()).hexdigest()
                for p in self.project.rglob("*") if p.is_file() and not p.is_symlink()}

    def command_texts(self, language):
        self.init(language)
        return {name: (self.project / ".claude/commands" / f"dixi.{name}.md").read_text(encoding="utf-8")
                for name in COMMANDS}

    def test_init_help_announces_claude(self):
        result = self.cli("init", "--help")
        self.assertEqual(result.returncode, 0)
        self.assertIn("claude", result.stdout)
        self.assertNotIn("cursor", result.stdout)

    def test_installs_only_commands(self):
        self.init()
        installed = sorted(p.name for p in (self.project / ".claude").rglob("*") if p.is_file())
        self.assertEqual(installed, sorted([f"dixi.{name}.md" for name in COMMANDS] +
                                           [f"dixi-{name}.md" for name in SUBAGENTS]))
        self.assertEqual(sorted(p.name for p in (self.project / ".claude").iterdir()), ["agents", "commands"])
        self.assertFalse((self.project / ".mcp.json").exists())
        self.assertFalse((self.project / ".git").exists())
        self.assertIn("@AGENTS.md", (self.project / "CLAUDE.md").read_text())
        metadata = self.metadata()
        self.assertEqual(metadata["agent"], "claude")
        for name in ["CLAUDE.md"] + [f".claude/commands/dixi.{c}.md" for c in COMMANDS]:
            self.assertIn(name, metadata["managed_files"])
            self.assertEqual(hashlib.sha256((self.project / name).read_bytes()).hexdigest(),
                             metadata["managed_files"][name])

    def test_none_agent_unchanged(self):
        result = self.cli("init", str(self.project), "--agent", "none")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse((self.project / ".claude").exists())
        self.assertFalse((self.project / "CLAUDE.md").exists())

    def test_existing_claude_dir_untouched(self):
        own = self.project / ".claude/commands/dixi.plan.md"
        own.parent.mkdir(parents=True)
        own.write_text("mine")
        before = self.snapshot()
        result = self.cli("init", str(self.project), "--agent", "claude")
        self.assertEqual(result.returncode, 3)
        self.assertEqual(self.snapshot(), before)

    def test_frontmatter(self):
        for language in ("es", "en"):
            with self.subTest(language=language):
                for name, text in self.command_texts(language).items():
                    match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
                    self.assertIsNotNone(match, name)
                    fields = dict(line.split(": ", 1) for line in match.group(1).splitlines())
                    self.assertEqual(set(fields), {"description", "argument-hint"}, name)
                    self.assertTrue(all(value.strip() for value in fields.values()), name)
                shutil.rmtree(self.project)

    def test_commands_declare_limits(self):
        for language in ("es", "en"):
            with self.subTest(language=language):
                for name, text in self.command_texts(language).items():
                    lowered = text.casefold()
                    for phrase in LIMITS[language]:
                        self.assertIn(phrase.casefold(), lowered, f"{language}/{name}: {phrase}")
                shutil.rmtree(self.project)

    def test_commands_avoid_dangerous_operations(self):
        for language in ("es", "en"):
            with self.subTest(language=language):
                for name, text in self.command_texts(language).items():
                    for forbidden in ("git push", "--no-verify", "allowed-tools", "rm -rf", "sudo ",
                                      "/Users/", "/home/", "http://", "https://"):
                        self.assertNotIn(forbidden, text, f"{language}/{name}")
                shutil.rmtree(self.project)

    def test_commands_reference_existing_operations(self):
        for language in ("es", "en"):
            with self.subTest(language=language):
                texts = self.command_texts(language)
                for name, text in texts.items():
                    for sub in re.findall(r"`dixi ([a-z-]+)", text):
                        self.assertIn(sub, CLI_COMMANDS, f"{language}/{name}: dixi {sub}")
                    for op in re.findall(r"dixi workflow (?:prepare|show) ([a-z-]+)", text):
                        self.assertIn(op, WORKFLOW_OPERATIONS, f"{language}/{name}: {op}")
                    for other in re.findall(r"/dixi\.([a-z-]+)", text):
                        self.assertIn(other, COMMANDS, f"{language}/{name}: /dixi.{other}")
                for name in ("build", "verify"):
                    self.assertIn("make verify", texts[name])
                for name in ("discover", "specify", "clarify", "plan"):
                    self.assertIn(f"dixi workflow prepare {name}", texts[name])
                shutil.rmtree(self.project)

    def test_language_parity(self):
        es = self.command_texts("es")
        shutil.rmtree(self.project)
        en = self.command_texts("en")
        self.assertEqual(es.keys(), en.keys())
        self.assertNotEqual(es["plan"], en["plan"])

    def test_generated_claude_project_passes(self):
        self.init()
        result = self.cli("--json", "check", cwd=self.project)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        doctor = self.cli("--json", "doctor", cwd=self.project)
        self.assertEqual(doctor.returncode, 0, doctor.stdout + doctor.stderr)
        messages = json.loads(doctor.stdout)["messages"]
        claude = [m for m in messages if m["key"] == "agent_claude"]
        self.assertEqual(len(claude), 1, messages)
        self.assertEqual(claude[0]["params"]["commands"], len(COMMANDS))

    def test_check_detects_deleted_command(self):
        self.init()
        (self.project / ".claude/commands/dixi.build.md").unlink()
        result = self.cli("--json", "check", cwd=self.project)
        self.assertEqual(result.returncode, 1)
        data = json.loads(result.stdout)
        self.assertTrue(any(m["key"] == "missing_file" and m["params"].get("path") == ".claude/commands/dixi.build.md"
                            for m in data["messages"]), data)

    def test_unknown_agent_metadata(self):
        self.init()
        data = self.metadata()
        data["agent"] = "codex"
        (self.project / ".dixi/project.json").write_text(json.dumps(data))
        self.assertEqual(self.cli("check", cwd=self.project).returncode, 1)

    def test_incomplete_adapter_inventory(self):
        self.init()
        data = self.metadata()
        del data["managed_files"][".claude/commands/dixi.review.md"]
        (self.project / ".dixi/project.json").write_text(json.dumps(data))
        self.assertEqual(self.cli("check", cwd=self.project).returncode, 1)

    def test_wheel_contains_adapter_resources(self):
        wheels = list((ROOT / "dist").glob("dixi_spec_kit-*.whl"))
        self.assertEqual(len(wheels), 1, "Build exactly one wheel before verification")
        with zipfile.ZipFile(wheels[0]) as archive:
            names = set(archive.namelist())
        for language in ("es", "en"):
            self.assertIn(f"dixi_spec_kit/resources/claude/{language}/CLAUDE.md", names)
            for name in COMMANDS:
                self.assertIn(f"dixi_spec_kit/resources/claude/{language}/dixi.{name}.md", names)

    def test_example_passes_check_and_verify(self):
        example = ROOT / "examples/notes"
        self.assertTrue((example / ".dixi/project.json").is_file(), "examples/notes is missing")
        work = self.base / "notes"
        shutil.copytree(example, work, ignore=shutil.ignore_patterns("__pycache__"))
        shim = self.base / "bin"
        shim.mkdir()
        (shim / "dixi").write_text(f"#!/bin/sh\nexec {shlex.quote(sys.executable)} -m dixi_spec_kit \"$@\"\n")
        (shim / "dixi").chmod(0o755)
        env = dict(self.env(), PATH=str(shim) + os.pathsep + os.environ["PATH"])
        check = subprocess.run([sys.executable, "-m", "dixi_spec_kit", "check"], cwd=work, env=env,
                               text=True, capture_output=True, timeout=20)
        self.assertEqual(check.returncode, 0, check.stdout + check.stderr)
        verify = subprocess.run(["make", "verify"], cwd=work, env=env, text=True, capture_output=True, timeout=60)
        self.assertEqual(verify.returncode, 0, verify.stdout + verify.stderr)
        self.assertRegex(verify.stdout + verify.stderr, r"Ran [1-9]\d* tests?")


if __name__ == "__main__":
    unittest.main()
