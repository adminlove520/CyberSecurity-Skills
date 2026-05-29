# Cursor Platform Configuration

## Directory Structure

```
.cursor/
├── AGENTS.md              # Agent definitions for Cursor IDE
├── mcp.json               # MCP server connections
└── rules/
    ├── security-rules.mdc # Security-first coding rules (always applied)
    └── code-audit.mdc     # Code audit workflow rules (Python files)
```

## Usage

These files are automatically loaded by Cursor IDE when working with this project.

- `AGENTS.md` - Defines all security agents and their roles
- `rules/*.mdc` - Coding rules with frontmatter metadata for auto-triggering
- `mcp.json` - MCP server connections for external tool integration

## Quick Start

```bash
# Run 8-stage security audit
python cli.py audit --target https://example.com --max-cost 50

# WeChat Mini Program audit
python cli.py wxmini --path /path/to/miniapp --deep

# Java code audit
python cli.py java --path /path/to/project --type full
```
