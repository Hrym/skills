# Staying in control

An agent can spend substantial time doing things that resemble rigor without answering the actual engineering question. The remedy is not “never test” or “never worry about security.” It is to tie work to observable requirements and material risks.

## Overlapping workflows

Two installed skill collections may both claim discovery, implementation, testing, or review. They do not need to race as software processes to cause trouble: the agent can load both sets of instructions and try to satisfy both.

Symptoms include repeated design approval, a second implementation plan for already planned work, duplicate reviewer agents, or conflicting rules about when to refactor or commit. Names/descriptions affect skill selection. Identically named skills in different discovery locations introduce another ambiguity; do not rely on accidental load order.

Choose one owner per phase. This profile recommends grilling with documented decisions for unresolved design, the execution adapter for implementation, behavioral TDD at agreed boundaries, and independent standards/spec review. Superpowers is an alternative orchestration choice, not a prerequisite for OpenCode workers. Do not combine mandatory orchestration procedures accidentally.

Some skill formats support metadata that another application ignores. In particular, do not assume `disable-model-invocation` makes a skill manual-only in OpenCode. Use supported configuration, explicit standing policy, and discovery checks instead.

## Ceremonial testing

Useful tests can disagree with incorrect behavior. Tests of private method names, implementation structure, or mocks calling themselves often protect an implementation rather than a requirement.

Consider a game-input feature whose public contract says what action valid input produces and how invalid input is handled. Inspecting IL deep inside the application to prove generic input safety may add fragility without establishing that contract. It needs a concrete requirement about generated code, execution semantics, or a relevant failure that ordinary behavioral testing cannot establish adequately.

IL inspection is not categorically wrong. A compiler, runtime tool, or explicitly constrained generated-code system may need it. The question is **what property must be established here**, not whether a sophisticated test is possible.

Useful intervention:

> Test the approved behavior through the agreed public boundary. Explain any property that requires internal or IL inspection before adding those tests.

For configuration and documentation, native loading, schema, and link checks may be the right evidence. Do not build a new test harness just to perform a test-first ritual on a prose edit.

## Speculative threat models

“Someone could hijack this” is not yet a useful threat scenario. Ask what the adversary controls, how that input reaches the changed code, what consequence follows, and why that operating condition is supported or relevant.

Do not use this policy to dismiss real injection, credential exposure, or data-loss risks. A new material risk should be surfaced with evidence and a narrowly proposed scope change. It should not be silently ignored, nor should it silently turn an ordinary feature into a broad hardening project.

Useful intervention:

> Name the reachable trust boundary or observed failure. If this is optional robustness outside the contract, defer it rather than treating it as an acceptance blocker.

## Repeated checks and review churn

A full test suite after every small edit or from every reviewer can cost more than the implementation. Preserve evidence tied to the code, inputs, and environment. Reuse it while applicable; rerun affected checks after changes, and complete the agreed broader checks on the integrated tree.

Independent review is still valuable. Its purpose is to identify concrete defects or requirement gaps, not maximize findings. The coordinator should judge contested findings before commissioning another fix. A request for broader coverage without a material gap is normally a suggestion, not proof that the task is incomplete.

## Missing stop conditions

Agents can keep finding things to improve indefinitely. A verification contract should say what makes the task complete and what would justify revisiting scope.

Finish when the accepted behavior, required checks, and blocking findings are resolved. Report optional improvements separately. Do not impose an arbitrary test-count limit on genuinely complex behavior; bound obligations and reasons to continue instead.

## Confidence is not evidence

Ask for exact checks/results, source passages for consequential claims, and a review of the actual changed files. A model's configured name is not proof it ran; a passing configuration parse is not proof of account access; a summary of a source is not the source.

If checks cannot run, a source cannot be read, or independent review is unavailable, the agent should say so. You can then decide whether to gather more evidence or accept a known limitation.
