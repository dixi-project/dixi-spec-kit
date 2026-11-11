import hashlib
from importlib.resources import files
import unicodedata

from .core import METADATA, PARENTS, TRACE, project_metadata, traceability
from .filesystem import Issue, decode_json, read_file, root_directory


OPERATIONS = ("discover", "specify", "clarify", "plan", "tasks", "build", "verify", "review", "analyze", "status",
              "domain", "architecture", "contract", "threat-model", "handoff", "change", "data", "quality", "ai",
              "release", "promote", "operate", "finops", "compliance", "duediligence", "interview", "risk-review",
              "constitution", "checklist", "converge")
COMMON_SOURCES = (METADATA, TRACE, "MODE", "AGENTS.md", "00-master-spec.md")


def load_recipes(language):
    resources = files("dixi_spec_kit").joinpath("resources")
    try:
        index = decode_json(resources.joinpath("workflows.json").read_bytes(), "workflows.json")
        localized = decode_json(resources.joinpath(f"workflows.{language}.json").read_bytes(), "workflows")
        if (index["schema_version"] != 1 or set(index["operations"]) != set(OPERATIONS)
                or set(localized["operations"]) != set(OPERATIONS)):
            raise ValueError
        guards = localized["guards"]
        if not isinstance(guards, list) or not guards or any(not isinstance(g, str) or not g for g in guards):
            raise ValueError
        result = {}
        for name in OPERATIONS:
            definition = index["operations"][name]
            text = localized["operations"][name]
            for key in ("target_kinds", "next_operations"):
                allowed = PARENTS if key == "target_kinds" else OPERATIONS
                if not isinstance(definition[key], list) or any(value not in allowed for value in definition[key]):
                    raise ValueError
            if not definition["target_kinds"]:
                raise ValueError
            for key in ("title", "purpose"):
                if not isinstance(text[key], str) or not text[key]:
                    raise ValueError
            for key in ("inputs", "steps", "outputs", "gates", "checks"):
                if not isinstance(text[key], list) or not text[key] or any(not isinstance(t, str) or not t for t in text[key]):
                    raise ValueError
            result[name] = {"id": name, **definition, **text, "guards": guards}
        return result
    except (Issue, KeyError, TypeError, ValueError, OSError):
        raise Issue("invalid_resources", 5) from None


def prepare_packet(path, recipe, target, request):
    if (not request.strip() or len(request) > 4096
            or any(unicodedata.category(c) in {"Cc", "Cs"} and c not in "\n\t" for c in request)):
        raise Issue("invalid_workflow_request", 2)
    with root_directory(path) as root:
        metadata = project_metadata(root)
        items, issues = traceability(root)
        if issues:
            raise Issue("invalid_trace")
        by_id = {item["id"]: item for item in items}
        if target not in by_id or by_id[target]["kind"] not in recipe["target_kinds"]:
            raise Issue("invalid_workflow_target", 2)
        pending, visited = [target], set()
        names = set(COMMON_SOURCES)
        while pending:
            identifier = pending.pop()
            if identifier in visited:
                continue
            visited.add(identifier)
            item = by_id[identifier]
            names.add(item["path"])
            pending.extend(item["parents"])
        if len(names) > 64:
            raise Issue("workflow_context_limit")
        sources, total, mode = [], 0, None
        for name in sorted(names):
            data = read_file(root, name)
            total += len(data)
            if total > 2 * 1024 * 1024:
                raise Issue("workflow_context_limit")
            if name == "MODE":
                if data.strip() not in (b"mvp", b"prod"):
                    raise Issue("invalid_workflow_mode")
                mode = data.strip().decode("ascii")
            sources.append({"path": name, "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)})
        return {"schema_version": 1, "status": "prepared", "execution": "manual_or_external",
                "operation": recipe["id"], "request": request,
                "target": {key: by_id[target][key] for key in ("id", "kind", "path", "parents")},
                "project_language": metadata["language"], "mode": mode,
                "recipe": recipe, "sources": sources}


def workflow_result(args, path):
    recipes = load_recipes(args.lang)
    if args.workflow_action == "list":
        return {"operations": [{key: recipe[key] for key in ("id", "title", "purpose", "target_kinds")}
                               for recipe in recipes.values()]}
    recipe = recipes[args.operation]
    if args.workflow_action == "show":
        return {"recipe": recipe}
    return {"packet": prepare_packet(path, recipe, args.target, args.request)}
