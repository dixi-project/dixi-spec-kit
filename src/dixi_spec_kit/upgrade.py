import hashlib

from . import __version__
from .core import (KIT_VERSION, adapter_files, check_profile, control_files, profile_files, project_metadata,
                   recorded_profile, templates)
from .filesystem import Issue, read_file, root_directory

STATUSES = ("unchanged", "updatable", "conflict", "new", "missing", "obsolete")


def version_key(text):
    match = KIT_VERSION.fullmatch(text)
    return tuple(int(part) for part in match.groups()[:3])


def local_digest(root, name):
    try:
        return hashlib.sha256(read_file(root, name)).hexdigest()
    except Issue as error:
        if error.key == "missing_file":
            return None
        raise


def plan(path, profile=None, regulated=None, controls=None):
    with root_directory(path) as root:
        metadata = project_metadata(root)
        current_profile, current_regulated = recorded_profile(metadata)
        if profile is None:
            profile = current_profile
            regulated = current_regulated if regulated is None else regulated
        check_profile(profile, bool(regulated))
        if version_key(metadata["kit_version"]) > version_key(__version__):
            raise Issue("project_newer", 4, version=metadata["kit_version"])
        shipped = {name: text.encode("utf-8") for name, text in templates(metadata["language"]).items()}
        shipped.update(profile_files(metadata["language"], profile, bool(regulated)))
        shipped.update(adapter_files(metadata["agent"], metadata["language"]))
        if metadata.get("controls", False) if controls is None else controls:
            shipped.update(control_files(metadata["agent"]))
        recorded = metadata["managed_files"]
        files = {status: [] for status in STATUSES}
        for name in sorted(set(shipped) | set(recorded)):
            current = local_digest(root, name)
            if name not in shipped:
                files["obsolete"].append(name)
            elif name not in recorded:
                files["new" if current is None else "conflict"].append(name)
            elif current is None:
                files["missing"].append(name)
            elif hashlib.sha256(shipped[name]).hexdigest() == recorded[name]:
                files["unchanged"].append(name)
            else:
                files["updatable" if current == recorded[name] else "conflict"].append(name)
    return {"from": metadata["kit_version"], "to": __version__, "files": files}
