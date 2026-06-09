# 理念

KZ AI Coding SOP 的目标是让 AI Coding 变得可控、一致、可维护。

## 人定义规则

产品意图、工程约束、架构边界和验收标准由人负责。Agent 可以帮助发现实现细节，但不能静默替人做业务决策。

## Agent 遵守流程

AI Agent 真正可靠的时候，是在遵守明确流程的时候。KZ SOP 默认使用 Superpowers 作为规划、TDD、调试、验证和 Review 的工作流基线。

## 项目规则跟随项目

当团队需要共享同一套契约时，可以主动提交 Agent 规则；但 `kz-sop init` 默认会忽略这些文件，避免打扰已有仓库的提交范围。`AGENTS.md` 是主要 SOP 入口，`.kz/` 用来保存 KZ 的机器可读元数据。

## 验证优先于口头声明

Agent 必须说明实际验证了什么。没有跑测试就不能说测试通过。没有安装 Superpowers 时，也必须明确说明，并执行 KZ fallback 工作流。
