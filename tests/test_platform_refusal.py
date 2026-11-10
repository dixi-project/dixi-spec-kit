"""ADR-107 phase 0: without safe filesystem operations, dixi refuses explicitly (exit 4) and writes nothing.

Runs on every platform, including native Windows, so it uses no POSIX-only helper.
"""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
UNSUPPORTED = (
    "import sys\n"
    "import dixi_spec_kit.core as core, dixi_spec_kit.filesystem as filesystem\n"
    "filesystem.supported = core.supported = lambda: False\n"
    "from dixi_spec_kit.cli import main\n"
    "sys.exit(main(sys.argv[1:]))\n"
)
MESSAGES = {
    "en": "Platform lacks required safe filesystem operations; no unsafe fallback was used.",
    "es": "Plataforma sin las operaciones seguras de filesystem requeridas; no se ha aplicado una alternativa insegura.",
}


class PlatformRefusalTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)

    def run_cli(self, *args, simulate=True, cwd=None):
        env = dict(os.environ, PYTHONPATH=str(ROOT / "src"), PYTHONDONTWRITEBYTECODE="1", PYTHONIOENCODING="utf-8")
        command = [sys.executable, "-c", UNSUPPORTED, *args] if simulate else [sys.executable, "-m", "dixi_spec_kit", *args]
        return subprocess.run(command, cwd=cwd or self.base, env=env, text=True, encoding="utf-8", capture_output=True,
                              timeout=60)

    def test_file_commands_exit_4_and_write_nothing(self):
        project = self.base / "project"
        project.mkdir()
        commands = (
            ("init", str(self.base / "new")),
            ("init", str(self.base / "new"), "--agent", "claude", "--controls"),
            ("check",),
            ("doctor",),
            ("upgrade", "--dry-run"),
            ("placeholders",),
            ("workflow", "prepare", "plan", "--target", "05-features/x/plan.md", "--request", "plan the feature"),
        )
        for language, message in MESSAGES.items():
            for args in commands:
                with self.subTest(language=language, args=args):
                    result = self.run_cli("--lang", language, *args, cwd=project)
                    self.assertEqual(result.returncode, 4, result.stdout + result.stderr)
                    self.assertIn(message, result.stdout + result.stderr)
                    self.assertFalse((self.base / "new").exists(), "nothing may be created")
                    self.assertEqual(list(project.iterdir()), [], "nothing may be written in the project")

    def test_json_error_is_unsupported_platform(self):
        result = self.run_cli("--json", "init", str(self.base / "new"))
        self.assertEqual(result.returncode, 4)
        data = json.loads(result.stdout)
        self.assertIn("unsupported_platform", json.dumps(data))

    def test_commands_that_do_not_touch_a_project_still_work(self):
        for args in (("--help",), ("--version",), ("workflow", "list"), ("workflow", "show", "plan")):
            with self.subTest(args=args):
                result = self.run_cli(*args)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    @unittest.skipIf(os.name == "posix", "native refusal is observable only where the platform lacks the operations")
    def test_native_platform_refuses_init(self):
        result = self.run_cli("init", str(self.base / "native"), simulate=False)
        self.assertEqual(result.returncode, 4, result.stdout + result.stderr)
        self.assertFalse((self.base / "native").exists())


class SourceEncodingTests(unittest.TestCase):
    def test_verify_source_reads_text_as_utf8(self):
        import ast
        tree = ast.parse((ROOT / "scripts/verify-source.py").read_text(encoding="utf-8"))
        calls = [node for node in ast.walk(tree) if isinstance(node, ast.Call)
                 and isinstance(node.func, ast.Attribute) and node.func.attr == "read_text"]
        self.assertTrue(calls)
        for call in calls:
            keywords = {k.arg: k.value for k in call.keywords}
            self.assertIn("encoding", keywords, f"read_text without encoding at line {call.lineno}")
            self.assertEqual(getattr(keywords["encoding"], "value", None), "utf-8")

    def test_repository_forces_lf(self):
        attributes = (ROOT / ".gitattributes").read_text(encoding="utf-8").splitlines()
        self.assertIn("* text=auto eol=lf", attributes)


if __name__ == "__main__":
    unittest.main()
