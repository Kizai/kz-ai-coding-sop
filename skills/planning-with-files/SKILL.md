---
name: planning-with-files
description: Use when a task needs 5+ tool calls, multi-step research, or must survive context loss, compaction, or /clear. Keep task_plan.md, findings.md, and progress.md on disk as durable working memory, re-read the plan before decisions, and update after every step.
---

# Planning With Files

Adoption layer for OthmanAdi's planning-with-files. Treat the filesystem as durable working memory so long tasks survive context loss.

This KZ skill captures the core file pattern and rules. It does not copy the upstream hooks, attestation scripts, or per-harness adapters. Install those upstream if you want automatic enforcement.

## Core Idea

```
Context window = RAM (volatile, limited)
Filesystem     = Disk (persistent, unlimited)
-> Anything important gets written to disk.
```

## The Three Files

These live in your project root, not in the skill folder.

| File | Purpose | Update when |
| --- | --- | --- |
| `task_plan.md` | Goal, 3-7 phases, checkboxes, current phase | After each phase |
| `findings.md` | Research, discoveries, decisions and rationale | After any discovery |
| `progress.md` | Session log, test results, errors | Throughout the session |

## When To Use

Use for multi-step tasks (3+ steps or 5+ tool calls), research tasks, building projects, and anything spanning many tool calls.

Skip for simple questions, single-file edits, and quick lookups.

## Critical Rules

1. Create `task_plan.md` FIRST. Never start complex work without it.
2. 2-action rule: after every ~2 view, browser, or search operations, immediately save key findings to disk. Visual and multimodal information is lost otherwise.
3. Read before decide: re-read the plan before major decisions to keep the goal in the attention window.
4. Update after act: mark a phase pending then in_progress then complete, and note files changed.
5. Log ALL errors in the plan or progress file so they are never repeated.

## The 3-Strike Error Protocol

1. Diagnose and fix the root cause.
2. Same error? Use a different method, tool, or library. Never repeat the exact failing action.
3. Broader rethink: question assumptions and update the plan.

After 3 failures, escalate to the user with what you tried and the exact error.

## The 5-Question Reboot Test

If you can answer these from the files, your state is recoverable after any context loss:

- Where am I? -> current phase in `task_plan.md`
- Where am I going? -> remaining phases
- What is the goal? -> goal statement in `task_plan.md`
- What have I learned? -> `findings.md`
- What have I done? -> `progress.md`

## Anti-Patterns

| Don't | Do instead |
| --- | --- |
| Use an ephemeral todo list for persistence | Write `task_plan.md` |
| State the goal once and forget | Re-read the plan before decisions |
| Hide errors and retry silently | Log them to the plan or progress file |
| Stuff everything into context | Store large content in files |
| Create planning files in the skill folder | Create them in the project root |

## KZ Integration

- Pair with `ralph-loop` for autonomous multi-iteration builds. The progress file is the shared memory.
- Pair with `spec-driven-development` so the plan's goal traces to an approved spec.
- Superpowers-first for workflow: `superpowers:writing-plans`, `superpowers:executing-plans`.

## Upstream Reference

Repository: https://github.com/OthmanAdi/planning-with-files

## Attribution

Adapted from `OthmanAdi/planning-with-files`, MIT License.
