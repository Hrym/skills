# Progress and recovery

Read before multi-task/session execution, resuming interrupted work, or handling a stalled worker. This is a small Markdown record and coordinator procedure, not a scheduler, database, parser, or transcript archive.

## Keep a durable record

Follow repository convention; otherwise suggest an ignored `<primary-checkout>/.hrym/work/<initiative>/progress.md`. Resolve and disclose its actual location outside disposable worktrees and temporary storage. Ensure it is ignored through existing policy or an appropriate local exclusion, without an automatic commit. Keep canonical intent/specs/ADRs in project documentation; link them rather than copying them. Sharing local progress through Git or a tracker requires authorization.

In read-only Plan, write no files, including progress or ignore rules. Provide the draft/handoff in chat and explicitly disclose that recovery has not been persisted; request an authorized editing mode, not a worker bypass.

Record plan/intent identity and revision, workspace path/branch/base, current revision plus staged/unstaged/untracked state, and unrelated exclusions. Use stable task IDs with dependencies, assigned boundaries, implementation state, worker/session IDs when available, and a separate acceptance state. Record partial edits, check evidence tied to its actual snapshot/inputs/environment, review findings, coordinator rulings/waivers, and next action. Keep enough evidence outside the worktree to survive its cleanup; a path to a disposable log alone is insufficient.

Illustrative Markdown; replace placeholders with observed facts:

```markdown
# Initiative: input-validation
Intent/spec: docs/spec.md @ revision S; plan: docs/plan.md @ revision P
Workspace: /repo/.worktree/input-validation; branch: feat/input-validation
Base: B; current: H; snapshot: local diff D + relevant untracked-file copies
Dirty: staged none; unstaged src/input; untracked tests/input; exclusions: notes/

| Task | Depends | Boundary | Worker/session | Implementation | Acceptance |
| --- | --- | --- | --- | --- | --- |
| T1 | none | input API | worker-7/session-2 | DONE, stopped | accepted at D |
| T2 | T1 | validation | worker-9/session-2 | NEEDS_CONTEXT, partial edits, stopped | pending |

T1 evidence: command C, exit 0, cases/results, inputs/environment E, retained log L.
T1 review: snapshot D; standards/spec verdicts; findings resolved; ruling R.
T2 partial work: files/hunks; checks run/skipped; missing fact: empty-input policy.
Next: ask user for policy; preserve T2 edits; confirm ownership before continuation.
```

Update at dispatch, partial/blocking returns, review rulings, acceptance, and handoff; this is not a per-tool diary. Tell the user briefly when a meaningful task, decision, or blocker changes.

## Reconcile before continuing

1. Read the record and current instructions, intent, spec, and plan. Compare their identities and relevant content; a changed spec can invalidate acceptance even with unchanged code.
2. Inspect the actual branch/base and committed, staged, unstaged, and relevant untracked work against the recorded snapshot. Preserve unrelated edits. Current HEAD alone does not identify dirty work or establish that checks still apply.
3. Reconcile live workers using only the application's available native status, wait, resume, or stop mechanisms. A lost conversation or absent report does not prove a writer stopped. Reuse/resume only when supported and useful. Before a replacement writes the same files, establish the previous writer has stopped and explicitly transfer ownership. If this cannot be established, pause those writes and ask for help; do not invent polling/cancel APIs or start a competing writer.
4. Retain accepted, unchanged tasks when their requirement, dependency, snapshot, review, and evidence assumptions still hold; do not redispatch them merely because context was lost. Reopen only affected acceptance/checks when code, spec, dependencies, inputs, environment, or review evidence changed or cannot be established. Stale green logs are not current verification.
5. Record the reconciled state and next action. A fresh worker handoff includes relevant facts, authoritative links, ownership, partial-work snapshot/exclusions, applicable evidence, unresolved findings, and the precise continuation goal, not merely the original task prompt.

## Diagnose stalled work before retrying

- **Context:** identify the missing fact. Inspect repository sources directly for ordinary facts; ask the user for product choices or changed authority. Preserve partial edits while waiting.
- **Tooling/permissions:** capture the unavailable capability or denial and its impact. Use a permitted alternative only if it meets the same contract; otherwise request the needed authority or report the blocker. A stronger model cannot bypass denied permission.
- **Task scope:** narrow or split only when it preserves approved outcomes and ownership. Ask before changing behavior, scope, trade-offs, or material risk.
- **Reasoning:** supply concrete counterexamples or new evidence; narrow the question or choose a suitably capable available worker only with a reason it should help.

No blind retries, fixed retry count, or automatic model/effort ladder. When attempts stop yielding new evidence, stop and report the blocker, partial-work state, and recommended next action. Resume or reassign only after identifying what has changed and securing ownership; keep implementation status distinct from coordinator acceptance.
