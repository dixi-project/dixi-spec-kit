"""ADR-107 phase 1 done: WSL 2 is documented as supported with evidence; native Windows and /mnt stay out."""
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


class WslSupportDocsTests(unittest.TestCase):
    def matrix_rows(self):
        return [line for line in read("docs/support-matrix.md").splitlines() if line.startswith("| Windows")]

    def test_support_matrix_has_wsl_2_row_with_evidence(self):
        rows = self.matrix_rows()
        wsl = [r for r in rows if r.startswith("| Windows (WSL 2")]
        self.assertEqual(len(wsl), 1, "one WSL 2 row expected")
        self.assertIn("| Supported", wsl[0])
        self.assertIn("wsl.yml", wsl[0])
        self.assertIn("/mnt/c", wsl[0])

    def test_native_windows_stays_unsupported(self):
        native = [r for r in self.matrix_rows() if r.startswith("| Windows (native)")]
        self.assertEqual(len(native), 1)
        self.assertIn("| Not supported", native[0])
        self.assertNotIn("planned", native[0])

    def test_readmes_and_local_development_explain_wsl_2(self):
        for path in ("README.md", "README.es.md", "docs/local-development.md"):
            with self.subTest(path=path):
                text = read(path)
                self.assertIn("WSL 2", text)
                self.assertIn("/mnt/c", text)
        self.assertIn("\n## Windows (WSL 2)\n", read("docs/local-development.md"))

    def test_contract_records_the_wsl_run(self):
        contract = read("07-contracts/commands/local-core-contract.md")
        self.assertIn("WSL 2", contract)
        self.assertIn("microsoft-standard-WSL2", contract)
        self.assertIn("actions/runs/", contract)


if __name__ == "__main__":
    unittest.main()
