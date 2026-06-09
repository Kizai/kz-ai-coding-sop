# 快速开始

KZ AI Coding SOP 用来给项目初始化统一的 Agent 规则，并默认路由到 Superpowers 工作流。

## 1. 初始化

```bash
npx kz-sop init
```

或者：

```bash
pnpm dlx kz-sop init
```

Python 用户可以执行：

```bash
pip install kz-ai-coding-sop
kz-sop init
```

## 2. 在 Agent 环境里安装 Superpowers

KZ SOP 不会自动安装第三方插件。你需要分别在 Codex、Claude Code、Cursor 或其他 Agent 环境里安装 Superpowers。

上游仓库：https://github.com/obra/superpowers

## 3. 保持初始化低噪音

默认情况下，`kz-sop init` 会把生成的 SOP 文件加入 `.gitignore`：

```txt
AGENTS.md
.kz/
```

如果你想把 KZ SOP 作为团队共享契约，再主动移除这些 ignore 规则并提交文件。

## 4. 第一次让 Agent 进入项目

```txt
Please follow KZ AI Coding SOP for this project.
First read AGENTS.md.
Do not write code immediately.
Start by reporting project understanding, stack detection, structure analysis, plan, relevant Superpowers skills, risks, and verification steps.
```
