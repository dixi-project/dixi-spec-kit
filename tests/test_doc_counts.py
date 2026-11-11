"""Public texts state the real number of agent commands and the current Windows support."""
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
RESOURCES = ROOT / "src/dixi_spec_kit/resources"
UNITS_EN = "zero one two three four five six seven eight nine".split()
UNITS_ES = "cero uno dos tres cuatro cinco seis siete ocho nueve".split()


def english(n):
    tens = {2: "twenty", 3: "thirty", 4: "forty"}[n // 10]
    return tens if n % 10 == 0 else f"{tens}-{UNITS_EN[n % 10]}"


def spanish(n):
    if n // 10 == 2:
        return "veinte" if n % 10 == 0 else "veinti" + {"dos": "dós", "tres": "trés", "seis": "séis"}.get(
            UNITS_ES[n % 10], UNITS_ES[n % 10])
    tens = {3: "treinta", 4: "cuarenta"}[n // 10]
    return tens if n % 10 == 0 else f"{tens} y {UNITS_ES[n % 10]}"


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


class DocCountsTests(unittest.TestCase):
    def setUp(self):
        self.claude = sorted(p.stem for p in (RESOURCES / "claude/en").glob("dixi.*.md"))
        self.codex = sorted(p.stem for p in (RESOURCES / "codex/en").glob("dixi-*.md"))
        self.assertEqual([c.replace("dixi.", "dixi-") for c in self.claude], self.codex,
                         "Claude commands and Codex skills must match")
        self.count = len(self.claude)

    def test_support_matrix_states_the_real_count(self):
        matrix = read("docs/support-matrix.md")
        english_part, spanish_part = matrix.split("## Resumen en español", 1)
        word = english(self.count)
        self.assertIn(f"{word} `/dixi.*` commands", english_part)
        self.assertIn(f"{word} skills", english_part)
        self.assertIn(f"{spanish(self.count)} skills", spanish_part)
        self.assertIn(f"{spanish(self.count)} comandos", spanish_part)
        for number in range(20, 40):
            if number != self.count:
                self.assertNotRegex(english_part, rf"\b{english(number)} (`/dixi\.\*` commands|skills)\b")
                self.assertNotRegex(spanish_part, rf"\b{spanish(number)} (comandos|skills)\b")

    def test_support_matrix_spanish_summary_matches_wsl_support(self):
        spanish_part = read("docs/support-matrix.md").split("## Resumen en español", 1)[1]
        self.assertNotIn("Windows no está soportado", spanish_part)
        self.assertIn("WSL 2", spanish_part)
        self.assertIn("/mnt/c", spanish_part)

    def test_pypi_readme_is_current(self):
        text = read("packaging/README.md")
        for command in self.claude:
            self.assertIn(f"`/{command}`", text)
        for cli in ("init", "doctor", "check", "workflow", "upgrade --dry-run", "placeholders", "pr-size",
                    "--controls"):
            self.assertIn(cli, text)
        self.assertNotIn("(preview)", text)
        self.assertNotIn("Windows is not supported", text)
        self.assertNotIn("not hooks or permissions", text)
        self.assertIn("WSL 2", text)
        self.assertIn("pipx install dixi-spec-kit", text)


if __name__ == "__main__":
    unittest.main()
