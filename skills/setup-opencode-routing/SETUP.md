# Portable setup reference

## Quick reference

| Purpose | Command or location |
|---|---|
| Model candidates, not entitlement | `opencode models` |
| Actual config locations | `opencode debug paths` |
| Merged config and interpolated prompts | `opencode debug config` |
| Effective agent tools/model | `opencode debug agent NAME` |
| Skill discovery | `opencode debug skill` |
| Default global location | `~/.config/opencode/` |
| Skill installation | `~/.agents/skills/setup-opencode-routing/` |
| Authoritative schema | `https://opencode.ai/config.json` |

Use dedicated file tools for inspection/edits. Debug output can contain secrets: inspect selectively and never paste credentials into reports. Check `OPENCODE_CONFIG`, `OPENCODE_CONFIG_DIR`, and project/global scopes without dumping environment variables.

## Templates and model bindings

`templates/` is a **no-Astra OpenAI example** without a required orchestration plugin. It requires confirmed access to `openai/gpt-5.6-sol`, `openai/gpt-6-sol`, and `openai/gpt-6-luna` before activation. Preserve the directory structure when installing its files. Merge `opencode.jsonc`; do not replace the user's whole config. On Windows, inspect `opencode debug paths` rather than assuming the Linux configuration location.

| Destination | Purpose |
|---|---|
| `opencode.jsonc` | Defaults, existing built-ins, worker allowlists, context controls |
| `prompts/cost-aware-coordinator.md` | Shared Build/Plan coordination policy |
| `prompts/implementation-worker.md` | Standard worker contract |
| `agents/implement-small.md` | Economical implementation |
| `agents/implement-complex.md` | Strongest available implementation |
| `agents/architect.md` | Read-only architecture advice |
| `agents/researcher.md` | Read-only dense source interpretation |
| `agents/verify.md` | Noisy checks and evidence extraction |

For a confirmed Copilot-only environment, replace every template `openai/gpt-5.6-sol`, `openai/gpt-6-sol`, and `openai/gpt-6-luna` binding with exact confirmed `github-copilot/...` IDs. Do not assume identical suffixes exist: check the catalog, access evidence, and supported variants. If a model is unavailable, ask for an approved alternative; no bundled agent model binding requires Astra.

When adapting the bundled template to the full profile, change only `architect` and `implement-complex` to the confirmed Astra ID, and optionally replace its disabled `deep` entry below. When migrating existing configuration, also update old defaults and explicit Build/Plan models to GPT-5.6 Sol.

```json
{
  "mode": "primary",
  "disable": false,
  "description": "Strong-model coordination for globally complex architecture and cross-cutting diagnosis.",
  "model": "openai/gpt-6-astra",
  "variant": "high",
  "prompt": "{file:./prompts/cost-aware-coordinator.md}",
  "permission": {
    "skill": {
      "ask-matt": "deny",
      "brainstorming": "deny",
      "executing-plans": "deny",
      "finishing-a-development-branch": "deny",
      "implement": "deny",
      "implement-spec": "deny",
      "pr": "deny",
      "requesting-code-review": "deny",
      "subagent-driven-development": "deny",
      "systematic-debugging": "deny",
      "test-driven-development": "deny",
      "using-superpowers": "deny",
      "verification-before-completion": "deny",
      "writing-plans": "deny",
      "writing-skills": "deny"
    },
    "task": {
      "*": "deny",
      "explore": "allow",
      "researcher": "allow",
      "architect": "allow",
      "implement-small": "allow",
      "general": "allow",
      "implement-complex": "allow",
      "verify": "allow"
    }
  }
}
```

Keep the normal default/Build/Plan models on GPT-5.6 Sol. The user selects `deep` as a primary agent for globally complex work; workers cannot invoke it. On a restricted environment, disable an existing routing-owned `deep` and remove its stale model/prompt fields where owned, rather than leaving an unavailable model selectable. Never disable unrelated custom agents without agreement. For a price-prioritizing alternative, GPT-6 Sol can replace GPT-5.6 Sol in standard coordination/`general` after confirming access and evaluating representative work; this is not the bundled default.

## Workflow selection and migration

Use native OpenCode workers; Superpowers is not required. The default prompt recognizes an approved design, delegates bounded implementation, and preserves independent standards/spec review. `execute-approved-work` supplies the recommended procedure when installed; `setup-development-environment` installs the recommended skill set. A standalone router can follow the agreed task contract without claiming those skills are installed.

