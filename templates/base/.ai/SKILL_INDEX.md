# KZ Skill Index

This project uses KZ AI Coding SOP with Superpowers-first workflow routing.

Do not load long skill content unless the task needs it. Use this file as an index.

## Upstream Superpowers Skills

Install and use Superpowers from:

https://github.com/obra/superpowers

Recommended routing:

| Situation | Skill |
| --- | --- |
| Starting a session or checking whether skills apply | `superpowers:using-superpowers` |
| New feature, behavior change, or creative implementation | `superpowers:brainstorming` |
| Turning approved requirements into executable work | `superpowers:writing-plans` |
| Implementing feature, bug fix, refactor, or behavior change | `superpowers:test-driven-development` |
| Bug, failed test, build error, or unexpected behavior | `superpowers:systematic-debugging` |
| Completing work and validating claims | `superpowers:verification-before-completion` |
| Reviewing completed work before merge or after a major task | `superpowers:requesting-code-review` |
| Executing a plan with subagents | `superpowers:subagent-driven-development` |
| Executing a plan without subagents | `superpowers:executing-plans` |

## KZ-Owned Skills

KZ SOP packages a small curated set of supplemental skills. They are not copied into business projects by default; use `kz-sop skills list` to see what the package contains.

| Situation | Skill |
| --- | --- |
| Pressure-testing a startup idea before building | `startup-pressure-test` |
| Stress-testing a plan or design with focused questions | `grill-me` |
| Routing to Waza-style engineering habit workflows | `waza-router` |
| Auditing cross-harness agent workflow readiness | `ecc-operator-system` |

Future KZ-owned skills should follow the same discipline as Superpowers `writing-skills`: clear trigger conditions, red flags, anti-rationalization guidance, and verification scenarios.
