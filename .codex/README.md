# Codex CLI Platform Configuration

## Directory Structure

```
AGENTS.md                # Project-level agent instructions (root directory)
.codex/
└── config.toml          # Codex project configuration
```

## Usage

Codex CLI automatically loads `AGENTS.md` and `.codex/config.toml` when working with this project.

- `AGENTS.md` - Core agent instructions and project overview
- `.codex/config.toml` - MCP server connections, sandbox policy, and project settings

## Configuration Details

### config.toml
- **MCP Servers**: wxmini-server, java-server, burp-bridge, kali-bridge
- **Sandbox**: `read-only` by default (security-first approach)
- **Fallback Files**: Also recognizes `CLAUDE.md` and `GEMINI.md` for cross-platform compatibility

### AGENTS.md
- Contains full agent team definitions
- 8-stage pipeline overview
- Key CLI commands
- Safety rules and principles

## Notes

- Codex uses `AGENTS.md` as the primary instruction file
- `config.toml` is only loaded for trusted projects
- Rule chain has a 32 KiB size limit
- Sandbox defaults to read-only for security