Keep discovery, execution, and review owners explicit. The coordinator selects installed skills from an ordinary request and presents an appropriately sized behavior/checklist or spec, plan, and verification contract before edits. Approved grilling/design satisfies discovery; do not restart brainstorming. Explicit implementation authorization counts, while design approval by itself may not. Plan stays read-only and hands implementation to Build, never to a delegate as a workaround. Missing optional planning skills permit a disclosed local draft; publishing-capable planning flows require explicit authorization before invocation. Do not load a second implementation orchestrator under a worker. The supplied verification contract governs behavioral tests, checks, non-goals, scope changes, and completion. Optional improvements do not automatically block delivery; real new material risks require a scoped decision.

Where installed, `capture-intent` preserves feature/architecture purpose alongside `grill-with-docs` and reuses existing adequate artifacts. Intent is confirmed with the design rather than by another gate; Plan drafts remain in conversation. `write-commit-and-pr` drafts the rationale for actual changes without authorizing Git mutations or publication. Both are part of the recommended environment catalogue, not required third-party dependencies of a standalone router. The coordinator explicitly prefers representative scenarios over upstream exhaustive-story rules unless the user asks otherwise. Additional PM/documentation skills remain optional tools with one authoritative artifact/phase owner.

The selected profile adds explicit Build/Plan `permission.skill` denials for competing phase owners; see the template for the authoritative list and apply matching rules to an enabled `deep`. This is an intentional profile change requiring approval, not a global ban on using those skills elsewhere. Keep unrelated agent permissions intact. A plugin may still inject text even when its named skill is denied: inspect/remove a competing bootstrap separately, only with approval. Missing/duplicate skill copies and overrides can undermine the profile; report them rather than relying on `disable-model-invocation` metadata.

Implementation workers return DONE, DONE_WITH_CONCERNS, NEEDS_CONTEXT, or BLOCKED with partial-work/evidence context. DONE is ready for review, not acceptance. Preserve the execution skill's dependency preflight, scoped triage, worker-ownership checks, and recovery outside disposable worktrees. Default workspaces to repo-local `.worktree/`, overridable; persist multi-task progress under project convention or primary checkout `.hrym/work/<initiative>/progress.md`, ignored. Neither path is written from Plan.

The finisher performs only requested integration/cleanup, using a message for the whole feature when squashing. It does not automatically pull, publish, or discard ignored notes. Non-obvious diagnosis uses `diagnosing-bugs` with the profile's no-progress and authority bounds; hypothesis/repetition suggestions are not quotas. Learning proposals are nonblocking, grounded in evidence/expected reuse, and edited in maintained sources only after approval. Optional authoring installs Matt's writing-for-agents, not another TDD/authoring pipeline.

For migration, inspect existing plugin references and every active skill-discovery location. Removing Superpowers from a template does not remove a plugin inherited through configuration merging. After explicit approval, remove its bootstrap/plugin reference if selecting this profile; preserve unrelated and authentication plugins. Separately discovered overlapping skills may remain: disable conflicting triggers with supported per-agent skill permissions or move them outside discovery only with approval. Do not depend on `disable-model-invocation` metadata being honored by OpenCode. Do not edit cached upstream packages.

When Superpowers is deliberately retained, select that workflow explicitly rather than promising the default bounded procedure wins over its bootstrap. Model routing and task permissions remain separate from the workflow choice. Offline, use installed-version configuration checks and report inaccessible schema/provider facts rather than requiring a web fetch.

## Reasoning effort and optional Terra evaluation

Keep GPT-5.6 Sol for standard and no-Astra complex roles, GPT-6 Luna for economical roles, and GPT-6 Sol for the researcher, with Astra where confirmed. Terra is an optional candidate, not an automatic intermediate tier. Confirm its exact family/provider ID instead of assuming a GPT-6 Terra exists. Compare current provider pricing and representative task outcomes before adding it; a tier name or anecdote is not evidence of better value. Preserve unrelated existing Terra agents unless the user approves changing them.

Use these **starting defaults**, not claims of optimal performance:

| Role | Default variant |
|---|---|
| `explore`, `verify` | `low` |
| `build`, `plan`, `general`, `implement-small`, `researcher` | `medium` |
| `architect`, `implement-complex`, enabled `deep` | `high` |

The no-Astra advisor/complex roles use GPT-5.6 Sol `high`; this is more effort within that model, not Astra-equivalent reasoning. The researcher uses GPT-6 Sol `medium` for dense interpretation; it is a specialized role, not a universal superiority claim. Broad straightforward evidence discovery stays with the single Luna explorer at `low`. The coordinator still verifies decisive evidence.

