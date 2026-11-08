import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from notes.store import NoteError, NoteStore

ROOT = Path(__file__).resolve().parents[1]


class NoteStoreTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "notes.json"
        self.store = NoteStore(self.path)

    def test_add_assigns_increasing_ids(self):
        first = self.store.add("  primera idea ")
        second = self.store.add("segunda")
        self.assertEqual((first.id, first.text), (1, "primera idea"))
        self.assertEqual(second.id, 2)
        self.assertEqual([n.id for n in NoteStore(self.path).list()], [1, 2])

    def test_invalid_text_leaves_store_untouched(self):
        self.store.add("válida")
        before = self.path.read_bytes()
        for text in ("", "   ", "x" * 1001):
            with self.assertRaises(NoteError):
                self.store.add(text)
        self.assertEqual(self.path.read_bytes(), before)

    def test_missing_store_is_empty(self):
        self.assertEqual(self.store.list(), [])
        self.assertFalse(self.path.exists())

    def test_search_is_case_insensitive(self):
        self.store.add("Comprar CAFÉ")
        self.store.add("llamar a Ana")
        self.assertEqual([n.text for n in self.store.search("café")], ["Comprar CAFÉ"])
        self.assertEqual(self.store.search("nada"), [])

    def test_persisted_format(self):
        self.store.add("hola")
        data = json.loads(self.path.read_text(encoding="utf-8"))
        self.assertEqual(data["schema_version"], 1)
        self.assertEqual(data["notes"][0]["text"], "hola")


class CliTests(unittest.TestCase):
    def run_cli(self, folder, *args):
        return subprocess.run([sys.executable, "-m", "notes", "--file", str(Path(folder) / "n.json")] + list(args),
                              cwd=ROOT, text=True, capture_output=True, timeout=10)

    def test_cli_round_trip(self):
        with tempfile.TemporaryDirectory() as folder:
            self.assertEqual(self.run_cli(folder, "add", "Leer DDD").returncode, 0)
            listed = self.run_cli(folder, "list")
            self.assertEqual(listed.returncode, 0)
            self.assertIn("#1 Leer DDD", listed.stdout)
            found = self.run_cli(folder, "search", "ddd")
            self.assertIn("#1 Leer DDD", found.stdout)

    def test_cli_invalid_input_exit_code(self):
        with tempfile.TemporaryDirectory() as folder:
            result = self.run_cli(folder, "add", "   ")
            self.assertEqual(result.returncode, 2)
            self.assertTrue(result.stderr.strip())


if __name__ == "__main__":
    unittest.main()
