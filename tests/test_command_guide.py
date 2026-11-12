"""TASK-017: a public command guide replaces the internal working catalog."""
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OPERATIONS = sorted(path.name[5:-3] for path in
                    (ROOT / "src/dixi_spec_kit/resources/claude/en").glob("dixi.*.md"))
GUIDE = {"en": DOCS / "command-catalog.md", "es": DOCS / "command-catalog.es.md"}
SUFFIX = {"en": ".md", "es": ".es.md"}
JOURNEY = "discover → specify → clarify → plan → tasks → build → verify → review → release"
HEADINGS = {
    "en": {"journey": "## Journey", "table": "## Which command when", "walkthrough": "## Walkthrough",
           "groups": ("### Design", "### Quality", "### Continuity", "### Specialized")},
    "es": {"journey": "## Recorrido", "table": "## Qué comando usar y cuándo", "walkthrough": "## Ejemplo completo",
           "groups": ("### Diseño", "### Calidad", "### Continuidad", "### Especializadas")},
}
PROVISIONAL = {"en": r"(?i)\b(proposed|pending|deferred)\b", "es": r"(?i)\b(propuest[oa]s?|pendientes?|diferid[oa]s?)\b"}
MOVED = ("command-catalog.md", "v1-design-review.md")


def section(text, heading):
    return text.split(f"\n{heading}\n", 1)[1].split("\n## ", 1)[0]


def without_markers(text):
    return re.sub(r"\{\{pending[^}]*\}\}", "", text)


class CommandGuideTests(unittest.TestCase):
    def test_guide_exists_in_both_languages_with_the_journey(self):
        for lang, path in GUIDE.items():
            with self.subTest(lang=lang):
                text = path.read_text(encoding="utf-8")
                journey = section(text, HEADINGS[lang]["journey"])
                self.assertIn(JOURNEY, journey)
                for group in HEADINGS[lang]["groups"]:
                    self.assertIn(f"\n{group}\n", journey)

    def test_table_covers_every_operation_once_and_links_to_its_reference(self):
        for lang, path in GUIDE.items():
            table = section(path.read_text(encoding="utf-8"), HEADINGS[lang]["table"])
            rows = [line for line in table.splitlines() if line.startswith("| [")]
            self.assertEqual(len(rows), 33, lang)
            for operation in OPERATIONS:
                with self.subTest(lang=lang, operation=operation):
                    link = f"| [`/dixi.{operation}`](commands/{operation}{SUFFIX[lang]}) |"
                    self.assertEqual(sum(row.startswith(link) for row in rows), 1)
                    self.assertTrue((DOCS / "commands" / f"{operation}{SUFFIX[lang]}").is_file())
            for row in rows:
                self.assertEqual(row.count("|"), 4, row)
                self.assertGreater(len(row.split("|")[2].strip()), 20, row)

    def test_walkthrough_goes_from_init_to_a_release(self):
        steps = ("dixi init", "/dixi.discover", "/dixi.specify", "/dixi.clarify", "/dixi.plan", "/dixi.tasks",
                 "/dixi.build", "/dixi.verify", "/dixi.review", "/dixi.release")
        for lang, path in GUIDE.items():
            with self.subTest(lang=lang):
                walkthrough = section(path.read_text(encoding="utf-8"), HEADINGS[lang]["walkthrough"])
                positions = [walkthrough.index(step) for step in steps]
                self.assertEqual(positions, sorted(positions))
                self.assertIn("make verify", walkthrough)

    def test_guide_does_not_call_shipped_commands_provisional(self):
        for lang, path in GUIDE.items():
            with self.subTest(lang=lang):
                self.assertNotRegex(without_markers(path.read_text(encoding="utf-8")), PROVISIONAL[lang])

    def test_no_public_page_calls_commands_provisional(self):
        public = [ROOT / "README.md", ROOT / "README.es.md", *sorted(DOCS.glob("*.md"))]
        for path in public:
            lang = "es" if path.name.endswith(".es.md") else "en"
            for number, line in enumerate(without_markers(path.read_text(encoding="utf-8")).splitlines(), 1):
                if re.search(r"(?i)/dixi\.|\bcommands?\b|\bcomandos?\b|\bcatalog\b|\bcatálogo\b", line):
                    with self.subTest(page=path.name, line=number):
                        self.assertNotRegex(line, PROVISIONAL[lang])

    def test_working_documents_moved_to_history_with_a_note(self):
        for name in MOVED:
            with self.subTest(document=name):
                moved = DOCS / "history" / name
                self.assertTrue(moved.is_file())
                text = moved.read_text(encoding="utf-8")
                self.assertRegex(text, r"(?m)^> Historical record")
                self.assertIn("](../command-catalog.md)", text)
        self.assertFalse((DOCS / "v1-design-review.md").exists())
        self.assertNotIn("Historical record", GUIDE["en"].read_text(encoding="utf-8"))

    def test_links_to_the_guide_and_to_history_resolve(self):
        skipped = {".venv", ".git", "dist", "build", "node_modules", ".claude"}
        for path in ROOT.rglob("*.md"):
            if skipped & set(path.relative_to(ROOT).parts):
                continue
            for href in re.findall(r"\]\(([^)\s#]+)(?:#[^)\s]*)?\)", path.read_text(encoding="utf-8")):
                if href.rsplit("/", 1)[-1] in {*MOVED, "command-catalog.es.md"} and not href.startswith("http"):
                    with self.subTest(source=str(path.relative_to(ROOT)), href=href):
                        self.assertTrue((path.parent / href).resolve().is_file())

    def test_site_publishes_the_guide_in_both_languages_and_not_the_history(self):
        with tempfile.TemporaryDirectory() as folder:
            out = Path(folder).resolve() / "site"
            env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
            result = subprocess.run([sys.executable, str(ROOT / "scripts/build-site.py"), str(out)], cwd=ROOT,
                                    env=env, text=True, capture_output=True, timeout=60)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            english = (out / "en/command-catalog.html").read_text(encoding="utf-8")
            spanish = (out / "es/command-catalog.html").read_text(encoding="utf-8")
            self.assertIn("Which command when", english)
            self.assertIn("Qué comando usar y cuándo", spanish)
            self.assertNotIn("Which command when", spanish)
            self.assertIn('href="commands/specify.html"', english)
            self.assertIn('href="commands/specify.html"', spanish)
            self.assertNotIn("disponible solo en inglés", spanish)
            self.assertIn("disponible solo en inglés", (out / "es/support-matrix.html").read_text(encoding="utf-8"))
            names = {path.name for path in out.rglob("*.html")}
            self.assertNotIn("command-catalog.es.html", names)
            self.assertNotIn("v1-design-review.html", names)
            self.assertFalse((out / "en/history").exists())


if __name__ == "__main__":
    unittest.main()
