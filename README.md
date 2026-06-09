# Sentinel Integration Test Repository — BlackDuck

**⚠️ This repository is intentionally misconfigured for testing.**

This repository contains deliberately problematic dependencies with license compliance issues for testing Sentinel's **BlackDuck scanner integration**. It is NOT a real application and should NEVER be used in production.

## Purpose

- Test positive cases: Real license violations that BlackDuck detects
- Test negative cases: License issues that are already approved or fixed
- Validate LLM reasoning: Verify Sentinel generates correct remediation recommendations
- Integration testing: Verify end-to-end workflow (detect → plan → code → git → PR)

## Intentionally Problematic Packages

| Package | Version | License | Issue | Test Purpose |
|---|---|---|---|---|
| PyPDF2 | 3.0.1 | GPL-3.0-only | Copyleft obligation | POSITIVE: Detects license violation |
| flask | 1.1.2 | BSD (outdated) | Outdated version | POSITIVE: Detects deprecated package |
| django | 2.2.24 | BSD (LTS ended) | End-of-life | POSITIVE: Detects EOL package |
| requests | 2.25.1 | Apache 2.0 | Outdated but compliant | POSITIVE: Detects outdated dep |

## Test Scenarios

### Scenario 1: Positive Case (Real License Violation)
```bash
# requirements.txt contains PyPDF2 (GPL-3.0-only)
# Expected: BlackDuck reports license violation
# Sentinel: Generates replacement recommendation (pypdf, Apache-2.0)
```

### Scenario 2: Negative Case (License Approved)
```bash
# requirements-approved.txt has same packages but marked as approved
# Expected: BlackDuck scans, finds no violations (due to policy approval)
# Sentinel: Reports clean status
```

## Files

```
├── requirements.txt              # Problematic: GPL packages, outdated deps
├── requirements-approved.txt     # Alternative: Approved licenses
├── requirements-fixed.txt        # Remediation: Apache-licensed alternatives
├── app.py                        # Sample app using dependencies
├── app-secure.py                 # Version without GPL dependencies
└── README.md                     # This file
```

## License Issues Explained

### GPL-3.0-only (COPYLEFT)
```
PyPDF2 3.0.1 is GPL-3.0-only
↓
Using in commercial software requires:
  - Your entire codebase to be open-sourced under GPL-3.0
  - All derivative works to be GPL-3.0

Recommended replacement:
  - pypdf 3.x+ (Apache-2.0) ✓ Can use in commercial software
```

### Outdated Packages
```
flask 1.1.2 is end-of-life (released 2019)
↓
Security issues won't be patched
↓
Upgrade to flask 2.x+ (actively maintained)
```

## How to Use This Repo

**For Sentinel Integration Testing:**

```bash
# Clone or reference this repo in integration tests
# Tests will:
# 1. Read fixture from mocks/blackduck_findings.json (positive case)
# 2. Read fixture from mocks/blackduck_findings_approved.json (negative case)
# 3. Create branches like fix/blackduck-gpl-license-001
# 4. Generate requirements-fixed.txt with Apache-licensed replacements
# 5. Open PR for validation
```

**For Manual Testing:**

```bash
# Run BlackDuck manually
blackduck-detect --detect.source.path=.

# Expected: License violations reported for PyPDF2, EOL packages flagged
```

## Security & Compliance Notes

- ✅ This is a **test-only** repository
- ✅ License violations are intentional for testing
- ✅ No real commercial code included
- ❌ DO NOT use GPL packages in commercial closed-source projects without legal review
- ❌ DO NOT deploy this configuration to production

## License Compliance for Real Projects

**Always check:**
1. Package license (PyPI, GitHub, package manager)
2. Your project's license
3. Compatibility matrix (GPL ≠ proprietary)
4. Your company's license policy
5. Customer agreements regarding open-source

## Repository Lifecycle

This repo is created and maintained specifically for Sentinel integration testing. It is:
- ✅ Public (for testing, no sensitive code)
- ✅ Read-only (tests fork it, never push directly)
- ✅ Immutable (license issues stay, intentionally)

See also: [Sentinel Integration Testing Guide](../../docs/integration-testing.md)
