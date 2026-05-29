---
paths:
  - "agents/**/*.md"
---

# Agent Definition Rules

## Structure

Every agent definition must include:
1. **Role** - Clear one-line description
2. **Mission** - Primary objective
3. **Responsibilities** - Numbered list of duties
4. **Tools** - Available tools and integrations
5. **Constraints** - Safety and scope limitations

## Quality Standards

1. Agent prompts must be specific and actionable
2. Avoid vague instructions - be precise
3. Include escalation triggers
4. Define handoff format for inter-agent communication

## Safety

1. Every agent must include authorization verification steps
2. Destructive capabilities must require explicit confirmation
3. Scope boundaries must be clearly defined
4. Emergency stop procedures must be documented
