import json
from pathlib import Path
import re
import sys
import tempfile
import unittest
import zipfile


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from dixi_spec_kit import core  # noqa: E402

CONTRACT = ROOT / "07-contracts/commands/remaining-content-contract.md"
TEMPLATES = ROOT / "src/dixi_spec_kit/resources/templates"
PROFILES = ("site", "app", "platform")
E_AREAS = ("00-governance/", "01-business/", "02-platform/", "06-flows/", "07-contracts/", "12-observability/",
           "14-delivery/", "15-operations/", "16-product/", "17-ux/", "18-knowledge-base/", "19-references/",
           "20-repos/", "22-finops/", "23-compliance/", "24-research/", "25-growth/", "26-customer-success/",
           "27-fixtures/", "28-due-diligence/")
ROW = re.compile(r"^\| `([^`]+)`[^|]*\| (✓|R|—) \| (✓|R|—) \| (✓|R|—) \|\s*$")
HEADING = re.compile(r"^### `([^`]+/)`")
AREA = re.compile(r"^[0-9]{2}-[a-z-]+/")
TOTALS = {("site", False): 77, ("site", True): 94, ("app", False): 190, ("app", True): 226,
          ("platform", False): 241, ("platform", True): 273}
DISCLAIMER = {"en": "not legal advice", "es": "no es asesoría legal"}


def contract_table():
    table, prefix = {}, None
    for line in CONTRACT.read_text(encoding="utf-8").splitlines():
        heading = HEADING.match(line)
        if heading:
            prefix = heading.group(1)
            continue
        row = ROW.match(line)
        if row and prefix:
            name = row.group(1) if AREA.match(row.group(1)) else prefix + row.group(1)
            table[name] = row.groups()[1:]
    return table


def expected(profile, regulated):
    column = PROFILES.index(profile)
    return {path for path, marks in contract_table().items()
            if marks[column] == "✓" or (regulated and marks[column] == "R")}


class RemainingContentTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()

    def files(self, project):
        return {p.relative_to(project).as_posix() for p in project.rglob("*") if p.is_file()}

    def test_contract_table_is_readable(self):
        table = contract_table()
        self.assertEqual(len(table), 177)
        self.assertTrue(all(path.startswith(E_AREAS) for path in table), [p for p in table if not p.startswith(E_AREAS)])

    def test_profiles_install_the_contract_files(self):
        baseline = set(json.loads((ROOT / "src/dixi_spec_kit/resources/project.en.json").read_text()))
        for profile in PROFILES:
            for regulated in (False, True):
                with self.subTest(profile=profile, regulated=regulated):
                    project = self.base / f"{profile}-{regulated}"
                    core.initialize(str(project), "en", "none", profile=profile, regulated=regulated)
                    installed = self.files(project)
                    in_e = {p for p in installed if p.startswith(E_AREAS)}
                    self.assertEqual(in_e, expected(profile, regulated) | {p for p in baseline if p.startswith(E_AREAS)})
                    templates = installed - baseline - {".dixi/project.json"}
                    self.assertEqual(len(templates), TOTALS[(profile, regulated)])

    def test_templates_exist_in_both_languages(self):
        for language in ("en", "es"):
            missing = sorted(p for p in contract_table() if not (TEMPLATES / language / p).is_file())
            self.assertEqual(missing, [], f"{language}: {missing[:5]}")

    def test_compliance_templates_carry_the_disclaimer(self):
        for language in ("en", "es"):
            for path in sorted(contract_table()):
                if not path.startswith("23-compliance/") or not path.endswith(".md"):
                    continue
                with self.subTest(language=language, path=path):
                    text = (TEMPLATES / language / path).read_text(encoding="utf-8").casefold()
                    self.assertIn(DISCLAIMER[language], text)

    def test_internal_material_is_not_shipped(self):
        forbidden = re.compile(r"(^14-devops/|ci-runner|/cuentas/|org-structure|project-catalog|"
                               r"competitive-products|integracion-sys-task|/adr/ADR-)")
        for language in ("en", "es"):
            names = [p.relative_to(TEMPLATES / language).as_posix()
                     for p in (TEMPLATES / language).rglob("*") if p.is_file()]
            self.assertEqual([n for n in names if forbidden.search(n)], [])

    def test_community_files(self):
        for name in ("CODE_OF_CONDUCT.md", "SUPPORT.md"):
            self.assertTrue((ROOT / name).is_file(), name)
        self.assertIn("Contributor Covenant", (ROOT / "CODE_OF_CONDUCT.md").read_text(encoding="utf-8"))
        for document in ("README.md", "CONTRIBUTING.md"):
            text = (ROOT / document).read_text(encoding="utf-8")
            for name in ("CODE_OF_CONDUCT.md", "SUPPORT.md"):
                self.assertIn(f"]({name})", text, f"{document} -> {name}")

    def test_wheel_contains_remaining_templates(self):
        wheels = list((ROOT / "dist").glob("dixi_spec_kit-*.whl"))
        self.assertEqual(len(wheels), 1, "Build exactly one wheel before verification")
        with zipfile.ZipFile(wheels[0]) as archive:
            names = set(archive.namelist())
        for language in ("en", "es"):
            for path in contract_table():
                self.assertIn(f"dixi_spec_kit/resources/templates/{language}/{path}", names)


if __name__ == "__main__":
    unittest.main()
