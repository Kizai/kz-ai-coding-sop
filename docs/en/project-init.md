# Project Initialization

Run `kz-sop init` from the root of a project.

The command is non-destructive:

- It creates missing KZ SOP files.
- It skips files that already exist.
- It appends one KZ generated-files block to `.gitignore`.
- It does not overwrite project code.
- It does not install Superpowers or any other third-party plugin.

## Generated Structure

```txt
AGENTS.md
.kz/
  sop.config.json
```

By default, the generated files are ignored to avoid changing the user's normal commit surface:

```gitignore
# KZ AI Coding SOP generated files
.kz/
AGENTS.md
```

## Doctor

Run:

```bash
kz-sop doctor
```

`doctor` checks whether required KZ files exist and reminds you to confirm Superpowers is installed in each agent harness.
