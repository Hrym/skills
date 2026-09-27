# Working on larger features

Use more structure when the work needs decisions or multiple coherent deliveries—not merely because an agent has a long skill menu.

## Start with the problem

In Build or Plan, describe the goal and boundaries in ordinary language. The coordinator investigates existing formats and decisions, then chooses a design skill such as `grill-with-docs` only if consequential behavior is unresolved. That skill can retain terminology in `CONTEXT.md` and meaningful choices in ADRs; neither is a transcript of every question.

Example:

> I want older save games to work after the next format change. Investigate existing formats and help me choose the supported upgrade behavior. Keep failure handling proportional to how save files are used. Propose the design and checks before editing.

Expect focused questions about unresolved compatibility decisions, not a request to choose skills. Approve the design when those decisions are settled. The coordinator should not run another brainstorming procedure afterward simply because it is installed. Reopen design only for missing acceptance criteria or new material evidence. Design approval is not automatically permission to edit: when implementation has not been authorized, the coordinator should propose the scoped delivery and ask once. In Plan mode it can draft the handoff in the conversation but must ask you to switch to Build before writing project files, including ADRs or specifications; it must never delegate around the boundary.

For example, after checking existing formats, the agent might ask: “Old saves have no version marker. Should we support only the known legacy layout, or attempt to infer unknown layouts?” You could answer: “Support the known layout only; report unsupported saves without modifying them. Record that decision, but do not edit the application yet.”

## Keep the purpose visible

Use [capture-intent](capture-intent.md) alongside discovery, not as a second interview. A colleague should be able to understand why the feature exists, what should become better, and why its boundaries matter without reconstructing the transcript. Reuse an adequate solution brief or spec introduction; otherwise preserve a concise intent anchor as the design develops. In Plan, draft it in the conversation until file edits are authorized in Build.

Confirm the intent with the design rather than add another approval ceremony. Link the anchor from the spec/tasks and keep ADRs for the individual consequential choices. Optional PM techniques can supply evidence or an adequate brief; they are not additional mandatory stages. An intent change should trigger review of affected decisions and scope, not a rewrite of history to match code.

## Produce a specification and tasks when useful

The optional `planning` group supplies `to-spec` and `to-tickets`. They work with the project's configured tracker. A local Markdown tracker is an option when no issue service is available; installing skills does not grant tracker credentials.

Expect the coordinator to propose a specification capturing behavior, constraints, verification, and non-goals, with tasks only when coherent slices and dependencies help. A short checklist may suffice. If optional planning skills are absent, it should disclose that and offer a local draft rather than block progress or silently install them.

The pinned upstream `to-spec` asks for exhaustive user stories. This selected workflow instead uses representative scenarios and the requirements needed for the approved scope; the coordinator must apply that explicit customization rather than turn every feature into a story inventory. Request exhaustive coverage deliberately when the work actually needs it.

For example, the agent might propose: “I can draft a compatibility spec and two verifiable slices locally, then show them for approval. Do you want these published to the tracker?” You can answer:

> Draft them locally first. Do not publish. Once I approve the plan, ask before implementing it.

Installed `to-spec`/`to-tickets` flows can publish to a configured tracker; the coordinator must not invoke a publishing-capable flow until publication is authorized. Local drafts are a suitable alternative. Approval to publish is separate from approval to implement.

The recommended delivery owner is `execute-approved-work`, not an additional `implement`/`implement-spec` or another orchestration framework. Those can be valid alternative workflows, but should not be stacked under this one.

## Execute in meaningful slices

After you approve substantive implementation, the coordinator establishes suitable isolation, normally `.worktree/<feature>/` inside the repository unless you/project policy specifies otherwise. Reuse an existing suitable workspace; do not create a new worktree per task. Keep it ignored without an automatic preparatory commit. The coordinator checks task dependencies/interfaces, then passes the authoritative spec, tasks, and verification contract without repeating approvals. It starts sequentially unless separate ownership and integration are clear.

For multi-task/session work, keep the [execution record](progress-and-recovery.md) outside removable worktrees. If you return later, the coordinator reconciles that record with approved artifacts, actual dirty changes, worker state, and applicable evidence before continuing. It should not redispatch accepted work simply because conversation context was lost. Routine reversible corrections within intent can proceed with a recorded reason; changed behavior, scope, important trade-offs, or authority still need your decision.

For example, after reviewing the draft and its checks, switch to Build if you are in Plan, then say: “Approved. Implement these two slices; keep the result uncommitted.” The coordinator then chooses suitable workers and runs the agreed checks without another permission round for each slice.

Perform independent review at a coherent delivery boundary. Review an important persistence/interface decision before dependent work builds on it. Do not dispatch a full branch-review process after every small edit or duplicate the coordinator's review inside a worker.

Expect behavioral tests at the agreed seam, focused checks during work, completion checks on the integrated tree, independent standards/spec review, and a final evidence summary. Commits, pushes, PRs, destructive actions, and permission changes are separate user decisions, not automatic phases.

Worker statuses distinguish completion, concerns, missing context, and blockers; none alone proves acceptance. The coordinator resolves repository facts and diagnoses stalled work rather than retrying through every model. [Finishing](finish-work.md) is a separately authorized operation, using the whole feature's rationale for a squash and preserving unique local notes before cleanup.

Use a fresh context or handoff at an appropriate phase boundary when the conversation becomes unwieldy. Carry the intent anchor, spec, decisions, current revision/dirty state, completed tasks, outstanding questions, and verification evidence—not an ever-growing narrative replay. When preparing a [commit or PR](write-commit-and-pr.md), explain the reason and chosen approach using that context and the actual diff.

## Know when to involve stronger judgment

Changing shared interfaces, persistence formats, concurrency/lifecycle behavior, or resolving contradictory evidence warrants focused advice. Use a stronger model only if configured and available. A same-model advisor provides independent context, not guaranteed superior reasoning.

When the overall decomposition is itself difficult, a stronger primary coordinator may help. Model access and pricing are environment-specific; do not let the agent repeatedly call an unavailable model or cycle through reasoning settings without evidence that doing so addresses the blocker.
