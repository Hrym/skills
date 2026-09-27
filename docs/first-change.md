# Your first change

Choose a small behavior you understand. This example adds a case-insensitive `help` command to an existing game's command-input interface. The exact files and commands depend on your project; the workflow does not.

## 1. Start with an ordinary request

Use a branch or agreed isolated workspace. In Build, ask:

> Add a case-insensitive `help` command that returns the existing help text. Keep other commands working. Show me the behavior and checks you propose before editing; leave the change uncommitted.

The coordinator should inspect the interface, tests, and existing changes, select its installed workflow skills, and propose a compact contract and implementation approach. You do not need to name or sequence skills. This request asks for a proposal before edits, so the agent should wait for your response; a direct request to implement an already clear scoped change would count as implementation authorization. In Plan mode, even an authorized request remains read-only: the agent should prepare the proposal and ask you to switch to Build for edits.

## 2. Approve behavior and verification

A suitable contract might be:

```text
Behavior: help, HELP, and Help return the existing help text.
Boundary: the public command-input interface.
Required checks: a representative mixed-case help input; existing non-help behavior.
During implementation: the focused input tests.
Completion: input tests and the project's relevant build/type check.
Non-goals: new help formatting, a new parser, private-method or IL assertions.
Reopen scope: evidence of a real trust-boundary issue or incompatible existing contract.
Done: behavior implemented, required checks pass, blocking review findings resolved.
```

Existing tests may already cover some cases. Do not demand new tests solely to duplicate that evidence. Test-first work is valuable when it establishes new behavior or reproduces a bug—not because every edit needs a ceremonial red result.

Approve or correct the proposal once:

> Approved. Implement this behavior and run the proposed checks. Keep changes uncommitted for review.

## 3. Let the coordinator assign bounded work

The coordinator may use a small implementation worker, or work directly if it already has all relevant context. It selects the installed execution and testing skills itself; a worker should get the requirement and contract, not the entire conversation. Worker selection and ordinary checks do not require another approval.

Substantive work normally uses repository-local `.worktree/<feature>/` isolation; a small change may stay on an appropriate working branch. Existing project/user preferences take precedence. This does not imply permission for dependency installs or commits.

Expect a focused failing test for the new behavior, the minimal implementation, and passing relevant checks. Do not expect a new abstraction, a security framework, or an exhaustive suite of parser possibilities outside the contract.

If a worker discovers a genuine new risk, it should explain the evidence and propose a scoped decision. If it is merely curious about additional edge cases, those can be suggestions rather than blockers.

## 4. Inspect evidence and review

The handoff should identify changed files, exact check commands/results, and any limitations. A statement such as “all good” is not enough; a complete multi-page log is usually unnecessary.

Implementation reports use [explicit statuses](progress-and-recovery.md). `DONE` means ready for review, not accepted. `NEEDS_CONTEXT` should name the missing fact or decision and disclose any partial edits; the coordinator should answer it rather than start a duplicate writer.

At a meaningful delivery boundary, independent review checks whether the change matches the specification and the repository's standards. Because this example is uncommitted, the review must include the intended working-tree changes and relevant new files. `base...HEAD` alone would omit them. The agent should not commit just to make a review command convenient.

Ask about a questionable finding:

> Which requirement or concrete failure makes this blocking? If it is optional hardening, report it separately rather than expanding the implementation.

Reviewers may identify a real defect even when the implementation follows the plan. The coordinator should evaluate it, not treat either the reviewer or the plan as infallible. Fixes need focused rechecks and review of the affected change; unchanged full suites do not need repeated reassurance runs.

## 5. Finish deliberately

Inspect the final diff and summary. When acceptance and required checks are satisfied, the task is done even though more tests or improvements could be imagined.

If you want a commit, ask explicitly:

> Commit only the reviewed files with a message explaining the behavior change. Do not push.

The coordinator uses [write-commit-and-pr](write-commit-and-pr.md) for the explanation and [finish-approved-work](finish-work.md) for the authorized Git operation. A commit-only request does not authorize merging, pushing, or workspace cleanup. You can request just a message or PR-description draft first; that alone authorizes no Git action. A tiny change does not automatically need a separate intent document if its task already explains the purpose.

For the next small change, use another short contract; explicit skill-name requests remain optional controls. For unresolved or larger design work, follow [larger features](larger-work.md).
