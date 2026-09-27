# Start here

An AI coding agent can read a project, propose changes, edit files, and run tools. That makes it useful, but a confident explanation is not evidence that its changes are correct. This setup gives the agent clear responsibilities and gives you predictable points to make decisions.

You should already be comfortable with a terminal, Git, and your project's normal build/test process. No prior knowledge of agent orchestration is required.

## The concepts

| Term | Meaning |
|---|---|
| Agent application | The program through which you work with the agent. This setup initially configures OpenCode. |
| Model | The service that generates the agent's reasoning and responses. Different models have different capabilities, availability, and costs. |
| Skill | A set of instructions and resources the agent loads for a particular kind of work. Installing one makes it available; the configured coordinator selects applicable skills, not every skill on every request. |
| Coordinator | The agent responsible for understanding the task, assigning work, judging evidence, and integrating the result. |
| Worker/subagent | A separate task-focused agent. It can use a cheaper or stronger model without changing the coordinator's model. |
| Verification contract | The agreed behavior, testing boundary, required checks, non-goals, and definition of done. |
| ADR | A short architecture decision record: a consequential choice and why it was made. |
| Intent anchor | The authoritative explanation of a feature's purpose, outcome, and boundaries. It may already be part of an approved brief or specification. |
| Execution record | Local progress and evidence used to resume multi-task work, separate from the conversation and durable project documentation. |

Skills are instructions, not enforcement mechanisms. Application permissions, a version-control workflow, and your review remain important. A worker with a read-only prompt but an unrestricted shell is not a security sandbox.

## The normal loop

1. **Clarify:** start with an ordinary request. The coordinator checks existing decisions and investigates facts; use a design interview only when decisions are unresolved.
2. **Agree:** the coordinator proposes a sized checklist or specification, plan, and verification contract before edits. An explicit implementation request counts as authorization; otherwise approve the scoped implementation once. Plan remains read-only until you switch to Build.
3. **Implement:** the coordinator handles small local work directly or assigns bounded work to suitable workers. Workers report results and evidence; they do not invent their own orchestration trees.
4. **Review:** check specification and code quality independently at a meaningful delivery boundary. Decide which findings actually block acceptance.
5. **Finish:** required checks pass, blocking findings are resolved, and remaining limitations are explicit. Committing or publishing requires your authorization.

A small change can use a short checklist. A larger feature may need a design interview, ADRs, a spec, and tasks. You need not name or sequence skills; explicit skill names remain optional controls. Missing optional planning skills can be replaced by a disclosed local draft. Publishing tasks/issues, committing, pushing, and creating PRs require separate authorization. Installing this repository alone does not load the coordinator prompt: complete [environment setup](setup-development-environment.md), validate the resolved configuration, and restart OpenCode before relying on guided handoffs.

For substantial work, keep the [intent](capture-intent.md) readable by someone who did not attend the conversation. Grilling helps reach decisions; ADRs record consequential choices; an intent anchor explains how they serve the larger purpose. Later, [commit and PR explanations](write-commit-and-pr.md) carry the relevant reasoning into review and history rather than repeating the diff.

The [recommended profile](recommended-profile.md) also covers debugging, [interrupted-work recovery](progress-and-recovery.md), and [authorized integration](finish-work.md). Expect local `.worktree/` isolation for substantive implementation, not a disposable temporary checkout, unless you choose otherwise. A worker's completion report is not the same as the coordinator accepting the result.

## What you remain responsible for

- State requirements, acceptable trade-offs, and boundaries the agent cannot infer.
- Approve permission, scope, cost, and irreversible-action changes.
- Inspect the proposed diff and evidence before accepting work. Independent model review helps but does not remove human accountability.
- Keep credentials, private data, and restricted code within the environments/providers you are allowed to use.
- Stop an expanding task. Ask which requirement or concrete risk justifies extra work.

Model calls can cost money, including reasoning that is not printed in the response. A smaller model is not automatically cheaper per completed task if it needs many retries. The routing defaults are a starting point, not a bill-saving guarantee.

## Why this workflow is deliberately restrained

Agents can duplicate design interviews, rerun full suites after tiny edits, test private internals instead of behavior, or add hypothetical hardening unrelated to the task. Those activities can look rigorous while making the result slower and more complicated. This setup selects one owner per phase and makes verification scope explicit without dismissing genuine risks.

Read [staying in control](staying-in-control.md) for examples. Then [set up the environment](setup-development-environment.md) and follow [your first change](first-change.md).
