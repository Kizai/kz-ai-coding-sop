# KZ Workflow

KZ SOP is Superpowers-first. Use upstream Superpowers skills when they are installed in the current agent harness.

## Standard Route

1. New idea, feature, or behavior change: use `superpowers:brainstorming`.
2. Approved design or requirements: use `superpowers:writing-plans`.
3. Implementation: use `superpowers:test-driven-development`.
4. Bug, failure, or unexpected behavior: use `superpowers:systematic-debugging`.
5. Before claiming completion: use `superpowers:verification-before-completion`.
6. Before merge or after substantial work: use `superpowers:requesting-code-review`.
7. Plan execution: prefer `superpowers:subagent-driven-development`; otherwise use `superpowers:executing-plans`.

## Supplemental KZ Skills

Use packaged KZ skills when the task matches their narrower trigger:

- Startup validation: `startup-pressure-test`.
- Plan interrogation: `grill-me`.
- Waza habit routing: `waza-router`.
- Cross-harness workflow audit: `ecc-operator-system`.

## Fallback When Superpowers Is Unavailable

If Superpowers is not installed:

1. Say that Superpowers is unavailable in this harness.
2. Do not skip planning.
3. Inspect files before making assumptions.
4. Ask only for product decisions that cannot be discovered from the repository.
5. Write a short implementation plan before editing.
6. Keep edits small and reversible.
7. Run relevant verification.
8. Summarize changes and unresolved risks.

## Prohibited Shortcuts

- Do not start coding before understanding the task.
- Do not fix bugs without root-cause investigation.
- Do not add tests only as a formality after implementation when TDD is expected.
- Do not mark work done without verification.
- Do not ignore review findings with Critical or Important severity.
