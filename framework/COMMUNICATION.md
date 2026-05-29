# 🤝 Agent 协作与交接协议 (Communication Protocol)

为了确保多 Agent 协作时不丢失上下文，所有 Agent 之间的信息传递必须遵循以下协议。

## 1. 核心原则
- **证据导向**：任何结论必须附带工具输出或截图路径。
- **状态同步**：所有任务状态必须同步至 `MISSION_CONTROL.md`。
- **结构化交接**：使用标准 [HANDOFF_TEMPLATE.md](HANDOFF_TEMPLATE.md) 进行工作转交。

## 2. 协作角色 (Role Play)
- **Coordinator (总控)**：负责拆解任务、初始化 Mission、决策推进或重试。
- **Worker (执行者)**：如 ReconAgent, ExploitAgent，负责执行具体技能并产生证据。
- **Reviewer (审计者)**：负责验证 Worker 的输出是否符合验收标准。

## 4. 漏洞验证协议 (Vulnerability Validation Protocol)
所有发现的漏洞必须通过以下验证流程：
1.  **证据获取**：使用 MCP (Burp/Kali) 抓取漏洞触发的 Request/Response。
2.  **PoC 生成**：基于 `multi-CyberSecurity` 的模块 03 编写最小化验证脚本。
3.  **结果分类**：
    - `Verified`: 漏洞确实存在，且有证据支持。
    - `False Positive`: 验证失败，标注误报原因。
    - `Blocked`: 因安全边界或法律限制无法验证。

## 5. 自我修正与反思循环 (Self-Correction & Reflexion)
为了提高任务成功率，引入以下循环：
1.  **执行 (Execution)**：Worker Agent 执行任务并返回结果。
2.  **反思 (Reflexion)**：若任务失败或结果不理想，`Coordinator` 触发反思。
3.  **咨询 (Consultation)**：`Coordinator` 将失败上下文发送给 `Advisor`。
4.  **调整 (Adjustment)**：`Advisor` 提供优化后的策略或 Payload。
5.  **重试 (Retry)**：Worker Agent 携带新策略重新执行。
- *限制*：单个原子任务最多重试 3 次。
