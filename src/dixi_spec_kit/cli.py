import argparse
from importlib.resources import files
import json
from pathlib import Path
import sys

from . import __version__
from .core import check_project, doctor, initialize, message
from .filesystem import Issue
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
    parser.add_argument("--lang", choices=("es", "en"), default="es", help=catalog["lang"])
    parser.add_argument("--json", action="store_true", help=catalog["json"])
    commands = parser.add_subparsers(dest="command", required=True, title=catalog["commands"])
    for command in ("init", "doctor", "check", "workflow"):
        child = commands.add_parser(command, help=catalog[command], description=catalog[command],
                                    add_help=False, formatter_class=Formatter)
        child._positionals.title = catalog["arguments"]
        child._optionals.title = catalog["options"]
        child.add_argument("--help", "-h", action="help", help=catalog["help"])
        if command == "init":
            child.add_argument("directory", help=catalog["directory"])
            child.add_argument("--agent", choices=("none", "claude"), default="none", help=catalog["agent"])
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


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    language = "es"
    for index, arg in enumerate(argv):
        if arg == "--lang" and index + 1 < len(argv) and argv[index + 1] in ("es", "en"):
            language = argv[index + 1]
        elif arg in ("--lang=es", "--lang=en"):
            language = arg.split("=", 1)[1]
    catalog = json.loads(files("dixi_spec_kit").joinpath("locales", f"{language}.json").read_text(encoding="utf-8"))
    code = 0
    workflow = None
    try:
        args = parser_for(catalog).parse_args(argv)
        if args.command == "init":
            messages = initialize(args.directory, args.lang, args.agent)
        elif args.command == "doctor":
            messages = doctor(Path.cwd(), args.lang)
        elif args.command == "workflow":
            workflow = workflow_result(args, Path.cwd())
            messages = [message("workflow_scope")]
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
    if "--json" in argv:
        print(json.dumps(result, ensure_ascii=False))
    else:
        for entry in messages:
            print(entry["message"], file=sys.stderr if code else sys.stdout)
        if workflow is not None:
            print(format_workflow(workflow, catalog))
    return code


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
