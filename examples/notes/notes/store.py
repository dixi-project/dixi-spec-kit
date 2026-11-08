from dataclasses import dataclass
import json
import os
from pathlib import Path
import re

MAX_TEXT = 1000
TAG = re.compile(r"[a-z0-9_-]{1,32}")


class NoteError(ValueError):
    pass


@dataclass(frozen=True)
class Note:
    id: int
    text: str
    tags: tuple[str, ...] = ()


def normalize_tags(tags, strict=True):
    result = []
    for tag in tags:
        tag = tag.strip().lower()
        if not TAG.fullmatch(tag):
            if strict:
                raise NoteError("invalid_tag")
            continue
        if tag not in result:
            result.append(tag)
    return tuple(result)


class NoteStore:
    def __init__(self, path):
        self.path = Path(path)

    def _load(self):
        if not self.path.exists():
            return []
        data = json.loads(self.path.read_text(encoding="utf-8"))
        return [Note(item["id"], item["text"], normalize_tags(item.get("tags", ()), strict=False)) for item in data["notes"]]

    def _save(self, notes):
        payload = {"schema_version": 1,
                   "notes": [{"id": n.id, "text": n.text, "tags": list(n.tags)} for n in notes]}
        temporary = self.path.with_name(self.path.name + ".tmp")
        temporary.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        os.replace(temporary, self.path)

    def add(self, text, tags=()):
        text = text.strip()
        if not text or len(text) > MAX_TEXT:
            raise NoteError("invalid_text")
        tags = normalize_tags(tags)
        notes = self._load()
        note = Note(max((n.id for n in notes), default=0) + 1, text, tags)
        self._save(notes + [note])
        return note

    def list(self, tag=None):
        notes = self._load()
        if tag is None:
            return notes
        wanted = tag.strip().lower()
        return [n for n in notes if wanted in n.tags]

    def search(self, term):
        wanted = term.casefold()
        return [n for n in self._load() if wanted in n.text.casefold()]
