# KZ Review Checklist

Use this before marking work complete or asking for merge.

## Correctness

- The implementation matches the approved task or plan.
- Existing behavior is preserved unless the change explicitly requires otherwise.
- Edge cases and error paths are considered.
- Public APIs, schemas, and user-visible behavior are called out if changed.

## Quality

- The change is small enough to review.
- Names and boundaries are clear.
- No unrelated refactors are bundled.
- No unnecessary dependencies are added.
- Errors are not hidden or silently ignored.

## Tests and Verification

- Relevant tests were run.
- New or changed behavior has tests when practical.
- Failed or skipped tests are explained.
- Manual verification steps are provided when automated tests are missing.

## Superpowers

- The appropriate Superpowers skill was used when available.
- If Superpowers was unavailable, the fallback workflow was followed and disclosed.
- Completion claims are backed by actual verification.

