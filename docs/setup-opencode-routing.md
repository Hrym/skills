# Set up quality-first OpenCode agents

`setup-opencode-routing` configures role-based agents for exploration, dense-source research, implementation, verification, and architectural advice. Use it when you want suitable workers for bounded tasks without giving every task to the same model.

This is an **agent-guided setup skill**, not an installer script or a runtime model-switching service. It helps an OpenCode agent inspect your environment, propose model assignments, and merge configuration after approval. The resulting coordinator chooses workers using their roles and routing instructions; it does not optimize a measured cost function.

For the reasoning behind the defaults, see [Routing design](routing-design.md). For the recommended skill installation and workflow, begin with [environment setup](setup-development-environment.md). This guide remains useful for configuring the router independently.

## Requirements and compatibility

- OpenCode with native skills, custom agents, per-agent model variants, and task permissions.
- An authenticated provider with access to the models you select. The supplied no-Astra example uses `openai/gpt-6.1-sol` and `openai/gpt-6-luna`; Astra access is optional. Confirm each binding for your environment.
- Permission to modify your chosen global or project configuration.
- Native OpenCode subagents; no orchestration plugin is required. The recommended workflow uses `execute-approved-work` with behavioral TDD and independent review at meaningful delivery boundaries.

Configuration validation targets **OpenCode 1.18.30**. This is a validation baseline, not a claimed minimum version or a guarantee about every provider. Check your installation with `opencode --version` and validate before restarting. The skill must adapt or omit unsupported settings rather than invent replacements.