Before installation, inspect `opencode models PROVIDER --verbose` for each exact model's `variants` and their `reasoningEffort` mapping. The templates use OpenCode's agent `variant` field (JSON or Markdown frontmatter), not an assumed API parameter. Confirm it in the installed schema and `opencode debug agent NAME`. Recheck when changing providers, especially Copilot. If unsupported or unknown, omit the variant, report the provider default as unverified, and ask before adding provider-specific options. Successful parsing alone does not prove the provider honors effort.

Agent variants apply to the configured model; explicit session/model/variant choices may override defaults. A task prompt requesting “think harder” does not change the API setting, and the coordinator must not claim dynamic effort selection when its task tool exposes none. Do not add duplicate workers for every effort level by default.

Reasoning tokens are billed as output on OpenAI's reasoning API. Higher effort is not a fixed token budget, a free quality upgrade, or a substitute for a stronger model. Start with `low`/`medium`/`high`; only evaluate `xhigh`/`max` when measured benefits justify them. Do not silently enable pro reasoning mode or fast processing, which are separate controls. Avoid repeated trial-and-error escalation; diagnose missing evidence and requirements first.

For a recurring workload gap, compare Terra with Luna/Sol using the same task, tools, context, acceptance criteria, and recorded effort. Measure correct completion, retries, human intervention, latency, and total billed usage including reasoning/cache effects. Adopt only with repeatable benefit and user approval. Do not run paid comparisons without authorization.

