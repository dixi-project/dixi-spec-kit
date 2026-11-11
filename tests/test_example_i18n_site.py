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


ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "examples/i18n-site"
CHAIN = ("goal", "domain", "module", "feature", "contract", "test")


class I18nSiteExampleTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue((EXAMPLE / ".dixi/project.json").is_file(), "examples/i18n-site is missing")
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.work = self.base / "i18n-site"
        shutil.copytree(EXAMPLE, self.work, ignore=shutil.ignore_patterns("__pycache__", "node_modules", ".next"))
        shim = self.base / "bin"
        shim.mkdir()
        (shim / "dixi").write_text(f"#!/bin/sh\nexec {shlex.quote(sys.executable)} -m dixi_spec_kit \"$@\"\n")
        (shim / "dixi").chmod(0o755)
        self.env = dict(os.environ, PYTHONPATH=str(ROOT / "src"), PYTHONDONTWRITEBYTECODE="1",
                        PATH=str(shim) + os.pathsep + os.environ["PATH"])

    def run_in_example(self, *command, timeout=60):
        return subprocess.run(list(command), cwd=self.work, env=self.env, text=True, capture_output=True,
                              timeout=timeout)

    def test_example_is_a_site_project_with_full_traceability(self):
        metadata = json.loads((self.work / ".dixi/project.json").read_text())
        self.assertEqual((metadata["profile"], metadata["agent"], metadata["language"]), ("site", "claude", "en"))
        items = json.loads((self.work / ".dixi/traceability.json").read_text())["items"]
        kinds = {item["kind"] for item in items}
        self.assertTrue(set(CHAIN) <= kinds, kinds)
        code_tests = [item for item in items if item["kind"] == "test" and item["path"].endswith(".mjs")]
        self.assertTrue(code_tests, "no executable test is traced")
        for item in items:
            self.assertTrue((self.work / item["path"]).is_file(), item["path"])

    def test_example_ships_no_dependencies_and_no_hardcoded_copy(self):
        package = json.loads((self.work / "package.json").read_text())
        self.assertFalse(package.get("dependencies"), "runtime code must not need npm install")
        for name in ("lib/i18n.mjs", "app/[lang]/page.tsx", "proxy.ts"):
            self.assertTrue((self.work / name).is_file(), name)
        catalogs = [json.loads((self.work / "locales" / f"{lang}.json").read_text()) for lang in ("en", "es")]
        self.assertEqual(catalogs[0].keys(), catalogs[1].keys(), "catalogs differ")
        page = (self.work / "app/[lang]/page.tsx").read_text()
        for text in catalogs[0].values():
            self.assertNotIn(text, page, "user-facing text hardcoded in the page")

    def test_example_passes_check_and_verify(self):
        check = self.run_in_example(sys.executable, "-m", "dixi_spec_kit", "check", timeout=20)
        self.assertEqual(check.returncode, 0, check.stdout + check.stderr)
        verify = self.run_in_example("make", "verify")
        self.assertEqual(verify.returncode, 0, verify.stdout + verify.stderr)

    def test_verify_without_node_says_so_and_passes(self):
        verify = self.run_in_example("make", "verify", "NODE=dixi-example-missing-node")
        self.assertEqual(verify.returncode, 0, verify.stdout + verify.stderr)
        self.assertIn("node not found", verify.stdout + verify.stderr)

    def test_verify_runs_node_tests(self):
        if shutil.which("node", path=self.env["PATH"]) is None:
            self.skipTest("node is not installed")
        verify = self.run_in_example("make", "verify")
        output = verify.stdout + verify.stderr
        self.assertEqual(verify.returncode, 0, output)
        passed = re.search(r"^# pass (\d+)$", output, re.MULTILINE)
        self.assertIsNotNone(passed, output)
        self.assertGreaterEqual(int(passed.group(1)), 1, output)
        self.assertRegex(output, r"(?m)^# fail 0$")


if __name__ == "__main__":
    unittest.main()
