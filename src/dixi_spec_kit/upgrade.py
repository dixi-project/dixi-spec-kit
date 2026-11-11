import hashlib
import json
import os

from . import __version__
from .core import (KIT_VERSION, METADATA, adapter_files, check_profile, control_files, profile_files,
                   project_metadata, recorded_profile, templates)
from .filesystem import Issue, read_file, replace_file, root_directory, write_file

STATUSES = ("unchanged", "updatable", "conflict", "new", "missing", "obsolete")
LOCK = ".dixi-upgrade.lock"
UNSAFE = "unsafe"


def version_key(text):
    match = KIT_VERSION.fullmatch(text)
    return tuple(int(part) for part in match.groups()[:3])


def local_digest(root, name):
    """Hash of the local file, None when absent, UNSAFE for a symlink or a non-regular file."""
    try:
        return hashlib.sha256(read_file(root, name)).hexdigest()
    except Issue as error:
        if error.key == "missing_file":
            return None
        if error.key in ("unsafe_path", "invalid_file"):
            return UNSAFE
        raise


def compute(root, profile=None, regulated=None, controls=None):
    metadata = project_metadata(root)
    current_profile, current_regulated = recorded_profile(metadata)
    if profile is None:
        profile = current_profile
        regulated = current_regulated if regulated is None else regulated
    check_profile(profile, bool(regulated))
    if version_key(metadata["kit_version"]) > version_key(__version__):
        raise Issue("project_newer", 4, version=metadata["kit_version"])
    controls = metadata.get("controls", False) if controls is None else controls
    shipped = {name: text.encode("utf-8") for name, text in templates(metadata["language"]).items()}
    shipped.update(profile_files(metadata["language"], profile, bool(regulated)))
    shipped.update(adapter_files(metadata["agent"], metadata["language"]))
    if controls:
        shipped.update(control_files(metadata["agent"]))
    recorded = metadata["managed_files"]
    files = {status: [] for status in STATUSES}
    for name in sorted(set(shipped) | set(recorded)):
        current = local_digest(root, name)
        if name not in shipped:
            files["obsolete"].append(name)
            continue
        target = hashlib.sha256(shipped[name]).hexdigest()
        if current == UNSAFE:
            files["conflict"].append(name)
        elif name not in recorded:
            files["new" if current is None else "updatable" if current == target else "conflict"].append(name)
        elif current is None:
            files["missing"].append(name)
        elif target == recorded[name]:
            files["unchanged"].append(name)
        elif current in (recorded[name], target):
            files["updatable"].append(name)
        else:
            files["conflict"].append(name)
    settings = {"profile": profile, "regulated": bool(regulated), "controls": bool(controls)}
    return {"from": metadata["kit_version"], "to": __version__, "files": files}, shipped, metadata, settings


def plan(path, profile=None, regulated=None, controls=None):
    with root_directory(path) as root:
        return compute(root, profile, regulated, controls)[0]


def apply(path, profile=None, regulated=None, controls=None, planned=None):
    """Write only updatable and new files, re-checking each right before writing (contract: block A)."""
    with root_directory(path) as root:
        result, shipped, metadata, settings = compute(root, profile, regulated, controls)
        if planned is not None:
            result = {**result, "files": planned["files"]}
        try:
            write_file(root, LOCK, b"")
        except FileExistsError:
            raise Issue("upgrade_locked", 3) from None
        try:
            recorded = dict(metadata["managed_files"])
            applied, skipped = [], []
            for name in sorted(result["files"]["updatable"] + result["files"]["new"]):
                data = shipped[name]
                target = hashlib.sha256(data).hexdigest()
                current = local_digest(root, name)
                if current != target:
                    if current == UNSAFE or current != metadata["managed_files"].get(name):
                        skipped.append(name)
                        continue
                    try:
                        replace_file(root, name, data)
                    except Issue:
                        skipped.append(name)
                        continue
                recorded[name] = target
                applied.append(name)
            metadata.update(settings, managed_files=recorded, kit_version=__version__)
            replace_file(root, METADATA, (json.dumps(metadata, ensure_ascii=False, indent=2) + "\n").encode())
        finally:
            os.unlink(LOCK, dir_fd=root)
    return {**result, "applied": applied, "skipped": skipped}
