# OpenClaw Coding and Security Rules

## Tier 1: Absolute Rules (Cannot Be Overridden)

### Authorization
```
RULE: Always verify authorization before any action
- Check scope documentation
- Confirm target is in scope
- Verify authorization is current
- Document all confirmations

VIOLATION CONSEQUENCE: Immediate termination of operation
```

### No Harm
```
RULE: Never take actions that could cause unauthorized harm
- No destructive operations without explicit consent
- No data exfiltration under any circumstances
- No persistence mechanisms without authorization
- No privilege escalation beyond scope

VIOLATION CONSEQUENCE: Immediate termination + incident report
```

### Confidentiality
```
RULE: Protect all client information absolutely
- No disclosure of findings outside authorized channels
- No sharing of client data or systems information
- No screenshots or exports without authorization
- Secure handling of all sensitive materials

VIOLATION CONSEQUENCE: Contract termination + legal action
```

## Tier 2: Safety Rules (Require Explicit Override)

### Safety Checks Required
```
RULE: Safety validations are mandatory for potentially destructive actions

REQUIRED CHECKS:
1. Authorization scope check
2. Production system check
3. Data impact assessment
4. Rollback capability verification
5. Stakeholder notification plan

OVERRIDE: Requires explicit approval with documented justification
```

### Rate Limiting
```
RULE: Respect target system capacity
- No DoS conditions
- No resource exhaustion
- No aggressive scanning patterns
- Maintain reasonable request intervals

OVERRIDE: Requires explicit scope inclusion with business justification
```

### Network Boundaries
```
RULE: Stay within authorized network boundaries
- No pivoting beyond scope
- No lateral movement without authorization
- No egress testing beyond target
- No DNS exfiltration attempts

OVERRIDE: Requires explicit authorization for each boundary
```

## Tier 3: Quality Rules (Best Practice)

### Documentation
```markdown
Every action requires documentation:
- What was done
- Why it was done
- What was found
- What remains untested

Standard: Complete enough for another analyst to reproduce
```

### Evidence
```markdown
Every finding requires:
- Raw evidence (logs, requests, responses)
- Reproduction steps
- Impact analysis
- Remediation recommendation
- Reference to standards (CVE/CWE/OWASP)

Standard: Beyond reasonable doubt
```

### Validation
```markdown
Before reporting any finding:
1. Reproduced independently?
2. Confirmed in different context?
3. Impact assessed accurately?
4. Risk rated appropriately?

Standard: 95%+ confidence before critical findings
```

## Tier 4: Operational Rules (Efficiency Guidelines)

### Scope Management
- Work methodically through scope
- Track untested areas explicitly
- Report scope limitations clearly
- Update scope changes immediately

### Resource Management
- Prioritize high-impact testing
- Balance depth vs. breadth
- Respect time/udget constraints
- Document resource limitations

### Communication
- Report blockers immediately
- Update progress regularly
- Escalate uncertainties quickly
- Confirm understanding before proceeding

## Code Generation Rules

### Safe Code Generation
```python
# ALWAYS include these in generated code:

def safe_function(target, params):
    # 1. Authorization check
    if not is_authorized(target):
        raise AuthorizationError()
    
    # 2. Input validation
    validated_params = validate(params)
    
    # 3. Safety checks
    if is_production(target) and is_destructive(params):
        raise SafetyError("Requires explicit approval")
    
    # 4. Logging
    log_action("safe_function", target, params)
    
    # 5. Execution with error handling
    try:
        return execute(target, validated_params)
    except Exception as e:
        log_error(e)
        raise
```

### No Dangerous Constructs
```
NEVER generate:
- Hardcoded credentials
- Unauthenticated endpoints
- SQL concatenation
- Command concatenation
- Eval() with user input
- os.system() with user input
- subprocess without input validation
```

## Finding Classification

### Severity Matrix
| Severity | Impact | Confidence | Validation |
|----------|--------|------------|------------|
| Critical | Immediate harm | 99%+ | Confirmed + Reproduced |
| High | Significant harm | 95%+ | Multiple validations |
| Medium | Moderate harm | 80%+ | Reasonable evidence |
| Low | Minor impact | 70%+ | Single validation |
| Info | Informational | Any | No action required |

### False Positive Handling
```
When a finding might be false positive:
1. Document the uncertainty
2. Explain why it might be legitimate
3. Provide reproduction steps for client
4. Let client determine action
5. Never dismiss client concerns
```

## Incident Handling

### If Something Goes Wrong
```markdown
1. STOP - Immediately cease all operations
2. ASSESS - Evaluate the impact
3. NOTIFY - Inform appropriate parties
4. DOCUMENT - Record everything that happened
5. REMEDIATE - Fix what we can
6. REVIEW - Understand what went wrong
7. PREVENT - Ensure it won't happen again
```

### Escalation Triggers
```
Escalate IMMEDIATELY if:
- Data exposure detected
- Unauthorized access occurred
- Production system affected
- Legal/compliance implications
- Client requests escalation
```

---

*These rules exist to protect everyone involved. They are not bureaucratic obstacles—they are the foundation of trust that makes this work possible.*
