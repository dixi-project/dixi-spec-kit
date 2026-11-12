"""Local, data-only presets (ADR-109): override kit operation texts and templates (threat T15).

A preset is a folder with `preset.json` and replacement files under `operations/{en,es}/<kit operation>.md`
and `templates/{en,es}/<kit template path>`. Only project files still equal to the kit version are replaced;
the project's `.dixi/overrides/` and the person's edits always win; a higher-priority preset wins over a lower
one. The kit inventory keeps the kit hashes, so `upgrade` reports a preset file as a conflict instead of
overwriting it. Removal restores the kit text only where the preset text is still unchanged.
"""
import hashlib
import json
import os
from pathlib import PurePosixPath
import re

from .core import (CLAUDE_COMMANDS, METADATA, adapter_files, profile_files, profile_manifest, project_metadata,
                   recorded_profile, templates)
from .extensions import FRONTMATTER, LANGUAGES, NAME, entries, skill
from .filesystem import Issue, decode_json, directory, read_file, replace_file, root_directory, write_file

MAX_OPERATION = 64 * 1024
MAX_TEMPLATE = 256 * 1024
MAX_FILES = 300


def invalid(reason):
    return Issue("invalid_preset", 2, reason=reason)


def walk(root, parts, depth=0):
    """Relative paths of regular files under a directory, refusing links and anything that is not a file."""
    if depth > 8:
        raise invalid("templates/ is nested too deeply")
    found = []
    with directory(root, parts) as fd:
        for name, kind in sorted(entries(fd).items()):
            found += walk(root, [*parts, name], depth + 1) if kind == "dir" else ["/".join([*parts, name])]
    return found


def load(source):
    with root_directory(source) as root:
        top = entries(root)
        if top.get("preset.json") != "file" or set(top) - {"preset.json", "operations", "templates"} or any(
                top[n] != "dir" for n in set(top) - {"preset.json"}):
            raise invalid("the folder must hold preset.json and optional operations/ and templates/ only")
        manifest = decode_json(read_file(root, "preset.json"), "preset.json")
        if not isinstance(manifest, dict) or set(manifest) - {"id", "version", "priority", "requires"}:
            raise invalid("preset.json has unknown or missing fields")
        if not isinstance(manifest.get("id"), str) or not NAME.fullmatch(manifest["id"]) or manifest["id"] == "dixi":
            raise invalid("id must match [a-z0-9]+(-[a-z0-9]+)* and not be dixi")
        if not isinstance(manifest.get("version"), str) or not re.fullmatch(r"\d{1,4}\.\d{1,4}\.\d{1,4}",
                                                                            manifest["version"]):
            raise invalid("version must be X.Y.Z")
        priority = manifest.get("priority")
        if type(priority) is not int or not 0 <= priority <= 100:
            raise invalid("priority must be an integer from 0 to 100")
        known_templates = set(templates("en")) | set(profile_manifest())
        files = {}
        for kind in ("operations", "templates"):
            if kind not in top:
                continue
            with directory(root, [kind]) as fd:
                if entries(fd) != {language: "dir" for language in LANGUAGES}:
                    raise invalid(f"{kind}/ must hold exactly en/ and es/")
            sets = {}
            for language in LANGUAGES:
                names = [p.split("/", 2)[2] for p in walk(root, [kind, language])]
                sets[language] = set(names)
                for name in names:
                    data = read_file(root, f"{kind}/{language}/{name}")
                    if kind == "operations":
                        if not name.endswith(".md") or name[:-3] not in CLAUDE_COMMANDS:
                            raise invalid(f"operations/{language}/{name} is not a kit operation")
                        if len(data) > MAX_OPERATION or not FRONTMATTER.match(data.decode("utf-8", "replace")):
                            raise invalid(f"operations/{language}/{name} needs frontmatter and at most 64 KiB")
                    elif name not in known_templates or len(data) > MAX_TEMPLATE:
                        raise invalid(f"templates/{language}/{name} is not a kit template or is too large")
                    try:
                        data.decode("utf-8")
                    except UnicodeError:
                        raise invalid(f"{kind}/{language}/{name} is not UTF-8") from None
                    files[f"{kind}/{language}/{name}"] = data
            if sets["en"] != sets["es"]:
                raise invalid(f"{kind}/en and {kind}/es must override the same files")
        if not files or len(files) > MAX_FILES:
            raise invalid("a preset overrides 1 to 300 files")
    return manifest, files



