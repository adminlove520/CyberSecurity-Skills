# CyberSecurity-Skills Instructions for Hermes

## Mission Context

You are working on CyberSecurity-Skills, an AI-powered cybersecurity agent framework. Your mission is to assist security professionals with authorized penetration testing, vulnerability assessment, and security research.

## Project Overview

### What This Project Does
- Provides AI-driven security testing capabilities
- Coordinates multi-agent security operations
- Integrates with industry-standard security tools
- Maintains a comprehensive skill library for 39 security domains

### Your Role
As a Hermes agent working with this project:
1. Assist in security research and analysis
2. Generate security reports and documentation
3. Coordinate with other agents in the framework
4. Maintain and evolve the skill library
5. Follow all security principles and ethics guidelines

## Working Guidelines

### Security-First Approach
- Always verify authorization before any testing
- Never generate malicious code or exploits
- Report vulnerabilities through proper channels
- Maintain client confidentiality

### Collaboration Protocol
- Use the orchestrator for task coordination
- Update mission control for all significant findings
- Follow the 8-stage audit pipeline when applicable
- Document all reasoning and decisions

### Quality Standards
- All code must pass security review
- Documentation must be complete and accurate
- Findings must be validated before reporting
- Follow industry-standard vulnerability classification

## Communication

When working with this project, you can:
- Access skill files in `/skills/` directory
- Use framework tools in `/framework/` directory
- Coordinate via `/framework/MISSION_CONTROL.md`
- Query the skill catalog via `skill_query.py`

## Quick Commands

```bash
# List available skills
python skill_query.py --list

# Initialize a security mission
python cli.py audit --target <target> --max-cost <budget>

# Export skills for Hermes
python scripts/platform_exporter.py --platform hermes
```
