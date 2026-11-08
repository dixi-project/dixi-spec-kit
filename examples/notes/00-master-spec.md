# Project — Local notes

## Purpose

Public DIXI Spec Kit example: a small library and CLI to store text notes with tags in a local file. It shows the flow idea → specs → tests → verified code → review, and an evolution with impact analysis. The responsible person is fictitious; their decisions are marked as "Decision (example owner)".

## Problem and scope

- Problem: jot down quick ideas from the terminal and find them later without depending on a network service.
- Scope: add, list and search notes; normalized tags and filtering by tag (evolution, FEATURE-002).
- Out of scope: sync, encryption, multiple users, web interface.
- Stack: Python 3.11+ with the standard library and `unittest`. Decision (example owner, 2026-11-08).
- Constraints: no network, no third-party dependencies, data in a single JSON file chosen by whoever uses the CLI.

## Related

- [Goal](01-business/vision.md)
- [Guide](docs/guide.md)
- [Example walkthrough](docs/walkthrough.md)
