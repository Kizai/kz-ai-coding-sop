# Changelog

## 0.1.2

- Reduced default `kz-sop init` output to two core SOP files: `AGENTS.md` and `.kz/sop.config.json`.
- Stopped generating `.cursor/`, `.ai/`, and `CLAUDE.md` files by default.
- Merged the split SOP guidance into the generated `AGENTS.md` entrypoint.
- Minimized the `.gitignore` runtime block to `.kz/cache/` and `.kz/tmp/`.
- Updated `doctor` and generated config metadata for the two-file core mode.

## 0.1.1

- Clarified that KZ AI Coding SOP is Kizai's own project-level SOP and repository.
- Clarified that Superpowers is an upstream skill/workflow project used as an optional workflow baseline when installed.
- Removed ambiguous ownership wording and public-star-count language from the README.
- Fixed npm release metadata and build script for reliable publishing.

## 0.1.0

- Initial Superpowers-first KZ AI Coding SOP overlay.
- Added `kz-sop init`, `kz-sop update`, `kz-sop doctor`, and `kz-sop skills list`.
- Added Node and Python package metadata.
- Added base templates for multi-agent project initialization.
