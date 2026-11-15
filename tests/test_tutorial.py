"""TASK-032: a step-by-step tutorial on the documentation site."""
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import shlex
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
TUTORIAL = DOCS / "tutorial"
STEPS = ("01-install", "02-init", "03-specify", "04-plan", "05-tasks", "06-build", "07-verify")
PAGES = ("index",) + STEPS
SUFFIX = {"en": ".md", "es": ".es.md"}
PURPOSE = {"en": "\n## Purpose\n", "es": "\n## Propósito\n"}
# Lines of a tutorial code block that the test does not run, because they install software or need a tool
# outside the kit. Every other line must be `cd <folder>` or a `dixi` command, and it is run.
NOT_RUN = ("uv tool install", "pipx install", "git ", "make verify", "claude", "codex", "opencode")
AGENTS = ("--agent claude", "--agent codex", "--agent skills", "--agent none")


def read(path):
    return path.read_text(encoding="utf-8")


def source(page, lang):
    return TUTORIAL / f"{page}{SUFFIX[lang]}"


def code_lines(text):
    """Lines inside fenced ```bash blocks."""
    return [line.strip() for block in re.findall(r"```bash\n(.*?)```", text, re.S)
            for line in block.splitlines() if line.strip() and not line.strip().startswith("#")]


def terminal_commands(text):
    """The `dixi` subcommand named by every `dixi ...` in code spans and code blocks (global options skipped)."""
    found = set()
    for snippet in re.findall(r"`(dixi [^`]+)`", text) + [line for line in code_lines(text) if line.startswith("dixi ")]:
        tokens = shlex.split(snippet)[1:]
        while tokens and tokens[0].startswith("-"):
            tokens = tokens[2:] if tokens[0] == "--lang" else tokens[1:]
        if tokens:
            found.add(tokens[0])
    return found


class Nav(HTMLParser):
    def __init__(self):
        super().__init__()
        self.inside, self.items = False, []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.inside = self.inside or (tag == "ul" and attrs.get("id") == "pages")
        if self.inside and tag == "li":
            self.items.append(["group" in (attrs.get("class") or ""), ""])
        if self.inside and tag == "a" and self.items:
            self.items[-1][1] = attrs.get("href", "")

    def handle_endtag(self, tag):
        if tag == "ul":
            self.inside = False

    def handle_data(self, data):
        if self.inside and self.items and self.items[-1][0] and data.strip():
            self.items[-1][1] = data.strip()


class TutorialPagesTests(unittest.TestCase):
    def test_every_page_exists_in_both_languages(self):
        self.assertEqual(sorted(path.name for path in TUTORIAL.glob("*.md")),
                         sorted(f"{page}{suffix}" for page in PAGES for suffix in SUFFIX.values()))
        for page in PAGES:
            for lang in SUFFIX:
                with self.subTest(page=page, lang=lang):
                    text = read(source(page, lang))
                    self.assertTrue(text.startswith("# "))
                    self.assertIn(PURPOSE[lang], text)

    def test_spanish_pages_keep_the_same_links_commands_and_tables(self):
        for page in PAGES:
            with self.subTest(page=page):
                english, spanish = read(source(page, "en")), read(source(page, "es"))
                links = lambda text: sorted(link.replace(".es.md", ".md")  # noqa: E731
                                            for link in re.findall(r"\]\(((?!https?:)[^)#]+)", text))
                self.assertEqual(links(spanish), links(english))
                self.assertEqual(code_lines(spanish), code_lines(english))
                self.assertEqual(len(re.findall(r"(?m)^\| ", spanish)), len(re.findall(r"(?m)^\| ", english)))

    def test_introduction_links_every_step_in_order(self):
        for lang, suffix in SUFFIX.items():
            text = read(source("index", lang))
            positions = [text.find(f"]({step}{suffix})") for step in STEPS]
            with self.subTest(lang=lang):
                self.assertNotIn(-1, positions)
                self.assertEqual(positions, sorted(positions))

    def test_each_step_links_the_next_one_and_the_reference_of_its_commands(self):
        for lang, suffix in SUFFIX.items():
            for position, step in enumerate(STEPS):
                text = read(source(step, lang))
                with self.subTest(step=step, lang=lang):
                    if position + 1 < len(STEPS):
                        self.assertIn(f"]({STEPS[position + 1]}{suffix})", text)
                    for operation in set(re.findall(r"/dixi\.([a-z-]+)", text)):
                        self.assertIn(f"](../commands/{operation}{suffix})", text)
                    for command in terminal_commands(text):
                        self.assertIn(f"](../cli/{command}{suffix})", text)

    def test_every_command_named_exists(self):
        for page in PAGES:
            for lang in SUFFIX:
                text = read(source(page, lang))
                with self.subTest(page=page, lang=lang):
                    for operation in re.findall(r"/dixi\.([a-z-]+)", text):
                        self.assertTrue((DOCS / "commands" / f"{operation}.md").is_file(), operation)
                    for command in terminal_commands(text):
                        self.assertTrue((DOCS / "cli" / f"{command}.md").is_file(), command)

    def test_every_adapter_is_shown(self):
        for lang in SUFFIX:
            text = "".join(read(source(page, lang)) for page in ("index", "02-init"))
            for agent in AGENTS:
                with self.subTest(lang=lang, agent=agent):
                    self.assertIn(agent, text)


