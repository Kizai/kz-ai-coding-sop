---
name: spec-driven-development
description: Use when starting a feature or facing ambiguous requirements. Lock a small, verifiable spec (goal, scope, non-goals, acceptance criteria) and get human sign-off before writing code, then make every change trace back to a spec item.
---

# Spec-Driven Development

Lock the contract before the code. The spec is the source of truth; the implementation conforms to it, not the reverse. This is the KZ norm that feeds `ralph-loop`, which executes a spec, and `planning-with-files`, which tracks progress against one.

## When To Use

- Starting any non-trivial feature or behavior change.
- Requirements are ambiguous or have multiple interpretations.
- Before an autonomous or multi-iteration build, to give it a verifiable target.

Skip for trivial, unambiguous one-line edits.

## The Spec (keep it small)

A spec is decision-complete when an implementer needs no further product decisions:

- **Goal** — one sentence: the end state and the problem it solves.
- **Scope** — the specific behaviors that are in.
- **Non-goals** — what is explicitly out. The most undervalued section; it stops scope creep.
- **Acceptance criteria** — verifiable checks, not vibes.
- **Open questions** — anything blocking that needs a human decision.

## Acceptance Criteria Must Be Verifiable

Each criterion is something you can CHECK.

- Good: "POST /tasks with no title returns 400", "filter persists in URL params", "typecheck passes".
- Bad: "works correctly", "good UX", "handles edge cases".

Prefer criteria you can turn into a test or a single command.

## The Flow

1. Draft the spec from the request. Surface assumptions and alternatives explicitly; do not pick silently.
2. Resolve open questions with the human. Do not guess product decisions.
3. Get explicit sign-off on the spec.
4. Implement. Every change traces to a spec item; nothing extra.
5. Verify each acceptance criterion and report which passed and how.
6. If reality forces a change, amend the spec and call it out. Never silently diverge.

## Rules

- No code before the spec's acceptance criteria are agreed.
- Right-size: if a spec is too big for one reviewable change, split it into ordered, independently verifiable specs, dependencies first.
- Every implemented line should trace to a spec item. Flag anything that does not.
- A changed public API, schema, or user-visible behavior must appear in the spec.
- Done means all acceptance criteria are verified, or the gaps are explained.

## KZ Integration

- Hand an approved spec to `ralph-loop` as right-sized, dependency-ordered stories.
- Track execution against the spec with `planning-with-files`.
- Stress-test a draft spec with `grill-me`; pressure-test product viability with `startup-pressure-test`.
- Superpowers-first: `superpowers:brainstorming` to shape, `superpowers:writing-plans` for the plan, `superpowers:verification-before-completion` to close.
