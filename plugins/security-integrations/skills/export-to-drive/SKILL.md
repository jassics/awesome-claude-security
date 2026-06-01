---
name: export-to-drive
description: >-
  Export a finished security artifact (report, executive summary, diagram,
  spreadsheet of findings) to Google Drive — right folder, clear naming, and shareable
  with the intended audience. Use when a deliverable needs to be handed to
  stakeholders who live in Drive/Docs/Sheets rather than a wiki or tracker.
---

# Goal

The deliverable lands in the right Drive location with a clear, dated name and the
correct sharing — ready to hand to a client or leadership. Uses a connected Google
Drive MCP server / connector; if none is available, say so and produce the
export-ready file locally for manual upload.

# Steps

1. **Identify the artifact & audience** — report/summary from `security-reporting`,
   a diagram export from `security-diagramming`, or a findings spreadsheet. Audience
   determines format (Doc vs. PDF vs. Sheet) and sharing scope.
2. **Name and place** — `YYYY-MM-DD <client/scope> <artifact>` in the target folder;
   reuse an existing engagement folder rather than scattering files.
3. **Choose format** — narrative → Doc/PDF; finding lists/metrics → Sheet; diagrams →
   image/PDF. Convert as needed.
4. **Set sharing deliberately** — least-exposure: specific people/groups over
   link-sharing; never world-readable for sensitive security content. Confirm scope
   before sharing externally.
5. **Export/upload** via the Drive connector; return the file link and its sharing
   scope.

# Output

The Drive file link, its folder, and the exact sharing scope set. If no connector is
available, the formatted file path + intended folder/name/sharing for manual upload.

# Notes

Security deliverables are sensitive — confirm the sharing scope explicitly before
sharing externally; link-sharing a pentest report is a leak. Consistent
date+scope naming makes engagements findable months later. Sharing externally
publishes the content — treat it as a release, not a save.
