import hashlib
from importlib.resources import files
import json
import os
from pathlib import Path, PurePosixPath
import posixpath
import re
import sys
from urllib.parse import unquote, urlsplit

from . import __version__
from .filesystem import (Issue, decode_json, directory, read_file, read_json,
                         root_directory, safe_path, supported, write_file)


PARENTS = {"goal": set(), "domain": {"goal"}, "module": {"domain"},
           "feature": {"module"}, "contract": {"feature", "module"},
           "test": {"feature", "contract"}}
METADATA = ".dixi/project.json"
AGENTS = ("none", "claude", "codex")
CODEX_POLICY = b"policy:\n  allow_implicit_invocation: false\n"
CLAUDE_REQUIRED = ("discover", "specify", "clarify", "plan", "tasks", "build", "verify", "review", "analyze", "status")
CLAUDE_COMMANDS = CLAUDE_REQUIRED + ("domain", "architecture", "contract", "threat-model", "handoff", "change",
                                     "data", "quality", "ai", "release", "promote", "operate", "finops",
                                     "compliance", "duediligence")
TRACE = ".dixi/traceability.json"
INLINE_LINK = re.compile(r"!?\[[^\[\]\n]{0,999}\]\(([^)\n]{1,4096})\)")
KIT_VERSION = re.compile(r"(0|[1-9][0-9]{0,3})\.(0|[1-9][0-9]{0,3})\.(0|[1-9][0-9]{0,3})(?:\.dev[0-9]{1,4}|rc[0-9]{1,4})?")
REFERENCE_LINK = re.compile(r"^ {0,3}\[[^\[\]\n]{1,999}\]:[ \t]*(<[^>\n]{1,4096}>|[^\s<>]{1,4096})(?=[ \t]|$)", re.MULTILINE)


def templates(language):
    data = files("dixi_spec_kit").joinpath("resources", f"project.{language}.json").read_bytes()
    payload = decode_json(data, "resources")
    if not isinstance(payload, dict) or not 1 <= len(payload) <= 500:
        raise Issue("invalid_resources", 5)
    if any(not safe_path(k) or not isinstance(v, str) for k, v in payload.items()):
        raise Issue("invalid_resources", 5)
    return payload


def codex_files(language):
    folder = files("dixi_spec_kit").joinpath("resources", "codex", language)
    payload = {}
    for name in CLAUDE_COMMANDS:
        payload[f".agents/skills/dixi-{name}/SKILL.md"] = folder.joinpath(f"dixi-{name}.md").read_bytes()
        payload[f".agents/skills/dixi-{name}/agents/openai.yaml"] = CODEX_POLICY
    return payload


def required_adapter_files(agent):
    if agent == "claude":
        return {"CLAUDE.md"} | {f".claude/commands/dixi.{name}.md" for name in CLAUDE_REQUIRED}
    if agent == "codex":
        return {f".agents/skills/dixi-{name}/{suffix}" for name in CLAUDE_REQUIRED
                for suffix in ("SKILL.md", "agents/openai.yaml")}
    return set()


def adapter_files(agent, language):
    if agent == "none":
        return {}
    if agent == "codex":
        return codex_files(language)
    folder = files("dixi_spec_kit").joinpath("resources", "claude", language)
    payload = {"CLAUDE.md": folder.joinpath("CLAUDE.md").read_bytes()}
    for name in CLAUDE_COMMANDS:
        payload[f".claude/commands/dixi.{name}.md"] = folder.joinpath(f"dixi.{name}.md").read_bytes()
    try:
        for data in payload.values():
            data.decode("utf-8")
    except UnicodeError:
        raise Issue("invalid_resources", 5) from None
    return payload


def message(key, **params):
    return {"key": key, "params": params}


def initialize(destination, language, agent="none"):
    path = Path(destination)
    if ".." in path.parts or not path.name:
        raise Issue("unsafe_path", 3)
    payload = {name: text.encode("utf-8") for name, text in templates(language).items()}
    payload.update(adapter_files(agent, language))
    metadata = {"schema_version": 1, "kit_version": __version__, "language": language,
                "agent": agent, "policy": "portable",
                "managed_files": {name: hashlib.sha256(data).hexdigest() for name, data in payload.items()}}
    try:
        with root_directory(path.parent) as parent:
            try:
                os.mkdir(path.name, mode=0o700, dir_fd=parent)
            except FileExistsError:
                pass
            with directory(parent, [path.name]) as root:
                if os.listdir(root):
                    raise Issue("destination_conflict", 3)
                write_file(root, ".dixi-init.lock", b"")
                for name, data in payload.items():
                    write_file(root, name, data)
                write_file(root, METADATA, (json.dumps(metadata, ensure_ascii=False, indent=2) + "\n").encode())
                os.unlink(".dixi-init.lock", dir_fd=root)
    except Issue as error:
        if error.key == "unsafe_path":
            error.code = 3
        raise
    except FileExistsError:
        raise Issue("destination_conflict", 3) from None
    return [message("initialized", path=str(path)), message("structure_only")]


