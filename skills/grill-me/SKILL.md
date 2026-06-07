---
name: grill-me
description: Use when the user wants to stress-test a plan or design, get grilled on a design, resolve decision dependencies, or mentions "grill me".
---

# Grill Me

Interview the user relentlessly about every aspect of the plan until there is shared understanding.

Walk down each branch of the design tree, resolving dependencies between decisions one by one. For each question, provide your recommended answer.

## Rules

- Ask one question at a time.
- If a question can be answered by exploring the codebase, explore the codebase instead.
- Do not ask the user to provide facts that are discoverable from files, tests, docs, or current implementation.
- Keep pressing until goal, success criteria, constraints, tradeoffs, risks, and verification are clear.
- Stop when the plan is decision-complete enough for an implementation agent to execute without making product decisions.

## Output Pattern

For each turn:

1. Ask the next highest-leverage question.
2. Include your recommended answer.
3. Explain briefly why the answer changes the plan.

## Attribution

Adapted from `mattpocock/skills/skills/productivity/grill-me/SKILL.md`, MIT License.

