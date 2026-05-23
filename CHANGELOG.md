# Changelog

All notable changes to this project will be documented in this file.

## [2.0.0] - 2026-05-23

### Added
- **Framework Core**: Introduced the `framework/` directory featuring a multi-agent orchestration system.
- **Orchestration**: Added `MISSION_CONTROL.md` (Blackboard) for real-time mission tracking and cross-agent state sharing.
- **Specialized Agents**: 
  - `CoordinatorAgent`: Mission planning and delegation.
  - `ReconAgent`: Passive/active reconnaissance specialist.
  - `ExploitAgent`: Vulnerability exploitation specialist.
  - `ValidatorAgent`: Evidence-based vulnerability verification.
  - `AdvisorAgent`: Strategic decision making and self-correction (Reflexion).
  - `BlueAgent`: Defense, hardening, and mitigation specialist.
  - `LibrarianAgent`: Autonomous skill distillation and library evolution.
- **MCP Integration**: Support for Burp Suite (REST API) and Kali Linux (SSH/WSL) via Model Context Protocol patterns.
- **Skill Evolution**: Autonomous "Learning Loop" that distills successful mission logs into reusable skills.
- **CLI Tool**: Unified `skill.py` for library management (lint, export, graph, evolve, mission-init).
- **Docker Lab**: Integrated `playground/` with OWASP Juice Shop and DVWA for safe agent testing.
- **Semantic Layer**: Generated `skill_graph.json` mapping MITRE ATT&CK techniques to specific skills.
- **External Skills**: Integrated `SecSkills`, `AboutSecurity`, `agency-agents` as submodules.

### Changed
- **Platform Support**: Upgraded `platform_exporter.py` to support OpenClaw, Trae, Codex, and Hermes formats.
- **Communication Protocol**: Standardized agent hand-offs using `HANDOFF_TEMPLATE.md`.
- **Reporting**: Upgraded `reporter.py` to generate PTES-compliant markdown reports with evidence.

### Fixed
- **Skill Indexing**: Automated `index.json` synchronization via `update_index.json.py`.
- **Validation**: Added `linter.py` to enforce metadata standards for all skill files.

## [1.1.0] - 2024
- Initial structured release with 39 modules and 195 skills.
