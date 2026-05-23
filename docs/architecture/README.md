# 🏗️ 系统架构 (Architecture)

## 1. 整体架构图 (System Architecture)

```mermaid
graph TD
    User((User)) -->|Commands/Tasks| Coordinator[Coordinator Agent]
    Coordinator -->|Delegates| Recon[ReconAgent]
    Coordinator -->|Delegates| Exploit[ExploitAgent]
    Coordinator -->|Strategic Advice| Advisor[AdvisorAgent]
    
    subgraph "Execution Layer (MCP)"
        Recon -->|Burp API| Burp[Burp Suite]
        Recon -->|SSH/WSL| Kali[Kali Linux]
        Exploit -->|Exploit Scripts| Kali
    end

    subgraph "Knowledge & Memory"
        Recon -.->|Query| Skills[(Skill Library)]
        Exploit -.->|Query| Skills
        Librarian[LibrarianAgent] -->|Distill| Skills
        Librarian -.->|Review Logs| MissionLogs[(Mission Logs)]
    end

    subgraph "Feedback Loop"
        Exploit -->|Failures| Advisor
        Advisor -->|Bypass Strategies| Exploit
    end
```

## 2. 核心组件说明
- **Orchestration Core**: 基于 Python 的调度引擎，管理任务状态与 Agent 通讯。
- **Skill Library**: 195+ 结构化安全技能，支持 RAG 语义搜索。
- **MCP Connectors**: 标准化接口，用于控制外部安全工具（BurpSuite REST API, Kali SSH）。
- **Learning Engine**: 自动提取实战经验并沉淀为技能的闭环系统。
