# Changelog

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

### 📁 New Directory Structure
```
CyberSecurity-Skills/
├── .trae/                    # NEW: Trae IDE configuration
├── agents/
│   └── specialized/          # NEW: Specialized audit agents
│       ├── wxmini/           # NEW: WeChat Mini Program agents
│       └── java/             # NEW: Java audit agents
├── framework/
│   ├── core/
│   │   └── pipeline.py       # NEW: 8-stage pipeline
│   ├── mcp/
│   │   ├── client.py         # NEW: MCP client
│   │   └── registry.json     # NEW: MCP service registry
│   └── stages/               # NEW: Stage definitions
├── skills/
│   └── catalog.json          # NEW: Skill catalog
└── cli.py                    # NEW: Enhanced CLI
```

### 🔗 Integration Sources
- [ECC](https://github.com/affaan-m/ECC) - Multi-platform IDE support patterns
- [audit](https://github.com/evilsocket/audit) - 8-stage pipeline architecture
- [wxmini-security-audit](https://github.com/sssmmmwww/wxmini-security-audit) - WeChat Mini Program audit
- [java-audit-skills](https://github.com/RuoJi6/java-audit-skills) - Java code audit pipeline
- [wmpf-mcp-bridge](https://github.com/an7ln/wmpf-mcp-bridge) - MCP service architecture

### 🛡️ Security Principles Maintained
- Pure static analysis (no network requests)
- No attack code generation
- Minimal privileges (read-only source, write-only output)
- Local processing only

### 📝 Documentation
- New README_v3.md with v3.0 features
- Architecture diagrams for 8-stage pipeline
- Agent orchestration documentation
- MCP service configuration guide

### 🐛 Bug Fixes
- Fixed unused yaml import in orchestrator.py
- Enhanced type hints throughout codebase
- Improved error handling in MCP client

### ⚠️ Breaking Changes
- New CLI structure (cli.py) replaces direct skill.py usage for new features
- skill.py maintained for backward compatibility
- New SQLite database schema (framework/state.db)

### 🔄 Migration Guide
1. Run `pip install -r requirements.txt` to install new dependencies
2. Initialize MCP servers using `python cli.py mcp list`
3. Use new CLI for v3.0 features: `python cli.py audit --target ...`
4. Existing skill.py workflows remain functional

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
