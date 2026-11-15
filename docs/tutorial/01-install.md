# 1. Install the kit

## Purpose

Install the `dixi` command and check that it runs. It is a Python tool without runtime dependencies, and it never uses the network.

## What you do

Install it from PyPI with `uv` or, if you prefer, with `pipx`:

```bash
uv tool install dixi-spec-kit
pipx install dixi-spec-kit
```

You need only one of the two. Then check the installed version:

```bash
dixi --version
```

## What you should see

One line with `dixi` and the version number, the same as the latest release on PyPI. If your shell says that `dixi` is not found, the folder where `uv` or `pipx` installs tools is not on your `PATH`; `uv tool update-shell` or `pipx ensurepath` adds it.

To upgrade later, run the install again with `uv tool install --force --refresh dixi-spec-kit`.

## Next

[2. Create the project](02-init.md).

## Related

- [Tutorial](index.md)
- [Support matrix](../support-matrix.md)
- [CLI reference](../cli/index.md)
