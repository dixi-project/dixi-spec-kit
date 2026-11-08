import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
import zipfile


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from dixi_spec_kit import core  # noqa: E402

CONTRACT = ROOT / "07-contracts/commands/profiles-contract.md"
TEMPLATES = ROOT / "src/dixi_spec_kit/resources/templates"
PROFILES = ("site", "app", "platform")
COMBINATIONS = [("minimal", False)] + [(p, r) for p in PROFILES for r in (False, True)]
D_AREAS = ("08-data/", "09-architecture/", "10-engineering/", "11-quality/", "13-security/", "21-ai/")
E_AREAS = ("00-governance/", "01-business/", "02-platform/", "06-flows/", "07-contracts/", "12-observability/",
           "14-delivery/", "15-operations/", "16-product/", "17-ux/", "18-knowledge-base/", "19-references/",
           "20-repos/", "22-finops/", "23-compliance/", "24-research/", "25-growth/", "26-customer-success/",
           "27-fixtures/", "28-due-diligence/")
ROW = re.compile(r"^\| `([^`]+)`[^|]*\| (✓|R|—) \| (✓|R|—) \| (✓|R|—) \|\s*$")
HEADING = re.compile(r"^### `([^`]+/)`")
MARKERS = (re.compile(r"EIS-IA", re.I), re.compile(r"ecosystem_dixi", re.I), re.compile(r"Dixi Project", re.I),
           re.compile(r"bedrock", re.I), re.compile(r"sys[_-]?task", re.I), re.compile(r"code(build|pipeline)", re.I),
           re.compile(r"(?<![0-9])[0-9]{12}(?![0-9])"))
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+\.[A-Za-z]{2,})")


def contract_table():
    """Return {path: (site, app, platform)} from the block D contract tables."""
    table, prefix = {}, None
    for line in CONTRACT.read_text(encoding="utf-8").splitlines():
        heading = HEADING.match(line)
        if heading:
            prefix = heading.group(1)
            continue
        row = ROW.match(line)
        if row and prefix:
            table[prefix + row.group(1)] = row.groups()[1:]
    return table


def expected(profile, regulated):
    if profile == "minimal":
        return set()
    column = PROFILES.index(profile)
    return {path for path, marks in contract_table().items()
            if marks[column] == "✓" or (regulated and marks[column] == "R")}


def baseline(language):
    return json.loads((ROOT / f"src/dixi_spec_kit/resources/project.{language}.json").read_text(encoding="utf-8"))


class ProfilesTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()

    def cli(self, *args, cwd=None):
        env = dict(os.environ, PYTHONPATH=str(ROOT / "src"), PYTHONDONTWRITEBYTECODE="1")
        command = [sys.executable, "-c", "import socket, runpy; "
                   "socket.socket=lambda *a, **k: (_ for _ in ()).throw(AssertionError('network')); "
                   "runpy.run_module('dixi_spec_kit', run_name='__main__')"]
        return subprocess.run(command + list(args), cwd=cwd or self.base, env=env,
                              text=True, capture_output=True, timeout=30)

    def init(self, name, *options):
        project = self.base / name
        result = self.cli("init", str(project), *options)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return project

    def files(self, project):
        return {str(p.relative_to(project)) for p in project.rglob("*") if p.is_file()}

    def metadata(self, project):
        return json.loads((project / ".dixi/project.json").read_text(encoding="utf-8"))

    def test_contract_table_is_readable(self):
        table = contract_table()
        self.assertEqual(len(table), 96)
        self.assertTrue(all(path.startswith(D_AREAS) for path in table))

    def test_help_lists_profile_options(self):
        result = self.cli("init", "--help")
        for option in ("--profile", "--regulated", "minimal", "site", "app", "platform"):
            self.assertIn(option, result.stdout)

    def test_default_and_minimal_are_the_baseline(self):
        for language in ("en", "es"):
            for agent in core.AGENTS:
                with self.subTest(language=language, agent=agent):
                    default = self.base / f"default-{language}-{agent}"
                    minimal = self.base / f"minimal-{language}-{agent}"
                    for project, extra in ((default, []), (minimal, ["--profile", "minimal"])):
                        result = self.cli("--lang", language, "init", str(project), "--agent", agent, *extra)
                        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                    self.assertEqual(self.files(default), self.files(minimal))
                    for name in self.files(default):
                        self.assertEqual((default / name).read_bytes(), (minimal / name).read_bytes(), name)
                    installed = self.files(default) - {".dixi/project.json"}
                    adapter = set(core.adapter_files(agent, language))
                    self.assertEqual(installed - adapter, set(baseline(language)))
                    for name, text in baseline(language).items():
                        self.assertEqual((default / name).read_text(encoding="utf-8"), text, name)
                    data = self.metadata(default)
                    self.assertEqual((data["profile"], data["regulated"]), ("minimal", False))

    def test_profiles_install_the_contract_files(self):
        base = set(baseline("en"))
        for profile, regulated in COMBINATIONS[1:]:
            with self.subTest(profile=profile, regulated=regulated):
                options = ["--profile", profile] + (["--regulated"] if regulated else [])
                project = self.init(f"{profile}-{regulated}", *options)
                installed = self.files(project) - {".dixi/project.json"}
                in_d = {p for p in installed if p.startswith(D_AREAS)}
                self.assertEqual(in_d, expected(profile, regulated) | {p for p in base if p.startswith(D_AREAS)})
                extra = installed - base - in_d
                self.assertTrue(all(p.startswith(E_AREAS) for p in extra), sorted(extra)[:5])
                data = self.metadata(project)
                self.assertEqual((data["profile"], data["regulated"]), (profile, regulated))
                for name in installed:
                    self.assertEqual(hashlib.sha256((project / name).read_bytes()).hexdigest(),
                                     data["managed_files"][name], name)

    def test_invalid_profile_options_write_nothing(self):
        for options in (["--profile", "minimal", "--regulated"], ["--regulated"], ["--profile", "huge"]):
            with self.subTest(options=options):
                project = self.base / "invalid"
                result = self.cli("init", str(project), *options)
                self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
                self.assertFalse(project.exists())

    def test_every_combination_passes_check(self):
        for language in ("en", "es"):
            for agent in core.AGENTS:
                for profile, regulated in COMBINATIONS:
                    with self.subTest(language=language, agent=agent, profile=profile, regulated=regulated):
                        project = self.base / f"{language}-{agent}-{profile}-{regulated}"
                        core.initialize(str(project), language, agent, profile=profile, regulated=regulated)
                        code, issues = core.check_project(project)
                        self.assertEqual(code, 0, [i for i in issues if i["key"] != "structure_only"][:5])

    def test_templates_exist_in_both_languages_and_follow_the_rules(self):
        sets = {}
        for language in ("en", "es"):
            folder = TEMPLATES / language
            sets[language] = {str(p.relative_to(folder)) for p in folder.rglob("*") if p.is_file()}
        self.assertEqual(sets["en"], sets["es"])
        self.assertTrue(set(contract_table()) <= sets["en"], sorted(set(contract_table()) - sets["en"])[:5])
        for language in ("en", "es"):
            for name in sorted(sets[language]):
                if not name.endswith(".md"):
                    continue
                with self.subTest(language=language, name=name):
                    text = (TEMPLATES / language / name).read_text(encoding="utf-8")
                    self.assertTrue(text.startswith("# "), "title")
                    self.assertIn("\n## Purpose\n" if language == "en" else "\n## Propósito\n", text)
                    self.assertIn("{{pending:", text)
                    self.assertIn("\n## Related\n" if language == "en" else "\n## Relacionados\n", text)

    def test_templates_contain_no_internal_markers(self):
        for path in sorted(TEMPLATES.rglob("*")):
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8")
            with self.subTest(path=str(path.relative_to(TEMPLATES))):
                for marker in MARKERS:
                    self.assertIsNone(marker.search(text), marker.pattern)
                for domain in EMAIL.findall(text):
                    self.assertTrue(domain.endswith("example.com"), domain)

    def test_deleted_profile_template_is_optional(self):
        project = self.init("app", "--profile", "app")
        (project / "08-data/data-architecture.md").unlink()
        self.assertEqual(self.cli("check", cwd=project).returncode, 0)
        plan = self.cli("--json", "upgrade", "--dry-run", cwd=project)
        self.assertEqual(plan.returncode, 0, plan.stdout)
        self.assertEqual(json.loads(plan.stdout)["upgrade"]["files"]["missing"], ["08-data/data-architecture.md"])
        (project / "00-master-spec.md").unlink()
        self.assertEqual(self.cli("check", cwd=project).returncode, 1)

    def test_upgrade_plan_for_another_profile(self):
        project = self.init("minimal")
        reference = self.init("reference", "--profile", "app", "--regulated")
        plan = self.cli("--json", "upgrade", "--dry-run", "--profile", "app", "--regulated", cwd=project)
        self.assertEqual(plan.returncode, 0, plan.stdout + plan.stderr)
        new = set(json.loads(plan.stdout)["upgrade"]["files"]["new"])
        self.assertEqual(new, self.files(reference) - self.files(project))
        self.assertEqual(self.cli("upgrade", "--dry-run", "--regulated", cwd=project).returncode, 2)

    def test_metadata_profile_values(self):
        project = self.init("meta", "--profile", "site")
        path = project / ".dixi/project.json"
        original = path.read_text(encoding="utf-8")
        for field, value in (("profile", "huge"), ("profile", 3), ("regulated", "yes")):
            with self.subTest(field=field, value=value):
                data = json.loads(original)
                data[field] = value
                path.write_text(json.dumps(data))
                self.assertEqual(self.cli("check", cwd=project).returncode, 1)
        legacy = self.init("legacy")
        data = self.metadata(legacy)
        del data["profile"], data["regulated"]
        (legacy / ".dixi/project.json").write_text(json.dumps(data))
        self.assertEqual(self.cli("check", cwd=legacy).returncode, 0)
        doctor = json.loads(self.cli("--json", "doctor", cwd=legacy).stdout)["messages"]
        self.assertIn({"profile": "minimal", "regulated": False},
                      [m["params"] for m in doctor if m["key"] == "profile"])

    def test_doctor_reports_profile(self):
        project = self.init("doctor", "--profile", "app", "--regulated")
        result = self.cli("--json", "doctor", cwd=project)
        self.assertEqual(result.returncode, 0, result.stdout)
        messages = json.loads(result.stdout)["messages"]
        self.assertIn({"profile": "app", "regulated": True}, [m["params"] for m in messages if m["key"] == "profile"])

    def test_inventory_accepts_up_to_one_thousand_files(self):
        project = self.init("big")
        data = self.metadata(project)
        extra = project / "docs/extra"
        extra.mkdir(parents=True)
        for index in range(1000 - len(data["managed_files"])):
            name = f"docs/extra/{index}.md"
            (project / name).write_text(f"# {index}\n")
            data["managed_files"][name] = hashlib.sha256(f"# {index}\n".encode()).hexdigest()
        (project / ".dixi/project.json").write_text(json.dumps(data))
        self.assertEqual(self.cli("check", cwd=project).returncode, 0)
        (project / "docs/extra/over.md").write_text("# over\n")
        data["managed_files"]["docs/extra/over.md"] = hashlib.sha256(b"# over\n").hexdigest()
        (project / ".dixi/project.json").write_text(json.dumps(data))
        self.assertEqual(self.cli("check", cwd=project).returncode, 1)

    def test_wheel_contains_templates_and_manifest(self):
        wheels = list((ROOT / "dist").glob("dixi_spec_kit-*.whl"))
        self.assertEqual(len(wheels), 1, "Build exactly one wheel before verification")
        with zipfile.ZipFile(wheels[0]) as archive:
            names = set(archive.namelist())
        self.assertIn("dixi_spec_kit/resources/profiles.json", names)
        for language in ("en", "es"):
            for path in contract_table():
                self.assertIn(f"dixi_spec_kit/resources/templates/{language}/{path}", names)


if __name__ == "__main__":
    unittest.main()
