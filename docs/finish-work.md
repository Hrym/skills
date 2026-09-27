# Finish and integrate approved work

`write-commit-and-pr` explains a change. `finish-approved-work` performs a requested Git delivery operation. Neither grants the other automatic authority: drafting a PR body is not publishing, and completing implementation is not permission to merge.

## Make the operation clear

Ordinary requests are sufficient:

> Commit only the reviewed change on this branch. Do not merge or push.

> Squash this feature into main locally and complete its worktree. Do not push.

> Draft the PR description, but do not create the PR or modify Git state.

> Keep the branch and worktree; I will review them later.

The coordinator should honor an explicit choice rather than present the same menu again. It asks only about missing scope or authority. A commit-only request needs no remote/merge target and authorizes no later integration or cleanup. A clear integration request can include necessary local commits for that operation; ambiguity about intended content still needs clarification.

## Review the whole feature

Before mutation, establish the repository, target/base, source branch, workspace ownership, and intended change. Inspect relevant dirty and untracked content as well as committed work. Preserve unrelated edits and pre-existing staged changes. Never stage everything merely because a helper says to finish a merge.

For a squash, use a rationale-first message for the entire feature relative to the correct target—not the latest worker commit. Reuse an approved message if the scope is unchanged. When the target has advanced, preserve its unrelated fixes and inspect the actual integrated result; simple source/target tree equality is not always the correct test.

There is no automatic pull, fetch, dependency installation, or push. If remote freshness is necessary and not known, the coordinator should ask before obtaining it and not pretend a local tracking reference proves the current remote state.

## Validate before cleanup

Verify the integrated result with relevant checks, reusing evidence only while its code/inputs/environment remain applicable. Documentation work does not automatically require an unrelated full application suite.

Conflicts or failed checks preserve the branch/worktree while they are investigated. Preserve both sides' intent where possible; ask about conflicting product choices rather than invent behavior. Neither automatic abort nor automatic continuation is the default. An explicit abort request is handled within its authority and with attention to what would be discarded.

## Clean up only owned resources

The recommended worktree path is repository-local `.worktree/<feature>/`, but a matching path is not proof of ownership or permission to remove it. Check Git/native workspace records, writer state, and tracked/untracked/ignored human-authored material.

Preserve unique notes and recovery evidence outside any workspace being removed, usually in the project's ignored execution-record location. Confirm and report the retained path. Do not force-remove uncommitted material because it is inconvenient or ignored.

After a squash, Git may not recognize the feature as merged by ancestry. Deleting the completed branch reference requires coverage evidence for all intended work and appropriate authority; resetting the branch or fabricating ancestry to make deletion succeed is not a solution. If coverage or ownership is uncertain, keep it and ask.

For a published PR, keep the workspace for review by default unless removal was requested and cleanup conditions are satisfied. Report an actual PR URL only after creation, not for a draft.

## Completion report

Expect the performed operation, resulting commit/ref, checks and gaps, what was retained or removed, the recovery-record location, and whether anything was pushed/published. A blocked or partial integration should not be reported as complete.

See [the finishing skill](../skills/finish-approved-work/SKILL.md) and its [integration reference](../skills/finish-approved-work/INTEGRATION.md) for the operation and evidence boundaries.
