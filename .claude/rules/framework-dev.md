---
paths:
  - "framework/**/*.py"
---

# Framework Development Rules

## Security-First

1. All MCP connections must default to `127.0.0.1` only
2. Input validation is mandatory for all user-provided parameters
3. Error messages must never leak system information
4. All network operations must be logged and auditable

## Code Quality

1. Python code must pass pylint >= 8.0
2. Use type hints for all function signatures
3. Include docstrings for all public functions
4. Handle exceptions gracefully with proper logging

## Pipeline Development

1. Each stage must be independently testable
2. Stage transitions must validate data integrity
3. Budget checks must occur before each stage
4. State persistence via SQLite must be atomic
