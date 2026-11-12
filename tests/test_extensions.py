"""ADR-109: local, data-only extensions add operations named dixi-<extension>-<operation> (threat T14)."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
TEXT = {
    "en": '---\ndescription: "Check a deployment checklist"\nargument-hint: "[service]"\n---\n\n'
          "# /dixi-acme-deploy-check\n\n## Goal\n\nCheck the deployment of `$ARGUMENTS`; see `/dixi.release`.\n",
    "es": '---\ndescription: "Revisar una lista de despliegue"\nargument-hint: "[servicio]"\n---\n\n'
          "# /dixi-acme-deploy-check\n\n## Objetivo\n\nRevisar el despliegue de `$ARGUMENTS`; ver `/dixi.release`.\n",
}


def digest(data):
    return hashlib.sha256(data).hexdigest()


class ExtensionTests(unittest.TestCase):
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
                              text=True, capture_output=True, timeout=20)

    def project(self, agent="claude", language="en", name="project"):
        path = self.base / name
        result = self.cli("--lang", language, "init", str(path), "--agent", agent)
        self.assertEqual(result.returncode, 0, result.stderr)
        return path

    def extension(self, name="acme-ext", ext_id="acme", operations=("deploy-check",), texts=TEXT):
        folder = self.base / name
        (folder / "operations/en").mkdir(parents=True)
        (folder / "operations/es").mkdir(parents=True)
        (folder / "extension.json").write_text(json.dumps({"id": ext_id, "version": "1.0.0",
                                                           "operations": list(operations)}))
        for op in operations:
            for lang in ("en", "es"):
                (folder / f"operations/{lang}/{op}.md").write_text(texts[lang])
        return folder

    def snapshot(self, path):
        return {str(p.relative_to(path)): digest(p.read_bytes()) for p in path.rglob("*") if p.is_file()}

    def add(self, project, folder):
        return self.cli("--json", "extension", "add", str(folder), cwd=project)

    def metadata(self, project):
        return json.loads((project / ".dixi/project.json").read_text())

    def test_claude_project_gets_a_prefixed_command(self):
        project = self.project("claude")
        result = self.add(project, self.extension())
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        command = project / ".claude/commands/dixi-acme-deploy-check.md"
        self.assertEqual(command.read_text(), TEXT["en"])
        self.assertTrue((project / ".dixi/extensions/acme/extension.json").is_file())
        recorded = self.metadata(project)["extensions"]["acme"]
        self.assertEqual(recorded["version"], "1.0.0")
        self.assertIn(".claude/commands/dixi-acme-deploy-check.md", recorded["files"])
        self.assertEqual(self.cli("check", cwd=project).returncode, 0)
        listing = json.loads(self.cli("--json", "extension", "list", cwd=project).stdout)
        self.assertEqual([e["id"] for e in listing["extension"]["installed"]], ["acme"])

    def test_codex_and_skills_projects_get_converted_skills(self):
        for agent in ("codex", "skills"):
            with self.subTest(agent=agent):
                project = self.project(agent, name=f"p-{agent}")
                self.assertEqual(self.add(project, self.extension(name=f"e-{agent}")).returncode, 0)
                text = (project / ".agents/skills/dixi-acme-deploy-check/SKILL.md").read_text()
                self.assertTrue(text.startswith("---\nname: dixi-acme-deploy-check\n"))
                self.assertNotIn("$ARGUMENTS", text)
                self.assertNotIn("/dixi", text)
                self.assertEqual("disable-model-invocation: true" in text, agent == "skills")
                self.assertTrue((project / ".agents/skills/dixi-acme-deploy-check/agents/openai.yaml").is_file())

    def test_project_language_selects_the_text(self):
        project = self.project("claude", "es")
        self.assertEqual(self.add(project, self.extension()).returncode, 0)
        self.assertEqual((project / ".claude/commands/dixi-acme-deploy-check.md").read_text(), TEXT["es"])

    def test_crafted_folders_are_refused_without_writing(self):
        project = self.project("claude")
        before = self.snapshot(project)
        cases = {"bad id": dict(ext_id="Acme"), "reserved id": dict(ext_id="dixi"),
                 "traversal id": dict(ext_id="../x"), "bad operation": dict(operations=("Deploy",)),
                 "too long": dict(ext_id="a" * 40, operations=("b" * 30,))}
        for label, options in cases.items():
            with self.subTest(case=label):
                folder = self.extension(name=label.replace(" ", "-"), **options)
                self.assertEqual(self.add(project, folder).returncode, 2, label)
                self.assertEqual(self.snapshot(project), before)
        extra = self.extension(name="with-script")
        (extra / "install.sh").write_text("rm -rf /\n")
        link = self.extension(name="with-link")
        (link / "operations/en/deploy-check.md").unlink()
        (link / "operations/en/deploy-check.md").symlink_to(self.base / "with-script/install.sh")
        huge = self.extension(name="huge")
        (huge / "operations/en/deploy-check.md").write_text(TEXT["en"] + "x" * 70000)
        missing = self.extension(name="missing-es")
        (missing / "operations/es/deploy-check.md").unlink()
        nodesc = self.extension(name="no-description", texts={k: v.replace("description:", "summary:")
                                                             for k, v in TEXT.items()})
        for folder in (extra, link, huge, missing, nodesc):
            with self.subTest(folder=folder.name):
                self.assertEqual(self.add(project, folder).returncode, 2, folder.name)
                self.assertEqual(self.snapshot(project), before)

    def test_existing_target_and_repeated_add_are_refused(self):
        project = self.project("claude")
        (project / ".claude/commands/dixi-acme-deploy-check.md").write_text("mine\n")
        before = self.snapshot(project)
        self.assertEqual(self.add(project, self.extension()).returncode, 3)
        self.assertEqual(self.snapshot(project), before)
        (project / ".claude/commands/dixi-acme-deploy-check.md").unlink()
        self.assertEqual(self.add(project, self.extension(name="again")).returncode, 0)
        self.assertEqual(self.add(project, self.extension(name="again2")).returncode, 3)

    def test_agent_none_is_refused(self):
        project = self.project("none")
        before = self.snapshot(project)
        self.assertEqual(self.add(project, self.extension()).returncode, 2)
        self.assertEqual(self.snapshot(project), before)

    def test_remove_keeps_edited_files(self):
        project = self.project("codex")
        self.assertEqual(self.add(project, self.extension()).returncode, 0)
        skill = project / ".agents/skills/dixi-acme-deploy-check/SKILL.md"
        skill.write_text(skill.read_text() + "\nmy note\n")
        result = self.cli("--json", "extension", "remove", "acme", cwd=project)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        kept = json.loads(result.stdout)["extension"]["kept"]
        self.assertEqual(kept, [".agents/skills/dixi-acme-deploy-check/SKILL.md"])
        self.assertTrue(skill.is_file())
        self.assertFalse((project / ".agents/skills/dixi-acme-deploy-check/agents/openai.yaml").exists())
        self.assertNotIn("acme", self.metadata(project).get("extensions", {}))
        self.assertEqual(self.cli("check", cwd=project).returncode, 0)

    def test_upgrade_ignores_extension_files(self):
        project = self.project("claude")
        self.assertEqual(self.add(project, self.extension()).returncode, 0)
        plan = json.loads(self.cli("--json", "upgrade", "--dry-run", cwd=project).stdout)["upgrade"]["files"]
        for status in ("updatable", "conflict", "new", "missing", "obsolete"):
            self.assertEqual(plan[status], [], status)

    def test_messages_in_both_languages(self):
        for lang in ("en", "es"):
            catalog = json.loads((ROOT / f"src/dixi_spec_kit/locales/{lang}.json").read_text(encoding="utf-8"))
            for key in ("extension", "extension_add", "extension_list", "extension_remove", "extension_added",
                        "extension_removed", "invalid_extension", "extension_conflict", "extensions_require_agent"):
                self.assertIn(key, catalog)


if __name__ == "__main__":
    unittest.main()
