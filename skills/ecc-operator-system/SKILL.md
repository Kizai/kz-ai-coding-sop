---
name: ecc-operator-system
description: Use when designing or auditing cross-harness AI agent workflows, Codex/Claude/Cursor/OpenCode setup, agent skill catalogs, operator readiness, security guardrails, memory/learning loops, or verification gates.
---

# ECC Operator System

Use this skill when KZ SOP needs ECC-style operator thinking: cross-harness compatibility, instruction surfaces, security posture, verification gates, memory/learning loops, and agent workflow reliability.

ECC is a MIT-licensed upstream operator system by Affaan Mustafa. It is a large system with hundreds of skills and config assets. This KZ skill is a concise adoption layer, not a full copy of ECC.

## When To Use

- Setting up or reviewing Codex, Claude Code, Cursor, OpenCode, Gemini, GitHub Copilot, or multi-harness project support.
- Designing `AGENTS.md`, `.cursor/rules`, `.codex/config.toml`, `.opencode`, `.github/copilot-instructions.md`, or equivalent instruction surfaces.
- Auditing whether an agent workflow is production-ready.
- Adding security gates, sandbox expectations, prompt-injection awareness, or secret-handling rules.
- Designing persistent memory, learning loops, or project instinct extraction.
- Deciding whether a workflow needs hooks, skills, commands, agents, MCPs, or plain instructions.

## Operator Checklist

Before changing an agent workflow, answer:

- Which harnesses must support this behavior?
- Which instruction file or plugin surface does each harness actually read?
- Which parts are enforceable by tooling, and which are only instructions?
- What verification proves the agent followed the workflow?
- What secrets, local paths, private data, or machine-specific config must stay out of the repo?
- What should happen when a harness lacks hooks, subagents, MCPs, or skill auto-routing?
- Is this project-specific governance or a reusable skill?

## Routing Heuristics

| Need | Prefer |
| --- | --- |
| Cross-harness universal rule | `AGENTS.md` or project-level instruction file |
| Harness-specific behavior | harness-native config or plugin |
| Reusable judgment workflow | `SKILL.md` |
| Deterministic validation | script, test, CI, or hook |
| Security invariant | tooling gate first, instruction fallback second |
| Long-lived project context | committed docs plus explicit refresh/verification |

## KZ SOP Integration

Use ECC thinking to strengthen KZ SOP in these places:

- `doctor`: detect missing files and warn about manual upstream installs.
- `.ai/SKILL_INDEX.md`: route skills without loading long docs by default.
- `.ai/WORKFLOW.md`: declare fallback behavior when a harness lacks an upstream plugin.
- `.kz/sop.config.json`: keep machine-specific and secret data out of committed config.
- Future skills: separate reusable skills from project-only rules.

## Red Flags

- Assuming all harnesses read the same files.
- Treating hook-based enforcement as available in Codex when it is not.
- Copying private machine paths, tokens, certificate names, or local secrets into public docs.
- Adding many always-on instructions that consume context but do not improve behavior.
- Creating a skill for deterministic checks that should be a script or CI test.
- Installing a large skill pack without knowing which workflows will actually be used.

## Upstream Reference

Repository:

https://github.com/affaan-m/ECC

Use the upstream project for full ECC installation, command catalogs, security guidance, and harness-specific assets.

## Attribution

Adapted from `affaan-m/ECC`, MIT License.

