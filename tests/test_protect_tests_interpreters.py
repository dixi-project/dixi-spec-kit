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


class ProtectTestsInterpreterTests(unittest.TestCase):
    """protect_tests stops inline interpreter code that writes, moves or deletes a committed test."""

    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        project = Path(cls.temp.name).resolve() / "project"
        env = dict(os.environ, PYTHONPATH=str(ROOT / "src"), PYTHONDONTWRITEBYTECODE="1")
        result = subprocess.run([sys.executable, "-m", "dixi_spec_kit", "init", str(project), "--agent", "claude",
                                 "--controls"], env=env, text=True, capture_output=True, timeout=60)
        assert result.returncode == 0, result.stdout + result.stderr
        git(project, "init", "-q", "-b", "main")
        git(project, "config", "user.email", "person@example.com")
        git(project, "config", "user.name", "Person")
        (project / "tests").mkdir()
        (project / "tests/test_frozen.py").write_text("def test_ok():\n    assert True\n")
        (project / "src").mkdir()
        (project / "src/app.py").write_text("VALUE = 1\n")
        git(project, "add", "-A")
        git(project, "commit", "-qm", "initial")
        cls.project = project

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def run_hook(self, command):
        payload = {"hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": command},
                   "cwd": str(self.project)}
        environment = dict(os.environ, CLAUDE_PROJECT_DIR=str(self.project))
        environment.pop("DIXI_ALLOW_TEST_EDITS", None)
        return subprocess.run([sys.executable, str(self.project / ".dixi/hooks/protect_tests.py")],
                              input=json.dumps(payload), cwd=self.project, env=environment, text=True,
                              capture_output=True, timeout=60)

    def check(self, command, blocked):
        with self.subTest(command=command):
            result = self.run_hook(command)
            self.assertEqual(result.returncode, 2 if blocked else 0, result.stderr)
            if blocked:
                self.assertIn("DIXI protect_tests", result.stderr)

    def test_blocks_inline_code_that_writes_a_committed_test(self):
        for command in (
                "python3 -c \"open('tests/test_frozen.py', 'w').write('x')\"",
                "python3 -c \"import pathlib; pathlib.Path('tests/test_frozen.py').write_text('x')\"",
                "python -c \"import os; os.remove('tests/test_frozen.py')\"",
                "python3 -c \"import shutil; shutil.copy('src/app.py', 'tests/test_frozen.py')\"",
                "python3 - <<'EOF'\nopen('tests/test_frozen.py', 'a').write('x')\nEOF",
                "node -e \"require('fs').writeFileSync('tests/test_frozen.py', 'x')\"",
                "node -e \"require('fs').unlinkSync('tests/test_frozen.py')\"",
                "ruby -e \"File.write('tests/test_frozen.py', 'x')\"",
                "perl -e \"unlink 'tests/test_frozen.py'\"",
                "php -r \"file_put_contents('tests/test_frozen.py', 'x');\"",
        ):
            self.check(command, blocked=True)

    def test_allows_inline_code_that_only_reads_or_touches_other_files(self):
        for command in (
                "python3 -c \"print(open('tests/test_frozen.py').read())\"",
                "node -e \"console.log(require('fs').readFileSync('tests/test_frozen.py', 'utf8'))\"",
                "python3 -c \"open('src/out.txt', 'w').write('x')\"",
                "python3 -c \"open('tests/test_new.py', 'w').write('x')\"",
                "python3 -m unittest tests/test_frozen.py",
                "python3 -m pytest tests/test_frozen.py -x",
        ):
            self.check(command, blocked=False)


if __name__ == "__main__":
    unittest.main()
