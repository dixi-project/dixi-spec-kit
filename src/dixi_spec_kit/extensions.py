"""Local, data-only extensions (ADR-109): add operations named dixi-<extension>-<operation> (threat T14).

An extension is a folder with `extension.json` and `operations/{en,es}/<operation>.md`, nothing else. It is read
without following links, validated completely before anything is written, installed for the project's adapter,
and recorded in `.dixi/project.json` under `extensions` (outside the kit inventory, so `upgrade` ignores it).
"""
import hashlib
import json
import os
from pathlib import PurePosixPath
import re
import stat

from .core import CODEX_POLICY, METADATA, project_metadata
from .filesystem import Issue, decode_json, directory, read_file, replace_file, root_directory, write_file

NAME = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*")
MAX_TEXT = 64 * 1024
MAX_OPERATIONS = 50
LANGUAGES = ("en", "es")
REQUEST = {"es": "la petición de la persona (el texto escrito junto a la mención del skill)",
           "en": "the person's request (the text written with the skill mention)"}
REQUEST_SHORT = {"es": "la petición", "en": "the request"}
FRONTMATTER = re.compile(r'---\ndescription: ("[^"\n]{1,1022}")\nargument-hint: [^\n]*\n---\n')


def entries(fd):
    """Names in a directory fd, each required to be a regular file or a directory (never a link)."""
    result = {}
    for name in os.listdir(fd):
        info = os.stat(name, dir_fd=fd, follow_symlinks=False)
        if stat.S_ISREG(info.st_mode):
            result[name] = "file"
        elif stat.S_ISDIR(info.st_mode):
            result[name] = "dir"
        else:
            raise Issue("invalid_extension", 2, reason=f"not a regular file: {name}")
    return result


def load(source):
    """Read and validate an extension folder; return (manifest, {language: {operation: text}})."""
    invalid = lambda reason: Issue("invalid_extension", 2, reason=reason)  # noqa: E731
    with root_directory(source) as root:
        if entries(root) != {"extension.json": "file", "operations": "dir"}:
            raise invalid("the folder must hold only extension.json and operations/")
        manifest = decode_json(read_file(root, "extension.json"), "extension.json")
        if not isinstance(manifest, dict) or set(manifest) - {"id", "version", "operations", "requires"}:
            raise invalid("extension.json has unknown or missing fields")
        ext_id, version, operations = manifest.get("id"), manifest.get("version"), manifest.get("operations")
        if not isinstance(ext_id, str) or not NAME.fullmatch(ext_id) or ext_id == "dixi":
            raise invalid("id must match [a-z0-9]+(-[a-z0-9]+)* and not be dixi")
        if not isinstance(version, str) or not re.fullmatch(r"\d{1,4}\.\d{1,4}\.\d{1,4}", version):
            raise invalid("version must be X.Y.Z")
        if (not isinstance(operations, list) or not 1 <= len(operations) <= MAX_OPERATIONS
                or len(set(operations)) != len(operations)):
            raise invalid("operations must be a list of 1 to 50 unique names")
        for operation in operations:
            if not isinstance(operation, str) or not NAME.fullmatch(operation):
                raise invalid("operation names must match [a-z0-9]+(-[a-z0-9]+)*")
            if len(f"dixi-{ext_id}-{operation}") > 64:
                raise invalid("dixi-<extension>-<operation> must be at most 64 characters")
        with directory(root, ["operations"]) as ops:
            if entries(ops) != {language: "dir" for language in LANGUAGES}:
                raise invalid("operations/ must hold exactly en/ and es/")
        texts = {}
        for language in LANGUAGES:
            with directory(root, ["operations", language]) as folder:
                if entries(folder) != {f"{op}.md": "file" for op in operations}:
                    raise invalid(f"operations/{language}/ must hold exactly one .md per operation")
            texts[language] = {}
            for operation in operations:
                data = read_file(root, f"operations/{language}/{operation}.md")
                if len(data) > MAX_TEXT:
                    raise invalid(f"{language}/{operation}.md is larger than 64 KiB")
                try:
                    text = data.decode("utf-8")
                except UnicodeError:
                    raise invalid(f"{language}/{operation}.md is not UTF-8") from None
                if not FRONTMATTER.match(text):
                    raise invalid(f"{language}/{operation}.md needs description and argument-hint frontmatter")
                texts[language][operation] = text
    return manifest, texts


