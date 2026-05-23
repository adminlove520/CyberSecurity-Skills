# 🧠 长期记忆与经验库 (Long-term Memory & Experience)

本目录存储跨会话的持久化知识，Agent 在启动新任务前应优先检索此库。

## 1. 全局知识 (GLOBAL_KNOWLEDGE.md)
存储通用的渗透测试发现，如：
- **常用默认凭证**：从成功爆破中积累。
- **特定环境绕过模式**：如某版本 WAF 的通用绕过 Payload。
- **受信任的资产清单**。

## 2. 任务历史 (missions/)
存储以往任务的 `MISSION_CONTROL.md` 归档。Agent 可通过搜索过往对话和日志，了解类似目标的攻击路径。

## 3. 成功模式 (patterns/)
存储结构化的“攻击模板”。例如，如果一次对 SpringBoot 的审计非常成功，其步骤将被提取为 `pattern-springboot-audit.yaml`。
