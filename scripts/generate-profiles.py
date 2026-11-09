"""Generate resources/profiles.json from the profile tables of the content contracts.

Each table row `| `path` | S | A | P |` becomes one entry with a three-letter code in the order
site, app, platform: `y` installed, `r` installed only with --regulated, `n` not installed.
Run with --check to fail when the manifest is out of date.
"""
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
CONTRACTS = [ROOT / "07-contracts/commands/profiles-contract.md",
             ROOT / "07-contracts/commands/remaining-content-contract.md"]
MANIFEST = ROOT / "src/dixi_spec_kit/resources/profiles.json"
ROW = re.compile(r"^\| `([^`]+)`[^|]*\| (✓|R|—) \| (✓|R|—) \| (✓|R|—) \|\s*$")
HEADING = re.compile(r"^### `([^`]+/)`")
AREA = re.compile(r"^[0-9]{2}-[a-z-]+/")
CODE = {"✓": "y", "R": "r", "—": "n"}
ENABLED = {ROOT / "07-contracts/commands/profiles-contract.md"}


def table(path):
    entries, prefix = {}, None
    for line in path.read_text(encoding="utf-8").splitlines():
        heading = HEADING.match(line)
        if heading:
            prefix = heading.group(1)
            continue
        row = ROW.match(line)
        if row and prefix:
            name = row.group(1) if AREA.match(row.group(1)) else prefix + row.group(1)
            entries[name] = "".join(CODE[mark] for mark in row.groups()[1:])
    return entries


def build():
    files = {}
    for contract in CONTRACTS:
        if contract in ENABLED:
            files.update(table(contract))
    return json.dumps({"version": 1, "files": dict(sorted(files.items()))}, ensure_ascii=False, indent=2) + "\n"


def main():
    text = build()
    if "--check" in sys.argv[1:]:
        if MANIFEST.read_text(encoding="utf-8") != text:
            sys.exit("profiles.json is out of date: run scripts/generate-profiles.py")
        return
    MANIFEST.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
