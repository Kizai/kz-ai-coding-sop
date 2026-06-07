# AGENTS.md

This project follows KZ AI Coding SOP.

KZ AI Coding SOP is a controlled AI coding workflow. AI agents may assist development, but they must follow project rules, architecture boundaries, coding standards, workflow skills, and verification requirements.

KZ SOP is Superpowers-first. If the Superpowers plugin or skills are available in your agent harness, use them as the default workflow. If they are unavailable, follow the fallback rules in `.ai/` and clearly state that Superpowers is not available.

## Required Reading

Before making code changes, read:

1. `.ai/AGENT_ENTRY.md`
2. `.ai/CORE_RULES.md`
3. `.ai/WORKFLOW.md`
4. `.ai/SKILL_INDEX.md`

For larger work, also read:

1. `.ai/CODING_STANDARD.md`
2. `.ai/ARCHITECTURE_STANDARD.md`
3. `.ai/REVIEW_CHECKLIST.md`

## Core Rules

- Do not modify code before understanding the task and related files.
- Do not remove existing features unless explicitly requested.
- Do not introduce new production dependencies without explaining why.
- Prefer small, reviewable changes.
- Preserve existing architecture unless a refactor is explicitly approved.
- Do not hide errors or silently fail.
- Do not claim tests passed unless they were actually run.
- After changes, explain what changed, why it changed, affected files, and how to verify.

## Superpowers Routing

- New feature or behavior change: use `superpowers:brainstorming`.
- Approved requirements: use `superpowers:writing-plans`.
- Implementation: use `superpowers:test-driven-development`.
- Bug, failed build, or unexpected behavior: use `superpowers:systematic-debugging`.
- Before completion: use `superpowers:verification-before-completion`.
- Review: use `superpowers:requesting-code-review`.
- Plan execution: prefer `superpowers:subagent-driven-development`; otherwise use `superpowers:executing-plans`.

## Done Means

A task is not done until:

- Code compiles or type-checks where applicable.
- Relevant tests pass, or missing tests are explained.
- Edge cases and failure modes are considered.
- The change is summarized clearly.
- Verification steps are provided.

