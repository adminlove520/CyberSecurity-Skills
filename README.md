# 🔒 CyberSecurity-Skills v2.0 (Agentic Edition)

> **从静态知识库演进为自主渗透测试框架** — 基于多智能体协作、自主进化与实战工具集成的网络安全大模型技能库。

[![Version](https://img.shields.io/badge/version-2.0.0--beta-red.svg)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 🌟 核心特性

- **🤖 多专家协作 (Multi-Agent Team)**: 内置 Coordinator, Advisor, Recon, Exploit, Validator 等 7 个专家角色，实现全流程渗透测试自动化。
- **🧠 自主进化 (Self-Evolution)**: 引入 Librarian 角色，自动将任务经验沉淀为可复用的 .md 技能，实现“在实战中学习”。
- **🕹️ 任务控制台 (Mission Control)**: 采用 Blackboard 架构同步全局状态，通过 `MISSION_CONTROL.md` 实时监控任务进度与发现。
- **🔌 深度集成 (Tool Integration)**: 支持通过 MCP 协议直接控制 Burp Suite 与 Kali Linux (WSL/SSH)。
- **🛡️ 防御加固 (Blue Team)**: 新增蓝队专家 Agent，提供针对性的修复建议与系统加固方案。
- **🚀 AI IDE 原生支持**: 完美适配 Trae, Cursor, OpenClaw, Hermes 等 AI 开发与 Agent 平台。

## 📁 目录结构

```bash
CyberSecurity-Skills/
├── agents/             # 🤖 专家 Agent 系统提示词
├── framework/          # ⚙️ 核心框架 (Orchestrator, MCP, Memory)
│   ├── core/           # 任务编排与报告引擎
│   ├── mcp/            # Burp/Kali 插件集成
│   └── memory/         # 长期记忆与经验沉淀
├── playground/         # 🧪 Docker 演练靶场 (Juice Shop/DVWA)
├── scripts/            # 🛠️ 自动化工具 (Linter, Graph Builder)
├── skills/             # 📚 核心技能库 (39个模块)
└── skill.py            # 统一管理 CLI
```

## 🛠️ 快速开始

### 1. 初始化任务
使用统一 CLI 初始化一个渗透测试任务：
```bash
python skill.py mission-init --name "Web-Audit-01" --target "http://example.com"
```

### 2. 多平台集成
同步规则到您的 AI IDE（如 Trae）：
```bash
python skill.py export
```

### 3. 开启自主进化
任务完成后，沉淀实战经验：
```bash
python skill.py evolve
```

## 📚 详细文档

请参阅 [docs/README.md](docs/README.md) 获取以下详细指南：
- [用户指南 (User Guide)](docs/guide/README.md)
- [Agent 协作协议 (Orchestration)](framework/COMMUNICATION.md)
- [法律与伦理守则 (Safety)](framework/SAFETY.md)

## 🤝 参考项目
本项目深度集成了以下优秀开源项目的理念与能力：
- [pen-agents](https://github.com/lzy756/pen-agents)
- [HackerTeam](https://github.com/lfz97/HackerTeam)
- [agency-agents](https://github.com/msitarzewski/agency-agents)
- [SecSkills](https://github.com/DaoYiSec/SecSkills)

---
**免责声明**: 本项目仅供安全研究与教育使用，请在授权范围内操作。
