"""ADR-107 phase 1 (experimental CI): make verify inside WSL 2 on a GitHub-hosted Windows runner."""
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/wsl.yml"


class WslWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(WORKFLOW.is_file(), "missing .github/workflows/wsl.yml")
        self.text = WORKFLOW.read_text(encoding="utf-8")

    def test_least_privilege_and_pinned_actions(self):
        self.assertRegex(self.text, r"\npermissions:\n  contents: read\n")
        self.assertNotIn("secrets.", self.text)
        self.assertNotIn("id-token", self.text)
        self.assertIn("persist-credentials: false", self.text)
        uses = re.findall(r"uses: (\S+)", self.text)
        self.assertTrue(any(u.startswith("Vampire/setup-wsl@") for u in uses))
        for action in uses:
            self.assertRegex(action, r"^[\w.-]+/[\w.-]+@[0-9a-f]{40}$", f"{action} must be pinned to a full commit SHA")

    def test_runs_wsl_2_ubuntu_lts_on_windows(self):
        self.assertIn("runs-on: windows-latest", self.text)
        self.assertRegex(self.text, r"wsl-version: 2\b")
        self.assertRegex(self.text, r"distribution: Ubuntu-\d\d\.04\b")

    def test_proves_wsl_2_and_the_linux_filesystem(self):
        self.assertIn("WSL2", self.text, "the job must fail unless the kernel is WSL 2")
        self.assertIn("$HOME/kit", self.text, "the project must live under ~, not /mnt")
        self.assertIn("ext4", self.text)

    def test_runs_the_phase_1_commands(self):
        for command in ("make verify", "init demo --agent claude --controls", "check", "upgrade --dry-run",
                        "protect_tests.py", "guard_attestation.py"):
            self.assertIn(command, self.text)


if __name__ == "__main__":
    unittest.main()
