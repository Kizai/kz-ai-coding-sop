# Superpowers 集成

KZ SOP 是 Superpowers-first。

Superpowers 提供经过验证的 Agent 工作流技能。KZ SOP 提供项目级治理文件，用来告诉 Agent 什么时候、如何优先使用这些技能。

## Attribution

Superpowers 由 Jesse Vincent 和 Prime Radiant 维护。

- 仓库：https://github.com/obra/superpowers
- 许可证：MIT

KZ SOP v0.1.0 不复制、不内置、不修改 Superpowers skills。

## 默认 Skill 路由

| 场景 | 推荐 Superpowers skill |
| --- | --- |
| 会话开始或判断是否需要技能 | `superpowers:using-superpowers` |
| 新功能或行为变更 | `superpowers:brainstorming` |
| 已确认需求 | `superpowers:writing-plans` |
| 实现功能、修复或重构 | `superpowers:test-driven-development` |
| Bug、构建失败或异常行为 | `superpowers:systematic-debugging` |
| 完成前验证 | `superpowers:verification-before-completion` |
| Review | `superpowers:requesting-code-review` |
| 使用 subagent 执行计划 | `superpowers:subagent-driven-development` |
| 不使用 subagent 执行计划 | `superpowers:executing-plans` |

## 后续 KZ Skill

KZ 自有 Skill 只应该在跨项目可复用时加入。它们应该遵守和 Superpowers skill 写作相同的质量标准：清晰触发条件、反套路说明、红旗清单和验证场景。

## 补充内置 Skills

KZ SOP 现在包含一组精选 MIT 来源的补充 skills：

- `startup-pressure-test`
- `grill-me`
- `waza-router`
- `ecc-operator-system`

它们用于补充创业想法验证、方案拷问、Waza 路由和 ECC 风格的多 Agent 工具链审计，不替代 Superpowers 作为默认工程工作流。
