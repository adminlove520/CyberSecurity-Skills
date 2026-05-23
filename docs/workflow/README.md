# 🔄 协作逻辑 (Workflow Logic)

## 1. 渗透测试任务流 (Main Flow)

```mermaid
sequenceDiagram
    participant User
    participant Coord as Coordinator
    participant Recon as ReconAgent
    participant Advisor as AdvisorAgent
    participant Exploit as ExploitAgent
    
    User->>Coord: 启动任务
    Coord->>Coord: 初始化 MISSION_CONTROL
    Coord->>Recon: 执行资产发现 (T01)
    Recon-->>Coord: 发现潜在漏洞点 & 更新 Blackboard
    Coord->>Exploit: 执行漏洞利用 (T03)
    
    alt 利用失败
        Exploit->>Advisor: 请求策略建议
        Advisor->>Advisor: 分析失败日志 (Reflexion)
        Advisor-->>Exploit: 提供绕过 Payload
        Exploit->>Exploit: 重新尝试 (Max 3)
    end
    
    Exploit-->>Coord: 提交成功证据 (Handoff)
    Coord-->>User: 生成最终报告
```

## 2. 交接协议 (Handoff Protocol)
所有的 Agent 间转交必须使用 `framework/templates/HANDOFF_TEMPLATE.md`。这确保了：
1. **证据不丢失**：必须附带产出文件路径。
2. **上下文对齐**：必须包含已执行的操作与下一步建议。
