# Write commit messages and PR descriptions

A diff shows what changed. It rarely explains the problem that made the change necessary, why one approach was chosen, or which trade-off a reviewer should preserve in a later refactor.

`write-commit-and-pr` drafts that explanation from the actual change, repository conventions, and approved intent. It covers both Git commit messages and pull request descriptions without making their formats identical.

## Start from evidence, not a plausible story

The agent should inspect the intended change and its rationale. For a PR, that means the complete proposed range, not just the latest commit. For uncommitted work, it means the agreed staged, unstaged, and relevant untracked files—not an assumption that `HEAD` contains everything.

An [intent anchor](capture-intent.md), issue, or ADR can supply the reason. If the reason is missing, the agent should ask a focused question. It should not infer an attractive justification from the code and present it as an established decision.

If implementation and approved intent disagree, resolve the discrepancy before describing the change as complete. Do not rewrite the original rationale after the fact merely to make the diff look intentional.

## Commit messages: durable explanation

Use the repository's established style. Otherwise start with a concise imperative subject, a blank line, and a body that explains the problem/impact followed by the chosen solution and its rationale.

```text
Guide developers through approved workflow transitions

Developers currently have to know which skill to invoke after design
approval. This makes onboarding depend on memorizing the workflow
and leaves the next step ambiguous.

Let the coordinator propose the next phase and reuse existing
approvals. Keep planning read-only and require separate authorization
for publishing so guided execution does not imply broader permission.
```

The subject orients the reader to what changes. The body explains why the behavior and boundaries matter without enumerating the files already visible in the diff.

Wrap ordinary body prose around 72 columns, generally below 74, so indented Git output stays readable. Preserve long URLs, identifiers, and code when wrapping would damage them. Follow scope prefixes or other repository conventions when present; do not impose a new commit taxonomy as part of drafting.

A self-explanatory typo fix may need only a clear subject. Conversely, a small diff can need a substantial explanation when its reason is subtle. Length should follow the reasoning a future reader needs, not the line count of the patch.

## PR descriptions: help someone judge the whole change

Follow the repository's PR template. Otherwise cover:

- **Why:** the problem and intended outcome.
- **Approach:** how the change addresses it and the material trade-offs.
- **Validation:** checks actually performed, their results, and remaining gaps.
- **Impact or follow-ups:** compatibility, operational considerations, or deferred work when relevant.

Link the intent, issue, or decision record when useful, but make the explanation understandable without following every link. Diagrams are optional aids, not mandatory decoration. Omit irrelevant sections instead of filling them with boilerplate.

Do not claim tests passed because an example template says so. If checks were not run, state that and the known reason. Do not invent measurements, references, or attribution. The [skill examples](../skills/write-commit-and-pr/EXAMPLES.md) are illustrations, not verification evidence for another change.

## Use it through the guided workflow

You can ask in ordinary language:

> Draft a commit message for the reviewed change. Explain the problem and why we chose this approach. Do not commit yet.

Or:

> Draft the PR description for this branch against main. Include the reason, approach, actual validation, and any compatibility concerns. Do not create the PR.

The coordinator selects `write-commit-and-pr` when available. Drafting text does not authorize staging, committing, pushing, or creating a PR. Those are separate actions governed by your instructions.

The skill is portable and adds no third-party dependencies. See [its instructions](../skills/write-commit-and-pr/SKILL.md) for the agent procedure. The [kernel change-description guidance](https://www.kernel.org/doc/html/latest/process/submitting-patches.html#describe-your-changes) is useful further reading on explaining the problem and technical response; project contribution processes remain separate.
