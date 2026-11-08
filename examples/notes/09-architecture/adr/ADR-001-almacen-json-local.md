# ADR-001 — Local JSON store

## Purpose

Decide how notes are persisted.

## Status

Accepted. Decision (example owner, 2026-11-08), proposed by `/dixi.plan`.

## Decision

A JSON file with a schema version, written atomically. No database or dependencies.

## Consequences

Simple and portable; it does not scale to thousands of notes or concurrent access, which are out of scope.

## Related

- [Contract](../../07-contracts/example.md)
