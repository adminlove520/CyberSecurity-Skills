# Trae Rules for CyberSecurity-Skills

## Security-First Development
1. Never generate actual exploit code that could be used maliciously
2. All PoC code must include safety checks and authorization requirements
3. Tool integrations must validate inputs and sanitize outputs
4. MCP servers must enforce local-only access (127.0.0.1)

## Code Quality
1. All Python code must pass pylint with score >= 8.0
2. All markdown must pass markdownlint
3. JSON/JSONC files must be valid
4. Skills must include proper frontmatter

## Documentation
1. Every skill must have a README.md
2. Every agent must have a system prompt document
3. All public APIs must be documented
4. Examples must be provided for complex features

## Testing
1. New skills must include test cases
2. MCP tools must have integration tests
3. Pipeline stages must be validated
4. Cost estimation must be accurate
