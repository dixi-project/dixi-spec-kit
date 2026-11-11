"""The READMEs announce the PyPI install path once the first upload succeeded (ADR-106)."""
from pathlib import Path
import re
import tomllib
import unittest


ROOT = Path(__file__).resolve().parents[1]
READMES = ("README.md", "README.es.md")


class ReadmeInstallTests(unittest.TestCase):
    def setUp(self):
        self.version = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))["project"]["version"]

    def install_section(self, name):
        text = (ROOT / name).read_text(encoding="utf-8")
        match = re.search(r"\n## (?:Installation|Instalación)\n(.*?)\n## ", text, re.S)
        self.assertIsNotNone(match, f"{name} has no installation section")
        return match.group(1)

    def test_pypi_is_the_main_install_path(self):
        for name in READMES:
            with self.subTest(readme=name):
                section = self.install_section(name)
                self.assertIn("uv tool install dixi-spec-kit\n", section)
                self.assertIn("pipx install dixi-spec-kit\n", section)
                self.assertNotRegex(section, r"(?i)not on PyPI|no está publicado en PyPI")

    def test_alternatives_name_the_current_version(self):
        for name in READMES:
            with self.subTest(readme=name):
                section = self.install_section(name)
                self.assertIn(f"git+https://github.com/dixi-project/dixi-spec-kit@v{self.version}", section)
                for wheel in re.findall(r"dixi_spec_kit-[0-9.]+-py3-none-any\.whl", section):
                    self.assertEqual(wheel, f"dixi_spec_kit-{self.version}-py3-none-any.whl")


if __name__ == "__main__":
    unittest.main()
