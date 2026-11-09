import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


def git(cwd, *args):
    subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True)


class ProtectTestsShellTests(unittest.TestCase):
    """protect_tests also stops shell commands that write, move or delete a committed test."""

    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.base = Path(cls.temp.name).resolve()
        cls.projects = {}
        for agent in ("claude", "codex"):
            project = cls.base / agent
            env = dict(os.environ, PYTHONPATH=str(ROOT / "src"), PYTHONDONTWRITEBYTECODE="1")
            result = subprocess.run([sys.executable, "-m", "dixi_spec_kit", "init", str(project), "--agent", agent,
                                     "--controls"], env=env, text=True, capture_output=True, timeout=60)
            assert result.returncode == 0, result.stdout + result.stderr
            git(project, "init", "-q", "-b", "main")
            git(project, "config", "user.email", "person@example.com")
            git(project, "config", "user.name", "Person")
            (project / "tests").mkdir()
            (project / "tests/test_frozen.py").write_text("def test_ok():\n    assert True\n")
            (project / "src").mkdir()
            (project / "src/app.py").write_text("VALUE = 1\n")
            (project / "build").mkdir()
            (project / "build/out.txt").write_text("x\n")
            git(project, "add", "-A")
            git(project, "commit", "-qm", "initial")
            cls.projects[agent] = project

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def run_hook(self, agent, command, env=None, cwd=None):
        project = self.projects[agent]
        payload = {"hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": command},
                   "cwd": str(cwd or project)}
        environment = dict(os.environ, **(env or {}))
        environment.pop("DIXI_ALLOW_TEST_EDITS", None)
        environment.update(env or {})
        if agent == "claude":
            environment["CLAUDE_PROJECT_DIR"] = str(project)
        else:
            environment.pop("CLAUDE_PROJECT_DIR", None)
        return subprocess.run([sys.executable, str(project / ".dixi/hooks/protect_tests.py")], input=json.dumps(payload),
                              cwd=cwd or project, env=environment, text=True, capture_output=True, timeout=60)

    def check(self, command, blocked, **options):
        for agent in ("claude", "codex"):
            with self.subTest(agent=agent, command=command):
                result = self.run_hook(agent, command, **options)
                self.assertEqual(result.returncode, 2 if blocked else 0, result.stderr)
                if blocked:
                    self.assertIn("DIXI protect_tests", result.stderr)

    def test_blocks_shell_writes_to_a_committed_test(self):
        for command in (
                "sed -i 's/True/False/' tests/test_frozen.py",
                "sed -i.bak -e 's/True/False/' tests/test_frozen.py",
                "perl -pi -e 's/True/False/' tests/test_frozen.py",
                "echo 'def test_ok(): assert False' > tests/test_frozen.py",
                "echo x >> tests/test_frozen.py",
                "printf x>tests/test_frozen.py",
                "cat src/app.py | tee tests/test_frozen.py",
                "tee -a tests/test_frozen.py < src/app.py",
                "cp src/app.py tests/test_frozen.py",
                "mv tests/test_frozen.py tests/old.py",
                "mv src/app.py tests/test_frozen.py",
                "rm tests/test_frozen.py",
                "rm -rf tests",
                "rm -f ./tests/*.py",
                "git rm -q tests/test_frozen.py",
                "git mv tests/test_frozen.py tests/test_moved.py",
                "truncate -s 0 tests/test_frozen.py",
                "dd if=/dev/null of=tests/test_frozen.py",
                "cd tests && rm test_frozen.py",
                "bash -c \"echo x > tests/test_frozen.py\"",
                "env LANG=C sed -i 's/a/b/' tests/test_frozen.py",
                "ls; rm tests/test_frozen.py",
        ):
            self.check(command, blocked=True)

    def test_blocks_absolute_paths_inside_the_project(self):
        for agent in ("claude", "codex"):
            project = self.projects[agent]
            result = self.run_hook(agent, f"rm {project}/tests/test_frozen.py")
            self.assertEqual(result.returncode, 2, result.stderr)

    def test_resolves_paths_from_the_tool_cwd(self):
        for agent in ("claude", "codex"):
            project = self.projects[agent]
            result = self.run_hook(agent, "rm test_frozen.py", cwd=project / "tests")
            self.assertEqual(result.returncode, 2, result.stderr)

    def test_allows_reading_running_and_other_files(self):
        for command in (
                "cat tests/test_frozen.py",
                "grep -n assert tests/test_frozen.py",
                "sed -n 1p tests/test_frozen.py",
                "python3 -m unittest discover -s tests",
                "cp tests/test_frozen.py build/copy.py",
                "cat tests/test_frozen.py > build/out.txt",
                "echo x > tests/test_new.py",
                "sed -i 's/1/2/' src/app.py",
                "rm -rf build",
                "make verify 2>&1 | tail -5",
                "git commit -m 'touch tests/test_frozen.py'",
                "git add tests/test_new.py",
        ):
            self.check(command, blocked=False)

    def test_the_person_can_allow_shell_edits(self):
        self.check("rm tests/test_frozen.py", blocked=False, env={"DIXI_ALLOW_TEST_EDITS": "1"})

    def test_malformed_bash_input_blocks(self):
        project = self.projects["claude"]
        for payload in ({"tool_name": "Bash", "tool_input": {}}, {"tool_name": "Bash"}):
            result = subprocess.run([sys.executable, str(project / ".dixi/hooks/protect_tests.py")],
                                    input=json.dumps(payload), cwd=project,
                                    env=dict(os.environ, CLAUDE_PROJECT_DIR=str(project)), text=True,
                                    capture_output=True, timeout=60)
            self.assertEqual(result.returncode, 2, result.stderr)


if __name__ == "__main__":
    unittest.main()
