# KZ AI Coding SOP

This project follows KZ AI Coding SOP, Kizai's controlled AI coding workflow.

AI agents may assist development, but the human owns product intent, engineering constraints, architecture boundaries, and acceptance criteria. Agents must keep changes understandable, reviewable, and verifiable.

This file is the primary SOP entrypoint. The machine-readable config is `.kz/sop.config.json`.

## First Response

Before making code changes in a new task, report:

- project understanding
- relevant files or modules
- selected workflow skill or fallback route
- implementation plan
- risks and verification steps

Do not write code immediately on new feature requests unless the user explicitly asks for a trivial direct edit.

## Core Rules

- Inspect relevant files before making claims about stack, architecture, or behavior.
- Preserve existing features unless removal is explicitly requested.
- Prefer small, reviewable changes.
- Follow existing architecture, naming, formatting, and dependency patterns.
- Do not introduce production dependencies without explaining reason, scope, and risk.
- Do not hide errors, swallow failures, or silently fall back from real problems.
- Do not change public APIs, schemas, or user-visible behavior without calling it out.
- Do not claim tests, builds, or checks passed unless they were actually run.
- After changes, explain what changed, why it changed, affected files, and how to verify.

## Superpowers-First Routing

KZ SOP can route agents to upstream Superpowers skills when they are installed in the current harness. KZ SOP does not own, copy, bundle, modify, or claim authorship of Superpowers.

Upstream Superpowers repository:

https://github.com/obra/superpowers

Recommended routing:

| Situation | Skill |
| --- | --- |
| Starting a session or checking skill applicability | `superpowers:using-superpowers` |
| New feature, behavior change, or creative implementation | `superpowers:brainstorming` |
| Approved requirements or implementation plan writing | `superpowers:writing-plans` |
| Feature, bug fix, refactor, or behavior implementation | `superpowers:test-driven-development` |
| Bug, failed test, build error, or unexpected behavior | `superpowers:systematic-debugging` |
| Completing work and validating claims | `superpowers:verification-before-completion` |
| Reviewing completed work before merge or after major work | `superpowers:requesting-code-review` |
| Executing a plan with subagents | `superpowers:subagent-driven-development` |
| Executing a plan without subagents | `superpowers:executing-plans` |

## KZ-Packaged Skill Routing

Use packaged KZ skills when the task matches their narrower trigger:

| Situation | Skill |
| --- | --- |
| Pressure-testing a startup idea before building | `startup-pressure-test` |
| Stress-testing a plan or design with focused questions | `grill-me` |
| Reducing common LLM coding mistakes while writing, reviewing, or refactoring code | `karpathy-guidelines` |
| Routing to Waza-style engineering habit workflows | `waza-router` |
| Auditing cross-harness agent workflow readiness | `ecc-operator-system` |

## Fallback When Superpowers Is Unavailable

If Superpowers is not installed in the current harness:

1. Say that Superpowers is unavailable.
2. Do not skip planning.
3. Inspect files before making assumptions.
4. Ask only for product decisions that cannot be discovered from the repository.
5. Keep edits small and reversible.
6. Run relevant verification.
7. Summarize changes and unresolved risks.

## Coding Standard

- Use clear, descriptive names.
- Avoid vague names like `data`, `info`, `temp`, or `handleThing`.
- Keep functions focused on one responsibility.
- Avoid duplicated logic.
- Prefer explicit types when the language supports them.
- Use comments to explain why, not what.
- Validate inputs at boundaries where invalid data can enter.

## Architecture Standard

- Preserve current architecture unless a refactor is explicitly requested or required.
- Keep changes close to the affected behavior.
- Do not mix unrelated refactors with feature work.
- Keep business logic separate from transport, UI, persistence, and infrastructure when the project already follows that pattern.
- Do not bypass existing authorization, validation, or persistence boundaries.
- Do not create duplicate pathways for the same behavior.

Before changing architecture, explain:

- what problem the current architecture creates
- alternatives considered
- why the selected change is the smallest safe option
- affected files and public interfaces
- how compatibility will be verified

## Review Checklist

Before marking work complete:

- implementation matches the task or approved plan
- existing behavior is preserved unless explicitly changed
- edge cases and error paths are considered
- public APIs, schemas, and user-visible behavior are called out if changed
- no unrelated refactors are bundled
- no unnecessary dependencies are added
- relevant tests or checks were run
- skipped checks or missing tests are explained

## Done Means

A task is not done until:

- code compiles or type-checks where applicable
- relevant tests pass, or missing tests are explained
- edge cases and failure modes are considered
- the change is summarized clearly
- verification steps are provided
