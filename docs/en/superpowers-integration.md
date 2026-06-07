# Superpowers Integration

KZ SOP is Superpowers-first.

Superpowers provides the validated agent workflow skills. KZ SOP provides project-level governance files that tell agents when and how to use those skills.

## Attribution

Superpowers is maintained by Jesse Vincent and Prime Radiant.

- Repository: https://github.com/obra/superpowers
- License: MIT

KZ SOP v0.1.0 does not copy, vendor, or modify Superpowers skills.

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

KZ SOP includes a small curated set of packaged skills from MIT-licensed sources:

- `startup-pressure-test`
- `grill-me`
- `waza-router`
- `ecc-operator-system`

They supplement the SOP for startup validation, plan interrogation, Waza routing, and ECC-style operator readiness. They do not replace Superpowers as the default engineering workflow.
