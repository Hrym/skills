# Readable skill compression: review draft

Status: approved revisions applied to repository sources. The routing role table is retained. The coordinator prompt is renamed to `agent-coordinator.md`, with active references updated. Installed copies are unchanged. The examples below retain the proposal rationale; they are not evidence of measured behavioral or token improvements.

Baseline: `3a6b0cb58022b1a7da188f27de38dd5642f02248`.

## What this draft covers

All six repository-owned skills under `skills/`, plus the coordinator and worker prompts used by the routing skill. The examples below are replacement candidates for named passages, not complete replacement files. Unmentioned instructions remain unchanged. Supporting references, installer code, configuration bindings, and third-party skills are not being rewritten.

Goal: remove unnecessary context while preserving readable structure, workflow ownership, authority, and verification. This is not a target percentage reduction or a blanket conversion to telegraphic prose.

The repository's ADR separates workflow, installation, and application routing. Keep that separation: environment setup selects and installs skills; routing configures roles; execution owns delivery. Moving model tables out of the environment installer follows that existing boundary.

## How to read the proposal

Start with sections 1 and 2: they offer the clearest reductions by removing duplicated model/profile explanations. Sections 3–6 are smaller wording improvements; leaving already concise passages alone is a valid outcome. Section 7 applies our agreed coordinator direction. Section 8 explains why worker instructions need more caution.

Each example has a specific replacement boundary. Quotes labelled “current excerpt” may show only part of that boundary; the proposed text must be reviewed against the full source before application.

### Loading and savings

Skill discovery exposes descriptions; full skill bodies are normally loaded on invocation. Agent prompts apply to their configured roles. Retained instructions/history can be included in subsequent model requests, even without another file read. Provider caching may reduce billing, but not context occupancy; pruning and compaction depend on the application.

Therefore, prioritize recurring coordinator prompts and discovery descriptions, then frequently invoked skill bodies. A setup-only reference is not necessarily present during implementation. Moving a paragraph into a file that is always read immediately offers little context reduction; a reference saves context only when its loading condition is genuinely narrower.

No token or behavioral savings have been measured here. Fewer characters are not proof of fewer tokens, and shorter prompts are not proof of better task completion.

## 1. setup-development-environment: remove a duplicated routing manual

Source: `skills/setup-development-environment/SKILL.md`, first two paragraphs under “Configure the selected workflow” (baseline lines 25–27).

Current excerpt:

> The no-Astra starting profile uses GPT-6.1 Sol `medium` for coordination, `general`, and research; GPT-6.1 Sol `high` for architecture/complex work; and GPT-6 Luna `medium` for exploration, small changes, and verification.

Proposed replacement for those two paragraphs:

> After agreeing models and destination scope, invoke `setup-opencode-routing` to configure the selected workflow. It owns model bindings, effort settings, worker permissions, and coordinator handoffs. Follow its access and approval gates, including separate opt-in for `deep`; preserve prior explicit choices.
>
> Installing skills does not activate routing. Validate the resolved configuration and restart as described below. The installed workflow preserves intent, separates message drafting from authorized integration, and uses bounded execution, diagnosis, verification, and recovery. Do not add another orchestration or product-management pipeline.

Intent: let routing own routing details rather than maintaining another model table in the installer skill. Retain the distinction between installation and activation, and keep the explicit consent boundary for `deep` visible.

Leave the following plugin migration and project convention paragraphs intact. They contain installation-specific authority rules, not redundant prose.

Trade-off: the environment skill no longer gives a complete model-profile preview. The routing skill is already the next required step, so this is a deliberate reduction in duplication rather than a missing procedure.

## 2. setup-opencode-routing: separate triggering from profile examples

Source: `skills/setup-opencode-routing/SKILL.md`, frontmatter description and “Bind roles” table.

Current description:

> Use when setting up or migrating OpenCode quality-first agents, selected-workflow routing, or an environment with different provider access or no Astra. Applies to OpenCode configuration, not ordinary application development.

Proposed description:

> Use when configuring or migrating OpenCode agent roles, workflow routing, or model/provider bindings. Not for ordinary application development.

Intent: retain the distinct invocation branches without making a particular model's absence a permanent trigger phrase.

The role table could be replaced with:

> Before binding roles, read the model and effort profiles in SETUP.md, including provider requirements and variant support. Treat bundled models as examples; use confirmed IDs and approved alternatives for this environment. Keep `deep` opt-in and primary-only.

