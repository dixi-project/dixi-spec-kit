import ast
import json
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def main():
    for path in (ROOT / "src").rglob("*.py"):
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    catalogs = [json.loads((ROOT / "src/dixi_spec_kit/locales" / f"{lang}.json").read_text(encoding="utf-8"))
                for lang in ("es", "en")]
    assert catalogs[0].keys() == catalogs[1].keys(), "Message catalogs differ"
    for key in catalogs[0]:
        assert set(re.findall(r"\{(\w+)\}", catalogs[0][key])) == set(
            re.findall(r"\{(\w+)\}", catalogs[1][key])), f"Placeholder mismatch: {key}"
    resources = [json.loads((ROOT / "src/dixi_spec_kit/resources" / f"project.{lang}.json").read_text(encoding="utf-8"))
                 for lang in ("es", "en")]
    assert resources[0].keys() == resources[1].keys(), "Resource paths differ"
    for tree in resources:
        for name, text in tree.items():
            if name.endswith(".md"):
                assert text.startswith("# "), name
    sys.path.insert(0, str(ROOT / "src"))
    from dixi_spec_kit.core import CLAUDE_COMMANDS
    adapter = ROOT / "src/dixi_spec_kit/resources/claude"
    names = [sorted(p.name for p in (adapter / lang).glob("*.md")) for lang in ("es", "en")]
    assert names[0] == names[1] and len(names[0]) == len(CLAUDE_COMMANDS) + 1, "Claude adapter resources differ"
    skills = [sorted(p.name for p in (ROOT / "src/dixi_spec_kit/resources/codex" / lang).glob("*.md"))
              for lang in ("es", "en")]
    assert skills[0] == skills[1] and len(skills[0]) == len(CLAUDE_COMMANDS), "Codex adapter resources differ"
    agents = [sorted(p.name for p in (adapter / lang / "agents").glob("*.md")) for lang in ("es", "en")]
    assert agents[0] == agents[1] and len(agents[0]) == 4, "Claude subagent resources differ"
    hooks = sorted(p.name for p in (ROOT / "src/dixi_spec_kit/resources/hooks").glob("*.py"))
    assert len(hooks) == 5, "Hook resources differ"
    subprocess.run([sys.executable, str(ROOT / "scripts/generate-codex-skills.py"), "--check"], check=True)
    subprocess.run([sys.executable, str(ROOT / "scripts/generate-profiles.py"), "--check"], check=True)
    templates = ROOT / "src/dixi_spec_kit/resources/templates"
    trees = [{p.relative_to(templates / lang).as_posix() for p in (templates / lang).rglob("*") if p.is_file()}
             for lang in ("es", "en")]
    assert trees[0] == trees[1], "Template paths differ between languages"
    manifest = set(json.loads((ROOT / "src/dixi_spec_kit/resources/profiles.json").read_text(encoding="utf-8"))["files"])
    assert manifest <= trees[0], f"Templates missing: {sorted(manifest - trees[0])[:5]}"
    assert trees[0] <= manifest, f"Templates not in the manifest: {sorted(trees[0] - manifest)[:5]}"
    assert (ROOT / "LICENSE").read_bytes() == (ROOT / "src/dixi_spec_kit/LICENSE").read_bytes(), "LICENSE copies differ"
    subprocess.run(["git", "diff", "--check"], cwd=ROOT, check=True)
    print("Source syntax, es/en catalogs, resource parity and license: OK")


if __name__ == "__main__":
    main()
