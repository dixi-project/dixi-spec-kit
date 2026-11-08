import argparse
import json
from pathlib import Path
import sys

from .store import NoteError, NoteStore


def catalog(language):
    return json.loads((Path(__file__).parent / "locales" / f"{language}.json").read_text(encoding="utf-8"))


def line(note):
    tags = f" [{', '.join(note.tags)}]" if note.tags else ""
    return f"#{note.id} {note.text}{tags}"


def main(argv=None):
    parser = argparse.ArgumentParser(prog="notes")
    parser.add_argument("--file", default="notes.json")
    parser.add_argument("--lang", choices=("es", "en"), default="en")
    commands = parser.add_subparsers(dest="command", required=True)
    add = commands.add_parser("add")
    add.add_argument("text")
    add.add_argument("--tag", action="append", default=[])
    listing = commands.add_parser("list")
    listing.add_argument("--tag")
    search = commands.add_parser("search")
    search.add_argument("term")
    args = parser.parse_args(argv)
    messages = catalog(args.lang)
    store = NoteStore(args.file)
    try:
        if args.command == "add":
            note = store.add(args.text, args.tag)
            print(messages["added"].format(id=note.id))
            return 0
        notes = store.search(args.term) if args.command == "search" else store.list(args.tag)
    except NoteError as error:
        print(messages[str(error)], file=sys.stderr)
        return 2
    for note in notes:
        print(line(note))
    return 0


if __name__ == "__main__":
    sys.exit(main())