def skill(text, language, name, generic):
    match = FRONTMATTER.match(text)
    body = text[match.end():]
    body = body.replace("`$ARGUMENTS`", REQUEST[language], 1).replace("`$ARGUMENTS`", REQUEST_SHORT[language])
    prefix = "" if generic else "$"
    body = re.sub(r"/dixi[.-]([a-z0-9-]+)", rf"{prefix}dixi-\1", body)
    if "$ARGUMENTS" in body:
        raise Issue("invalid_extension", 2, reason="$ARGUMENTS must be written as `$ARGUMENTS`")
    extra = "disable-model-invocation: true\n" if generic else ""
    return f"---\nname: {name}\ndescription: {match.group(1)}\n{extra}---\n{body}"


def rendered(manifest, texts, agent, language):
    payload = {}
    folder = f".dixi/extensions/{manifest['id']}"
    payload[f"{folder}/extension.json"] = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode()
    for lang in LANGUAGES:
        for operation, text in texts[lang].items():
            payload[f"{folder}/operations/{lang}/{operation}.md"] = text.encode()
    for operation, text in texts[language].items():
        name = f"dixi-{manifest['id']}-{operation}"
        if agent == "claude":
            payload[f".claude/commands/{name}.md"] = text.encode()
        else:
            payload[f".agents/skills/{name}/SKILL.md"] = skill(text, language, name, agent == "skills").encode()
            payload[f".agents/skills/{name}/agents/openai.yaml"] = CODEX_POLICY
    return payload


def write_metadata(root, metadata):
    replace_file(root, METADATA, (json.dumps(metadata, ensure_ascii=False, indent=2) + "\n").encode())


def add(path, source):
    manifest, texts = load(source)
    with root_directory(path) as root:
        metadata = project_metadata(root)
        if metadata["agent"] == "none":
            raise Issue("extensions_require_agent", 2)
        installed = metadata.get("extensions", {})
        if manifest["id"] in installed:
            raise Issue("extension_conflict", 3, path=f".dixi/extensions/{manifest['id']}")
        payload = rendered(manifest, texts, metadata["agent"], metadata["language"])
        for name in payload:
            try:
                read_file(root, name)
                raise Issue("extension_conflict", 3, path=name)
            except Issue as error:
                if error.key != "missing_file":
                    raise Issue("extension_conflict", 3, path=name) from None
        for name, data in payload.items():
            try:
                write_file(root, name, data)
            except FileExistsError:
                raise Issue("extension_conflict", 3, path=name) from None
        installed[manifest["id"]] = {"version": manifest["version"],
                                     "files": {n: hashlib.sha256(d).hexdigest() for n, d in sorted(payload.items())}}
        metadata["extensions"] = installed
        write_metadata(root, metadata)
    return {"id": manifest["id"], "version": manifest["version"], "operations": manifest["operations"],
            "files": sorted(payload)}


def listing(path):
    with root_directory(path) as root:
        metadata = project_metadata(root)
    return [{"id": ext_id, "version": entry["version"], "files": len(entry["files"])}
            for ext_id, entry in sorted(metadata.get("extensions", {}).items())]


def remove(path, ext_id):
    with root_directory(path) as root:
        metadata = project_metadata(root)
        installed = metadata.get("extensions", {})
        if ext_id not in installed:
            raise Issue("extension_missing", 2, id=ext_id)
        removed, kept = [], []
        for name, recorded in sorted(installed[ext_id]["files"].items()):
            try:
                current = hashlib.sha256(read_file(root, name)).hexdigest()
            except Issue as error:
                if error.key == "missing_file":
                    continue
                kept.append(name)
                continue
            if current != recorded:
                kept.append(name)
                continue
            parts = PurePosixPath(name)
            with directory(root, parts.parts[:-1]) as parent:
                os.unlink(parts.name, dir_fd=parent)
            removed.append(name)
        for name in sorted({str(PurePosixPath(n).parent) for n in removed}, key=len, reverse=True):
            for folder in [PurePosixPath(name), *PurePosixPath(name).parents]:
                if str(folder) in (".", ".claude", ".claude/commands", ".agents", ".agents/skills", ".dixi"):
                    break
                try:
                    with directory(root, folder.parts[:-1]) as parent:
                        os.rmdir(folder.name, dir_fd=parent)
                except OSError:
                    break
        del installed[ext_id]
        if installed:
            metadata["extensions"] = installed
        else:
            metadata.pop("extensions", None)
        write_metadata(root, metadata)
    return {"id": ext_id, "removed": removed, "kept": kept}
