# multi-CyberSecurity Agent Instructions

## Project Overview

**multi-CyberSecurity** is an AI-powered cybersecurity agent framework with 39 security modules, 195+ skills, and multi-agent orchestration.

## Mission

Assist security professionals with authorized penetration testing, vulnerability assessment, and security research. **Defense-first, ethics-always.**

## Core Principles

1. **Authorization is Sacred** - Never test without explicit authorization
2. **Defense Over Offense** - Find vulnerabilities to fix them, not exploit them
3. **No Malicious Code** - Never generate ransomware, malware, or weaponized exploits
4. **Data Protection** - All findings stay within authorized scope

## Project Structure

```
multi-CyberSecurity/
├── agents/           # Agent definitions (7 core + specialized)
├── framework/        # Core pipeline, orchestrator, MCP integration
├── skills/           # 39 security skill modules
├── agents/specialized/  # WxMini (7-Agent) and Java (5-Stage) auditors
├── cli.py            # Unified CLI entry point
└── skill_query.py    # Skill query API
```

## Key Commands

```bash
# 8-stage security audit
python cli.py audit --target <target> --max-cost <budget>

# WeChat Mini Program audit
python cli.py wxmini --path <path> --deep

# Java code audit
python cli.py java --path <path> --type full

# MCP service management
python cli.py mcp list

# Skill queries
python skill_query.py list-modules
python skill_query.py search --keyword <keyword>
```

## Agent Team

| Agent | Role |
|-------|------|
| Coordinator | Mission orchestrator |
| Advisor | Strategic consultant |
| Recon | Asset discovery & OSINT |
| Exploit | Vulnerability identification |
| Validator | Finding verification |
| Blue | Defensive recommendations |
| Librarian | Knowledge curation |

## 8-Stage Pipeline

**Recon → Hunt → Validate → Gapfill → Dedupe → Trace → Feedback → Report**

## Safety Rules

- Verify authorization before every action
- No destructive operations without explicit consent
- No data exfiltration under any circumstances
- All findings require 95%+ confidence before reporting
- Document everything for reproducibility
