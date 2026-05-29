# Changelog

## [3.3.0] - 2026-05-29

### 🚀 新增功能

#### Cursor IDE 支持
- 新增 `.cursor/` 配置目录
  - `AGENTS.md` - Cursor专用Agent定义
  - `rules/security-rules.mdc` - 安全规则（alwaysApply）
  - `rules/code-audit.mdc` - 代码审计规则（Python文件触发）
  - `mcp.json` - MCP服务器连接配置
  - `README.md` - 配置说明

#### Claude Code 支持
- 新增 `CLAUDE.md` - 项目级指令（根目录）
- 新增 `.claude/` 配置目录
  - `rules/framework-dev.md` - 框架开发规则（Python文件）
  - `rules/agent-definitions.md` - Agent定义标准（Markdown文件）
  - `agents/security-auditor.md` - 安全审计子代理
  - `settings.json` - 权限控制和Git Hooks
  - `README.md` - 配置说明

#### OpenAI Codex CLI 支持
- 新增 `AGENTS.md` - 项目级Agent指令（根目录）
- 新增 `.codex/` 配置目录
  - `config.toml` - MCP服务器、沙箱策略、项目配置
  - `README.md` - 配置说明

### 🔧 修复

#### 数据修复
- 修复 `index.json` 中模块 17-26 的重复数据（删除10个重复模块）
- 更新 `index.json` 版本从 2.2.0 到 3.2.0
- 更新 `index.json` schema URL 指向新仓库名
- 更新 `skills/catalog.json` 版本从 3.0.0 到 3.2.0
- 修复 README.md 版本徽章从 3.0.0 到 3.2.0

#### 名称统一
- 批量替换 21 个文件中的旧项目名 `CyberSecurity-Skills` → `multi-CyberSecurity`
- 涵盖配置文件、Python脚本、Agent定义、文档等

#### 架构图更新
- README架构图新增 `.cursor/`、`.claude/`、`.codex/` 三个平台配置
- 多平台支持状态全部更新为 ✅ 已支持

#### .gitignore 增强
- 新增 `.claude/settings.local.json` 排除
- 新增 `CLAUDE.local.md` 排除
- 新增 `.env` / `.env.local` 排除
- 新增 `*.db` / `*.sqlite` 排除

### 📁 新增文件

```
.cursor/
├── AGENTS.md
├── mcp.json
├── README.md
└── rules/
    ├── security-rules.mdc
    └── code-audit.mdc

.claude/
├── README.md
├── agents/
│   └── security-auditor.md
├── rules/
│   ├── framework-dev.md
│   └── agent-definitions.md
└── settings.json

.codex/
├── README.md
└── config.toml

CLAUDE.md              # Claude Code 项目指令
AGENTS.md              # Codex/Cursor 项目指令
```

---

## [3.2.0] - 2026-05-29

### 🏷️ 项目重命名

**项目名称从 `CyberSecurity-Skills` 正式更名为 `multi-CyberSecurity`**

#### 更新内容
- 更新了所有配置文件中的项目名称引用
  - `agent-manifest.json` - 项目元数据
  - `index.json` - 技能库索引
  - `README.md` - 完整文档
- 更新了GitHub仓库链接
- 更新了所有徽章和shields链接

#### 重命名原因
- 更好地反映项目多平台、多Agent、多技能集成的特点
- "multi" 代表：
  - **Multi-Platform**: 支持 Trae, Hermes, OpenClaw, Cursor, Claude, Codex
  - **Multi-Agent**: 7个核心智能体 + 专项审计Agent
  - **Multi-Skill**: 39个安全模块，195+技能
  - **Multi-Protocol**: MCP服务集集成

---

## [3.1.0] - 2026-05-29

### 🚀 新增功能

#### Hermes Agent 支持
- 新增 `.hermes/` 配置目录
- 包含 `instructions.md` - Hermes专用指令
- 包含 `rules.md` - 安全规则
- 包含 `identity.md` - Agent身份定义
- 完整的Hermes平台集成指南

#### OpenClaw IDE 支持
- 新增 `.openclaw/` 配置目录
- 包含 `AGENTS.md` - OpenClaw专用Agent定义
- 包含 `IDENTITY.md` - 项目身份定义
- 包含 `SOUL.md` - 项目哲学和价值观
- 包含 `RULES.md` - 完整安全规则集
- 详细的Agent协作协议

