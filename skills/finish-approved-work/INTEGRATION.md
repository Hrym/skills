# Integration evidence and safe cleanup

This is decision guidance, not an executable recipe. Substitute actual repository facts; the example identities below are illustrative, not check evidence.

## Identify the work before changing state

For a commit-only request, establish the current repository/branch and intended index/change; do not demand a remote or merge target. Apply the scope-isolation rules below, but skip integration-specific base and cleanup steps. Report the commit without silently merging, publishing, or removing its workspace.

Distinguish the approved feature's original base, its merge-base with the target, and the target's current tip. Record their full object IDs, the source tip, repository identity, workspace paths, and target/source refs. Inspect local tracking configuration without silently refreshing it. If remote freshness is necessary but unknown, request authorization to check it rather than claiming the local view is current.

Review all included commits, staged and unstaged diffs, and the contents of relevant untracked files. Record intended paths/hunks and exclusions, including pre-existing staged changes. A three-dot committed diff omits dirty work; a two-tip tree diff can also include target-only changes when the base advanced. Neither alone proves feature scope. Capture the reviewed snapshot with exact commit/tree IDs and, for uncommitted content, a retained scoped patch or content identities. Store sensitive material only in an approved local location.

Only selected paths/hunks may enter a necessary commit. Check the entire proposed index, not merely the newly staged paths: pre-existing staged changes can otherwise leak into the commit. If intended and unrelated edits cannot safely be separated, stop for a scope/isolation decision. Do not silently unstage, move, stash, or commit someone else's work. Check the target workspace too; use a suitable authorized isolated workspace or ask if integration would disturb it. Reconfirm refs and state immediately before mutation; unexpected movement or writers invalidates the snapshot.

## Illustrative squash with a moved base

Suppose feature `F` started at base `B`, but target now points to `T`, which contains another developer's fix. The feature also has an intended unstaged documentation change and an unrelated untracked notebook.

The approved squash request is already the operation choice. Include the intended dirty change only within clear commit authority; leave the notebook untouched. Explain the whole feature from `B` through the reviewed feature snapshot, then reconcile with `T`. Review the integrated result `R` against `T`: the feature must be present and the target fix preserved. Do not overwrite `T` with the source tree or use the latest worker commit as the message scope. If target movement changes the effective feature, update the explanation and affected verification; ask when intent is ambiguous.

Record `B`, `F`, `T`, the scoped dirty-content evidence, `R` and its tree, the actual reviewed integration diff, and applicable checks with commands, exit codes, and logs when available. Recheck the final state after hooks/checks that might alter files. This ties acceptance to content, not merely a branch name or successful Git exit status.

## Conflicts and failed verification

Inspect the common ancestor and both sides to identify why each changed. Preserve compatible intent from both within the approved goal, stage only resolved in-scope changes, and rerun affected checks on the integrated result. Escalate conflicting product choices or uncertain scope. On unexpected conflicts or failed checks, preserve the current operation state and recovery evidence while triaging; neither automatic continuation nor automatic abort is the default. If the user requests abort, inspect what it would discard and act only within that authority, protecting unrelated edits. Never clean up a failed integration as though it succeeded.

## Workspace and branch gates

Establish provenance from Git worktree registration and native/external workspace-tool records or explicit user confirmation. A matching `.worktree/` path alone proves neither ownership nor disposability. Identify active writers through available application/tool state; if ownership or quiescence cannot be established, retain and ask. Respect the managing tool's lifecycle rather than bypassing it with directory deletion.

Inspect actual tracked modifications, all untracked files, and ignored contents before removal. Unique notes and progress are not disposable merely because ignored. Preserve them outside every workspace being removed, preferably the durable repository's local ignored `.hrym/work/<initiative>/progress.md` or the project's chosen alternative. Verify that location is retained and ignored, verify preserved content, and report its actual path. If its status is uncertain, retain the workspace rather than automatically committing notes or discarding them as cache.

Verified integration must cover every intended change, including formerly uncommitted content. After a squash, ancestry may not mark the feature branch merged. Whole-tree equality is useful when identical final trees are expected; with an advanced base, use the actual reviewed integration diff and intent/check evidence that account for both feature and target changes. Matching commit subjects, patch identifiers, or a successful squash alone are insufficient.

Workspace removal and branch-reference deletion are separate decisions. Recheck branch identity and coverage before deleting the reference, including any subsequent commits. Use an authorized safe operation; if ancestry-based deletion refuses after squash, explain the coverage evidence and request specific permission for reference deletion if no permitted safe operation exists. Never reset the branch or fabricate ancestry to make `-d` pass. Reference deletion after verified coverage is distinct from discarding unmerged work; without coverage, retain the branch and ask. Never use `--force` to remove a workspace containing uncommitted data.