def project_metadata(root):
    try:
        data = read_json(root, METADATA)
    except Issue as error:
        if error.key == "missing_file":
            raise Issue("missing_project", 2) from None
        raise
    if not isinstance(data, dict) or type(data.get("schema_version")) is not int:
        raise Issue("invalid_metadata")
    if data["schema_version"] != 1:
        raise Issue("unsupported_schema", 4)
    if (not isinstance(data.get("kit_version"), str) or data.get("language") not in ("es", "en")
            or data.get("agent") not in AGENTS or data.get("policy") != "portable"):
        raise Issue("invalid_metadata")
    version = KIT_VERSION.fullmatch(data["kit_version"])
    if not version:
        raise Issue("invalid_metadata")
    if version.group(1) != __version__.split(".")[0]:
        raise Issue("unsupported_schema", 4)
    inventory = data.get("managed_files")
    if not isinstance(inventory, dict) or not 1 <= len(inventory) <= 500:
        raise Issue("invalid_metadata")
    for name, digest in inventory.items():
        if not safe_path(name) or not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
            raise Issue("invalid_metadata")
    required = set(templates(data["language"])) | required_adapter_files(data["agent"])
    if not required <= set(inventory):
        raise Issue("invalid_metadata")
    return data


def traceability(root):
    data = read_json(root, TRACE)
    if (not isinstance(data, dict) or type(data.get("schema_version")) is not int
            or data["schema_version"] != 1 or not isinstance(data.get("items"), list)
            or len(data["items"]) > 500):
        raise Issue("invalid_trace")
    items = data["items"]
    by_id = {}
    for item in items:
        if (not isinstance(item, dict) or not isinstance(item.get("id"), str)
                or not re.fullmatch(r"[A-Za-z][A-Za-z0-9._-]{0,127}", item["id"])
                or not isinstance(item.get("kind"), str) or item["kind"] not in PARENTS
                or not safe_path(item.get("path")) or not isinstance(item.get("parents"), list)
                or len(item["parents"]) > 500 or any(not isinstance(p, str) for p in item["parents"])):
            raise Issue("invalid_trace")
        if item["id"] in by_id or len(item["parents"]) != len(set(item["parents"])):
            raise Issue("invalid_trace")
        by_id[item["id"]] = item
    issues = []
    for item in items:
        allowed = PARENTS[item["kind"]]
        if bool(item["parents"]) != bool(allowed) or any(
                p not in by_id or by_id[p]["kind"] not in allowed for p in item["parents"]):
            issues.append(message("invalid_parent", path=item["id"]))
    return items, issues


def markdown_links(root, name, data):
    try:
        text = data.decode("utf-8")
    except UnicodeError:
        raise Issue("invalid_file", path=name) from None
    issues = []
    targets = INLINE_LINK.findall(text) + REFERENCE_LINK.findall(text)
    if len(targets) > 500:
        raise Issue("invalid_file", path=name)
    for target in targets:
        target = target.strip()
        if not target:
            continue
        target = target[1:target.index(">")] if target.startswith("<") and ">" in target else target.split()[0]
        try:
            link = urlsplit(target)
            if link.scheme in {"http", "https", "mailto"}:
                continue
            if link.scheme or link.netloc or link.path.startswith("/"):
                raise Issue("unsafe_path")
            if not link.path:
                continue
            relative = posixpath.normpath(posixpath.join(str(PurePosixPath(name).parent), unquote(link.path)))
            read_file(root, relative)
        except (Issue, ValueError):
            issues.append(message("invalid_link", path=name))
    return issues


def check_project(path):
    issues = []
    with root_directory(path) as root:
        metadata = project_metadata(root)
        names = set(metadata["managed_files"])
        try:
            items, graph_issues = traceability(root)
            issues.extend(graph_issues)
            names.update(item["path"] for item in items)
        except Issue as error:
            issues.append(message(error.key, **error.params))
        for name in sorted(names):
            try:
                data = read_file(root, name)
                if name.endswith(".md"):
                    issues.extend(markdown_links(root, name, data))
            except Issue as error:
                issues.append(message(error.key, **error.params))
    return (1 if issues else 0), issues + [message("structure_only")]


def doctor(path, language):
    if not supported():
        raise Issue("unsupported_platform", 4)
    templates(language)
    results = [message("runtime", version=sys.version.split()[0]), message("resources_ok")]
    with root_directory(path) as root:
        try:
            metadata = project_metadata(root)
            if metadata["agent"] == "claude":
                installed = sum(f".claude/commands/dixi.{name}.md" in metadata["managed_files"]
                                for name in CLAUDE_COMMANDS)
                results.append(message("agent_claude", language=metadata["language"],
                                       commands=installed, available=len(CLAUDE_COMMANDS)))
                if installed < len(CLAUDE_COMMANDS):
                    results.append(message("upgrade_hint"))
            elif metadata["agent"] == "codex":
                installed = sum(f".agents/skills/dixi-{name}/SKILL.md" in metadata["managed_files"]
                                for name in CLAUDE_COMMANDS)
                results.append(message("agent_codex", language=metadata["language"],
                                       skills=installed, available=len(CLAUDE_COMMANDS)))
                if installed < len(CLAUDE_COMMANDS):
                    results.append(message("upgrade_hint"))
            else:
                results.append(message("agent_none", language=metadata["language"]))
        except Issue as error:
            if error.code != 2:
                raise
            results.append(message("no_project_optional"))
    return results