#### README 美化
- 完整的项目架构图
- 8阶段流水线可视化
- 专项审计能力展示
- MCP服务集表格
- 多平台支持状态表
- 统一的视觉风格和徽章

### 📁 新增文件

```
.hermes/
├── README.md           # Hermes配置说明
├── instructions.md     # Hermes指令
├── rules.md           # 安全规则
└── identity.md        # Agent身份

.openclaw/
├── README.md           # OpenClaw配置说明
├── AGENTS.md          # Agent定义
├── IDENTITY.md         # 项目身份
├── SOUL.md            # 项目哲学
└── RULES.md           # 完整规则集
```

### 🛠️ 改进

#### 目录结构优化
- 统一的平台配置目录
- 清晰的模块划分
- 完整的文档结构

#### 文档完善
- README完整重写
- 架构图清晰展示
- 快速开始指南

---

## [3.0.0] - 2026-05-29

### 🚀 Major Features

#### 8-Stage Security Audit Pipeline
- Implemented 8-stage vulnerability discovery pipeline inspired by Cloudflare Project Glasswing
- Stages: Recon → Hunt → Validate → Gapfill → Dedupe → Trace → Feedback → Report
- SQLite-based state management for runs, tasks, and findings
- Budget control with `--max-cost-usd` parameter
- Cost tracking per task and stage

#### MCP Service Integration
- New MCP (Model Context Protocol) client and registry system
- MCP Servers:
  - `wxmini-server`: WeChat Mini Program analysis (port 43827)
  - `java-server`: Java code auditing (port 8082)
  - `burp-bridge`: Burp Suite Professional integration (port 8090)
  - `kali-bridge`: Kali Linux tool execution (port 8081)

#### Specialized Audit Agents

**WeChat Mini Program Audit Agent**
- 7-Agent architecture: Decompiler, SecretScanner, EndpointMiner, CryptoAnalyzer, VulnAnalyzer, Reporter, CustomAnalyzer
- Double-layer architecture: Python scripts (100% coverage) + LLM analysis
- 4-way parallel analysis in Phase 2
- File size-based processing strategy
- Degradation strategy for Python unavailability

**Java Code Audit Agent**
- 5-stage pipeline: Info Gathering → Cross Analysis → Route Tracing → Deep Analysis → Quality Check
- Dynamic worker creation for route tracing
- 9 specialized skills: route-mapper, route-tracer, sql-audit, auth-audit, file-upload-audit, file-read-audit, xxe-audit, vuln-scanner, audit-pipeline
- Automatic CFR decompiler integration
- Quality check points after each stage

#### Enhanced CLI
- New unified CLI (`cli.py`) with subcommands:
  - `audit`: Run 8-stage security audit
  - `wxmini`: WeChat Mini Program audit
  - `java`: Java code audit
  - `mcp`: MCP server management
  - `skill`: Skill management
- Colorized output for better UX
- Progress tracking through 8 stages

#### Multi-Platform IDE Support
- Added `.trae/` configuration for Trae IDE
- Structure for `.cursor/`, `.claude/`, `.codex/` configurations
- Platform-specific agent definitions and rules

#### Skill Catalog System
- Centralized skill registry (`skills/catalog.json`)
- Skill dependencies and stage mapping
- MCP server associations
- Version tracking

### 🔧 Technical Improvements

#### Enhanced Orchestrator
- Full budget management (allocation, tracking, checking)
- Finding lifecycle management (validation, reachability)
- Mission summary statistics
- Improved markdown report generation

#### Pipeline Module
- Stage enum and task dataclasses
- SQLite schema for runs, tasks, findings
- Deduplication logic
- Report generation with severity breakdown

#### Quality and Cost Controls
- Per-task cost estimation and tracking
- Budget overrun protection
- Quality validation at each stage
- Reachability verification for findings

---

## [2.0.0] - 2026-05-23

### Features
- Multi-agent framework with 7 core agents
- 39 security skill modules
- Mission Control dashboard
- Self-evolution with Librarian agent
- MCP integration for Burp Suite and Kali Linux

---

## [1.0.0] - 2026-05-20

### Initial Release
- Basic skill library structure
- 20 security modules
- Agent system prompts
