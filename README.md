# kz-ai-coding-sop

Kizai's controlled AI Coding SOP for agent-based software development.

中文定位：Kizai 的可控式 AI Coding 标准作业流程。

Controlled AI coding means the human defines the rules, the agent follows the workflow, and every change stays understandable, reviewable, and verifiable.

## What This Is

KZ AI Coding SOP is a project governance overlay for AI coding agents. It initializes a project with shared instructions for Codex, Claude Code, Cursor, Antigravity, OpenClaw, and similar agents.

It is Superpowers-first: KZ SOP does not duplicate or vendor the Superpowers workflow skills. Instead, it routes agents toward the proven Superpowers skills when they are available, and keeps KZ-specific project rules in the repository.

Superpowers is maintained by Jesse Vincent and Prime Radiant:

- Repository: https://github.com/obra/superpowers
- License: MIT
- Public validation: 220k+ GitHub stars at the time KZ SOP v0.1 was planned

## Current Status

This repository is ready for a first npm/PyPI release, but the public install commands only work after you publish the packages:

- npm package: `kz-sop`
- PyPI package: `kz-ai-coding-sop`
- CLI command: `kz-sop`

Before publishing, use the local development commands below.

## Quick Start After Publishing

Use npm or pnpm:

```bash
npx kz-sop init
pnpm dlx kz-sop init
```

Or use Python:

```bash
pip install kz-ai-coding-sop
kz-sop init
```

This initializes the current project with KZ SOP files.

## Local Usage Before Publishing

Python can be tested immediately from this repository:

```bash
cd kz-ai-coding-sop
python3 -m kz_sop.cli skills list
python3 -m kz_sop.cli init
python3 -m kz_sop.cli doctor
```

To install the local Python package into your environment:

```bash
cd kz-ai-coding-sop
python3 -m pip install .
kz-sop init
```

For npm, install Node.js first, then run:

```bash
cd kz-ai-coding-sop
npm install
npm run build
node dist/cli.js init
```

You can also test the package before publishing:

```bash
npm pack
```

## Commands

```bash
kz-sop init
kz-sop update
kz-sop doctor
kz-sop skills list
```

- `init` generates KZ SOP files without overwriting existing files.
- `update` is a safe non-overwriting sync in v0.1.0.
- `doctor` checks required KZ files and reminds you to confirm Superpowers is installed in your agent harness.
- `skills list` lists recommended upstream Superpowers skills and any packaged KZ-owned skills.

## Typical Project Setup

In a new project:

```bash
mkdir my-project
cd my-project
git init
npx kz-sop init
```

or:

```bash
mkdir my-project
cd my-project
git init
pip install kz-ai-coding-sop
kz-sop init
```

Then commit the SOP files:

```bash
git add AGENTS.md CLAUDE.md .ai .cursor .kz .gitignore
git commit -m "chore: initialize KZ AI Coding SOP"
```

Superpowers should be installed separately in each agent harness you use. KZ SOP does not auto-install third-party plugins.

## Packaged Skills

KZ SOP v0.1.0 includes a small curated set of packaged skills:

- `startup-pressure-test`: pressure-test startup ideas before building.
- `grill-me`: stress-test a plan or design through focused questioning.
- `waza-router`: route work to Waza-style engineering habits.
- `ecc-operator-system`: audit cross-harness AI agent workflow readiness.

These extend KZ SOP without changing the default Superpowers-first workflow. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for attribution.

## Generated Files

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
.gitignore
```

The `.gitignore` update only adds local runtime paths:

```gitignore
# KZ AI Coding SOP local runtime files
.ai/cache/
.ai/tmp/
.ai/logs/
.ai/session/
.kz/cache/
.kz/tmp/
```

## Recommended First Prompt

```txt
Please follow KZ AI Coding SOP for this project.
First read AGENTS.md and .ai/AGENT_ENTRY.md.
Do not write code immediately.
Start by reporting project understanding, stack detection, structure analysis, plan, relevant Superpowers skills, risks, and verification steps.
```

## Release Checklist

Before publishing npm:

```bash
npm install
npm run build
npm publish
```

Before publishing PyPI:

```bash
python3 -m pip install build twine
python3 -m build
python3 -m twine upload dist/*
```

Recommended pre-release verification:

```bash
python3 -m compileall kz_sop
python3 -m pip wheel . --no-deps -w /tmp/kz-sop-wheel
```

## Philosophy

AI is not a free-form developer. It is an engineering worker that must follow project rules, load the right workflow skills, preserve architecture, verify results, and explain its changes.

KZ SOP owns project governance. Superpowers owns the default agent workflow.

## Documentation

- [English getting started](docs/en/getting-started.md)
- [English philosophy](docs/en/philosophy.md)
- [English project init](docs/en/project-init.md)
- [English Superpowers integration](docs/en/superpowers-integration.md)
- [English curated skills](docs/en/curated-skills.md)
- [中文快速开始](docs/zh-CN/getting-started.md)
- [中文理念](docs/zh-CN/philosophy.md)
- [中文项目初始化](docs/zh-CN/project-init.md)
- [中文 Superpowers 集成](docs/zh-CN/superpowers-integration.md)
- [中文精选 Skills](docs/zh-CN/curated-skills.md)
