# ADR-001 — Almacén JSON local

## Propósito

Decidir cómo se persisten las notas.

## Estado

Aceptado. Decisión (persona del ejemplo, 2026-11-08), propuesta por `/dixi.plan`.

## Decisión

Un archivo JSON con versión de esquema, escrito de forma atómica. Sin base de datos ni dependencias.

## Consecuencias

Simple y portable; no escala a miles de notas ni a acceso concurrente, fuera de alcance.

## Relacionados

- [Contrato](../../07-contracts/example.md)
