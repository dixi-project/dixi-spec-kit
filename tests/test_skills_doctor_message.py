"""TASK-031: `dixi doctor` does not list VS Code/Copilot among the agents that read .agents/skills/."""
import json
from pathlib import Path
import unittest


LOCALES = Path(__file__).resolve().parents[1] / "src" / "dixi_spec_kit" / "locales"


class SkillsDoctorMessageTests(unittest.TestCase):
    def test_agent_skills_message_matches_the_re_read_documentation(self):
        for language in ("en", "es"):
            with self.subTest(language=language):
                message = json.loads((LOCALES / f"{language}.json").read_text(encoding="utf-8"))["agent_skills"]
                self.assertIn(".agents/skills/", message)
                self.assertIn("OpenCode", message)
                self.assertNotIn("VS Code", message)
                self.assertNotIn("Copilot", message)


if __name__ == "__main__":
    unittest.main()
