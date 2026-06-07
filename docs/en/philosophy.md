# Philosophy

KZ AI Coding SOP exists to make AI coding controllable, consistent, and maintainable.

## Human Defines Rules

The human owns product intent, engineering constraints, architecture boundaries, and acceptance criteria. The agent can help discover implementation details, but it must not silently invent business decisions.

## Agent Follows Workflow

AI agents are effective when they use a disciplined process. KZ SOP uses Superpowers as the default workflow baseline for brainstorming, planning, TDD, debugging, verification, and review.

## Project Rules Live With The Project

Agent rules should be committed to the repository so every harness sees the same expectations. `AGENTS.md`, `.ai/`, `.cursor/rules/`, and `.kz/` make the workflow explicit and portable.

## Verification Beats Claims

The agent must report what it actually verified. If tests were not run, it must say so. If Superpowers is unavailable, it must say so and follow the fallback workflow.

