import os
from pathlib import Path
import subprocess
import sys
import tarfile
import tempfile
import unittest
import venv
import zipfile


ROOT = Path(__file__).resolve().parents[1]


class DistributionTests(unittest.TestCase):
    def artifacts(self):
        wheels = list((ROOT / "dist").glob("dixi_spec_kit-*.whl"))
        sources = list((ROOT / "dist").glob("dixi_spec_kit-*.tar.gz"))
        self.assertEqual(len(wheels), 1, "Build exactly one wheel before verification")
        self.assertEqual(len(sources), 1, "Build exactly one sdist before verification")
        return wheels[0], sources[0]

    def test_artifact_allowlist(self):
        wheel, sdist = self.artifacts()
        with zipfile.ZipFile(wheel) as archive:
            names = archive.namelist()
            for name in names:
                self.assertTrue(name.startswith("dixi_spec_kit/") or ".dist-info/" in name, name)
                self.assertNotIn("__pycache__", name)
            self.assertIn("dixi_spec_kit/resources/project.es.json", names)
            self.assertIn("dixi_spec_kit/resources/project.en.json", names)
            metadata = archive.read(next(n for n in names if n.endswith("/METADATA"))).decode()
            self.assertNotIn("Requires-Dist:", metadata)
        with tarfile.open(sdist) as archive:
            for entry in archive.getmembers():
                parts = Path(entry.name).parts
                self.assertFalse(entry.issym() or entry.islnk(), entry.name)
                if entry.isdir():
                    continue
                relative = Path(*parts[1:]).as_posix()
                self.assertTrue(relative.startswith("src/dixi_spec_kit/") or
                                relative.startswith("src/dixi_spec_kit.egg-info/") or
                                relative in {"pyproject.toml", "MANIFEST.in", "PKG-INFO", "setup.cfg",
                                             "packaging/README.md"}, relative)

    def test_clean_installations(self):
        wheel, sdist = self.artifacts()
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder).resolve()
            extracted = base / "source"
            extracted.mkdir()
            with tarfile.open(sdist) as archive:
                archive.extractall(extracted, filter="data")
            source = next(extracted.iterdir())
            wheel_dir = base / "rebuilt"
            wheel_dir.mkdir()
            build = subprocess.run([sys.executable, "-c", "from setuptools.build_meta import build_wheel; "
                                    f"build_wheel({str(wheel_dir)!r})"], cwd=source,
                                   text=True, capture_output=True, timeout=60)
            self.assertEqual(build.returncode, 0, build.stdout + build.stderr)
            rebuilt = next(wheel_dir.glob("*.whl"))
            for index, artifact in enumerate((wheel, rebuilt)):
                with self.subTest(artifact=artifact.name, source=index):
                    environment = base / f"venv-{index}"
                    venv.EnvBuilder(with_pip=True).create(environment)
                    python = environment / "bin/python"
                    install = subprocess.run([str(python), "-m", "pip", "--isolated", "install",
                                              "--no-index", "--no-deps", str(artifact)],
                                             text=True, capture_output=True, timeout=60)
                    self.assertEqual(install.returncode, 0, install.stdout + install.stderr)
                    executable = environment / "bin/dixi"
                    project = base / f"project-{index}"
                    env = dict(os.environ, PATH=str(environment / "bin") + os.pathsep + os.environ["PATH"])
                    for args, cwd in ((["--version"], base), (["init", str(project)], base),
                                      (["check"], project), (["doctor"], project)):
                        run = subprocess.run([str(executable)] + args, cwd=cwd, env=env,
                                             capture_output=True, text=True, timeout=20)
                        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
                    verify = subprocess.run(["make", "verify"], cwd=project, env=env,
                                            text=True, capture_output=True, timeout=20)
                    self.assertEqual(verify.returncode, 0, verify.stdout + verify.stderr)


if __name__ == "__main__":
    unittest.main()
