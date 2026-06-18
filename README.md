# kz-ai-coding-sop

Kizai's own AI Coding SOP for controlled, agent-based software development.

中文定位：Kizai 的可控式 AI Coding 标准作业流程。

Controlled AI coding means the human defines the rules, the agent follows the workflow, and every change stays understandable, reviewable, and verifiable.

## What This Is

KZ AI Coding SOP is Kizai's project-level SOP and governance toolkit for AI coding agents. Its repository is:

- KZ repository: https://github.com/Kizai/kz-ai-coding-sop

It initializes a project with shared instructions for Codex, Claude Code, Cursor, Antigravity, OpenClaw, and similar agents.

KZ SOP uses a Superpowers-first workflow: when Superpowers skills are available in the current agent harness, KZ SOP routes agents to those skills as the workflow baseline. KZ SOP does not own, copy, bundle, modify, or claim authorship of Superpowers.

Superpowers is an upstream skill/workflow project maintained by Jesse Vincent and Prime Radiant:

- Repository: https://github.com/obra/superpowers
- License: MIT

In short: KZ SOP is Kizai's own development process and repository-level rules; Superpowers is an upstream skill capability that KZ SOP can reference and route to when installed.

## Package Status

KZ SOP is distributed through npm and PyPI:

- npm package: `kz-sop`
- PyPI package: `kz-ai-coding-sop`
- CLI command: `kz-sop`

Public install commands work for versions already published on the corresponding package registry. For local development or pre-release verification, use the local commands below.

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
- `update` refreshes the KZ-owned generated files (`AGENTS.md`, `.kz/sop.config.json`) to the packaged version and prints which files changed. Re-run it after upgrading the package to pull the latest SOP. Local edits to those two files are overwritten, so keep project-specific notes elsewhere; everything else is left untouched.
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

By default, `kz-sop init` keeps the generated SOP files local and low-noise by adding them to `.gitignore`:

```gitignore
# KZ AI Coding SOP generated files
.kz/
AGENTS.md
```

If you want to make KZ SOP a shared team contract, remove those ignore entries intentionally and commit the files.

Superpowers should be installed separately in each agent harness you use. KZ SOP does not auto-install third-party plugins.

## Packaged Skills

KZ SOP v0.1.x includes a small curated set of packaged skills:

- `startup-pressure-test`: pressure-test startup ideas before building.
- `grill-me`: stress-test a plan or design through focused questioning.
- `karpathy-guidelines`: reduce common LLM coding mistakes while writing, reviewing, or refactoring code.
- `spec-driven-development`: lock a verifiable spec and acceptance contract before writing code.
- `waza-router`: route work to Waza-style engineering habits.
- `ecc-operator-system`: audit cross-harness AI agent workflow readiness.
- `ralph-loop`: run an autonomous fresh-context iteration loop for work larger than one context window.
- `planning-with-files`: keep a long task on disk so it survives context loss, compaction, or `/clear`.

These extend KZ SOP without changing the default Superpowers-first workflow. Attribution for adapted upstream material is listed in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Generated Files

```txt
AGENTS.md
.kz/
  sop.config.json
.gitignore
```

The `.gitignore` update only adds generated SOP paths:

```gitignore
# KZ AI Coding SOP generated files
.kz/
AGENTS.md
```

## Recommended First Prompt

```txt
Please follow KZ AI Coding SOP for this project.
First read AGENTS.md.
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
