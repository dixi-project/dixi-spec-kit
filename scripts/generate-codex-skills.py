"""Derive the Codex skills from the Claude Code commands so both adapters share steps and limits."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "src/dixi_spec_kit/resources/claude"
TARGET = ROOT / "src/dixi_spec_kit/resources/codex"
REQUEST = {"es": "la petición de la persona (el texto escrito junto a la mención del skill)",
           "en": "the person's request (the text written with the skill mention)"}
REQUEST_SHORT = {"es": "la petición", "en": "the request"}


def convert(text, language, operation):
    match = re.match(r"---\ndescription: (.*)\nargument-hint: .*\n---\n", text)
    if not match:
        raise ValueError(f"unexpected frontmatter: {operation}")
    body = text[match.end():]
    body = body.replace(f"# /dixi.{operation}", f"# $dixi-{operation}", 1)
    body = body.replace("`$ARGUMENTS`", REQUEST[language], 1).replace("`$ARGUMENTS`", REQUEST_SHORT[language])
    body = re.sub(r"/dixi\.([a-z-]+)", r"$dixi-\1", body)
    if "$ARGUMENTS" in body or "/dixi." in body:
        raise ValueError(f"unconverted reference: {operation}")
    return f"---\nname: dixi-{operation}\ndescription: {match.group(1)}\n---\n{body}"


def main():
    check = "--check" in sys.argv
    stale = []
    for language in ("es", "en"):
        for source in sorted((SOURCE / language).glob("dixi.*.md")):
            operation = source.stem.removeprefix("dixi.")
            output = TARGET / language / f"dixi-{operation}.md"
            text = convert(source.read_text(encoding="utf-8"), language, operation)
            if check:
                if not output.is_file() or output.read_text(encoding="utf-8") != text:
                    stale.append(str(output.relative_to(ROOT)))
            else:
                output.parent.mkdir(parents=True, exist_ok=True)
                output.write_text(text, encoding="utf-8")
    if stale:
        sys.exit("Codex skills are out of date; run scripts/generate-codex-skills.py:\n" + "\n".join(stale))


if __name__ == "__main__":
    main()
