"""TASK-021: `/dixi.status` tells a returning person where the last session left off, and stays read-only."""
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
RESOURCES = ROOT / "src/dixi_spec_kit/resources"
TEXTS = {
    ("claude", "en"): RESOURCES / "claude/en/dixi.status.md",
    ("claude", "es"): RESOURCES / "claude/es/dixi.status.md",
    ("codex", "en"): RESOURCES / "codex/en/dixi-status.md",
    ("codex", "es"): RESOURCES / "codex/es/dixi-status.md",
}
READ_ONLY = {"en": "Do not modify files, commit or push.", "es": "No modifiques archivos, no hagas commits ni push."}
LEFT_OFF = {"en": "where the last session left off", "es": "dónde se quedó la última sesión"}


def section(text, heading):
    return text.split(f"\n## {heading}\n", 1)[1].split("\n## ", 1)[0]


def run(script, *arguments):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    return subprocess.run([sys.executable, str(ROOT / "scripts" / script), *arguments], cwd=ROOT, env=env, text=True,
                          capture_output=True, timeout=60)


class StatusResumeTests(unittest.TestCase):
    def test_steps_read_the_handoff_recent_contracts_and_open_tasks(self):
        for (adapter, lang), path in TEXTS.items():
            with self.subTest(adapter=adapter, lang=lang):
                text = path.read_text(encoding="utf-8")
                steps = section(text, "Steps" if lang == "en" else "Pasos")
                self.assertIn("`.context/handoff.md`", steps)
                self.assertIn("`git log --oneline -10 -- 07-contracts/`", steps)
                self.assertIn("`05-features/*/tasks.md`", steps)
                self.assertIn(LEFT_OFF[lang], text)
                order = [steps.index(piece) for piece in ("`dixi doctor`", "`.context/handoff.md`", "07-contracts/",
                                                          "dixi-build T-003" if adapter == "codex" else "/dixi.build T-003")]
                self.assertEqual(order, sorted(order))

    def test_it_stays_read_only(self):
        for (adapter, lang), path in TEXTS.items():
            with self.subTest(adapter=adapter, lang=lang):
                text = path.read_text(encoding="utf-8")
                steps = section(text, "Steps" if lang == "en" else "Pasos")
                self.assertTrue(steps.rstrip().endswith(READ_ONLY[lang]), steps[-120:])
                commands = re.findall(r"`(git [^`]+|gh [^`]+)`", text)
                self.assertEqual(commands, ["git log --oneline -10 -- 07-contracts/"])
                self.assertNotRegex(steps, r"(?i)\b(write|create|update|escribe|crea|actualiza)\b")

    def test_a_missing_handoff_or_repository_is_reported_not_an_error(self):
        for (adapter, lang), path in TEXTS.items():
            with self.subTest(adapter=adapter, lang=lang):
                steps = section(path.read_text(encoding="utf-8"), "Steps" if lang == "en" else "Pasos")
                self.assertRegex(steps, r"does not exist|no existe")
                self.assertRegex(steps, r"not a Git repository|no es un repositorio Git")

    def test_recipe_matches_the_command_in_both_languages(self):
        for lang in ("en", "es"):
            recipe = json.loads((RESOURCES / f"workflows.{lang}.json").read_text(encoding="utf-8"))["operations"]["status"]
            with self.subTest(lang=lang):
                text = " ".join([*recipe["inputs"], *recipe["steps"], *recipe["outputs"], *recipe["checks"]])
                self.assertIn(".context/handoff.md", text)
                self.assertIn("07-contracts/", text)
                self.assertIn(LEFT_OFF[lang], text)
                self.assertRegex(recipe["checks"][0], r"No file was modified|No se modificó ningún archivo")

    def test_derived_texts_and_reference_pages_are_current(self):
        self.assertEqual(run("generate-codex-skills.py", "--check").returncode, 0)
        self.assertEqual(run("build-command-reference.py", "--check").returncode, 0)
        page = (ROOT / "docs/commands/status.md").read_text(encoding="utf-8")
        self.assertIn("- `.context/handoff.md`", page)

    def test_contract_describes_what_status_reads(self):
        contract = (ROOT / "07-contracts/commands/claude-code-adapter-contract.md").read_text(encoding="utf-8")
        row = next(line for line in contract.splitlines() if line.startswith("| `/dixi.status` |"))
        self.assertIn("Nothing (report only)", row)
        self.assertIn("`.context/handoff.md`", row)
        self.assertIn("`07-contracts/`", row)


if __name__ == "__main__":
    unittest.main()
