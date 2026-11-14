"""TASK-031: an agent is supported with --agent skills only with a recorded run, in both languages."""
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = "07-contracts/commands/agent-skills-adapter-contract.md"
MATRIX = "docs/support-matrix.md"
AGENTS = ("Cursor", "VS Code/Copilot", "OpenCode", "Gemini CLI", "Goose", "Amp")
AGENT_VERSION = re.compile(r"(" + "|".join(re.escape(a) for a in AGENTS) + r") (\d+\.\d+\.\d+)")
TASK_DATE = "2026-11-14"


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def section(text, heading):
    start = text.index(f"\n## {heading}\n")
    end = text.find("\n## ", start + 1)
    return text[start:end if end != -1 else None]


class VerifiedAgentsTests(unittest.TestCase):
    def skills_status(self):
        rows = [line for line in read(MATRIX).splitlines() if line.startswith("| `--agent skills`")]
        self.assertEqual(len(rows), 1, "one --agent skills row expected")
        return rows[0].split("|")[2]

    def verified(self):
        status = self.skills_status()
        supported = status.split("format compatible")[0]
        pairs = AGENT_VERSION.findall(supported)
        self.assertTrue(pairs, "the --agent skills row names at least one verified agent with its version")
        return pairs

    def test_every_supported_agent_has_a_recorded_run(self):
        runs = section(read(CONTRACT), "Manual runs")
        entries = [line for line in runs.splitlines() if line.startswith("- ")]
        for agent, version in self.verified():
            with self.subTest(agent=agent):
                self.assertTrue(
                    any(agent in entry and version in entry for entry in entries),
                    f"{agent} {version} is supported in the matrix without a manual-run entry in the contract",
                )

    def test_unverified_agents_stay_format_compatible(self):
        self.assertIn("format compatible, not verified", self.skills_status())

    def test_spanish_summary_names_the_verified_agents(self):
        spanish = [line for line in read(MATRIX).splitlines() if line.startswith("Soportado:")]
        self.assertEqual(len(spanish), 1, "one Spanish summary expected")
        self.assertIn("--agent skills", spanish[0])
        for agent, version in self.verified():
            with self.subTest(agent=agent):
                self.assertIn(f"{agent} {version}", spanish[0])

    def test_discovery_table_was_re_read_for_this_task(self):
        found = re.search(r"\| Source \(read (\d{4}-\d{2}-\d{2})\) \|", read(CONTRACT))
        self.assertIsNotNone(found, "the discovery table states when its sources were read")
        self.assertGreaterEqual(found.group(1), TASK_DATE)


if __name__ == "__main__":
    unittest.main()
