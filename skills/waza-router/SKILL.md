---
name: waza-router
description: Use when selecting Waza-style engineering habit workflows for thinking, UI design, review, debugging, reading sources, writing prose, learning a domain, or auditing agent health.
---

# Waza Router

Use this skill to route work into Waza-style engineering habits. Waza is a MIT-licensed upstream skill pack by Tw93 that turns common engineering habits into skills.

This KZ skill is an adoption router, not a full copy of Waza. If Waza is installed in the current harness, invoke the matching upstream Waza skill. If it is not installed, use this routing table as a lightweight fallback and tell the user that full Waza is unavailable.

## Route By Situation

| Situation | Upstream Waza skill |
| --- | --- |
| New feature, architecture decision, plan, product judgment, "is this worth it" | `think` |
| Frontend UI, component, page, visual polish, screenshot aesthetic issue | `design` |
| Completed task, pre-merge review, release gate, project audit | `check` |
| Bug, regression, failed test, unexpected behavior, stale generated artifact | `hunt` |
| URL, web page, PDF, source ingestion | `read` |
| Writing, editing, release notes, launch copy, Chinese/English polish | `write` |
| Learning an unfamiliar domain and producing a synthesis | `learn` |
| Auditing Codex/Claude/project instruction health, verification drift, maintainability drift | `health` |

## Disambiguation

- UI decision goes to `design`; non-UI product or architecture judgment goes to `think`.
- Code already works and needs review goes to `check`; code is broken or behavior is wrong goes to `hunt`.
- A message containing a URL first goes to `read`; if the user wants a synthesized article or research output, follow with `learn`.
- Release notes prose goes to `write`; publishing, tagging, release assets, or issue follow-through goes to `check`.
- Agent harness configuration, ignored instructions, hook/MCP problems, context confusion, or verification drift goes to `health`.

## Fallback Behavior

If the upstream Waza skill is unavailable:

1. State which Waza skill would have applied.
2. Apply the corresponding KZ/Superpowers workflow when possible.
3. Keep work bounded to the selected habit.
4. Do not silently perform unrelated chained work. Stop at the natural handoff point.

## Install Reference

Upstream repository:

https://github.com/tw93/Waza

Typical install routes are documented upstream for Claude Code, Codex, Antigravity, OpenCode, Claude Desktop, and Pi.

## Attribution

Adapted from `tw93/Waza`, MIT License.

