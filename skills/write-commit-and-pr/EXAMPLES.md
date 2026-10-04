# Rationale-first examples

These are illustrative writing examples, not claims about current repository changes or checks. Follow a repository's actual conventions and inspect its real diff before drafting.

## Commit: problem, solution, reason

```text
Guide developers through approved workflow transitions

Developers currently have to know which skill to invoke after design
approval. This makes onboarding depend on memorizing the workflow
and leaves the next step ambiguous.

Let the coordinator propose the next phase and reuse existing
approvals. Keep planning read-only and require separate authorization
for publishing so guided execution does not imply broader permission.
```

The subject identifies the change. The body explains the friction and why the chosen boundaries matter. It does not enumerate edited files or require the reader to open an issue to understand the motivation.

## PR: reviewer-oriented explanation

```markdown
## Why

Players should not lose access to supported saved games when they
upgrade. Game logic currently receives version-specific payloads,
making compatibility changes spread beyond the load boundary.

## Approach

Translate supported legacy payloads at the load boundary and expose
the current save model to game logic. Keep existing files unchanged
on read; unknown formats remain unsupported rather than guessed.

## Validation

Not run: this example describes a proposal, not an implemented change.

## Scope

Bulk rewriting of existing saves and recovery of corrupt files are
separate decisions. Supported legacy versions must be agreed before
implementation.
```

For an implemented PR, replace proposal language with the actual behavior and checks/results. Link the authoritative intent and relevant ADR when they exist; never invent a reference or imply an unknown API is final. The explanation should still stand on its own.

## Authorial voice: evidence, not a conversation recap

Avoid:

> The user observed a normal dispatch after giving the same corrective instruction in-session.

Prefer:

> A subsequent dispatch used normal spacing after an explicit instruction. This supports the clarification but does not establish the original cause or long-term reliability.

The revision preserves the observation and its limits without treating the author as an assistant's conversation partner. It does not invent first-person testing. Likewise, use “orchestrator-to-subagent handoffs” when describing a general handoff problem; do not imply that it is exclusive to Deep merely because it was observed there. Keep relevant test conditions explicit without turning an observation into an unsupported generalization.

## Keep small changes small

`Correct the offline installation command` can be enough for a self-explanatory typo fix. If the reason is not obvious—such as an argument changed to preserve a Windows path—explain that consequence in a short body. Do not manufacture a long problem statement.

## When rationale is absent

Ask the question that matters: “What behavior or constraint made this alternative preferable?” A plausible story inferred from code is not necessarily the author's intent. State uncertainty until it is resolved.

Writing reference: [Describe your changes](https://www.kernel.org/doc/html/latest/process/submitting-patches.html#describe-your-changes) explains problem/impact, technical response, and self-contained rationale. Repository-specific contribution processes are separate from these writing principles.
