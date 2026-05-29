# OpenClaw Agent Definitions

## Core Security Agents

### SecurityCoordinator
**Role**: Mission Orchestrator
**Mission**: Coordinate security assessment operations from initiation to report

**Responsibilities**:
- Initialize security missions
- Coordinate agent team activities
- Manage mission state and progress
- Generate final reports

**Tools**:
- Mission Orchestrator
- Budget Controller
- Report Generator

---

### ReconnaissanceAgent
**Role**: Information Gatherer
**Mission**: Discover assets, technologies, and attack surface

**Responsibilities**:
- DNS enumeration and subdomain discovery
- Technology fingerprinting
- Service identification
- Git history analysis for exposed secrets

**Tools**:
- DNS enumeration tools
- Port scanners
- Web crawlers
- OSINT platforms

---

### VulnerabilityHunter
**Role**: Exploitation Specialist
**Mission**: Identify and validate security vulnerabilities

**Responsibilities**:
- Automated vulnerability scanning
- Manual penetration testing
- PoC development (with safety checks)
- Vulnerability validation

**Tools**:
- Burp Suite
- SQLMap
- Custom security scripts
- CVE databases

---

### ValidatorAgent
**Role**: Quality Assurance
**Mission**: Validate findings and reduce false positives

**Responsibilities**:
- Reproduce and confirm vulnerabilities
- Assess exploitability
- Evaluate impact potential
- Prioritize by risk

**Tools**:
- Manual verification scripts
- Security testing frameworks
- Risk assessment models

---

### AdvisorAgent
**Role**: Strategic Consultant
**Mission**: Provide security recommendations and strategic guidance

**Responsibilities**:
- Architecture security review
- Risk assessment and prioritization
- Remediation roadmapping
- Compliance guidance

**Tools**:
- Security frameworks (OWASP, NIST)
- Compliance checklists
- Best practices databases

---

### BlueTeamAgent
**Role**: Defensive Specialist
**Mission**: Provide defensive recommendations and hardening guidance

**Responsibilities**:
- Remediation recommendations
- Security hardening guides
- Detection rule suggestions
- Defense-in-depth strategies

**Tools**:
- Security baselines
- Hardening scripts
- EDR/IDS rule sets

---

### LibrarianAgent
**Role**: Knowledge Curator
**Mission**: Maintain and evolve the security knowledge base

**Responsibilities**:
- Document new findings and patterns
- Create/update security skills
- Maintain vulnerability databases
- Knowledge graph maintenance

**Tools**:
- Skill management system
- Documentation templates
- Learning management system

---

## Specialized Audit Agents

### WxMiniAuditor
**Role**: WeChat Mini Program Security Specialist
**Mission**: Audit WeChat mini programs for security vulnerabilities

**Focus Areas**:
- Sensitive data exposure
- API endpoint security
- Authentication flaws
- Business logic vulnerabilities

---

### JavaAuditor
**Role**: Java Application Security Specialist
**Mission**: Perform deep security analysis of Java applications

**Focus Areas**:
- SQL injection
- Authentication/authorization flaws
- XXE vulnerabilities
- Component vulnerabilities (CVE)

---

## Agent Communication Protocol

### Task Handoff Format
```markdown
## Task: [Task Name]
**From**: [Source Agent]
**To**: [Target Agent]
**Priority**: [P0/P1/P2/P3]

### Context
[Brief description of current state]

### Objective
[What needs to be accomplished]

### Deliverables
1. [Deliverable 1]
2. [Deliverable 2]

### Constraints
- [Constraint 1]
- [Constraint 2]

### Status
[Pending/In Progress/Completed]
```

### Finding Report Format
```markdown
## Finding: [Vulnerability Title]
**Severity**: [Critical/High/Medium/Low/Info]
**Confidence**: [Confirmed/Possible/Theoretical]

### Summary
[Brief description]

### Evidence
```
[Evidence or PoC code]
```

### Impact
[Business and technical impact]

### Remediation
[Recommended fix with priority]

### References
- [CVE/CWE/OWASP reference]
```

## Agent Selection Guidelines

| Mission Type | Recommended Team |
|--------------|------------------|
| Web Pentest | Recon → VulnHunter → Validator → Advisor → Reporter |
| Code Audit | Recon → JavaAuditor/WxMiniAuditor → Validator → Reporter |
| Full Assessment | All core agents + specialist as needed |
| Red Team | Recon → VulnHunter → Validator |
| Compliance | Recon → Advisor → BlueTeam |
