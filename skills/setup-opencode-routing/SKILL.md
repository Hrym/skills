---
name: setup-opencode-routing
description: Use when setting up or migrating OpenCode quality-first agents, selected-workflow routing, or an environment with different provider access or no Astra. Applies to OpenCode configuration, not ordinary application development.
---

# Set up OpenCode routing

Bind stable roles to models confirmed for this environment. Catalog presence is not entitlement. Keep prompts concise and preserve the selected workflow's obligations. No orchestration plugin is required.

Use `customize-opencode` when available. Read [SETUP.md](SETUP.md) and the relevant files under `templates/` before editing. These are a complete **GPT-6.1 Sol / GPT-6 Luna no-Astra example**, not an automatic installer or universal model list.

## Discover

1. Establish global/project scope, provider/account, and explicit model exclusions. Read existing config, agent/command files, project overrides, and instructions; identify active config-directory/environment overrides. Preserve unrelated settings and user-authored prompts. Do not print credentials.
2. Use `opencode models` for candidate IDs. Confirm access from the user or successful calls under the intended account. Local catalog visibility and `debug config` alone cannot confirm access. If unknown, ask one focused question; keep model-specific changes staged until confirmed. Run paid smoke tests only with permission.
3. Select economical, standard, research, and strongest confirmed models. Do not substitute another provider/account without approval. Missing Astra is a normal profile, not an error to retry. Ask separately whether to enable `deep` even when Astra access and the full worker profile are approved; confirmed access alone is not consent. Preserve an existing explicit `deep` choice unless the user requests a change.

## Bind roles

| Role | Full profile (confirmed Astra) | No-Astra profile |
|---|---|---|
| Top-level default, `build`, `plan` | GPT-6.1 Sol `medium` | GPT-6.1 Sol `medium` |
| `general` | GPT-6.1 Sol `medium` | GPT-6.1 Sol `medium` |
| `explore`, `implement-small`, `verify` | GPT-6 Luna `medium` | GPT-6 Luna `medium` |
| `researcher` | GPT-6.1 Sol `medium` | GPT-6.1 Sol `medium` |
| `architect` | GPT-6 Astra `medium` | GPT-6.1 Sol `high` |
| `implement-complex` | GPT-6 Astra `medium` | GPT-6.1 Sol `high` |
| `deep` primary | Disabled by default; GPT-6 Astra `medium` only on separate opt-in | Disabled/omitted |

Names are examples; use exact confirmed provider/model IDs. If Luna is unavailable, bind its roles to the economical confirmed alternative or standard model. Do not activate a role without confirmed access to its model; choose an approved alternative if necessary. Same-model architecture/review gives separate context, not a capability upgrade. Never demote `general` to Luna merely because Superpowers names it. `deep` remains disabled by default even in the Astra worker profile, and cannot be dispatched as a worker.

Keep Terra optional, not a default tier. Apply SETUP.md's effort defaults only after checking provider/model variants; unsupported settings stay omitted. Effort does not imply stronger-model equivalence or guaranteed savings.

## Install

Merge the templates into the selected scope; adapt all model IDs. Preserve existing plugins, providers, MCP, permissions, and unrelated agents. Put prompts beside the target config; resolve duplicate inline/Markdown definitions. Repeated setup must update its roles without appending duplicate instructions.

Confirm intended role/permission changes. Adding `researcher` and `architect` to an explore-only Plan is a deliberate setup change: explain it and obtain approval if not already authorized. Plan may delegate only to read-only `explore`, `researcher`, and `architect`; the latter two deny shell/edit tools. Build may use all seven workers. Keep workers non-delegating and `verify` separate from implementation. Use one delegation level and bounded tool previews where supported. Preserve unrelated denied permissions.

Agree one workflow owner per phase. Install the shared Build/Plan prompt's guided handoffs: ordinary requests get a sized proposal and authorization boundary before edits, approved work proceeds without re-interview, and Plan stays read-only. The coordinator uses `execute-approved-work` when installed, behavioral TDD at agreed seams, and independent standards/spec review at meaningful boundaries. Keep its verification/stop rules; do not stack discovery or implementation frameworks. Existing plugin/skill removal needs explicit approval; omission from the template does not remove a merged plugin. See SETUP.md for migration. On restricted machines, inspect defaults, commands, and overrides for unavailable model references.

Retain intent/change-writing handoffs, bounded diagnosis, implementation statuses/recovery, and authorized `finish-approved-work`. Configure overridable repository-local `.worktree/` isolation and progress outside disposable worktrees. The learning checkpoint proposes, not silently installs, improvements; optional authoring uses `writing-for-agents` only. Preserve read-only Plan and no-Astra boundaries.

Review the template's Build/Plan competing-skill denials before applying them; preserve unrelated profiles. Use the same denials for enabled `deep`. They restrict skill loading, not plugin injection or arbitrary file reads. Check all active configuration/discovery scopes and report remaining conflicts; never promise isolation from a source-file edit alone.

Install the template's research rule: routine lookups stay direct, broad straightforward discovery goes to `explore`, and dense source interpretation goes directly to `researcher`. The coordinator checks original passages and consequential omissions; architectural advice is for difficult design, not source volume. See SETUP.md.

## Verify and hand off

Run `opencode debug config` and `opencode debug agent NAME` from each target project. Confirm loaded prompts, models, effective permissions, no active unavailable routes, and optional `deep` state. Check native parsing before claiming schema compatibility.

Report installed files, role bindings, permission checks, access-evidence level, and remaining gaps. Inspect the guided handoff scenarios in SETUP.md against the resolved Build/Plan prompts; static loading does not prove runtime compliance. Tell the user to quit/restart OpenCode and start a fresh conversation. Copy this entire skill directory to another environment for reuse.