class TutorialRunsTests(unittest.TestCase):
    def test_terminal_commands_run_in_order_in_an_empty_folder(self):
        lines = [line for step in STEPS for line in code_lines(read(source(step, "en")))]
        self.assertTrue(any(line.startswith("dixi init") for line in lines))
        env = dict(os.environ, PYTHONPATH=str(ROOT / "src"), PYTHONDONTWRITEBYTECODE="1")
        with tempfile.TemporaryDirectory() as temp:
            cwd = Path(temp).resolve()
            for line in lines:
                with self.subTest(line=line):
                    if line.startswith(NOT_RUN):
                        continue
                    if line.startswith("cd "):
                        cwd = (cwd / shlex.split(line)[1]).resolve()
                        self.assertTrue(cwd.is_dir(), line)
                        continue
                    self.assertTrue(line.startswith("dixi "), f"not a terminal command the test can run: {line}")
                    result = subprocess.run([sys.executable, "-m", "dixi_spec_kit", *shlex.split(line)[1:]],
                                            cwd=cwd, env=env, text=True, capture_output=True, timeout=30)
                    self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


class TutorialSiteTests(unittest.TestCase):
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

    def test_tutorial_is_a_menu_group_before_the_command_reference(self):
        self.assertEqual(self.result.returncode, 0, self.result.stdout + self.result.stderr)
        for lang in SUFFIX:
            catalog = json.loads(read(ROOT / "scripts/site" / f"{lang}.json"))
            nav = Nav()
            nav.feed(read(self.out / lang / "index.html"))
            groups = [text for is_group, text in nav.items if is_group]
            with self.subTest(lang=lang):
                self.assertIn(catalog["tutorial"], groups)
                self.assertLess(groups.index(catalog["tutorial"]), groups.index(catalog["commands"]))
                start = [index for index, item in enumerate(nav.items) if item == [True, catalog["tutorial"]]][0]
                pages = [href for _, href in nav.items[start + 1:start + 1 + len(PAGES)]]
                self.assertEqual(pages, [f"tutorial/{page}.html" for page in PAGES])

    def test_pages_are_published_in_each_language(self):
        for lang in SUFFIX:
            for page in PAGES:
                with self.subTest(lang=lang, page=page):
                    title = read(source(page, lang)).splitlines()[0][2:]
                    self.assertIn(f">{title}</h1>", read(self.out / lang / "tutorial" / f"{page}.html"))


class TutorialLinkedTests(unittest.TestCase):
    def test_documentation_index_and_readmes_link_the_tutorial(self):
        for name, target in (("docs/documentation.md", "tutorial/index.md"),
                             ("docs/documentation.es.md", "tutorial/index.es.md"),
                             ("README.md", "docs/tutorial/index.md"), ("README.es.md", "docs/tutorial/index.es.md")):
            with self.subTest(document=name):
                self.assertIn(f"]({target})", read(ROOT / name))


if __name__ == "__main__":
    unittest.main()
