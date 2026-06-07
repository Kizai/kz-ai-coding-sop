# KZ Architecture Standard

## Principles

- Preserve the current architecture unless a refactor is explicitly requested or required.
- Keep changes close to the affected behavior.
- Prefer clear module boundaries and explicit interfaces.
- Do not mix unrelated refactors with feature work.
- Avoid introducing framework, storage, or deployment changes as side effects.

## Before Changing Architecture

Explain:

- what problem the current architecture creates
- what alternatives were considered
- why the selected change is the smallest safe option
- what files and public interfaces are affected
- how compatibility will be verified

## Boundaries

- Keep business logic separate from transport, UI, persistence, and infrastructure when the project already follows that pattern.
- Do not bypass existing authorization, validation, or persistence boundaries.
- Do not create duplicate pathways for the same behavior.

