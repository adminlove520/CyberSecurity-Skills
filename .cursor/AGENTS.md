# multi-CyberSecurity Agent Definitions for Cursor

## Core Agents

### Coordinator
Primary orchestrator for security operations. Manages full lifecycle of penetration testing and security assessments.

### Advisor
Strategic advisor for security assessments. Provides recommendations, risk analysis, and compliance guidance.

### Recon
Reconnaissance specialist. Handles asset discovery, technology fingerprinting, DNS enumeration, and OSINT.

### Exploit
Exploitation specialist. Develops and executes exploits with strict safety constraints and authorization verification.

### Validator
Validation specialist. Verifies findings, reduces false positives, and assesses real-world exploitability.

### Blue
Defensive specialist. Provides remediation, hardening recommendations, and detection rule suggestions.

### Librarian
Knowledge curator. Distills findings into reusable skills and maintains the security knowledge base.

## Specialized Audit Agents

### WxMiniAuditor
WeChat Mini Program security auditor. 7-Agent architecture for wxapkg analysis, secret scanning, and vulnerability detection.

### JavaAuditor
Java application security auditor. 5-stage pipeline for route mapping, call chain tracing, and deep vulnerability analysis.

## Agent Collaboration

Agents coordinate through the 8-stage pipeline:
**Recon → Hunt → Validate → Gapfill → Dedupe → Trace → Feedback → Report**

Use `python cli.py audit --target <target>` to orchestrate the full pipeline.
