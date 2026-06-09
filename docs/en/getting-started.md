# Getting Started

KZ AI Coding SOP initializes a project with shared agent rules and Superpowers-first workflow routing.

## 1. Install

```bash
npx kz-sop init
```

or:

```bash
pnpm dlx kz-sop init
```

Python users can run:

```bash
pip install kz-ai-coding-sop
kz-sop init
```

## 2. Install Superpowers In Your Agent Harness

KZ SOP does not auto-install third-party plugins. Install Superpowers separately for Codex, Claude Code, Cursor, or any other supported harness you use.

Upstream: https://github.com/obra/superpowers

## 3. Keep Initialization Low-Noise

By default, `kz-sop init` adds the generated SOP files to `.gitignore`:

```txt
AGENTS.md
.kz/
```

If you want to make KZ SOP a shared team contract, remove those ignore entries intentionally and commit the files.

## 4. First Agent Prompt

```txt
Please follow KZ AI Coding SOP for this project.
First read AGENTS.md.
Do not write code immediately.
Start by reporting project understanding, stack detection, structure analysis, plan, relevant Superpowers skills, risks, and verification steps.
```
