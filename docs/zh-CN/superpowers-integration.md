# Superpowers 集成

KZ SOP 是 Superpowers-first。

KZ SOP 是 Kizai 自己的项目级开发流程和治理层。Superpowers 是上游 skill/workflow 项目；当当前 Agent 环境已经安装这些 skills 时，KZ SOP 可以把 Agent 路由到对应工作流。

KZ SOP 提供仓库级规则、提示词、检查清单和 fallback 行为。Superpowers 提供可复用的工作流 skills。两者有意保持独立。

KZ 仓库：

- https://github.com/Kizai/kz-ai-coding-sop

## Attribution

Superpowers 由 Jesse Vincent 和 Prime Radiant 维护。

- 仓库：https://github.com/obra/superpowers
- 许可证：MIT

KZ SOP v0.1.x 不拥有、不复制、不内置、不修改，也不声称作者身份属于 Superpowers skills。

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

KZ SOP 现在包含一组精选补充 skills：

- `startup-pressure-test`
- `grill-me`
- `karpathy-guidelines`
- `waza-router`
- `ecc-operator-system`

它们用于补充创业想法验证、方案拷问、LLM Coding 纪律、Waza 路由和 ECC 风格的多 Agent 工具链审计，不替代 Superpowers 作为默认工程工作流。
