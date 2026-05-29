# Changelog v4.0

## Release v4.0 - Architecture Refactoring

> Major architecture refactoring based on professional security framework design principles.

### 🏗️ Architecture Changes

#### New Core Components

1. **Agent Registry** (`framework/core/agent_registry.py`)
   - Unified agent registration and discovery
   - Capability-based agent lookup
   - Dynamic agent loading from markdown definitions

2. **RedTeam Gateway** (`framework/core/redteam_gateway.py`)
   - Centralized gateway for all sensitive operations
   - Mandatory environment detection
   - Automatic jailbreak level selection
   - Complete audit logging
   - Sockpuppeting/ACI support

3. **Jailbreak Engine** (`framework/core/jailbreak_engine.py`)
   - 4-level jailbreak system (L1-L4)
   - Environment-based level enforcement
   - Platform-specific payload templates
   - Safe escalation paths

#### Layered Jailbreak System

| Level | Name | Technique | Environment |
|-------|------|-----------|-------------|
| L1 | Soft | CTF Mode Instructions | Any (default) |
| L2 | Medium | Role Playing & Scenario | Pentest Authorized |
| L3 | Hard | Sockpuppeting / ACI | CTF Sandbox or RedTeam Exercise |
| L4 | Deep | Multi-Turn Context + Memory Pollution | CTF Sandbox + deep_jailbreak:true |

### 🔧 Agent Restructuring

#### Simplified Agent Architecture

| Agent | New Role | Change |
|-------|----------|--------|
| Coordinator | Task orchestration only | Simplified |
| Exploit | Attack execution + RedTeam | **Merged** |
| Recon | Information gathering | Unchanged |
| Validator | Finding validation | Unchanged |
| Blue | Defense analysis | Unchanged |
| Advisor | Strategic guidance | Unchanged |
| ~~RedTeam~~ | ~~Merged into Exploit~~ | **Removed** |
| ~~Librarian~~ | ~~Tool Agent~~ | **Removed** |

### 🛠️ CLI Enhancements

#### New Commands

```bash
# Red team operations via Gateway
cli.py redteam --operation recon --target 192.168.1.1 --platform claude

# Agent management
cli.py agent list
cli.py agent info --agent-name exploit
cli.py agent capabilities --capability "vulnerability_exploitation"

# Jailbreak engine
cli.py jailbreak status
cli.py jailbreak levels
cli.py jailbreak payload --level L2 --platform claude
```

### 📁 New Directory Structure

```
framework/
├── core/
│   ├── agent_registry.py      # NEW
│   ├── redteam_gateway.py     # NEW
│   ├── jailbreak_engine.py    # NEW
│   ├── orchestrator.py        # Enhanced
│   └── ...
└── skills/
    ├── index.md               # NEW - Categorized index
    └── redteam/
        └── jailbreak/
            ├── L1_soft/       # NEW
            ├── L2_medium/     # NEW
            ├── L3_hard/       # NEW
            └── L4_deep/       # NEW
```

### 📚 Documentation

- `framework/skills/index.md` - Categorized skills index
- `.ctf/AUTHORIZED_TESTING.md` - Environment marker template
- `agents/exploit_agent.md` - Merged RedTeam capabilities
- `agents/coordinator_agent.md` - Simplified orchestration role

### 🔒 Security Improvements

1. **Mandatory Environment Detection**
   - File-based markers (`.ctf/CTF_MODE.md`)
   - Environment variable checks
   - Level enforcement based on environment type

2. **Audit Logging**
   - All operations logged
   - Environment type recorded
   - Success/failure tracking

3. **Safe Escalation**
   - Clear level requirements
   - Environment-appropriate restrictions
   - No silent bypasses

### 🔄 Migration Guide

#### From v3.x to v4.0

1. **Agent Usage**
   ```python
   # Old
   from agents.redteam_agent import RedTeamAgent
   
   # New
   from framework.core.redteam_gateway import execute_redteam_operation
   result = await execute_redteam_operation(operation="exploit", target="...")
   ```

2. **Jailbreak Usage**
   ```python
   # Old - Platform-specific REDTEAM.md files
   
   # New - Unified jailbreak engine
   from framework.core.jailbreak_engine import get_jailbreak_engine
   engine = get_jailbreak_engine()
   payload = engine.get_payload_auto("claude")
   ```

3. **Environment Setup**
   ```bash
   # Create environment marker
   touch .ctf/CTF_MODE.md
   # or
   export CTF_MODE=1
   ```

### ⚠️ Breaking Changes

- Removed: `agents/redteam_agent.md` (merged into `exploit_agent.md`)
- Removed: `agents/librarian_agent.md` (converted to tool)
- Deprecated: Platform-specific `REDTEAM.md` files (use jailbreak engine)
- Changed: Coordinator no longer executes operations (pure orchestration)

### 🐛 Bug Fixes

- Fixed agent responsibility overlap
- Centralized jailbreak payload management
- Unified CLI entry point

### 📊 Statistics

- New files: 10+
- Modified files: 5+
- Lines of code: ~1500+
- Skills indexed: 39 categories

---

**Full Changelog**: https://github.com/adminlove520/multi-CyberSecurity/compare/v3.6.0...v4.0.0
