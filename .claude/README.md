# Claude Code Platform Configuration

## Directory Structure

```
.claude/
├── rules/
│   ├── framework-dev.md    # Framework development rules (Python files)
│   └── agent-definitions.md # Agent definition standards (Markdown files)
├── agents/
│   └── security-auditor.md # Sub-agent definition for security audits
└── settings.json           # Project permissions and hooks

CLAUDE.md                   # Project-level instructions (root directory)
```

## Usage

Claude Code automatically loads `CLAUDE.md` and `.claude/` configurations when working with this project.

- `CLAUDE.md` - Core project instructions and quick commands
- `rules/*.md` - Path-scoped rules with YAML frontmatter
- `agents/*.md` - Sub-agent definitions for specialized tasks
- `settings.json` - Permission controls and git hooks

## Notes

- `CLAUDE.md` imports `@AGENTS.md` for full agent definitions
- Rules use `paths` frontmatter to auto-trigger on matching files
- Settings restrict dangerous operations while allowing development workflow
