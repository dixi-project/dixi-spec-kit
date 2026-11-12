import argparse
from importlib.resources import files
import json
from pathlib import Path
import sys

from . import __version__
from .core import METADATA, PROFILES, check_project, doctor, initialize, message, placeholders, pr_size
from .filesystem import Issue, read_json, root_directory
from .upgrade import STATUSES, apply as upgrade_apply, plan as upgrade_plan
from .workflows import OPERATIONS, workflow_result


class Parser(argparse.ArgumentParser):
    def error(self, message):
        raise Issue("invalid_arguments", 2)


def parser_for(catalog):
    class Formatter(argparse.HelpFormatter):
        def _format_usage(self, usage, actions, groups, prefix):
            return super()._format_usage(usage, actions, groups, prefix or catalog["usage"])

    parser = Parser(prog="dixi", description=catalog["description"], add_help=False, formatter_class=Formatter)
    parser._positionals.title = catalog["arguments"]
    parser._optionals.title = catalog["options"]
    parser.add_argument("--help", "-h", action="help", help=catalog["help"])
    parser.add_argument("--version", action="version", version=f"dixi {__version__}", help=catalog["version"])
    parser.add_argument("--lang", choices=("es", "en"), default=None, help=catalog["lang"])
    parser.add_argument("--json", action="store_true", help=catalog["json"])
    commands = parser.add_subparsers(dest="command", required=True, title=catalog["commands"])
    for command in ("init", "doctor", "check", "workflow", "upgrade", "placeholders", "pr-size"):
        child = commands.add_parser(command, help=catalog[command], description=catalog[command],
                                    add_help=False, formatter_class=Formatter)
        child._positionals.title = catalog["arguments"]
        child._optionals.title = catalog["options"]
        child.add_argument("--help", "-h", action="help", help=catalog["help"])
        if command == "init":
            child.add_argument("directory", help=catalog["directory"])
            child.add_argument("--agent", choices=("none", "claude", "codex", "skills"), default="none", help=catalog["agent"])
            child.add_argument("--profile", choices=PROFILES, default="minimal", help=catalog["profile_option"])
            child.add_argument("--regulated", action="store_true", help=catalog["regulated_option"])
            child.add_argument("--controls", action="store_true", help=catalog["controls_option"])
        elif command == "placeholders":
            child.add_argument("--strict", action="store_true", help=catalog["placeholders_strict"])
        elif command == "pr-size":
            child.add_argument("--base", default="main", help=catalog["pr_size_base"])
            child.add_argument("--max", type=int, default=1500, dest="limit", help=catalog["pr_size_max"])
        elif command == "upgrade":
            child.add_argument("--dry-run", action="store_true", help=catalog["upgrade_dry_run"])
            child.add_argument("--apply", action="store_true", help=catalog["upgrade_apply"])
            child.add_argument("--profile", choices=PROFILES, default=None, help=catalog["profile_option"])
            child.add_argument("--regulated", action="store_true", default=None, help=catalog["regulated_option"])
            child.add_argument("--controls", action="store_true", default=None, help=catalog["controls_option"])
        elif command == "workflow":
            actions = child.add_subparsers(dest="workflow_action", required=True, title=catalog["commands"])
            for action in ("list", "show", "prepare"):
                operation = actions.add_parser(action, help=catalog[f"workflow_{action}"], add_help=False,
                                               description=catalog[f"workflow_{action}"], formatter_class=Formatter)
                operation._positionals.title = catalog["arguments"]
                operation._optionals.title = catalog["options"]
                operation.add_argument("--help", "-h", action="help", help=catalog["help"])
                if action != "list":
                    operation.add_argument("operation", choices=OPERATIONS, help=catalog["workflow_operation"])
                if action == "prepare":
                    operation.add_argument("--target", required=True, help=catalog["workflow_target"])
                    operation.add_argument("--request", required=True, help=catalog["workflow_request"])
    return parser


def project_language():
    try:
        with root_directory(Path.cwd()) as root:
            language = read_json(root, METADATA).get("language")
    except (Issue, OSError, AttributeError):
        return None
    return language if language in ("es", "en") else None


