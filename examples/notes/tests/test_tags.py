import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from notes.store import NoteError, NoteStore

ROOT = Path(__file__).resolve().parents[1]


class TagTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "notes.json"
        self.store = NoteStore(self.path)

    def test_tags_are_normalized(self):
        note = self.store.add("idea", [" Trabajo", "trabajo", "URGENTE", "ddd"])
        self.assertEqual(note.tags, ("trabajo", "urgente", "ddd"))

    def test_invalid_tags_rejected_without_writing(self):
        self.store.add("base")
        before = self.path.read_bytes()
        for tag in ("", "  ", "x" * 33, "con espacio", "ñandú"):
            with self.assertRaises(NoteError):
                self.store.add("otra", [tag])
        self.assertEqual(self.path.read_bytes(), before)

    def test_filter_by_tag(self):
        self.store.add("a", ["casa"])
        self.store.add("b", ["trabajo"])
        self.store.add("c", ["Casa", "trabajo"])
        self.assertEqual([n.text for n in self.store.list(tag="CASA")], ["a", "c"])

    def test_legacy_tags_normalized_on_read(self):
        legacy = {"schema_version": 1, "notes": [{"id": 1, "text": "vieja", "tags": ["Casa", "casa", " Ideas "]}]}
        self.path.write_text(json.dumps(legacy), encoding="utf-8")
        before = self.path.read_bytes()
        self.assertEqual(self.store.list()[0].tags, ("casa", "ideas"))
        self.assertEqual(self.path.read_bytes(), before)

    def test_cli_filter_and_invalid_tag(self):
        file = str(self.path)
        run = lambda *a: subprocess.run([sys.executable, "-m", "notes", "--file", file] + list(a),
                                        cwd=ROOT, text=True, capture_output=True, timeout=10)
        self.assertEqual(run("add", "uno", "--tag", "Casa").returncode, 0)
        self.assertEqual(run("add", "dos").returncode, 0)
        listed = run("list", "--tag", "casa")
        self.assertEqual(listed.stdout.strip(), "#1 uno [casa]")
        self.assertEqual(run("--lang", "en", "add", "tres", "--tag", "bad tag").returncode, 2)


if __name__ == "__main__":
    unittest.main()