def targets(files, agent, language):
    """Project path -> preset content for the project's agent and language."""
    result = {}
    for name, data in files.items():
        kind, lang, rest = name.split("/", 2)
        if lang != language:
            continue
        if kind == "templates":
            result[rest] = (name, data)
            continue
        operation, text = rest[:-3], data.decode("utf-8")
        if agent == "claude":
            result[f".claude/commands/dixi.{operation}.md"] = (name, data)
        elif agent in ("codex", "skills"):
            converted = skill(text, language, f"dixi-{operation}", agent == "skills")
            result[f".agents/skills/dixi-{operation}/SKILL.md"] = (name, converted.encode())
    return result


def shipped(metadata):
    profile, regulated = recorded_profile(metadata)
    payload = {name: text.encode("utf-8") for name, text in templates(metadata["language"]).items()}
    payload.update(profile_files(metadata["language"], profile, regulated))
    payload.update(adapter_files(metadata["agent"], metadata["language"]))
    return payload


def digest_of(root, name):
    try:
        return hashlib.sha256(read_file(root, name)).hexdigest()
    except Issue:
        return None


def write_metadata(root, metadata):
    replace_file(root, METADATA, (json.dumps(metadata, ensure_ascii=False, indent=2) + "\n").encode())


def add(path, source):
    manifest, files = load(source)
    with root_directory(path) as root:
        metadata = project_metadata(root)
        installed = metadata.get("presets", {})
        if manifest["id"] in installed:
            raise Issue("preset_conflict", 3, path=f".dixi/presets/{manifest['id']}")
        copy = {f".dixi/presets/{manifest['id']}/preset.json":
                (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode()}
        copy.update({f".dixi/presets/{manifest['id']}/{name}": data for name, data in files.items()})
        for name in copy:
            if digest_of(root, name) is not None:
                raise Issue("preset_conflict", 3, path=name)
        applied, kept = {}, []
        inventory = metadata["managed_files"]
        for target, (origin, data) in sorted(targets(files, metadata["agent"], metadata["language"]).items()):
            if target not in inventory:
                continue
            if digest_of(root, f".dixi/overrides/{origin}") is not None:
                kept.append(target)
                continue
            current = digest_of(root, target)
            owner = next((other for other, entry in installed.items() if target in entry["files"]), None)
            if owner is not None:
                if installed[owner]["priority"] >= manifest["priority"] or current != installed[owner]["files"][target]:
                    kept.append(target)
                    continue
            elif current != inventory[target]:
                kept.append(target)
                continue
            replace_file(root, target, data)
            applied[target] = hashlib.sha256(data).hexdigest()
            if owner is not None:
                del installed[owner]["files"][target]
        for name, data in copy.items():
            write_file(root, name, data)
        installed[manifest["id"]] = {"version": manifest["version"], "priority": manifest["priority"],
                                     "files": applied, "copy": {n: hashlib.sha256(d).hexdigest()
                                                                for n, d in sorted(copy.items())}}
        metadata["presets"] = installed
        write_metadata(root, metadata)
    return {"id": manifest["id"], "version": manifest["version"], "applied": sorted(applied), "kept": kept}


def listing(path):
    with root_directory(path) as root:
        metadata = project_metadata(root)
    return [{"id": pid, "version": entry["version"], "priority": entry["priority"], "files": len(entry["files"])}
            for pid, entry in sorted(metadata.get("presets", {}).items())]


def remove(path, preset_id):
    with root_directory(path) as root:
        metadata = project_metadata(root)
        installed = metadata.get("presets", {})
        if preset_id not in installed:
            raise Issue("preset_missing", 2, id=preset_id)
        kit = shipped(metadata)
        restored, kept = [], []
        for target, recorded in sorted(installed[preset_id]["files"].items()):
            if digest_of(root, target) != recorded or target not in kit:
                kept.append(target)
                continue
            replace_file(root, target, kit[target])
            restored.append(target)
        for name, recorded in sorted(installed[preset_id]["copy"].items()):
            if digest_of(root, name) == recorded:
                parts = PurePosixPath(name)
                with directory(root, parts.parts[:-1]) as parent:
                    os.unlink(parts.name, dir_fd=parent)
        for folder in sorted({str(PurePosixPath(n).parent) for n in installed[preset_id]["copy"]},
                             key=lambda f: f.count("/"), reverse=True):
            parts = PurePosixPath(folder)
            for candidate in [parts, *parts.parents]:
                if str(candidate) in (".", ".dixi"):
                    break
                try:
                    with directory(root, candidate.parts[:-1]) as parent:
                        os.rmdir(candidate.name, dir_fd=parent)
                except OSError:
                    break
        del installed[preset_id]
        if installed:
            metadata["presets"] = installed
        else:
            metadata.pop("presets", None)
        write_metadata(root, metadata)
    return {"id": preset_id, "restored": restored, "kept": kept}
