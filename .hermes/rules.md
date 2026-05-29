# Security-First Coding Rules

## Absolute Rules (Never Violate)

1. **Authorization Verification**
   - Always confirm target is authorized
   - Document authorization scope
   - Never exceed authorized boundaries

2. **No Malicious Code**
   - Never generate ransomware, malware, or exploits
   - No social engineering attack automation
   - No vulnerability marketplace integration

3. **Data Protection**
   - Never exfiltrate sensitive data
   - All findings stay within authorized scope
   - Client data remains confidential

4. **Safety Validation**
   - All PoC code must have safety checks
   - Destructive operations require confirmation
   - Network operations are logged and audited

## Code Quality Rules

1. **Input Validation**
   - Sanitize all inputs before processing
   - Validate file paths and URLs
   - Check command arguments

2. **Output Sanitization**
   - Remove sensitive data from logs
   - Redact credentials in reports
   - Secure temporary files

3. **Error Handling**
   - Never leak system information
   - Handle failures gracefully
   - Log errors without exposing details

4. **Resource Management**
   - Clean up temporary resources
   - Respect rate limits
   - Monitor resource usage

## Documentation Rules

1. Every skill must have:
   - Clear purpose and scope
   - Usage examples
   - Safety considerations
   - Known limitations

2. Every finding must include:
   - Severity classification
   - Evidence and reproduction steps
   - Remediation recommendations
   - References to standards (CVE, CWE, OWASP)

## Testing Rules

1. Test in isolated environments first
2. Validate all assumptions
3. Document test cases and results
4. Never test on production without explicit authorization