References to recheck during setup: [OpenCode agent schema](https://opencode.ai/config.json), [OpenAI reasoning guide](https://developers.openai.com/api/docs/guides/reasoning), [Terra model](https://developers.openai.com/api/docs/models/gpt-5.6-terra), [GPT-5.6 Sol model](https://developers.openai.com/api/docs/models/gpt-5.6-sol), [GPT-6 Sol model](https://developers.openai.com/api/docs/models/gpt-6-sol). Model-specific settings and prices can change.

## Permission and compatibility checks

- `build`: seven named workers allowed; other task targets denied.
- `plan`: only `explore`, `researcher`, and `architect` allowed. Retain built-in Plan restrictions.
- `general`, `implement-small`, `implement-complex`: editing permitted subject to existing policy; `task` denied.
- `explore`: retain native read-only tool restrictions; `task` denied.
- `researcher`: `edit`, `bash`, and `task` denied; native read/web tools remain available under existing permissions. Review custom mutation-capable tools. This is not a filesystem sandbox.
- `architect`: `edit`, `bash`, and `task` denied. Also deny any installed custom mutation-capable tools. This is a tool-access boundary, not a full filesystem sandbox.
- `verify`: `edit` and `task` denied; shell available for requested checks subject to existing policy. Its no-source-edit rule is also prompt-enforced because shell commands can write.
- `deep`: enabled only for a confirmed stronger-model profile, primary mode, same seven-worker allowlist as Build.
- Build/Plan and enabled `deep`: selected-profile skill denials resolve as configured; permitted core skills remain callable. Tool permission checks do not establish that all bootstrap/instruction conflicts are absent.

Role migration intentionally changes the task allowlists. Explain adding the read-only researcher and advisor to Plan; obtain approval if the user's requested setup does not already authorize it. Preserve unrelated stricter rules and explain resulting limitations. If native loading rejects `subagent_depth`, `tool_output`, or `compaction.prune`, consult the installed-version schema/docs before adapting. Per-worker task denial still prevents nesting; do not invent unsupported replacement settings.

Changing a model binding is an installation-time choice, not automatic runtime failover. If access later fails, report it and reconfigure against confirmed available models. Same-model fallback offers independent context, not a stronger capability tier; improve scope, evidence, and independent review rather than advertising stronger reasoning.

## Local-document and web research

Keep this rule in the shared coordinator prompt. The separate researcher is an OpenCode agent config, not an installer skill or a required stage for every lookup.

1. **Route:** handle routine contextual lookups directly. Assign broad straightforward discovery to `explore` with concrete questions and an evidence index. Route dense local-specification or web-source interpretation directly to `researcher`, without a mandatory Luna → researcher → coordinator → architect chain. The researcher cannot delegate or escalate itself; it reports blockers.
2. **Evidence:** require a bounded answer, original excerpts preserving headings/table headers and qualifiers with URL/section or file/line locations, source authority/version/date or local revision, applicability, exceptions/conflicts, search coverage/gaps, uncertainties, and important passages to check. Prefer primary sources; mark missing access unverified.
3. **Verification:** the coordinator opens decisive original passages and checks scope, applicability, exceptions, and citation support. For consequential decisions, perform a targeted independent search for omissions and conflicting evidence. Do not rubber-stamp a summary; a shortlist cannot prove completeness. Consult `architect` for difficult architecture only when warranted, not because of document volume. Preserve Plan's read-only boundaries and required reviews without automatic extra research stages.

Example: a source summary says a model is unavailable because a table says “Coming soon.” Open the original row **and headers**: if this is the model-card link column, it does not establish model availability. Neither a researcher nor an advisor substitutes for checking the source.

## Validation scenarios

1. **Full:** confirmed GPT-5.6 Sol/GPT-6 Sol/Luna/Astra. GPT-5.6 Sol coordinates; Luna explores, implements small changes, and verifies; GPT-6 Sol interprets dense sources; Astra advises and handles complex work. Plan reaches only read-only workers. Optional `deep` is selectable but never a worker.
2. **Restricted:** confirmed GPT-5.6 Sol/GPT-6 Sol/Luna through Copilot, explicitly no Astra. Preserve unrelated MCP/plugin settings. Remove unavailable references from routing-owned global/project agents, commands and defaults. Architect/complex use GPT-5.6 Sol; `deep` is disabled. Standard `general` remains GPT-5.6 Sol.
3. **Unknown:** a model catalog lists Astra without access evidence. Do not activate model-specific changes or claim a working route. Ask for confirmation; paid smoke calls require permission. Static validation proves loading only.
4. **Research:** a researcher confuses a table's documentation-status column with feature availability. Coordinator checks original row/headers before concluding. For a consequential local specification, also search omitted exceptions/version differences; report inaccessible references. A large result set alone does not trigger Astra, and no-Astra mode must not attempt it.
5. **Effort/Terra:** a provider lists no verified `high` variant, and a user anecdote recommends Terra. Omit unsupported effort rather than inventing a mapping; preserve confirmed roles. Do not install Terra automatically or equate Luna `high` with Sol. Propose a bounded evaluation only for a relevant workload gap, with approval before paid calls.
6. **Bounded delivery:** approved gameplay behavior does not justify IL assertions without a concrete requirement/risk. Review intended dirty/untracked changes, not only `base...HEAD`; do not commit merely to satisfy the review skill. A new actual data-loss/security risk is surfaced rather than dismissed.
7. **Guided handoffs (static review of resolved Build/Plan prompt):** a small explicitly authorized change receives a compact contract and proceeds in Build without another approval; a larger unresolved design receives focused questions and a spec/plan proposal before implementation authorization; an implementation request in Plan produces a read-only proposal and asks for Build, with no worker edits. With planning skills absent, offer a local draft and disclose the gap; with publishing unapproved, avoid invoking publishing-capable skills. Resuming an approved artifact reuses decisions and check scope rather than repeating discovery. Check these branches against installed prompts and effective permissions; static review cannot prove an agent will obey them at runtime.
8. **Intent/change writing:** reuse an adequate approved PM brief instead of creating another intent document; preserve emerging purpose without duplicating grilling. A commit/PR draft with missing motivation asks for the missing rationale rather than inventing it. Dirty changes are inspected as dirty changes, and a text draft triggers no Git or publishing action. Examples follow the repository language and ordinary Mermaid syntax; a later project diagram convention takes precedence.
9. **Recovery/finishing:** NEEDS_CONTEXT with partial edits leads to precise context repair, not a duplicate writer; denied tooling is not solved by a stronger model. On resume, reconcile accepted tasks and evidence with current dirty state/spec. A squash request uses the feature-wide rationale and preserves ignored progress outside the owned worktree before cleanup. Failed checks retain recovery resources. A reusable learning candidate is an optional proposal, not a new acceptance gate.

## Common mistakes

- **Only changing the top-level model:** explicit Build/Plan, Markdown agents, commands, and project overrides can still select the old model.
- **Copying provider IDs from another account:** catalog names do not prove account access.
- **Plan delegates edits:** allow only genuinely read-only workers; an implementation worker with a "just advise" prompt is insufficient.
- **Dropping verification/review to save tokens:** keep required stages; bound their scope and reports.
- **Long setup guidance in every worker:** this skill is setup-only. Runtime agents receive only their compact role prompts.
- **Appending on every installation:** update owned definitions in place; inspect conflicts and preserve user modifications.
- **Expensive approval of a cheap summary:** check decisive original evidence and consequential omissions, not just summary plausibility. Keep discovery, verification, and interpretation distinct without automatically creating three agents.
