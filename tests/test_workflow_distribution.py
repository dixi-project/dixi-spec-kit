import json
import os
from pathlib import Path
import subprocess
import sys
import tarfile
import tempfile
import unittest
import venv


ROOT = Path(__file__).resolve().parents[1]


class WorkflowDistributionTests(unittest.TestCase):
    def test_installed_workflow_from_wheel_and_sdist(self):
        wheel = next((ROOT / "dist").glob("*.whl"))
        source = next((ROOT / "dist").glob("*.tar.gz"))
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder).resolve()
            extracted = base / "source"
            extracted.mkdir()
            with tarfile.open(source) as archive:
                archive.extractall(extracted, filter="data")
            rebuilt = base / "rebuilt"
            rebuilt.mkdir()
            build = subprocess.run([sys.executable, "-c", "from setuptools.build_meta import build_wheel; "
                                    f"build_wheel({str(rebuilt)!r})"], cwd=next(extracted.iterdir()),
                                   text=True, capture_output=True, timeout=60)
            self.assertEqual(build.returncode, 0, build.stdout + build.stderr)
            for index, artifact in enumerate((wheel, next(rebuilt.glob("*.whl")))):
                with self.subTest(index=index):
                    environment = base / f"env-{index}"
                    venv.EnvBuilder(with_pip=True).create(environment)
                    install = subprocess.run([str(environment / "bin/python"), "-m", "pip", "--isolated", "install",
                                              "--no-index", "--no-deps", str(artifact)],
                                             text=True, capture_output=True, timeout=60)
                    self.assertEqual(install.returncode, 0, install.stdout + install.stderr)
                    cli = str(environment / "bin/dixi")
                    env = dict(os.environ)
                    env.pop("PYTHONPATH", None)
                    project = base / f"project-{index}"
                    init = subprocess.run([cli, "init", str(project)], cwd=base, env=env, capture_output=True, text=True)
                    self.assertEqual(init.returncode, 0, init.stdout + init.stderr)
                    for language in ("es", "en"):
                        prepared = subprocess.run([cli, "--lang", language, "--json", "workflow", "prepare", "plan",
                                                   "--target", "FEATURE-001", "--request", "Notes library"],
                                                  cwd=project, env=env, capture_output=True, text=True, timeout=10)
                        self.assertEqual(prepared.returncode, 0, prepared.stdout + prepared.stderr)
                        packet = json.loads(prepared.stdout)["workflow"]["packet"]
                        self.assertEqual(packet["status"], "prepared")
                        self.assertEqual(packet["recipe"]["id"], "plan")
                        self.assertTrue(packet["sources"])