The template does not install or remove plugins. Migrating from a bootstrap-driven workflow requires explicit review of its plugin references and separately discovered skills; preserve unrelated/authentication plugins. See [workflow migration](../skills/setup-development-environment/SETUP.md#workflow-migration).

## 1. Install the skill

Copy the entire [skill directory](../skills/setup-opencode-routing/), including its reference and templates, into an OpenCode skill-discovery location. From this repository's root, the following installs it in the cross-runtime user skill directory **only if that destination does not already exist**:

The following shell example is a manual standalone alternative. For Windows-compatible dependency-aware installation, prefer the [Python environment installer](setup-development-environment.md).

```bash
mkdir -p "$HOME/.agents/skills"
test ! -e "$HOME/.agents/skills/setup-opencode-routing" &&
  cp -R skills/setup-opencode-routing "$HOME/.agents/skills/"
```

If the destination already exists, compare it with this version and back it up before updating. Do not overwrite local modifications blindly. Installing the skill makes its instructions discoverable; it does **not** apply the agent configuration.

Restart OpenCode after installing or updating skills. See [OpenCode skills documentation](https://opencode.ai/docs/skills/) for other discovery locations.

## 2. Back up the configuration you intend to change

For the default global location, copy `~/.config/opencode/` to a dated backup outside this repository. If you use project configuration, `OPENCODE_CONFIG`, `OPENCODE_CONFIG_DIR`, or a custom config location, back up those affected files as well.

Backups may contain credentials or private provider/MCP settings. Keep them local and out of Git. Record which files existed before setup so you can distinguish updated files from newly created ones when undoing the change.

## 3. Ask OpenCode to configure the environment

State the scope, provider, confirmed models, and exclusions. For example:

> Use setup-opencode-routing to configure my global OpenCode agents. GPT-6.1 Sol and GPT-6 Luna work through Copilot; Astra is unavailable. Preserve my existing settings and show the proposed changes before applying them.

For a stronger-model profile:

> Use setup-opencode-routing for this project. GPT-6.1 Sol, GPT-6 Luna, and GPT-6 Astra are available through OpenAI. Use Astra for architect and implement-complex. Ask me separately whether to enable Deep; preserve unrelated configuration.

The skill should inspect existing configuration and overrides, confirm exact model IDs, and explain intended permission changes before merging the templates. A model listed by `opencode models` is a candidate, not proof that your account can invoke it. Confirm access or explicitly authorize a small paid test; do not activate unverified model-specific routes.

Confirmed Astra access and approval of Astra workers do not enable `deep`. Ask for separate opt-in; keep it disabled by default, and preserve a previously explicit Deep choice unless the user requests a change. Enabled Deep is an Astra `medium` primary, not a worker.

## What gets configured

The role structure stays stable while model assignments adapt to your provider and available capability tiers.

| Agent | Purpose | Quality-first (no Astra) | Optional stronger profile | Effort default |
|---|---|---|---|---|
| Top-level default, `build`, `plan` | Coordinate work and integrate results | GPT-6.1 Sol | GPT-6.1 Sol | `medium` for agents |
| `general` | Standard implementation and independent review | GPT-6.1 Sol | GPT-6.1 Sol | `medium` |
| `explore` | Broad read-only code, document, and web discovery | GPT-6 Luna | GPT-6 Luna | `medium` |
| `researcher` | Read-only dense local-specification/web-source interpretation | GPT-6.1 Sol | GPT-6.1 Sol | `medium` |
| `implement-small` | Clear, localized, existing-pattern changes | GPT-6 Luna | GPT-6 Luna | `medium` |
| `verify` | Noisy builds/tests and log triage; no fixes | GPT-6 Luna | GPT-6 Luna | `medium` |
| `architect` | Read-only design advice | GPT-6.1 Sol | GPT-6 Astra, if confirmed | `high` without Astra; `medium` with Astra |
| `implement-complex` | Difficult implementation, diagnosis, and review | GPT-6.1 Sol | GPT-6 Astra, if confirmed | `high` without Astra; `medium` with Astra |
| `deep` | Optional primary coordinator for globally complex work | Disabled | Disabled until separate opt-in; then GPT-6 Astra | `medium` if enabled |

These OpenAI bindings are starting defaults, not a required provider contract or benchmark-proven optimum. Check variants for the exact provider/model before applying them. Higher effort or separate context is not equivalent to Astra.

Setup merges these files into the chosen config directory:

```text
opencode.jsonc
prompts/
  cost-aware-coordinator.md
  implementation-worker.md
agents/
  architect.md
  implement-complex.md
  implement-small.md
  researcher.md
  verify.md
```

Existing plugins, providers, MCP settings, unrelated agents, and stricter unrelated permissions should be preserved. The configuration changes the default model, Build/Plan prompts, named worker bindings and variants, task allowlists, and context controls. It can affect all projects when installed globally.

Build and enabled `deep` can invoke the seven workers (`explore`, `researcher`, `architect`, `implement-small`, `general`, `implement-complex`, `verify`). Plan can invoke only read-only `explore`, `researcher`, and `architect`. Workers cannot delegate. The researcher and architect deny task, edit, and shell tools; native read/web tools remain available under existing permissions. `verify` denies edit tools but can run checks under the existing shell policy. **Tool permissions are not a filesystem sandbox**: verification commands can create artifacts. Review custom tools separately.

Routine contextual lookups stay with the coordinator; broad straightforward discovery goes to Luna `explore`, while dense source reconciliation can go straight to the read-only GPT-6.1 Sol `researcher`. No mandatory discovery/research/advisor chain: the coordinator checks decisive original passages and searches consequential omissions independently. Consult `architect` for difficult design, not just more documents. Researcher evidence includes original excerpts with headers/qualifiers and locations, source authority/version, applicability, exceptions/conflicts, coverage/gaps, and uncertainty.

The example enables compaction/pruning, limits delegation depth where supported, and caps inline tool previews at 300 lines or 24,000 bytes. The shared Build/Plan prompt lets a developer start with an ordinary request: the coordinator selects installed skills, proposes a sized behavior/spec, plan, and verification contract before editing, then proceeds on scoped implementation authorization without repeating approved decisions. Plan stays read-only and asks for Build when edits are needed. Optional planning skills are not required for a small local checklist; publishing-capable flows wait for explicit publication authorization. The selected workflow retains required verification and independent review, bounded by the task's contract rather than every installed framework's ceremonies.

Build/Plan also have explicit `permission.skill` denials for competing workflow owners; the optional `deep` example applies the same set. These are profile-specific changes to approve, not a reason to alter unrelated agents or automatically remove installed files. Check effective rules after merging. They do not block a bootstrap plugin's direct instruction injection; migration still requires inspecting/removing that bootstrap with approval. See the [recommended profile](recommended-profile.md#preventing-overlapping-workflows).

The coordinator now carries implementation-status and durable-recovery rules, the overridable repository-local `.worktree/` preference, scoped diagnosis, and separate drafting/finishing responsibilities. Its nonblocking learning checkpoint suggests reusable improvements based on evidence; it does not silently edit installed skills. These process changes do not change the model/effort table above.

## 4. Validate and activate

Run checks from each target project so project-level overrides are included:

```bash
opencode --version
opencode models openai --verbose
opencode debug config
opencode debug agent build
opencode debug agent plan
opencode debug agent general
opencode debug agent explore
opencode debug agent researcher
opencode debug agent implement-small
opencode debug agent verify
opencode debug agent architect
opencode debug agent implement-complex
```

Replace `openai` with your intended provider and inspect `deep` if enabled. Review output locally; resolved configuration may contain sensitive values.

Check model IDs, supported variants, loaded prompts, task allowlists, worker edit/shell permissions, and unavailable-model references in defaults, commands, agent files, or project overrides. See [the setup reference](../skills/setup-opencode-routing/SETUP.md#permission-and-compatibility-checks) for expected permissions.

Successful loading proves configuration validity, not provider access, actual model use, or routing quality. After validation, **quit and restart OpenCode and start a fresh conversation**. Existing session selections can override defaults.

Try a bounded task and ask the coordinator to explain its agent selections briefly. Use recorded execution metadata when available to verify what ran; configured model names and agent self-reports are not equivalent to a provider execution trace.

## Customize the setup

- **Different providers or models:** adapt exact bindings rather than copying provider prefixes blindly. Keep economical, standard, research, and optional Astra roles distinct; do not assume matching provider suffixes or supported variants.
- **No stronger model:** bind `architect` and `implement-complex` to approved confirmed models suitable for their roles in the table above. Leave `deep` disabled on a fresh setup; if a prior explicit Deep choice is now unavailable, resolve that choice with the user before changing it or proceeding with an unavailable route. Resolve hard questions through narrower scope, evidence, and user clarification—not unavailable-model retries.
- **Different effort:** use supported agent `variant` settings. A task prompt requesting more thought does not change the API setting. Higher reasoning effort can increase output-token charges.
- **Different workload:** adjust defaults after comparing correct completion, review findings, retries, user intervention, latency, and total billed usage. Terra or another model is an optional measured alternative, not an automatic extra tier.
- **Existing permission restrictions:** preserve them. If they prevent part of the workflow, explain the limitation rather than silently granting more access.

The [agent-facing reference](../skills/setup-opencode-routing/SETUP.md) contains the detailed model/profile adaptation rules. Keep your installed skill and configuration changes under your own update process; updating this repository does not update an installed copy automatically.

## Undo the setup

Removing `~/.agents/skills/setup-opencode-routing/` only removes the setup instructions; it does **not** undo configuration changes.

Compare the affected config, prompt, and agent files against your backup. Restore settings changed by setup and remove only files introduced by it. Preserve unrelated changes made since the backup. If no later changes occurred, restoring the complete affected backup is simpler. Check both global and project scopes, then validate and restart OpenCode.

## Limitations

- Routing is instruction-driven, not a deterministic optimizer or automatic runtime failover system.
- Delegation adds startup, handoff, and review costs. Smaller-model token rates alone do not establish lower completed-task cost.
- Reasoning defaults and model bindings must be validated for the selected provider and current software versions.
- Tool permissions and prompt instructions are useful boundaries, not a complete security sandbox.
- Required checks and independent reviews should remain in place even when they reduce apparent savings.

For the design trade-offs and source references, read [Routing design](routing-design.md).
