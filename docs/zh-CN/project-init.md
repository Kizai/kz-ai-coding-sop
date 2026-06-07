# 项目初始化

在项目根目录执行：

```bash
kz-sop init
```

这个命令是非破坏性的：

- 只创建缺失的 KZ SOP 文件。
- 已存在的文件会跳过。
- 只向 `.gitignore` 追加一次 KZ 本地运行目录。
- 不覆盖业务代码。
- 不自动安装 Superpowers 或其他第三方插件。

## 生成结构

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

执行：

```bash
kz-sop doctor
```

`doctor` 会检查必需的 KZ 文件是否存在，并提醒你确认每个 Agent 环境都已经安装 Superpowers。

