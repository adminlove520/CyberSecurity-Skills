# 🕹️ 任务控制台 (Mission Control)

> 本文件是整个渗透测试任务的“单一真理来源 (SSOT)”。

## 1. 任务概览
- **项目名称**: [Project Name]
- **目标**: [Target URL/IP/Scope]
- **当前阶段**: [Recon / Scan / Exploit / Post / Reporting]
- **总控 Agent**: Coordinator

## 2. 任务看板 (Kanban)

| ID | 任务描述 | 负责人 | 状态 | 依赖 | 交付物 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| T01 | 被动信息搜集 | Recon | Pending | - | recon_passive.json |
| T02 | 子域名枚举 | Recon | Pending | T01 | subdomains.txt |
| T03 | 漏洞扫描 | Recon | Pending | T02 | vulns.json |
| T04 | 关键漏洞利用 | Exploit | Pending | T03 | exploit_report.md |

## 3. 知识共享区 (Blackboard)
> 记录所有 Agent 共享的关键变量（如发现的内部 IP、凭证等）。

- `TARGET_DOMAIN`: 
- `IDENTIFIED_SERVICES`: 
- `CREDENTIALS`: 

## 4. 专家建议区 (Advisor Insights)
> 记录 Advisor 提供的策略调整建议。

- [Timestamp] Advisor: 

## 5. 协作日志 (Log)
- [Timestamp] Coordinator: Mission initialized.
