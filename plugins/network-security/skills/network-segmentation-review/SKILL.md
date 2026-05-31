---
name: network-segmentation-review
description: >-
  Review network segmentation and firewall/ACL design for security: zone
  separation, ruleset hygiene, lateral-movement containment, and zero-trust /
  microsegmentation. Use to assess or design network architecture defensively (not
  active testing).
---

# Goal

An assessment of how well the network limits blast radius: are zones separated, are
firewall rules least-privilege, and is lateral movement contained — with prioritized
fixes.

# What to review

1. **Zoning & trust** — segmentation between internet/DMZ/internal/management/OT,
   per-environment (prod/dev) and per-tenant separation; where trust changes.
2. **Firewall / ACL hygiene** — overly broad rules (`any/any`), unused/shadowed
   rules, stale entries, missing egress filtering, default-allow.
3. **Lateral-movement containment** — is the internal network flat? Can one
   compromised host reach the whole estate? East-west controls, microsegmentation.
4. **Management & sensitive planes** — isolated management network, jump hosts,
   restricted access to admin interfaces, OT/ICS separation.
5. **Zero-trust posture** — identity-aware access vs. pure network location; explicit
   allow-listing.

# Steps

1. Gather topology, firewall rulesets/ACLs, and zone definitions.
2. Assess against the areas above; flag broad/stale rules and flat segments.
3. Model the lateral-movement blast radius from a typical foothold.
4. Recommend segmentation, rule tightening (least privilege, default-deny egress),
   and management isolation, prioritized by blast-radius reduction.

# Output

A review: zone/rule · issue · severity · fix, plus a target segmentation design and
egress policy. Visualize zones with `security-diagramming:architecture-diagram`;
report with `security-reporting`.

# Notes

Flat networks are the force-multiplier behind most breaches — containing east-west
movement limits blast radius more than almost any other network control. Hunt broad
(`any/any`) and stale firewall rules; default-deny egress is commonly missing and
high-value. Pairs with `network-pentest` (which demonstrates the lateral paths).
