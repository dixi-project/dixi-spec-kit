"""ADR-108 phase E: a static documentation site in English and Spanish, built with the standard library."""
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/pages.yml"


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.alternates, self.scripts, self.lang, self.canonical = [], {}, [], None, None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html":
            self.lang = attrs.get("lang")
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag == "link" and attrs.get("rel") == "alternate":
            self.alternates[attrs.get("hreflang")] = attrs.get("href")
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical = attrs.get("href")
        if tag == "script" and attrs.get("src"):
            self.scripts.append(attrs["src"])


class SiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.out = Path(cls.temp.name).resolve() / "site"
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
        cls.result = subprocess.run([sys.executable, str(ROOT / "scripts/build-site.py"), str(cls.out)],
                                    cwd=ROOT, env=env, text=True, capture_output=True, timeout=60)

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def parse(self, path):
        parser = Links()
        parser.feed(path.read_text(encoding="utf-8"))
        return parser

    def test_build_succeeds(self):
        self.assertEqual(self.result.returncode, 0, self.result.stdout + self.result.stderr)

    def test_language_prefixed_pages_with_hreflang_and_canonical(self):
        for lang in ("en", "es"):
            with self.subTest(lang=lang):
                page = self.parse(self.out / lang / "index.html")
                self.assertEqual(page.lang, lang)
                self.assertEqual(set(page.alternates), {"en", "es", "x-default"})
                self.assertTrue(page.canonical.endswith(f"/{lang}/"), page.canonical)
        self.assertIn("Instalación", (self.out / "es/index.html").read_text(encoding="utf-8"))
        self.assertIn("Installation", (self.out / "en/index.html").read_text(encoding="utf-8"))

    def test_root_redirects_by_browser_language_with_a_fallback(self):
        text = (self.out / "index.html").read_text(encoding="utf-8")
        self.assertIn("navigator.language", text)
        self.assertIn('href="en/"', text)
        self.assertIn('href="es/"', text)

    def test_every_doc_page_exists_in_both_trees(self):
        for doc in ("support-matrix", "coming-from-spec-kit", "spec-kit-comparison", "workflow-quickstart"):
            for lang in ("en", "es"):
                self.assertTrue((self.out / lang / f"{doc}.html").is_file(), f"{lang}/{doc}")

    def test_internal_links_resolve_and_no_external_scripts(self):
        for page in self.out.rglob("*.html"):
            parsed = self.parse(page)
            self.assertEqual(parsed.scripts, [s for s in parsed.scripts if not re.match(r"https?:", s)], page)
            for href in parsed.links:
                if re.match(r"(https?:|mailto:|#)", href):
                    continue
                target = (page.parent / href.split("#", 1)[0]).resolve()
                if href.endswith("/"):
                    target = target / "index.html"
                self.assertTrue(target.exists(), f"{page.relative_to(self.out)} -> {href}")

    def test_search_index_and_ui_catalogs(self):
        for lang in ("en", "es"):
            index = json.loads((self.out / lang / "search.json").read_text(encoding="utf-8"))
            self.assertTrue(any(entry["url"] == "index.html" for entry in index))
            catalog = json.loads((ROOT / f"scripts/site/{lang}.json").read_text(encoding="utf-8"))
            self.assertIn("search", catalog)
            self.assertIn(catalog["search"], (self.out / lang / "index.html").read_text(encoding="utf-8"))

    def test_pages_workflow_is_pinned_and_least_privilege(self):
        text = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("python3 scripts/build-site.py", text)
        for action in re.findall(r"uses: (\S+)", text):
            self.assertRegex(action, r"^[\w.-]+/[\w.-]+@[0-9a-f]{40}$", action)
        self.assertRegex(text, r"\npermissions:\n  contents: read\n")
        deploy = text.split("\n  deploy:\n", 1)[1]
        self.assertIn("pages: write", deploy)
        self.assertIn("id-token: write", deploy)
        self.assertIn("refs/heads/main", deploy)
        self.assertNotIn("secrets.", text)

    def test_commands_section_in_both_languages(self):
        operations = sorted(path.name[5:-3] for path in
                            (ROOT / "src/dixi_spec_kit/resources/claude/en").glob("dixi.*.md"))
        words = {"en": ("Steps", "Commands"), "es": ("Pasos", "Comandos")}
        for lang in ("en", "es"):
            for name in [*operations, "index"]:
                self.assertTrue((self.out / lang / "commands" / f"{name}.html").is_file(), f"{lang}/{name}")
            with self.subTest(lang=lang):
                page = self.parse(self.out / lang / "commands/specify.html")
                text = (self.out / lang / "commands/specify.html").read_text(encoding="utf-8")
                self.assertEqual(page.lang, lang)
                self.assertTrue(page.canonical.endswith(f"/{lang}/commands/specify.html"), page.canonical)
                self.assertTrue(page.alternates["es"].endswith("/es/commands/specify.html"), page.alternates)
                self.assertIn(f'>{words[lang][0]}</h2>', text)
                self.assertIn("../assets/mark.svg", text)
                self.assertIn("../search.json", text)
                self.assertIn("plan.html", page.links)
                self.assertIn("../index.html", page.links)
                home = self.parse(self.out / lang / "index.html")
                self.assertIn("commands/index.html", home.links)
                self.assertIn("commands/specify.html", home.links)
                self.assertIn(words[lang][1], (self.out / lang / "index.html").read_text(encoding="utf-8"))
                index = json.loads((self.out / lang / "search.json").read_text(encoding="utf-8"))
                self.assertTrue(any(entry["url"] == "commands/specify.html" for entry in index))
        notice = json.loads((ROOT / "scripts/site/es.json").read_text(encoding="utf-8"))["english_only"]
        self.assertNotIn(notice, (self.out / "es/commands/specify.html").read_text(encoding="utf-8"))
        self.assertIn(notice, (self.out / "es/support-matrix.html").read_text(encoding="utf-8"))

    def test_logo_files_are_self_contained(self):
        for name in ("logo-light.svg", "logo-dark.svg", "mark.svg"):
            with self.subTest(logo=name):
                text = (ROOT / "docs/assets" / name).read_text(encoding="utf-8")
                self.assertIn("<title", text)
                for forbidden in ("<text", "<script", "<image", "font-family", "href="):
                    self.assertNotIn(forbidden, text)

    def test_readmes_show_the_logo_for_both_color_schemes(self):
        for name in ("README.md", "README.es.md"):
            with self.subTest(readme=name):
                text = (ROOT / name).read_text(encoding="utf-8")
                self.assertIn('srcset="docs/assets/logo-dark.svg"', text)
                self.assertIn('src="docs/assets/logo-light.svg" alt="DIXI Spec Kit"', text)
                self.assertIn("\n# DIXI Spec Kit\n", text)

    def test_pypi_readme_shows_the_logo_from_an_absolute_url(self):
        text = (ROOT / "packaging/README.md").read_text(encoding="utf-8")
        images = re.findall(r'<img src="([^"]+)"', text)
        self.assertEqual(len(images), 1, images)
        prefix = "https://raw.githubusercontent.com/dixi-project/dixi-spec-kit/main/"
        self.assertTrue(images[0].startswith(prefix), images[0])
        self.assertTrue((ROOT / images[0][len(prefix):]).is_file(), images[0])
        self.assertIn('alt="DIXI Spec Kit"', text)
        self.assertNotIn("<picture", text)
        self.assertIn("\n# DIXI Spec Kit\n", text)

    def test_site_shows_the_mark_and_hides_the_readme_banner(self):
        self.assertEqual((self.out / "assets/mark.svg").read_bytes(), (ROOT / "docs/assets/mark.svg").read_bytes())
        for lang in ("en", "es"):
            for page in ("index.html", "support-matrix.html"):
                with self.subTest(lang=lang, page=page):
                    text = (self.out / lang / page).read_text(encoding="utf-8")
                    self.assertIn('<link rel="icon" type="image/svg+xml" href="../assets/mark.svg">', text)
                    self.assertIn('<img src="../assets/mark.svg" alt="" width="28" height="28">', text)
                    self.assertNotIn("&lt;picture", text)
                    self.assertNotIn("&lt;p align", text)
                    self.assertNotIn("img.shields.io", text)


if __name__ == "__main__":
    unittest.main()
