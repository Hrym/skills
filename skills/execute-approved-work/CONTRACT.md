# Verification and handoff contract

Keep this small. Reuse approved spec decisions; do not make the user repeat them.

```text
Observable behavior:
Public boundary under test:
Required cases and material failure modes:
Focused implementation checks:
Completion checks:
Non-goals:
New evidence that would reopen scope:
Acceptance criteria and stop conditions:
```

For a gameplay-input change, a contract might require valid commands to produce the expected action and invalid commands to return the specified result through the input interface. IL inspection and hostile in-process code are not part of that contract unless generated code or such a trust boundary is an actual requirement. A discovered injection path is material new evidence; the coordinator must raise it.

## Worker brief

- Approved task/spec, authoritative intent link when present, and relevant project instructions.
- Working directory, starting state, assigned files/boundaries, and dependencies.
- Verification contract, with concrete commands where known.
- No further delegation or automatic commits.
- Return the implementation-worker report below. The coordinator owns acceptance.

## Implementation-worker report

Every return uses one status. These are implementation outcomes, not review verdicts or acceptance marks.

| Status | Meaning | Coordinator action |
| --- | --- | --- |
| `DONE` | Assigned implementation is ready for review; not accepted delivery. | Inspect actual changes and check evidence, then obtain required review before accepting. |
| `DONE_WITH_CONCERNS` | Implementation is ready for review, but a risk, assumption, or incomplete check needs a ruling. | Classify each concern. Resolve blockers or obtain an explicit authorized waiver; missing required checks prevent acceptance without that waiver. |
| `NEEDS_CONTEXT` | A precise missing fact or decision prevents responsible continuation; partial edits may exist. | Preserve and inspect partial work. Resolve repository facts directly; ask the user for product or authority decisions. Supply the answer and continue only after ownership is settled. |
| `BLOCKED` | A concrete obstacle prevents progress with available tools, permissions, scope, or reasoning. | Diagnose the obstacle and choose an evidence-backed next action using [RECOVERY.md](RECOVERY.md); do not blindly redispatch. |

Include:

- Task ID, status, workspace, changed files, and partial-work state: what is complete, incomplete, or unsafe to use. State whether the worker has stopped editing.
- Exact check commands, exit codes when available, results, evidence/log paths, and skipped/incomplete checks. Include red/green evidence where TDD applies; concise decisive excerpts, not full logs.
- Material assumptions, remaining risks, and the precise missing fact or blocker (or explicitly none). Separate observations from hypotheses.
- Recommended next action and what fact, permission, or evidence would make it useful. A status label alone is insufficient.

Do not claim checks ran when they did not. A concern's severity, not the selected status, determines whether acceptance is blocked.

## Review brief

- Exact change snapshot and exclusions, not merely a commit ID when the tree is dirty.
- Requirement/spec, authoritative intent, and the same verification contract given to the implementer. Report a mismatch with intended outcomes rather than inventing new requirements.
- Documented repository standards and applicable design decisions.
- Existing check evidence and what changes, if any, invalidate it.
- Separate standards and spec verdicts. Each finding names the violated requirement or concrete failure/risk, evidence, impact, location, and whether it blocks acceptance. Additional coverage without a material gap is a suggestion.

Independent review means a reviewer other than the implementer examines the change; it does not imply a stronger model. For consequential decisions, choose capable available review and explicit evidence. If unavailable, disclose the gap and involve the user.

## When to revisit scope

An actual trust boundary, data-loss risk, or inconsistent requirement can justify deeper investigation. State the scenario, evidence, and smallest necessary expansion. “More tests could exist” or “someone could theoretically hijack it” is not a sufficient reason alone. Do not demand private-method, source-text, or IL tests to prove ordinary public behavior.

This contract bounds obligations, not an arbitrary test count. A larger set of genuinely required behaviors needs adequate coverage; a tiny metadata change does not need a new testing framework.

## Learning checkpoint

At meaningful delivery boundaries, suggest a reusable improvement when a non-obvious technique is intended to recur, repeated user corrections reveal a pattern, or evidence invalidates guidance. Do not manufacture a lesson for every task or block acceptance on an optional improvement.

Choose the smallest useful artifact: project facts/decisions in docs or ADRs; navigation/conventions in agent instructions; deterministic repeated work in a script/check; portable judgment in a skill. Prefer correcting an existing skill to creating another owner. Propose evidence, expected reuse, target artifact, and a bounded validation check; keep incident history separate from reusable guidance and sanitize examples.

After approval, edit maintained source and report actual validation and limitations. No automatic global/cached skill edits, deployment, or commits; installation is a separate authorized action. `writing-for-agents` may help if available, but adds no required dependency.
