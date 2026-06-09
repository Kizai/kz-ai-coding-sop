# 项目初始化

在项目根目录执行：

```bash
kz-sop init
```

这个命令是非破坏性的：

- 只创建缺失的 KZ SOP 文件。
- 已存在的文件会跳过。
- 只向 `.gitignore` 追加一次 KZ 生成文件规则。
- 不覆盖业务代码。
- 不自动安装 Superpowers 或其他第三方插件。

## 生成结构

```txt
AGENTS.md
.kz/
  sop.config.json
```

默认会忽略生成文件，避免影响用户原有提交范围：

```gitignore
# KZ AI Coding SOP generated files
.kz/
AGENTS.md
```

## Doctor

执行：

```bash
kz-sop doctor
```

`doctor` 会检查必需的 KZ 文件是否存在，并提醒你确认每个 Agent 环境都已经安装 Superpowers。
