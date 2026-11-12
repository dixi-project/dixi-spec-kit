"""TASK-020: the key pages of the documentation site have Spanish versions."""
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
DOCS = ROOT / "docs"
# Flat documents with a Spanish source (`<name>.es.md`). Every other flat page keeps the English-only notice.
TRANSLATED = {"command-catalog": "Guía de comandos de DIXI Spec Kit", "coming-from-spec-kit": "Si vienes de Spec Kit"}
NOTICE = json.loads((ROOT / "scripts/site/es.json").read_text(encoding="utf-8"))["english_only"]


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.inside, self.links, self.ids = False, [], set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.inside = self.inside or tag == "main"
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if self.inside and tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])

    def handle_endtag(self, tag):
        if tag == "main":
            self.inside = False


def parse(path):
    page = Page()
    page.feed(path.read_text(encoding="utf-8"))
    return page


class SpanishSiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.out = Path(cls.temp.name).resolve() / "site"
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
        cls.result = subprocess.run([sys.executable, str(ROOT / "scripts/build-site.py"), str(cls.out)], cwd=ROOT,
                                    env=env, text=True, capture_output=True, timeout=60)

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def test_these_flat_pages_have_spanish_sources(self):
        self.assertEqual(self.result.returncode, 0, self.result.stdout + self.result.stderr)
        self.assertEqual({path.name[:-len(".es.md")] for path in DOCS.glob("*.es.md")}, set(TRANSLATED))
        for name, title in TRANSLATED.items():
            with self.subTest(page=name):
                self.assertTrue((DOCS / f"{name}.es.md").read_text(encoding="utf-8").startswith(f"# {title}\n"))
                spanish = (self.out / "es" / f"{name}.html").read_text(encoding="utf-8")
                self.assertIn(f">{title}</h1>", spanish)
                self.assertNotIn(NOTICE, spanish)
                self.assertNotIn(f">{title}</h1>", (self.out / "en" / f"{name}.html").read_text(encoding="utf-8"))

    def test_pages_only_in_english_keep_the_notice(self):
        english_only = sorted(path.stem for path in DOCS.glob("*.md")
                              if not path.name.endswith(".es.md") and path.stem not in TRANSLATED)
        self.assertIn("support-matrix", english_only)
        self.assertGreaterEqual(len(english_only), 8)
        for name in english_only:
            with self.subTest(page=name):
                self.assertIn(NOTICE, (self.out / "es" / f"{name}.html").read_text(encoding="utf-8"))
        self.assertIn("Resumen en español", (self.out / "es/support-matrix.html").read_text(encoding="utf-8"))

    def test_references_are_in_spanish_in_the_spanish_tree(self):
        for page, title in (("commands/index.html", "Referencia de comandos"), ("cli/index.html", "Referencia de la CLI"),
                            ("commands/specify.html", "Propósito"), ("cli/init.html", "Propósito")):
            with self.subTest(page=page):
                text = (self.out / "es" / page).read_text(encoding="utf-8")
                self.assertIn(title, text)
                self.assertNotIn(NOTICE, text)

    def test_spanish_pages_keep_the_same_links_and_commands(self):
        for name in TRANSLATED:
            with self.subTest(page=name):
                english, spanish = (parse(self.out / lang / f"{name}.html") for lang in ("en", "es"))
                internal = lambda links: sorted({link for link in links if not link.startswith("http")})  # noqa: E731
                self.assertEqual(internal(spanish.links), internal(english.links))
                sources = [(DOCS / f"{name}{suffix}").read_text(encoding="utf-8") for suffix in (".md", ".es.md")]
                commands = [set(re.findall(r"`((?:/dixi\.|/speckit\.|dixi )[^`]*)`", text)) for text in sources]
                self.assertEqual({c.split()[0] for c in commands[0]}, {c.split()[0] for c in commands[1]})
                self.assertEqual(len(re.findall(r"(?m)^\| ", sources[0])), len(re.findall(r"(?m)^\| ", sources[1])))

    def test_every_anchor_link_resolves_in_both_trees(self):
        pages = {path: parse(path) for path in self.out.rglob("*.html") if path.parent != self.out}
        for path, page in pages.items():
            for link in page.links:
                target, _, anchor = link.partition("#")
                if link.startswith("http") or not anchor:
                    continue
                destination = (path.parent / target).resolve() if target else path
                with self.subTest(page=str(path.relative_to(self.out)), link=link):
                    self.assertIn(anchor, pages[destination].ids)


if __name__ == "__main__":
    unittest.main()
