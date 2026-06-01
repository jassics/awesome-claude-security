# security-integrations

Publish security work **where teams already live**. Turn findings into **Jira**
issues, push reports/runbooks/threat models to **Confluence**, and export
reports/diagrams to **Google Drive** — so the output of every other plugin lands in
the tracker, wiki, or drive instead of a local file.

A **core**, cross-cutting plugin. It doesn't produce content — it *delivers* what
`security-reporting`, `security-diagramming`, `vulnerability-management`, and the
domain plugins generate.

## Install

```
/plugin install security-integrations@awesome-claude-security
```

## MCP

Ships an `.mcp.json` wiring the **Atlassian remote MCP server** (Jira + Confluence)
via `mcp-remote`; you'll authenticate to Atlassian on first use. Google Drive export
uses a connected Drive MCP server / connector if available. Every skill degrades
gracefully: if the integration isn't connected, it outputs publish-ready content for
manual paste/upload.

## Skills

| Skill | When it fires |
| --- | --- |
| `/security-integrations:publish-finding-to-jira` | Turn a finding into a deduped, well-formed Jira issue (severity→priority, repro, labels). |
| `/security-integrations:publish-report-to-confluence` | Publish a report/runbook/threat model to the right Confluence space with structure + cross-links. |
| `/security-integrations:export-to-drive` | Export a report/summary/diagram to Google Drive with clear naming and deliberate sharing. |

## Pairs well with

`security-reporting` and `security-diagramming` (the content), `vulnerability-management`
(issue/SLA fields), and every domain/role plugin that produces a deliverable.
