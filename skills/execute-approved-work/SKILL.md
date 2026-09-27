---
name: execute-approved-work
description: Use when implementing an approved requirement, specification, or task list, including resuming interrupted approved work.
license: MIT
---

# Execute approved work

Own delivery, not additional ceremony. Use available application workers and permissions; no particular model or plugin is required. Disclose unavailable independent review and agree an alternative.

## Establish the contract

Read project instructions, approved requirements, decisions, and authoritative intent; reuse adequate artifacts rather than restarting discovery. Confirm implementation authorization; design approval alone may not suffice. In a read-only planning mode, provide an in-chat draft/handoff, disclose that recovery is not persisted, and request editing mode. No file writes or worker bypass.

Establish the [verification and worker contract](CONTRACT.md), presenting it before implementation unless already approved. Reuse approved testing decisions. For multi-task work, scan dependencies, shared interfaces, and contradictions before dispatch; no mandatory pairwise table. Correct reversible technical details within approved intent and record why. Ask about behavior, scope, important trade-offs, permission, or material-risk changes.

Substantive implementation authorization includes suitable isolation. Reuse a suitable workspace; small changes may use a working branch, avoiding main by default. Default: `.worktree/<feature>/` inside the repository, overridable by project/user policy. Ensure ignored before creation using existing policy or temporary local `.git/info/exclude`; no preparatory commit, automatic dependency installs, or pulls. Preserve unrelated work; ask about unexpected/unsafe operations.

Record base revision and dirty state. Before multi-task/session work, interruption recovery, or stalled-worker handling, read [RECOVERY.md](RECOVERY.md). Keep progress outside disposable worktrees; reconcile before redispatch.

## Implement bounded slices

Do context-local work directly; delegate sustained work using CONTRACT.md. Start sequentially; parallel edits require separate ownership and safe integration. Workers neither delegate nor restart orchestration. Reports use DONE, DONE_WITH_CONCERNS, NEEDS_CONTEXT, or BLOCKED; DONE means ready for review, not acceptance. Triage before retrying; establish the previous writer stopped and transfer ownership before replacement on the same files.

Use `tdd` for meaningful new behavior/fixes at approved seams: observe failure, implement minimally, verify. Reuse behavioral tests for refactoring; use appropriate native/schema/link checks for configuration/documentation. No test padding or unrelated refactoring. Run focused checks during edits and completion checks on the stable integrated tree; reuse only applicable evidence.

Give brief user progress at meaningful task, decision, and blocker transitions, not every tool result.

## Review the actual change

Obtain independent standards/spec review at meaningful boundaries, including consequential configuration/documentation. Review shared interfaces early when needed; multi-task delivery requires final integrated review. Use `code-review` for committed ranges with exact base/head. Otherwise snapshot intended committed, staged, unstaged, and relevant untracked changes with exclusions; `base...HEAD` omits dirty work. Never auto-commit for review.

Supply contract and source evidence. Adjudicate disputed findings before fixes; distinguish blockers from suggestions. Re-review fixes and affected checks, not unchanged work repeatedly. No fixed retry count or review churn.

## Stop

Record accepted only when behavior meets the contract, required checks/reviews pass, and blocking findings resolve; record explicit authorized waivers rather than silently relaxing obligations. Report changed files, exact checks/results, limitations, and blockers.

Apply CONTRACT.md's nonblocking learning checkpoint. Git mutations, publishing, destructive actions, permission expansion, and installed-environment changes require applicable authorization. No automatic commits.

For requested message drafts use `write-commit-and-pr` if installed; writing grants no Git authority. At an authorized integration/cleanup endpoint, hand off to `finish-approved-work` if installed, with acceptance evidence and recovery location. Keep writing and integration responsibilities separate.
