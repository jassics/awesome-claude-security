---
hide:
  - navigation
  - toc
---

<div class="acs-hero" markdown>

![awesome-claude-security — a Claude Code plugin marketplace](assets/banner.png)

# Teach Claude Code to do security work

<p class="acs-tagline">
A Claude Code plugin marketplace for the full cybersecurity &amp; GenAI-security
lifecycle — from recon and threat modeling to detection engineering, GRC, and
CISO-level strategy. Add the marketplace once, then install only the plugins you need.
</p>

</div>

```
/plugin marketplace add jassics/awesome-claude-security
/plugin install llm-security@awesome-claude-security
```

> A pentester knows which OWASP test bends a broken-access-control endpoint. An analyst
> knows which Sigma rule catches Kerberoasting. **Claude Code doesn't — until you install
> the plugin that teaches it.**

There's nothing to run. Each plugin adds **skills** — namespaced slash commands like
`/llm-security:owasp-llm-top10` — and **agents** to your Claude Code session. Everything
installs **à la carte**, or grab a **bundle** (a role like `pentester`, a suite like
`genai-suite`) and it auto-pulls its parts.

<div class="grid cards" markdown>

-   :material-rocket-launch: **New here? Start with Getting started**

    ---

    From "never heard of it" to installed-and-using in five steps, plus the bucket
    mental model.

    [:octicons-arrow-right-24: Getting started](GETTING_STARTED.md)

-   :material-shape: **Browse the plugin catalog**

    ---

    All 43 plugins, grouped by bucket and searchable. Generated straight from the
    marketplace, so it's never stale.

    [:octicons-arrow-right-24: Plugin catalog](catalog.md)

-   :material-book-open-variant: **Follow an end-to-end recipe**

    ---

    Web pentest, incident response, vuln triage, design review, securing a GenAI
    feature — each chains the right skills.

    [:octicons-arrow-right-24: Recipes](RECIPES.md)

-   :material-sitemap: **Understand the taxonomy**

    ---

    How plugins are bucketed — core, domain, GenAI security, AI safety, role,
    executive — and why AI security ≠ AI safety.

    [:octicons-arrow-right-24: Taxonomy](TAXONOMY.md)

-   :material-download: **Install &amp; use**

    ---

    Adding the marketplace, install scopes, bundles, MCP-dependent plugins, and
    updating or removing.

    [:octicons-arrow-right-24: Install & use](INSTALL.md)

-   :material-pencil-ruler: **Build a plugin**

    ---

    Scaffold from a template and follow the authoring conventions to contribute a new
    skill, agent, or domain.

    [:octicons-arrow-right-24: Authoring guide](AUTHORING.md)

</div>

!!! info "Scope & ethics"
    Everything here targets **authorized** security testing, defensive security,
    detection, GRC, research, education, and CTF use. Role agents confirm scope and
    rules of engagement before acting. This is a community project — it is not
    affiliated with or endorsed by Anthropic.
