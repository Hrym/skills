---
name: finish-approved-work
description: Use when the user explicitly requests a commit, keeping a completed branch, merging or squashing locally, pushing or creating a pull request, or cleaning up an owned development workspace.
license: MIT
---

# Finish approved work

Carry out the requested delivery operation, not merely its message. Follow repository instructions and application permissions. Writing/advice alone authorizes no Git mutations.

## Establish authority and scope

Honor an explicit choice, including squash; ask only for missing decisions, not a fixed menu. Necessary local commits may be covered by a clear delivery request; ambiguous commit scope requires clarification before mutation. Publication and cleanup need applicable authorization, not assumed implementation permission.

Confirm repository, source branch/workspace, approved intent, intended changes, dirty state, exclusions, and check evidence. For integration, also identify target/base, full starting object IDs, merge-base, and workspace provenance; inspect the entire feature plus intended uncommitted content. A committed diff alone is insufficient. Preserve unrelated work in all affected workspaces. Never stage everything, automatically stash, pull, fetch, or install dependencies.

Before any Git mutation, read [integration evidence](INTEGRATION.md) for scope isolation, moved bases, conflicts, and squash coverage. Proceed only with an identified change snapshot and safe target state.

## Perform only the chosen operation

- **Keep:** report branch/workspace and state; no hidden commits, staging, publication, or cleanup.
- **Commit only:** inspect the full proposed index, commit only the authorized change with its grounded explanation, and report the result. This authorizes no merge, push, or cleanup; a remote target is not required.
- **Merge/squash locally:** integrate only intended changes into the confirmed target. Inspect any proposed commit's exact staged diff first. Use `write-commit-and-pr` for the feature-level rationale draft: a squash explains the entire feature against the correct base, never just the last worker commit. Reuse an approved message if scope is unchanged; otherwise update it. Record resulting commit/tree identities and review the integrated diff.
- **Push/create PR:** after applicable checks, push only when approved, to the confirmed remote/ref. Examine all included commits and the full target-relative diff; use the available appropriate forge tool. Drafting a body creates nothing; report a PR URL only after confirmed creation. Preserve the workspace for ongoing review unless removal was requested and cleanup gates are met.

Validate the integrated result with relevant fresh checks. Reuse evidence only while code, inputs, and environment still apply; documentation changes do not automatically require a full application suite.

On conflict, failed checks, or uncertainty, retain branch/worktree and triage or request a decision. Preserve both sides' intent where possible under the approved goal; do not invent product behavior, automatically abort, or force cleanup. An explicit abort request can be handled within authority. Ask about ambiguous scope or irreversible operations.

## Cleanup and report

Default workspace location is repository-local `.worktree/`, overridable; location is not ownership proof. Remove only explicitly owned/requested workspaces after verified integration, checking actual dirty, untracked, ignored human files and active writers. Preserve progress/unique notes outside the worktree, report the chosen path, and follow the reference's branch-deletion gate. Never force removal of uncommitted data.

Report operation, exact identities, checks/results and gaps, retained/deleted resources, workspace path/state, and recovery-record path. Explicitly say **not pushed/not published** when applicable; blocked or partial delivery is not completion.
