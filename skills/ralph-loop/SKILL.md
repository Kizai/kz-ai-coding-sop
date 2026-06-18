---
name: ralph-loop
description: Use when running a coding agent in an autonomous loop, or building a feature larger than one context window. Break work into right-sized, dependency-ordered stories with verifiable acceptance, keep memory on disk via a status file, an append-only progress log, and git, then run fresh-context iterations until every story passes.
---

# Ralph Loop

Adoption layer for the Ralph autonomous-agent loop by snarktank. Use it when a task is too big for one context window and fresh-context iterations beat one long session that degrades as it fills.

This KZ skill captures the essence and routes to the upstream project for the full runner (`ralph.sh`, prompt templates, flowchart). It does not copy the loop scripts.

## When To Use

- Building a feature that exceeds a single context window.
- Running an agent repeatedly (Amp, Claude Code, Codex) until requirements are complete.
- Any work where fresh-context iterations beat one long session that degrades.

If the task fits in one context window, do NOT loop. Just implement it.

## Core Idea: Fresh Context + Memory On Disk

Each iteration is a fresh agent instance with clean context. Memory persists outside the model via:

- git history (previous commits)
- an append-only progress log (learnings plus a "codebase patterns" section)
- a status file listing each story and whether it passes

The loop ends when every story is marked passing.

## The Three Disciplines

### 1. Right-size every story (the number one rule)

Each story must be completable in ONE iteration / one context window.

- If you cannot describe the change in 2-3 sentences, it is too big. Split it.
- Right-sized: "add a status column and migration", "add one filter dropdown to a list".
- Too big: "build the dashboard", "add authentication". Split into schema, then backend, then UI.

### 2. Dependencies first

Stories run in priority order, and an earlier story must not depend on a later one.

Order: schema and migrations, then server and backend logic, then UI that consumes it, then aggregate or summary views.

### 3. Acceptance must be verifiable

Every criterion is something the agent can CHECK, not a vibe.

- Good: "filter has options All, Active, Done", "clicking delete shows a confirm dialog".
- Bad: "works correctly", "good UX", "handles edge cases".
- Always end each story with "Typecheck passes", and "Tests pass" where the logic is testable.
- A UI story is not done until it is visually verified in a browser.

## Per-Iteration Loop

1. Read the status file and the progress log (read the "codebase patterns" section first).
2. Confirm the working branch.
3. Pick the highest-priority story that is not yet passing.
4. Implement that ONE story.
5. Run quality checks (typecheck, lint, tests).
6. Record reusable patterns into nearby `AGENTS.md` files and the progress log.
7. If checks pass, commit, then mark the story passing.
8. Stop when all stories pass.

## Memory Hygiene

- Append to the progress log, never overwrite. Record what changed, files touched, and learnings for the next iteration.
- Promote general, reusable learnings into a "codebase patterns" section at the top of the log.
- Keep commits small and CI green. Never commit broken code.

## KZ Integration

- Use `spec-driven-development` to lock the acceptance contract before the loop starts.
- Pair with `planning-with-files` when you also need durable in-session planning. The progress log is the shared memory.
- Stay Superpowers-first for non-loop workflow: `superpowers:test-driven-development`, `superpowers:verification-before-completion`.

## Fallback When Ralph Is Not Installed

The upstream runner is not required. Apply the discipline manually:

1. Write a right-sized, dependency-ordered story list with verifiable acceptance.
2. Implement one story per pass, verify, commit, mark done.
3. Keep an append-only progress log so a fresh session can resume.

## Upstream Reference

Repository: https://github.com/snarktank/ralph

## Attribution

Adapted from `snarktank/ralph`, MIT License.
