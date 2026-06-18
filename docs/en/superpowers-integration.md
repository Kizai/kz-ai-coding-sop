# Superpowers Integration

KZ SOP is Superpowers-first.

KZ SOP is Kizai's own project-level development process and governance layer. Superpowers is an upstream skill/workflow project that KZ SOP can route agents to when those skills are installed in the current agent harness.

KZ SOP provides repository-level rules, prompts, checklists, and fallback behavior. Superpowers provides reusable workflow skills. The two are intentionally separate.

KZ repository:

- https://github.com/Kizai/kz-ai-coding-sop

## Attribution

Superpowers is maintained by Jesse Vincent and Prime Radiant.

- Repository: https://github.com/obra/superpowers
- License: MIT

KZ SOP v0.1.x does not own, copy, bundle, modify, or claim authorship of Superpowers skills.

## Default Skill Routing

| Situation | Recommended Superpowers skill |
| --- | --- |
| Starting a session or checking skill applicability | `superpowers:using-superpowers` |
| New feature or behavior change | `superpowers:brainstorming` |
| Approved requirements | `superpowers:writing-plans` |
| Implementation | `superpowers:test-driven-development` |
| Bug, failed build, or unexpected behavior | `superpowers:systematic-debugging` |
| Completion verification | `superpowers:verification-before-completion` |
| Review | `superpowers:requesting-code-review` |
| Plan execution with subagents | `superpowers:subagent-driven-development` |
| Plan execution without subagents | `superpowers:executing-plans` |

## Future KZ Skills

KZ-owned skills should be added only when they are reusable across projects. They should follow the same quality bar as Superpowers skill writing: clear trigger conditions, anti-rationalization guidance, red flags, and verification scenarios.

## Supplemental Packaged Skills

KZ SOP includes a small curated set of supplemental packaged skills:

- `startup-pressure-test`
- `grill-me`
- `karpathy-guidelines`
- `spec-driven-development`
- `waza-router`
- `ecc-operator-system`
- `ralph-loop`
- `planning-with-files`

They supplement the SOP for startup validation, plan interrogation, LLM coding discipline, spec-driven contracts, Waza routing, ECC-style operator readiness, autonomous fresh-context loops, and persistent file-based planning. They do not replace Superpowers as the default engineering workflow.
