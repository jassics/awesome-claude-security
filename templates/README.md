# Templates

Copy-to-start scaffolds for contributing to this marketplace. See
[../docs/AUTHORING.md](../docs/AUTHORING.md) for the full guide.

## Start a new plugin

```bash
cp -r templates/plugin-template plugins/<your-plugin-name>
```

Then:

1. Rename things in `.claude-plugin/plugin.json` (`name` must match the directory).
2. Replace the example skill/agent with real ones (delete what you don't need).
3. Update the plugin `README.md`.
4. Add an entry to `.claude-plugin/marketplace.json`.
5. `claude plugin validate ./plugins/<your-plugin-name> --strict`.

## Wire up a real security gate in your own project

`security-gates/` is a different kind of template — not for authoring a plugin,
but a ready-to-copy **pre-commit config + GitHub Actions workflow** for a project
*using* this marketplace's guidance, so "secure before commit/deploy" is an
actual enforced gate. See [`security-gates/README.md`](security-gates/README.md).

```bash
cp templates/security-gates/.pre-commit-config.yaml <your-repo>/
cp -r templates/security-gates/.github <your-repo>/
```

## Wire up a GenAI eval/red-team gate in your own project

`genai-eval-gates/` is the same idea applied to LLM/agent releases — a
ready-to-copy **promptfoo + garak CI workflow** that gates on safety-eval and
prompt-injection regressions instead of a one-off eval report. See
[`genai-eval-gates/README.md`](genai-eval-gates/README.md).

```bash
cp templates/genai-eval-gates/promptfoo.config.yaml <your-repo>/
cp -r templates/genai-eval-gates/.github <your-repo>/
```

## Files in the template

| File | Purpose |
| --- | --- |
| `.claude-plugin/plugin.json` | Plugin manifest. `name` is the only required field. |
| `README.md` | User-facing description, skill/agent tables, install line. |
| `skills/example-skill/SKILL.md` | A single-responsibility skill. The `description` is the trigger. |
| `skills/example-skill/reference.md` | Optional on-demand depth (checklists, payloads, rubrics). |
| `agents/example-agent.md` | Optional persona for multi-step delegation. |
