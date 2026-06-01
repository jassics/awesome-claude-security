---
name: publish-report-to-confluence
description: >-
  Publish a security report, runbook, threat model, or assessment writeup to
  Confluence — correct space/parent, consistent page structure, labels, and links
  back to related issues/pages. Use when a finished document needs to live in the
  team wiki, not just a local file.
---

# Goal

A well-placed, well-structured Confluence page that teammates can find and that links
to the related Jira issues and source material. Uses the Atlassian MCP server (wired
by this plugin); if it isn't connected, say so and output publish-ready content.

# Steps

1. **Take the source doc** — typically from `security-reporting` (pentest report,
   exec summary, finding set), `threat-modeling`, or a runbook from a defensive plugin.
2. **Place it** — target space and parent page; decide new page vs. update existing
   (check for a prior version and update in place to avoid stale duplicates).
3. **Structure** — title with date/scope, a TL;DR up top, then the body; convert
   tables/diagrams to Confluence-native format. Embed or link `security-diagramming`
   exports rather than pasting images blind.
4. **Cross-link** — link related Jira issues (from `publish-finding-to-jira`),
   prior assessments, and source repos. Add labels (`security`, type, year).
5. **Publish** via the Atlassian MCP; return the page URL.

# Output

The published page URL + where it sits (space/parent) and labels applied. If MCP is
unavailable, output the structured page content (title, labels, body) for manual
creation.

# Notes

Update in place over creating v2/v3 pages — wiki sprawl kills discoverability. A
TL;DR/summary at the top is what executives and on-call actually read. Link issues and
diagrams so the page is a hub, not a dead end.
