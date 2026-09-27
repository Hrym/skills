# Progress, context requests, and recovery

Separate three things: what a worker reports, what the coordinator has accepted, and what can safely continue after an interruption. Treating them as one status can cause duplicate work, lost edits, or false completion claims.

## Worker reports

Implementation workers use four outcomes:

| Status | Meaning | What happens next |
|---|---|---|
| `DONE` | Assigned implementation is ready for review | Coordinator checks the actual change and required evidence/review |
| `DONE_WITH_CONCERNS` | Work is ready for review, but assumptions, risks, or checks need attention | Coordinator separates blockers from observations; required gaps need resolution or an explicit authorized waiver |
| `NEEDS_CONTEXT` | A specific missing fact or decision prevents responsible continuation | Coordinator investigates ordinary repository facts or asks you for the real decision |
| `BLOCKED` | Available tools, permissions, scope, or reasoning are insufficient | Coordinator diagnoses the obstacle before selecting a next action |

A report includes the task/workspace, partial edits, whether editing has stopped, exact checks/results/gaps, evidence locations, and the missing fact or blocker. A status label alone is not useful evidence. Review-only assignments keep their review verdict format; they do not imply implementation acceptance.

For example, a worker may report: “NEEDS_CONTEXT: the format has two legacy variants, and the brief does not say which is supported. Added the version reader; no conversion yet. Editing stopped. Which variant is in scope?” The coordinator should preserve that work and answer the question—not start a second implementation from the original prompt.

## Diagnose the obstacle

- **Missing context:** look up repository facts; ask you about product choices or authority.
- **Tool/access limitation:** use an allowed equivalent if it meets the same contract, otherwise report the blocker. A stronger model cannot bypass denied permissions.
- **Excessive scope:** narrow or split while preserving approved outcomes and ownership; ask before changing those outcomes.
- **Reasoning difficulty:** provide a counterexample or new evidence, narrow the question, or choose an available worker for a specific reason.

Stop a retry loop that produces no new evidence. There is no required ladder through every model or a quota of failed attempts to exhaust.

## A local execution record

For multi-task/session work, follow project conventions or use:

```text
<primary-checkout>/.hrym/work/<initiative>/progress.md
```

Keep it ignored and outside disposable `.worktree/` directories. Resolve and report the actual location. No database or special service is required. A short Markdown record holds authoritative intent/spec links, workspace/base/dirty state, task ownership and implementation/acceptance states, partial work, checks/review findings, decisions, and the next action.

Update it at meaningful transitions, not after every tool call. Keep intent, specs, and ADRs in their normal durable project locations; the execution record links to them rather than copying a transcript. Sharing the record through Git or an issue service is a separate choice.

In read-only planning mode, the coordinator can prepare an in-chat handoff but cannot write this file or its ignore rule. It must say that recovery has not been persisted and request an editing mode when appropriate.

## Resume from evidence

After an interruption or context compaction, the coordinator should:

1. Read the record and the current authoritative requirements.
2. Compare the recorded work with the actual branch and intended staged, unstaged, and untracked changes. A commit ID alone does not describe a dirty tree.
3. Check worker state using available native tools. An absent report does not prove a writer stopped.
4. Preserve accepted, unchanged work only while its requirements, dependencies, review, and verification assumptions remain valid.
5. Reopen affected work when those assumptions changed, then record the next action.

Before replacing a worker on the same files, establish that it has stopped and transfer ownership. If this cannot be established, pause those writes rather than create a competing writer. Do not invent a polling or cancellation mechanism that the application lacks.

## Progress you should see

Expect short updates when a meaningful task completes, a blocker appears, or a decision changes the next action. You should not need to ask “are you still working?” indefinitely, but a running commentary on every file read is not helpful either. The coordinator should use the application's actual status mechanisms and disclose uncertainty about worker state.

The [execution contract](../skills/execute-approved-work/CONTRACT.md) and [recovery reference](../skills/execute-approved-work/RECOVERY.md) contain the agent-facing details. These are a coordination protocol, not a promise that interruption recovery is infallible.
