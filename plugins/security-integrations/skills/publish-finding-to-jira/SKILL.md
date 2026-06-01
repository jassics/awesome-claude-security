---
name: publish-finding-to-jira
description: >-
  Turn a security finding (vuln, pentest issue, review item) into a well-formed Jira
  issue — mapped severity→priority, remediation/repro in the body, labels and
  components set, and dedup-checked against existing issues. Use when findings need
  to become tracked, assignable work in Jira.
---

# Goal

A Jira issue an engineer can act on without going back to ask questions — and no
duplicates of an existing one. Uses the Atlassian MCP server (wired by this plugin);
if it isn't connected, say so and fall back to producing ready-to-paste issue content.

# Steps

1. **Gather the finding** — title, severity, affected asset/component, evidence/repro,
   impact, and remediation. If it came from `security-reporting`, reuse that structure.
2. **Map fields** — severity → Jira priority (e.g., Critical→Highest … Low→Low);
   set issue type (Bug/Vulnerability), project, components, and labels
   (`security`, source like `pentest`/`scan`, severity, framework tag).
3. **Dedup first** — search the target project for an existing open issue for the same
   vuln+asset before creating; if found, comment/update rather than duplicate.
4. **Write the body** — concise summary, then Steps to Reproduce / Evidence, Impact,
   Remediation, and references (CVE, OWASP, ATT&CK). Attach severity and any SLA/due
   date from `vulnerability-management`.
5. **Create (or update)** via the Atlassian MCP; return the issue key/link.

# Output

The created/updated issue key + URL, and a one-line summary of fields set. If MCP is
unavailable, output the full issue payload (project, type, priority, labels, body) for
manual paste.

# Notes

Dedup is the difference between a useful tracker and noise — always search before
create. Keep severity→priority mapping consistent across the program so metrics mean
something. Don't dump raw scanner text into the body; translate it into repro + impact
+ fix.