When applying this passage, link SETUP.md relative to the skill. From this draft, the reference is [routing SETUP.md](../skills/setup-opencode-routing/SETUP.md).

This table removal is optional, not an automatic win: the skill already requires reading SETUP.md, which repeats the profiles. Removing the duplicate saves repetition, but does not avoid loading the reference. Keep the table if users find the local overview materially useful.

Preserve discovery/access checks here. Unlike the runtime coordinator, this skill is responsible for configuring models and must distinguish catalog visibility from access. Do not generalize away provider-specific compatibility checks in SETUP.md or alter configured bindings as a prose cleanup.

Do not replace workflow handoff paragraphs with “follow the workflow.” Any later consolidation needs an explicit link to the governing instructions and a check that standalone setup still installs the required behavior.

## 3. capture-intent: shorten wording, not purpose

Source: `skills/capture-intent/SKILL.md`, “Locate the anchor” paragraph (baseline line 13).

Current excerpt:

> If an existing artifact already conveys purpose, outcome, boundaries, and tradeoffs, link it; do not require a second `intent.md`. A trivial change may need only its issue/task rationale.

Proposed replacement for the paragraph:

> Read the task, approved brief/spec introduction, glossary, and ADRs. Reuse and link an artifact that explains purpose, outcome, boundaries, and tradeoffs; a trivial change may need only its task rationale. Otherwise follow the project's location convention, defaulting to `docs/intent/<slug>.md`. Link authoritative specs, ADRs, and tasks instead of copying them. ADRs explain decisions and their history; glossaries define terms, not overall purpose.

Intent: preserve the reuse decision and default location while removing repeated explanation. This is a modest wording improvement, not a major context saving.

Keep the concrete brief content, evidence distinctions, read-only behavior, change-approval check, and completion criterion. Keep EXAMPLE.md optional. Moving required brief content into the example would weaken the skill.

## 4. execute-approved-work: make the review boundary easier to read

Source: `skills/execute-approved-work/SKILL.md`, first paragraph under “Review the actual change” (baseline line 31).

Current excerpt:

> Otherwise snapshot intended committed, staged, unstaged, and relevant untracked changes with exclusions; `base...HEAD` omits dirty work. Never auto-commit for review.

Proposed replacement for the paragraph:

> Obtain independent standards/spec review at meaningful boundaries, including consequential configuration and documentation changes. Review shared interfaces early when needed and the integrated result after multi-task work. For committed ranges, use `code-review` with exact base/head. Otherwise snapshot all intended committed, staged, unstaged, and relevant untracked changes, with explicit exclusions. `base...HEAD` omits dirty work; do not commit merely to enable review.

Intent: replace compressed slash constructions with clear relationships. This passage may not become shorter. Clarity is the reason to change it; do not present it as a token saving.

The existing CONTRACT.md and RECOVERY.md boundaries already provide useful progressive disclosure. Preserve the recovery triggers, writer-ownership check, DONE-versus-acceptance distinction, independent review, and authorized-waiver requirement. Do not reduce this skill to “dispatch, test, review.”

## 5. finish-approved-work: retain operation-specific authority

Source: `skills/finish-approved-work/SKILL.md`, “Commit only” bullet (baseline line 22).

Current:

> **Commit only:** inspect the full proposed index, commit only the authorized change with its grounded explanation, and report the result. This authorizes no merge, push, or cleanup; a remote target is not required.

Proposed:

> **Commit only:** inspect the complete proposed index, commit the authorized change with a grounded message, and report the result. No merge, push, cleanup, or remote target is implied.

Intent: express the operation and its boundary once. “No remote target is implied” means none is required by this operation, not that an existing remote is forbidden.

Recommendation: this skill is already compact. Retain its separate keep, commit, integration, and publication branches. Keep cleanup checks for ignored files, active writers, unique notes, and branch deletion; workspace location alone is not ownership proof. Do not save words by merging these into a generic “finish safely” instruction.

## 6. write-commit-and-pr: simplify the voice rule

Source: `skills/write-commit-and-pr/SKILL.md`, “Authorial voice” paragraph (baseline line 17).

Current excerpt:

> Write commits and PR descriptions as the change's author addressing future maintainers, not as an assistant reporting on a conversation.

Proposed replacement for the paragraph:

> **Authorial voice:** Address future maintainers as the change's author. Explain the problem, decision, and evidence directly, using neutral factual wording. Mention assistant/user interactions only when relevant to the change; references to actual product users are fine. Do not invent personal experience or extend claims beyond observed evidence.

