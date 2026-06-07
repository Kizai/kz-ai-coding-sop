# KZ Coding Standard

## Style

- Follow the existing formatter, linter, naming conventions, and project layout.
- Use clear and descriptive names.
- Avoid vague names like `data`, `info`, `temp`, and `handleThing`.
- Prefer explicit types when the language supports them.
- Keep functions focused on one responsibility.
- Avoid duplicated logic.
- Use comments to explain why, not what.

## Dependencies

- Do not add production dependencies unless they are necessary.
- Explain the reason, scope, and risk of any new dependency.
- Prefer existing project utilities and standard libraries.

## Error Handling

- Do not swallow errors.
- Do not replace real failures with silent fallback behavior.
- Preserve useful error messages and stack traces where possible.
- Add validation at boundaries where invalid input can enter.

## Tests

- Prefer test-first work for features, bug fixes, and behavior changes.
- If Superpowers is available, use `superpowers:test-driven-development`.
- If tests cannot be added, explain why and provide manual verification steps.

