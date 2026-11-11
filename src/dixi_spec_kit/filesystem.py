from contextlib import contextmanager
import errno
import json
import os
from pathlib import Path, PurePosixPath
import secrets
import stat
import unicodedata


MAX_BYTES = 1024 * 1024


class Issue(Exception):
    def __init__(self, key, code=1, **params):
        self.key, self.code, self.params = key, code, params
        super().__init__(key)


def supported():
    return (os.name == "posix" and hasattr(os, "O_NOFOLLOW")
            and os.open in os.supports_dir_fd and os.mkdir in os.supports_dir_fd
            and os.rename in os.supports_dir_fd)


def safe_path(name):
    if (not isinstance(name, str) or not name or "\\" in name or ":" in name
            or any(unicodedata.category(char) in {"Cc", "Cs"} for char in name)):
        return False
    parts = name.casefold().split("/")
    if any(p in {"", ".", "..", ".git", ".context", ".aws", ".ssh"} for p in parts):
        return False
    return not any(p.startswith(".env") or p in {"id_rsa", "id_ed25519"}
                   or p.endswith((".pem", ".key")) for p in parts)


@contextmanager
def directory(root_fd, parts, create=False):
    fd = os.dup(root_fd)
    try:
        for part in parts:
            if create:
                try:
                    os.mkdir(part, mode=0o700, dir_fd=fd)
                except FileExistsError:
                    pass
            new_fd = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = new_fd
        yield fd
    except OSError as error:
        if error.errno in {errno.ELOOP, errno.ENOTDIR}:
            raise Issue("unsafe_path") from None
        raise
    finally:
        os.close(fd)


@contextmanager
def root_directory(path):
    if not supported():
        raise Issue("unsupported_platform", 4)
    raw = Path(path)
    if ".." in raw.parts:
        raise Issue("unsafe_path")
    absolute = Path(os.path.abspath(raw))
    fd = os.open("/", os.O_RDONLY | os.O_DIRECTORY)
    try:
        with directory(fd, absolute.parts[1:]) as root:
            yield root
    finally:
        os.close(fd)


def read_file(root, name):
    if not safe_path(name):
        raise Issue("unsafe_path", path=str(name))
    path = PurePosixPath(name)
    try:
        with directory(root, path.parts[:-1]) as parent:
            fd = os.open(path.name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=parent)
            with os.fdopen(fd, "rb") as stream:
                info = os.fstat(stream.fileno())
                if not stat.S_ISREG(info.st_mode) or info.st_size > MAX_BYTES:
                    raise Issue("invalid_file", path=name)
                data = stream.read(MAX_BYTES + 1)
                if len(data) > MAX_BYTES:
                    raise Issue("invalid_file", path=name)
                return data
    except OSError as error:
        if error.errno in {errno.ELOOP, errno.ENOTDIR}:
            raise Issue("unsafe_path", path=name) from None
        if error.errno == errno.ENOENT:
            raise Issue("missing_file", path=name) from None
        raise


def write_file(root, name, data):
    if not safe_path(name):
        raise Issue("unsafe_path", 3)
    path = PurePosixPath(name)
    with directory(root, path.parts[:-1], create=True) as parent:
        fd = os.open(path.name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
                     0o600, dir_fd=parent)
        with os.fdopen(fd, "wb") as stream:
            stream.write(data)


def replace_file(root, name, data):
    """Write data to name atomically: exclusive temporary file in the same directory, then rename.

    Never follows symlinks; refuses to replace anything but a regular file. Renaming replaces a link
    swapped in at the last moment instead of writing through it.
    """
    if not safe_path(name):
        raise Issue("unsafe_path", 3)
    path = PurePosixPath(name)
    with directory(root, path.parts[:-1], create=True) as parent:
        try:
            info = os.stat(path.name, dir_fd=parent, follow_symlinks=False)
            if not stat.S_ISREG(info.st_mode):
                raise Issue("unsafe_path", 3, path=name)
        except FileNotFoundError:
            pass
        temporary = f".{path.name}.dixi-{secrets.token_hex(8)}"
        fd = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600, dir_fd=parent)
        try:
            with os.fdopen(fd, "wb") as stream:
                stream.write(data)
                stream.flush()
                os.fsync(stream.fileno())
            os.rename(temporary, path.name, src_dir_fd=parent, dst_dir_fd=parent)
        except BaseException:
            try:
                os.unlink(temporary, dir_fd=parent)
            except FileNotFoundError:
                pass
            raise


def unique_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate key")
        result[key] = value
    return result


def decode_json(data, path):
    try:
        return json.loads(data, object_pairs_hook=unique_keys)
    except (ValueError, UnicodeError, RecursionError):
        raise Issue("invalid_file", path=path) from None


def read_json(root, name):
    return decode_json(read_file(root, name), name)