Intent: retain the distinction between durable change explanation and session recap with fewer overlapping instructions. Keep the explicit product-user exception and evidence boundary.

Leave the drafting-versus-publishing rule, full-PR-range requirement, missing-rationale question, wrapping exceptions, and project-template precedence intact. EXAMPLES.md already carries optional examples without bloating the skill body.

## 7. Coordinator: readable structure, not token minimization

Source: `skills/setup-opencode-routing/templates/prompts/agent-coordinator.md`.

The repository baseline said “Cost-aware coordination.” The user reports changing a copy to “Agent coordination” elsewhere, with no observed recurrence yet. The approved revision uses that heading and renames the file to `agent-coordinator.md` to match the other environment. Do not infer that the behavior is fixed from the reported short-term result.

Replace the language-compression paragraph beside worker delegation with:

> Use concise, readable language in user messages and worker assignments. Bullets, labels, and short phrases are welcome when their meaning is explicit. Preserve normal word boundaries and the relationships between actions, objects, values, and conditions. Keep identifiers, commands, paths, and literal values exact.
>
> Reduce repetition and irrelevant context. If shortening makes an instruction require decoding or permits two interpretations, expand it. Before dispatch, check that scope, constraints, acceptance criteria, and stop conditions remain clear.

For example, use separate `File: examplefile` and `Hash: 34862347` fields instead of `hashis34862347byexamplefile`. The value and label boundaries matter; complete sentences are not required.

Replace the model-policy paragraph under “Roles” with:

> Choose configured worker roles by task ambiguity and correctness risk, not line count. Use their configured model and effort settings; effort is not model capability or a fixed token budget. Plan delegates only to `explore`, `researcher`, and `architect`.
>
> Consult `architect` for shared interfaces, persistence, subsystem boundaries, concurrency/lifecycle constraints, or difficult unresolved diagnosis—not document count. When the coordinator uses the same strong model, handle design directly when appropriate; another agent provides independent context, not a capability upgrade. Suggest `deep` only when enabled, never as a worker.

Intent: remove Astra/Terra access and model-selection policy from runtime coordination. Model selection belongs to setup; existing recovery instructions govern unavailable tooling. Keep the role restrictions and distinction between independent context and stronger capability.

Also expand terse assignment wording: “Supply workers directory, scope…” becomes “Give each worker its working directory, scope, authoritative references, relevant interfaces, acceptance criteria, verification checks, non-goals, and stop conditions.” This models the desired writing without adding a separate style manual.

## 8. Worker prompts: local repetition can be necessary

In the current template, only `general` references `prompts/implementation-worker.md`. `implement-small` and `implement-complex` have independent Markdown agent bodies; other workers use their own definitions or built-in behavior.

Do not remove repeated safety or handoff rules on the assumption that every worker inherits the shared file. They do not share that explicit binding. Changing inheritance or introducing a generated shared contract would be a separate configuration/design change, not prose compression.

A readability-only candidate for implementation-worker.md's final paragraph is:

> Resolve ambiguous assignments against authoritative artifacts. If a material requirement remains unclear, ask for clarification rather than guessing.

Intent: workers should respond to missing meaning, not treat all concise phrasing as defective. The source wording already works; this change is optional and has no demonstrated behavioral benefit.

Keep status definitions and required handoff evidence local to each worker that needs them. References alone are unsafe if the worker may not have access to the referenced document or is not instructed to read it.

## Review and trial before adoption

1. Check each replacement against the full source. Preserve triggers, authority, exceptions, exact commands/paths, verification, recovery, and completion criteria. Do not treat every repeated safety rule as redundant across separate contexts.
2. Check descriptions still trigger for the original cases, including offline installation, resumed work, changed model/provider bindings, and message drafting without publication.
3. Validate Markdown links and configuration references if live files change. Preserve role bindings and permissions during this prose-only pass.
4. Compare old and proposed coordinator prompts on equivalent assignments, including a longer multi-task exchange. Inspect actual worker assignments for spacing, unambiguous values, scope, conditions, and stop criteria. Short successful exchanges cannot rule out gradual degradation.
5. Record failures, clarification requests, retries, and task completion. Measure tokens with the relevant tokenizer/provider if savings matter; do not use word counts as billed-token evidence. Obtain permission before paid model trials.

Suggested adoption order: coordinator and installer duplication first; then routing description/table; finally the smaller individual wording edits. Do not alter live skills merely to make every section show a reduction.
