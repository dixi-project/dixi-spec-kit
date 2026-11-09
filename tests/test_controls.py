import ast
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
CONTROLS = ("protect_tests.py", "guard_secrets.py", "guard_attestation.py", "mode_gate.py", "verify_on_stop.py")
SUBAGENTS = ("architect", "tester", "developer", "reviewer")
STDLIB = {"json", "os", "re", "shlex", "subprocess", "sys", "pathlib"}
SCRIPT = re.compile(r"\.dixi/hooks/([a-z_]+\.py)")


def git(cwd, *args):
    subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True)


class ControlsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()

    def cli(self, *args, cwd=None):
        env = dict(os.environ, PYTHONPATH=str(ROOT / "src"), PYTHONDONTWRITEBYTECODE="1")
        return subprocess.run([sys.executable, "-m", "dixi_spec_kit", *args], cwd=cwd or self.base, env=env,
                              text=True, capture_output=True, timeout=60)

    def init(self, name, *options):
        project = self.base / name
        result = self.cli("init", str(project), *options)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return project

    def repository(self, name="repo", agent="claude"):
        project = self.init(name, "--agent", agent, "--controls")
        git(project, "init", "-q", "-b", "main")
        git(project, "config", "user.email", "person@example.com")
        git(project, "config", "user.name", "Person")
        (project / "tests").mkdir()
        (project / "tests/test_frozen.py").write_text("def test_ok():\n    assert True\n")
        git(project, "add", "-A")
        git(project, "commit", "-qm", "initial")
        return project

    def hook(self, project, script, payload, env=None):
        data = payload if isinstance(payload, str) else json.dumps(payload)
        environment = dict(os.environ, CLAUDE_PROJECT_DIR=str(project), **(env or {}))
        if "DIXI_ALLOW_TEST_EDITS" not in (env or {}):
            environment.pop("DIXI_ALLOW_TEST_EDITS", None)
        return subprocess.run([sys.executable, str(project / ".dixi/hooks" / script)], input=data, cwd=project,
                              env=environment, text=True, capture_output=True, timeout=60)

    def assertBlocks(self, project, script, payload, blocked=True, env=None):
        result = self.hook(project, script, payload, env)
        self.assertEqual(result.returncode, 2 if blocked else 0, f"{payload}\n{result.stderr}")
        if blocked:
            self.assertTrue(result.stderr.strip(), "a block must explain itself on stderr")

    def bash(self, command):
        return {"hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": command}}

    def metadata(self, project):
        return json.loads((project / ".dixi/project.json").read_text())

    def test_default_installs_no_controls(self):
        for agent in ("none", "claude", "codex"):
            with self.subTest(agent=agent):
                project = self.init(f"plain-{agent}", "--agent", agent)
                for absent in (".dixi/hooks", ".claude/settings.json", ".codex"):
                    self.assertFalse((project / absent).exists(), absent)
                self.assertFalse(self.metadata(project)["controls"])

    def test_controls_require_an_agent(self):
        project = self.base / "none"
        result = self.cli("init", str(project), "--controls")
        self.assertEqual(result.returncode, 2)
        self.assertFalse(project.exists())

    def test_claude_wiring(self):
        project = self.init("claude", "--agent", "claude", "--controls")
        settings = json.loads((project / ".claude/settings.json").read_text())
        self.assertEqual(set(settings), {"hooks"})
        wiring = {}
        for event, groups in settings["hooks"].items():
            for group in groups:
                for handler in group["hooks"]:
                    self.assertEqual(handler["type"], "command")
                    self.assertIn("$CLAUDE_PROJECT_DIR", handler["command"])
                    wiring.setdefault((event, group.get("matcher", "")), []).extend(SCRIPT.findall(handler["command"]))
        self.assertEqual(wiring, {
            ("PreToolUse", "Bash"): ["mode_gate.py", "guard_secrets.py", "guard_attestation.py"],
            ("PreToolUse", "Read|Grep"): ["guard_secrets.py"],
            ("PreToolUse", "Edit|Write|MultiEdit|NotebookEdit"): ["protect_tests.py"],
            ("Stop", ""): ["verify_on_stop.py"],
            ("SubagentStop", ""): ["verify_on_stop.py"]})
        data = self.metadata(project)
        self.assertTrue(data["controls"])
        for name in [".claude/settings.json"] + [f".dixi/hooks/{script}" for script in CONTROLS]:
            self.assertEqual(hashlib.sha256((project / name).read_bytes()).hexdigest(), data["managed_files"][name])

    def test_codex_wiring(self):
        project = self.init("codex", "--agent", "codex", "--controls")
        config = json.loads((project / ".codex/hooks.json").read_text())
        self.assertEqual(set(config), {"hooks"})
        self.assertEqual(sorted(p.name for p in (project / ".codex").iterdir()), ["hooks.json"])
        wiring = {}
        for event, groups in config["hooks"].items():
            for group in groups:
                for handler in group["hooks"]:
                    self.assertEqual(handler["type"], "command")
                    self.assertIn("git rev-parse --show-toplevel", handler["command"])
                    wiring.setdefault((event, group.get("matcher", "")), []).extend(SCRIPT.findall(handler["command"]))
        self.assertEqual(wiring, {
            ("PreToolUse", "^Bash$"): ["mode_gate.py", "guard_secrets.py", "guard_attestation.py"],
            ("PreToolUse", "^apply_patch$"): ["protect_tests.py"],
            ("Stop", ""): ["verify_on_stop.py"],
            ("SubagentStop", ""): ["verify_on_stop.py"]})

    def test_configured_commands_run(self):
        for agent, path in (("claude", ".claude/settings.json"), ("codex", ".codex/hooks.json")):
            with self.subTest(agent=agent):
                project = self.repository(f"run-{agent}", agent)
                config = json.loads((project / path).read_text())
                command = next(h["command"] for g in config["hooks"]["PreToolUse"] for h in g["hooks"]
                               if "guard_attestation.py" in h["command"])
                result = subprocess.run(command, shell=True, cwd=project, text=True, capture_output=True,
                                        input=json.dumps(self.bash("git commit -s -m done")),
                                        env=dict(os.environ, CLAUDE_PROJECT_DIR=str(project)), timeout=60)
                self.assertEqual(result.returncode, 2, result.stderr)

    def test_scripts_are_standalone(self):
        project = self.init("standalone", "--agent", "claude", "--controls")
        for script in CONTROLS:
            with self.subTest(script=script):
                tree = ast.parse((project / ".dixi/hooks" / script).read_text())
                modules = {alias.name.split(".")[0] for node in ast.walk(tree) if isinstance(node, ast.Import)
                           for alias in node.names}
                modules |= {node.module.split(".")[0] for node in ast.walk(tree)
                            if isinstance(node, ast.ImportFrom) and node.module}
                self.assertTrue(modules <= STDLIB, modules - STDLIB)

    def test_protect_tests(self):
        project = self.repository()
        edit = lambda path: {"tool_name": "Edit", "tool_input": {"file_path": str(project / path)}}
        self.assertBlocks(project, "protect_tests.py", edit("tests/test_frozen.py"))
        self.assertBlocks(project, "protect_tests.py", {"tool_name": "Write", "tool_input": {"file_path": "tests/test_frozen.py"}})
        self.assertBlocks(project, "protect_tests.py", edit("tests/test_new.py"), blocked=False)
        self.assertBlocks(project, "protect_tests.py", edit("src/app.py"), blocked=False)
        self.assertBlocks(project, "protect_tests.py", edit("tests/test_frozen.py"), blocked=False,
                          env={"DIXI_ALLOW_TEST_EDITS": "1"})
        patch = lambda header: {"tool_name": "apply_patch", "tool_input": {
            "command": f"*** Begin Patch\n{header}\n@@\n-a\n+b\n*** End Patch\n"}}
        self.assertBlocks(project, "protect_tests.py", patch("*** Update File: tests/test_frozen.py"))
        self.assertBlocks(project, "protect_tests.py", patch("*** Delete File: tests/test_frozen.py"))
        self.assertBlocks(project, "protect_tests.py", patch("*** Add File: tests/test_other.py"), blocked=False)
        self.assertBlocks(project, "protect_tests.py", patch("*** Update File: src/app.py"), blocked=False)
        self.assertBlocks(project, "protect_tests.py", "not json")
        self.assertBlocks(project, "protect_tests.py", {"tool_name": "Edit"})

    def test_guard_secrets(self):
        project = self.repository()
        read = lambda path: {"tool_name": "Read", "tool_input": {"file_path": path}}
        for blocked in (read(".env"), read(str(project / ".env.production")), read("certs/server.pem"),
                        read("deploy/id_rsa"), {"tool_name": "Grep", "tool_input": {"path": ".aws/credentials"}},
                        self.bash("cat .env"), self.bash("grep KEY config/.env.local"),
                        self.bash("head -n 3 ~/.ssh/id_ed25519"), self.bash("source .env && run"),
                        self.bash("bash -c 'cat .env'"), "{", {"tool_name": "Read"}):
            with self.subTest(blocked=blocked):
                self.assertBlocks(project, "guard_secrets.py", blocked)
        for allowed in (read(".env.example"), read("src/app.py"), self.bash("cat .env.sample"),
                        self.bash("ls -la"), self.bash("grep -r TODO src")):
            with self.subTest(allowed=allowed):
                self.assertBlocks(project, "guard_secrets.py", allowed, blocked=False)

    def test_guard_attestation(self):
        project = self.repository()
        for blocked in ("git commit -s -m fix", "git commit --signoff -m fix",
                        "git commit -m 'fix' -m 'Signed-off-by: Person <person@example.com>'",
                        "git commit --trailer 'Signed-off-by: Person <person@example.com>' -m x",
                        "git rebase --signoff HEAD~1", "git cherry-pick --signoff abc123",
                        "gh pr merge 3 --merge", "gh pr review 3 --approve",
                        "gh pr edit 3 --body '- [x] I attest that a person reviewed this change'",
                        "env GIT_AUTHOR_NAME=x git commit -s -m x", "bash -c 'git commit -s -m x'",
                        "echo ok && git commit --signoff -m x", "not json at all"):
            with self.subTest(blocked=blocked):
                self.assertBlocks(project, "guard_attestation.py", blocked if blocked == "not json at all"
                                  else self.bash(blocked))
        message = project / "message.txt"
        message.write_text("fix\n\nSigned-off-by: Person <person@example.com>\n")
        self.assertBlocks(project, "guard_attestation.py", self.bash(f"git commit -F {message}"))
        for allowed in ("git commit -m 'fix: handle empty input'", "git log --oneline", "gh pr view 3",
                        "gh pr create --title x --body 'Summary'", "git status"):
            with self.subTest(allowed=allowed):
                self.assertBlocks(project, "guard_attestation.py", self.bash(allowed), blocked=False)

    def test_mode_gate(self):
        project = self.repository()
        dangerous = ("rm -rf /var/data", "git push --force origin main", "git push -f", "terraform apply",
                     "tofu destroy", "pulumi up", "cdk deploy", "kubectl delete pod web",
                     "kubectl apply -f prod.yaml", "psql -c 'DROP TABLE users'", "mysql -e 'truncate table logs'",
                     "git reset --hard HEAD~1")
        for command in dangerous:
            with self.subTest(mode="mvp", command=command):
                self.assertBlocks(project, "mode_gate.py", self.bash(command), blocked=False)
        (project / "MODE").write_text("prod\n")
        for command in dangerous:
            with self.subTest(mode="prod", command=command):
                self.assertBlocks(project, "mode_gate.py", self.bash(command))
        for command in ("rm -rf dist", "rm -rf build/tmp", "ls", "git push origin feature", "terraform plan"):
            with self.subTest(mode="prod", allowed=command):
                self.assertBlocks(project, "mode_gate.py", self.bash(command), blocked=False)
        self.assertBlocks(project, "mode_gate.py", "[]")

    def test_verify_on_stop(self):
        project = self.repository()
        stop = {"hook_event_name": "Stop", "stop_hook_active": False}
        self.assertBlocks(project, "verify_on_stop.py", stop, blocked=False)  # clean tree
        (project / "Makefile").write_text(".PHONY: verify\nverify:\n\t@exit 1\n")
        self.assertBlocks(project, "verify_on_stop.py", stop)  # changed tree, red verify
        self.assertBlocks(project, "verify_on_stop.py", dict(stop, stop_hook_active=True), blocked=False)
        self.assertBlocks(project, "verify_on_stop.py", "garbage", blocked=False)
        (project / "Makefile").write_text(".PHONY: verify\nverify:\n\t@exit 0\n")
        self.assertBlocks(project, "verify_on_stop.py", stop, blocked=False)
        (project / "Makefile").write_text("all:\n\t@exit 1\n")
        self.assertBlocks(project, "verify_on_stop.py", stop, blocked=False)  # no verify target

    def test_check_doctor_and_upgrade(self):
        for agent in ("claude", "codex"):
            with self.subTest(agent=agent):
                project = self.init(f"checked-{agent}", "--agent", agent, "--controls")
                self.assertEqual(self.cli("check", cwd=project).returncode, 0)
                doctor = json.loads(self.cli("--json", "doctor", cwd=project).stdout)["messages"]
                self.assertIn({"controls": True}, [m["params"] for m in doctor if m["key"] == "controls"])
        plain = self.init("plain", "--agent", "claude")
        plan = self.cli("--json", "upgrade", "--dry-run", "--controls", cwd=plain)
        self.assertEqual(plan.returncode, 0, plan.stdout + plan.stderr)
        new = set(json.loads(plan.stdout)["upgrade"]["files"]["new"])
        self.assertEqual(new, {".claude/settings.json"} | {f".dixi/hooks/{s}" for s in CONTROLS})
        data = self.metadata(plain)
        data["controls"] = "yes"
        (plain / ".dixi/project.json").write_text(json.dumps(data))
        self.assertEqual(self.cli("check", cwd=plain).returncode, 1)

    def test_subagents(self):
        for language in ("en", "es"):
            with self.subTest(language=language):
                project = self.base / f"agents-{language}"
                self.assertEqual(self.cli("--lang", language, "init", str(project), "--agent", "claude").returncode, 0)
                limits = (("frozen tests", "do not sign, approve or merge") if language == "en"
                          else ("pruebas congeladas", "no firmes, no apruebes ni integres"))
                for role in SUBAGENTS:
                    text = (project / f".claude/agents/dixi-{role}.md").read_text(encoding="utf-8")
                    match = re.match(r"---\nname: (.+)\ndescription: \"(.+)\"\n---\n", text)
                    self.assertIsNotNone(match, role)
                    self.assertEqual(match.group(1), f"dixi-{role}")
                    for phrase in limits:
                        self.assertIn(phrase, text.casefold(), f"{role}: {phrase}")
                data = self.metadata(project)
                del data["managed_files"][".claude/agents/dixi-tester.md"]
                (project / ".claude/agents/dixi-tester.md").unlink()
                (project / ".dixi/project.json").write_text(json.dumps(data))
                self.assertEqual(self.cli("check", cwd=project).returncode, 0)

    def test_new_operations(self):
        for language in ("en", "es"):
            with self.subTest(language=language):
                project = self.base / f"ops-{language}"
                self.assertEqual(self.cli("--lang", language, "init", str(project), "--agent", "claude").returncode, 0)
                interview = (project / ".claude/commands/dixi.interview.md").read_text(encoding="utf-8")
                review = (project / ".claude/commands/dixi.risk-review.md").read_text(encoding="utf-8")
                self.assertIn("dixi placeholders", interview)
                self.assertIn("{{pending", interview)
                self.assertIn("dixi pr-size", review)

    def test_agents_md_declares_wip_limit(self):
        for language in ("en", "es"):
            with self.subTest(language=language):
                project = self.base / f"wip-{language}"
                self.assertEqual(self.cli("--lang", language, "init", str(project), "--agent", "claude").returncode, 0)
                self.assertRegex((project / "AGENTS.md").read_text(encoding="utf-8"), r"wip_limit: 3")
                self.assertIn("wip_limit", (project / ".claude/commands/dixi.build.md").read_text(encoding="utf-8"))

    def test_placeholders(self):
        project = self.init("pending")
        (project / "docs/extra.md").write_text("# Extra\n\n{{pending: a}} and {{pending: b}}\n\n"
                                              "```\n{{pending: in code}}\n```\n\n`{{pending: inline}}`\n")
        data = self.metadata(project)
        data["managed_files"]["docs/extra.md"] = hashlib.sha256((project / "docs/extra.md").read_bytes()).hexdigest()
        (project / ".dixi/project.json").write_text(json.dumps(data))
        result = self.cli("--json", "placeholders", cwd=project)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        output = json.loads(result.stdout)
        self.assertEqual(output["placeholders"]["docs/extra.md"], 2)
        self.assertEqual(output["total"], sum(output["placeholders"].values()))
        self.assertEqual(self.cli("placeholders", "--strict", cwd=project).returncode, 1)
        empty = self.base / "empty"
        empty.mkdir()
        self.assertEqual(self.cli("placeholders", cwd=empty).returncode, 2)

    def test_pr_size(self):
        project = self.repository("sized")
        git(project, "switch", "-q", "-c", "feature")
        (project / "src").mkdir()
        (project / "src/app.py").write_text("".join(f"line_{i} = {i}\n" for i in range(30)))
        (project / "tests/test_app.py").write_text("".join(f"# t{i}\n" for i in range(10)))
        (project / "docs/notes.md").write_text("".join(f"note {i}\n" for i in range(50)))
        git(project, "add", "-A")
        git(project, "commit", "-qm", "feature")
        result = self.cli("--json", "pr-size", "--base", "main", cwd=project)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        size = json.loads(result.stdout)["pr_size"]
        self.assertEqual((size["counted"], size["tests"], size["max"]), (30, 10, 1500))
        self.assertEqual(self.cli("pr-size", "--base", "main", "--max", "20", cwd=project).returncode, 1)
        self.assertEqual(self.cli("pr-size", "--base", "missing-branch", cwd=project).returncode, 2)
        status = subprocess.run(["git", "status", "--porcelain"], cwd=project, capture_output=True, text=True)
        self.assertEqual(status.stdout, "")


if __name__ == "__main__":
    unittest.main()
