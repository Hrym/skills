---
name: write-commit-and-pr
description: Use when drafting or revising Git commit messages or pull request descriptions, especially when the motivation and choice of solution must remain understandable beyond the diff.
license: MIT
---

# Write commit messages and PR descriptions

Explain why the change is needed and why this approach fits. Drafting text does not authorize staging, committing, pushing, opening a PR, or publishing a comment. Follow repository conventions and templates before these defaults.

## Establish the explanation

Read the intended change, repository instructions, relevant recent messages/template, and approved intent/spec/ADRs when available. For a PR, inspect the complete proposed range, not only the latest commit. For uncommitted work, agree the intended staged, unstaged, and relevant untracked scope; do not change Git state just to obtain a convenient diff.

Identify the problem and impact, desired outcome, chosen approach, and any non-obvious trade-off or compatibility consequence. Reuse established rationale. If it is missing, ask a focused question rather than invent motivation, measurements, attribution, issue references, or test results. If the change contradicts approved intent, surface the mismatch; do not rewrite history to justify it. Flag unrelated changes in the proposed scope without restructuring commits yourself.

**Authorial voice:** Write commits and PR descriptions as the change's author addressing future maintainers, not as an assistant reporting on a conversation. Describe the problem, decision, and evidence directly. Avoid references to “the user,” “the assistant,” or conversational approval unless that interaction is itself relevant to the change. Prefer neutral factual wording; do not invent first-person experience or broaden evidence beyond what was observed. References to actual product users remain appropriate.

## Commit message

Write a concise imperative subject describing the intended change, using the project's style. Add a blank line and explain the problem/impact, then the solution and the reason for choosing it. Include relevant constraints or verification when they explain the decision. Keep enough of the what to orient a reader, not a file-by-file diff inventory.

Wrap ordinary body prose around 72 columns, generally below 74. Preserve URLs, identifiers, and code that wrapping would break. A trivial change may need only a clear subject; do not add filler sections or enforce Conventional Commits where the repository does not use them. References supplement a self-contained explanation rather than replace it.

## PR description

Write for someone deciding whether the whole change should merge: problem and intended outcome, approach and meaningful trade-offs, actual validation and gaps, and compatibility/operational impact or follow-ups where relevant. Use the repository's template; otherwise a short Why/Approach/Validation structure is sufficient. Add diagrams only when they clarify the review. Omit irrelevant headings, not important uncertainty.

If checks were not run, say so with the known reason. A drafted PR body is not a created PR. Keep publishing as a separate authorized action.

## Check and finish

Can a reader understand the reason without reconstructing the conversation or reading every changed line? Does this read as a durable explanation from the author, rather than a recap of an assistant session? Does the text match the actual scope and distinguish evidence from expectations? Remove repeated diff narration and unsupported claims. Return the requested draft and any unresolved rationale question, then stop. See [examples](EXAMPLES.md) for shapes, not mandatory templates or current verification evidence.