def subcommand(argv):
    skip = False
    for arg in argv:
        if skip:
            skip = False
        elif arg == "--lang":
            skip = True
        elif not arg.startswith("-"):
            return arg
    return None


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    language = None
    for index, arg in enumerate(argv):
        if arg == "--lang" and index + 1 < len(argv) and argv[index + 1] in ("es", "en"):
            language = argv[index + 1]
        elif arg in ("--lang=es", "--lang=en"):
            language = arg.split("=", 1)[1]
    if language is None and subcommand(argv) != "init":
        language = project_language()
    language = language or "en"
    catalog = json.loads(files("dixi_spec_kit").joinpath("locales", f"{language}.json").read_text(encoding="utf-8"))
    code = 0
    workflow = None
    upgrade = None
    extra = {}
    try:
        args = parser_for(catalog).parse_args(argv)
        args.lang = args.lang or language
        if args.command == "init":
            messages = initialize(args.directory, args.lang, args.agent, args.profile, args.regulated, args.controls)
        elif args.command == "doctor":
            messages = doctor(Path.cwd(), args.lang)
        elif args.command == "workflow":
            workflow = workflow_result(args, Path.cwd())
            messages = [message("workflow_scope")]
        elif args.command == "upgrade":
            if args.dry_run == args.apply:
                raise Issue("upgrade_requires_mode", 2)
            if args.apply:
                upgrade = upgrade_apply(Path.cwd(), args.profile, args.regulated, args.controls)
                left = len(upgrade["files"]["conflict"]) + len(upgrade["skipped"])
                messages = [message("upgrade_applied", source=upgrade["from"], target=upgrade["to"],
                                    applied=len(upgrade["applied"]), left=left)]
            else:
                upgrade = upgrade_plan(Path.cwd(), args.profile, args.regulated, args.controls)
                messages = [message("upgrade_planned", source=upgrade["from"], target=upgrade["to"]),
                            message("upgrade_no_changes")]
        elif args.command == "placeholders":
            counts = placeholders(Path.cwd())
            total = sum(counts.values())
            extra = {"placeholders": counts, "total": total}
            messages = [message("placeholders_found", total=total, files=len(counts))]
            code = 1 if args.strict and total else 0
        elif args.command == "pr-size":
            size = pr_size(Path.cwd(), args.base, args.limit)
            extra = {"pr_size": size}
            messages = [message("pr_size_result", **size)]
            if size["counted"] > size["max"]:
                code = 1
                messages.append(message("pr_size_exceeded", counted=size["counted"], max=size["max"]))
        else:
            code, messages = check_project(Path.cwd())
    except Issue as error:
        code, messages = error.code, [message(error.key, **error.params)]
    except OSError:
        code, messages = 5, [message("io_error")]
    for entry in messages:
        entry["message"] = catalog[entry["key"]].format(**entry["params"])
    result = {"status": "completed" if code == 0 else "failed", "code": code, "messages": messages}
    if workflow is not None:
        result["workflow"] = workflow
    if upgrade is not None:
        result["upgrade"] = upgrade
    result.update(extra)
    if "--json" in argv:
        print(json.dumps(result, ensure_ascii=False))
    else:
        for entry in messages:
            print(entry["message"], file=sys.stderr if code else sys.stdout)
        if workflow is not None:
            print(format_workflow(workflow, catalog))
        if upgrade is not None:
            print(format_upgrade(upgrade, catalog))
        for name, count in extra.get("placeholders", {}).items():
            print(f"  {count:4d}  {name}")
    return code


def format_upgrade(upgrade, catalog):
    lines = []
    for status in STATUSES:
        names = upgrade["files"][status]
        lines.append(f"\n{catalog['upgrade_heading_' + status]} ({len(names)}):")
        if status != "unchanged":
            lines += [f"- {name}" for name in names]
    for key in ("applied", "skipped"):
        if key in upgrade:
            lines.append(f"\n{catalog['upgrade_heading_' + key]} ({len(upgrade[key])}):")
            lines += [f"- {name}" for name in upgrade[key]]
    return "\n".join(lines)


def format_workflow(workflow, catalog):
    if "operations" in workflow:
        return "\n".join(f"{op['id']} — {op['title']}\n  {op['purpose']}" for op in workflow["operations"])
    packet = workflow.get("packet")
    recipe = packet["recipe"] if packet else workflow["recipe"]
    lines = [f"\n{recipe['id']} — {recipe['title']}", recipe["purpose"]]
    if packet:
        lines += [catalog["workflow_prepared"].format(target=packet["target"]["id"], mode=packet["mode"],
                                                      language=packet["project_language"]),
                  catalog["workflow_request"] + ": " + json.dumps(packet["request"], ensure_ascii=False)]
    for key in ("target_kinds", "inputs", "steps", "outputs", "gates", "checks", "guards", "next_operations"):
        lines += ["\n" + catalog[f"workflow_heading_{key}"] + ":"]
        lines += [f"- {item}" for item in recipe[key]] or [catalog["workflow_no_next"]]
    if packet:
        lines += ["\n" + catalog["workflow_heading_sources"] + ":"]
        lines += [f"- {s['path']} · SHA-256 {s['sha256']} · {s['bytes']} B" for s in packet["sources"]]
    return "\n".join(lines)
