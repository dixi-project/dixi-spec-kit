"""AI-assisted pull requests end with the owner's declaration; the AI is a tool, not a co-author or rights holder."""
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
DECLARATION = (
    "**Desarrollo asistido por IA:** Claude Code (Anthropic).\n\n"
    "El código ha sido desarrollado bajo dirección y supervisión humana, utilizando inteligencia artificial "
    "como herramienta de asistencia técnica.\n\n"
    "El uso de esta herramienta no implica coautoría, cesión de derechos ni participación en la propiedad "
    "intelectual a favor de Anthropic. La titularidad de los desarrollos corresponde a sus legítimos titulares "
    "conforme a la legislación y los acuerdos aplicables."
)


class AiAttributionTests(unittest.TestCase):
    def test_project_settings_set_only_the_pull_request_declaration(self):
        settings = json.loads((ROOT / ".claude/settings.json").read_text(encoding="utf-8"))
        self.assertEqual(settings, {"attribution": {"pr": DECLARATION}},
                         "no permissions, hooks, MCP servers or commit attribution changes")

    def test_local_claude_files_stay_out_of_git(self):
        ignored = (ROOT / ".gitignore").read_text(encoding="utf-8").splitlines()
        self.assertIn(".claude/worktrees/", ignored)
        self.assertIn(".claude/settings.local.json", ignored)

    def test_contributing_explains_ai_assistance(self):
        text = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
        self.assertIn("Desarrollo asistido por IA", text)
        self.assertIn("Co-Authored-By", text)
        self.assertIn("Signed-off-by", text)


if __name__ == "__main__":
    unittest.main()
