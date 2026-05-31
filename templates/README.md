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

## Files in the template

| File | Purpose |
| --- | --- |
| `.claude-plugin/plugin.json` | Plugin manifest. `name` is the only required field. |
| `README.md` | User-facing description, skill/agent tables, install line. |
| `skills/example-skill/SKILL.md` | A single-responsibility skill. The `description` is the trigger. |
| `skills/example-skill/reference.md` | Optional on-demand depth (checklists, payloads, rubrics). |
| `agents/example-agent.md` | Optional persona for multi-step delegation. |
