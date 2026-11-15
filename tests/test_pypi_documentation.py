"""The PyPI page links the documentation site and the tutorial."""
from pathlib import Path
import re
import tomllib
import unittest


ROOT = Path(__file__).resolve().parents[1]
SITE = "https://dixi-project.github.io/dixi-spec-kit/"
PAGES = {f"{SITE}en/tutorial/index.html": "docs/tutorial/index.md",
         f"{SITE}es/tutorial/index.html": "docs/tutorial/index.es.md",
         f"{SITE}en/documentation.html": "docs/documentation.md",
         f"{SITE}es/documentation.html": "docs/documentation.es.md"}


def read(name):
    return (ROOT / name).read_text(encoding="utf-8")


class PypiDocumentationTests(unittest.TestCase):
    def setUp(self):
        self.readme = read("packaging/README.md")
        self.project = tomllib.loads(read("pyproject.toml"))["project"]

    def test_readme_has_a_documentation_section_with_the_site_and_the_tutorial(self):
        self.assertEqual(self.project["readme"], "packaging/README.md")
        self.assertIn("\n## Documentation / Documentación\n", self.readme)
        section = self.readme.split("\n## Documentation / Documentación\n", 1)[1].split("\n## ", 1)[0]
        self.assertIn(SITE, section)
        for url, source in PAGES.items():
            with self.subTest(url=url):
                self.assertIn(url, section)
                self.assertTrue((ROOT / source).is_file(), source)

    def test_readme_links_are_absolute(self):
        for href in re.findall(r"\]\(([^)]+)\)", self.readme) + re.findall(r'src="([^"]+)"', self.readme):
            with self.subTest(href=href):
                self.assertTrue(href.startswith("https://"), href)

    def test_project_urls_list_the_documentation_and_the_changelog(self):
        urls = self.project["urls"]
        self.assertEqual(urls["Documentation"], SITE)
        self.assertEqual(urls["Changelog"], "https://github.com/dixi-project/dixi-spec-kit/blob/main/CHANGELOG.md")
        self.assertEqual(urls["Homepage"], "https://github.com/dixi-project/dixi-spec-kit")

    def test_readme_names_only_current_agents(self):
        self.assertNotIn("Gemini CLI", self.readme)
        self.assertIn("OpenCode", self.readme)


if __name__ == "__main__":
    unittest.main()
