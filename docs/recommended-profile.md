# The recommended development profile

This profile covers ordinary development from an initial request through design, implementation, diagnosis, review, and authorized integration. It selects one owner per phase rather than installing every available workflow. The coordinator guides transitions; you supply decisions and authority, not a sequence of skill names.

## Default core

The catalogue resolves the core group to fourteen skills:

| Responsibility | Skill |
|---|---|
| Environment installation and migration | `setup-development-environment` |
| OpenCode roles, models, permissions, and standing policy | `setup-opencode-routing` |
| Design interview with retained terminology/decisions | `grill-with-docs`, using `grilling` and `domain-modeling` |
| Interface and testing-boundary vocabulary | `codebase-design` |
| Durable purpose without another interview | `capture-intent` |
| Bounded execution, worker recovery, and acceptance | `execute-approved-work` |
| Behavioral testing at agreed seams | `tdd` |
| Investigative bugs and performance regressions | `diagnosing-bugs` |
| Independent standards/spec review | `code-review` |
| Rationale-first change explanation | `write-commit-and-pr` |
| Authorized Git integration and owned-workspace cleanup | `finish-approved-work` |
| Project tracker and domain-document conventions | `setup-matt-pocock-skills` |

An installed capability is not a mandatory stage for every change. An obvious bug with a reproduction can go through ordinary execution; a hard-to-explain failure may need diagnosis. A typo does not need an architecture interview. An existing adequate specification can already be the intent anchor.

## Additional catalogue groups

| Group | Contents | Use |
|---|---|---|
| `planning` | `to-spec`, `to-tickets` and dependencies | Larger work benefiting from explicit specs/tasks; publishing requires authorization |
| `authoring` | Matt's `writing-for-agents` and its resources | Maintaining skills and agent-facing instructions |

For this skills repository, `core` plus `authoring` is a useful selection. No Superpowers authoring or additional TDD dependency is needed. Use `--group core --group authoring`; optional groups do not implicitly include core. See [setup](setup-development-environment.md).

Other tools—prototyping, triage, long-horizon planning, research reports, learning aids, and PM techniques—may be valuable for particular work, but are not promised by the shipped catalogue merely because they exist upstream. Review their prerequisites, scope, side effects, platform support, and conflicting owners before adding them.

## Behavior you can rely on asking for

The coordinator should:

- Reuse approved intent, decisions, and testing scope rather than repeat discovery.
- Check whether real design choices have been considered, relevant interfaces/data/error behavior are covered, and the plan is internally coherent. These are readiness checks, not another compulsory interview.
- Correct reversible implementation details within intent and record why. Ask about changed behavior, scope, material risk, important trade-offs, or authority.
- Use repository-local `.worktree/<feature>/` isolation for substantive work, unless you or the project chooses another location. Reuse suitable workspaces and keep their contents ignored; no automatic preparatory commit or dependency installation.
- Keep [recoverable progress](progress-and-recovery.md) for multi-task/session work, separate from public project intent/specs/ADRs.
- Judge worker evidence and review before accepting work. `DONE` from a worker is not acceptance.
- Review coherent changes and consequential interfaces, with a final integrated review for multi-task work. Re-review affected fixes rather than restart unchanged work.
- Stop retries when they cease producing new evidence and propose a next action.
- Perform Git/publication/cleanup actions only under applicable authorization, preserving unrelated work and unique local notes.

These are instructions and permission boundaries, not a guarantee that every model follows them. Use actual evidence and intervene when the behavior diverges.

## Debugging without a second implementation framework

`diagnosing-bugs` contributes a tight reproduction or measurement loop, falsifiable hypotheses, targeted probes, and a regression test at a valid seam. It does not replace the coordinator or authorize wider testing by itself.

The profile explicitly bounds its aggressive upstream suggestions: reuse existing evidence, do not pad hypotheses to a count, run stress/instrumentation only within scope and authority, and stop when attempts stop teaching anything. If a useful reproducer cannot be obtained, explain what is missing rather than guessing at a fix or building an endless harness.

A straightforward failure needs only enough investigation to justify the fix and checks. Diagnosis results feed the approved execution contract, not another nested orchestration chain.

## Preventing overlapping workflows

The template includes per-agent skill denials for Build/Plan, and the stronger-primary example applies the same selection. They keep alternative brainstorming, implementation, TDD, review-orchestration, finishing, and writing owners from taking over this profile. The exact list is in the [configuration template](../skills/setup-opencode-routing/templates/opencode.jsonc).

Review those permission changes before applying them. They do not remove another profile, uninstall files, or stop a bootstrap plugin from injecting instructions. Inspect global/project configuration and all active skill locations; removing a plugin reference alone does not remove separately installed copies. `disable-model-invocation` metadata is not a dependable manual-only boundary in OpenCode.

For example, Matt's merge-conflict skill can be useful under a deliberate recovery workflow, but its raw instructions stage everything and finish the operation. It is not part of this profile's core. A user can select another workflow when appropriate; the goal is explicit ownership, not a permanent ban on useful alternatives.

## Models and cost

Keep the [quality-first role bindings](setup-opencode-routing.md#what-gets-configured): GPT-5.6 Sol for standard coordination/implementation, GPT-6 Luna for bounded work, GPT-6 Sol for dense-source research, and optional Astra for difficult architecture/implementation. Same-model advice is still useful without Astra, but is not a capability upgrade.

Process controls and model selection solve different problems. More reasoning cannot supply a missing permission, and a cheaper worker is not cheaper per completed task if it repeatedly fails.

## Continuous improvement, not continuous scope growth

At meaningful completion, the coordinator may recommend preserving a reusable method or correcting existing guidance when evidence and expected repetition justify it. The current task can still finish. New skill/script work and deployment require their own authorization. See [improving reusable guidance](improving-skills.md).
