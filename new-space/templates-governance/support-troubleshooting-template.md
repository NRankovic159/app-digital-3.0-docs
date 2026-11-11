# Template: Support Troubleshooting & Escalation Guide

````markdown
# Support Runbook: [Issue / Category Name]

## 1. Issue Overview
- **Category:** [Account Access | Billing | Latency | Sync Errors]
- **Severity Level:** [Sev 1 (Critical) | Sev 2 (High) | Sev 3 (Normal)]
- **Estimated SLA:** [e.g., 2 hours / 24 hours]

## 2. Customer Symptoms & Identifying Indicators
- **Customer description:** "Unable to save document", "504 Gateway error"
- **Error Codes:** `ERR_NETWORK_DISCONNECTED`, `HTTP 502`
- **Telemetry Query:** `index=prod_gateway status=502 user_id="$USER_ID"`

## 3. Tier 1: Initial Troubleshooting & Fast Recovery
1. Ask customer to verify version: Minimum supported is `v3.2.0`.
2. Check internal status page: [Internal Status Dashboard Link].
3. Run diagnostic check: [Internal Admin Tool link -> "Inspect User State"].
4. Quick fix / reset action:
   - [Instruction for clearing cache or session reset]

## 4. Tier 2: Escalation Path
*If Tier 1 steps do not resolve within 15 minutes:*
- **Escalate To:** [Team / On-Call SRE]
- **Channel / Ticket Queue:** `#[team-oncall]` or Radar queue `[Component Name]`
- **Required Ticket Fields before escalation:**
  - Customer ID / Org ID:
  - Timestamp of failure (with timezone):
  - Screenshot of client error:
  - Trace ID / Request ID:

## 5. Customer-Facing Canned Response / Macro
```text
Hi [First Name],

Thank you for reporting this. Our engineering team is currently investigating the issue affecting [Feature Name]. We have flagged your account ([Account ID]) to our specialist team. 

In the meantime, you can continue working by [Workaround Step]. We will update you here as soon as we have a resolution.
```
````
