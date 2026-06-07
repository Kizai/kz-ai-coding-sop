# Project Initialization

Run `kz-sop init` from the root of a project.

The command is non-destructive:

- It creates missing KZ SOP files.
- It skips files that already exist.
- It appends one KZ runtime block to `.gitignore`.
- It does not overwrite project code.
- It does not install Superpowers or any other third-party plugin.

## Generated Structure

```txt
AGENTS.md
CLAUDE.md
.ai/
  AGENT_ENTRY.md
  CORE_RULES.md
  CODING_STANDARD.md
  ARCHITECTURE_STANDARD.md
  WORKFLOW.md
  SKILL_INDEX.md
  REVIEW_CHECKLIST.md
.cursor/
  rules/
    kz-ai-rules.mdc
.kz/
  sop.config.json
```

## Doctor

Run:

```bash
kz-sop doctor
```

`doctor` checks whether required KZ files exist and reminds you to confirm Superpowers is installed in each agent harness.

