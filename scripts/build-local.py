from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
SOURCES = ["pyproject.toml", "MANIFEST.in", "packaging/README.md",
           "src/dixi_spec_kit/__init__.py", "src/dixi_spec_kit/__main__.py",
           "src/dixi_spec_kit/cli.py", "src/dixi_spec_kit/core.py", "src/dixi_spec_kit/filesystem.py",
           "src/dixi_spec_kit/locales/es.json", "src/dixi_spec_kit/locales/en.json",
           "src/dixi_spec_kit/resources/project.es.json", "src/dixi_spec_kit/resources/project.en.json",
           "src/dixi_spec_kit/workflows.py", "src/dixi_spec_kit/resources/workflows.json",
           "src/dixi_spec_kit/resources/workflows.es.json", "src/dixi_spec_kit/resources/workflows.en.json",
           "src/dixi_spec_kit/LICENSE"]
SOURCES += sorted(p.relative_to(ROOT).as_posix()
                  for p in (ROOT / "src/dixi_spec_kit/resources/claude").glob("*/*.md"))


def main():
    output = ROOT / "dist"
    output.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as folder:
        staging = Path(folder)
        for name in SOURCES:
            source = ROOT / name
            if source.is_symlink():
                raise RuntimeError(f"Source must not be a symlink: {name}")
            destination = staging / name
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)
        command = ("from setuptools.build_meta import build_wheel, build_sdist; "
                   f"build_wheel({str(output)!r}); build_sdist({str(output)!r})")
        subprocess.run([sys.executable, "-c", command], cwd=staging, check=True)


if __name__ == "__main__":
    main()
