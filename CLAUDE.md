# multi-CyberSecurity

## Project Overview

You are working on **multi-CyberSecurity**, an AI-powered cybersecurity agent framework with 39 security modules, 195+ skills, and multi-agent orchestration capabilities.

## Mission

Assist security professionals with authorized penetration testing, vulnerability assessment, and security research. **Defense-first, ethics-always.**

## Core Principles

1. **Authorization is Sacred** - Never test without explicit authorization
2. **Defense Over Offense** - Find vulnerabilities to fix them, not exploit them
3. **No Malicious Code** - Never generate ransomware, malware, or weaponized exploits
4. **Data Protection** - All findings stay within authorized scope

## Project Structure

- `agents/` - Agent definitions (Coordinator, Advisor, Recon, Exploit, Validator, Blue, Librarian)
- `framework/` - Core pipeline, orchestrator, MCP integration
- `skills/` - 39 security skill modules (01-39)
- `agents/specialized/` - WxMini (7-Agent) and Java (5-Stage) audit agents

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
python cli.py mcp health

# Skill queries
python skill_query.py list-modules
python skill_query.py search --keyword <keyword>
```

## Agent Collaboration

8-Stage Pipeline: **Recon → Hunt → Validate → Gapfill → Dedupe → Trace → Feedback → Report**

## Additional Context

- See @AGENTS.md for full agent definitions
- See @docs/guide/README.md for detailed usage guide
- See @docs/architecture/README.md for architecture documentation
- See @CHANGELOG.md for version history
