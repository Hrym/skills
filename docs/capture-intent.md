# Preserve the intent behind a feature

A repository can contain correct code, a detailed specification, and sensible architecture decisions while still leaving a new reader asking: **What were we trying to achieve, and why did these choices make sense together?**

`capture-intent` preserves that explanation while a feature or architecture change takes shape. It gives colleagues a concise entry point for discussion and gives later implementers and reviewers the context they cannot recover from a diff alone. It works with the existing design process rather than replacing it.

## The gap this solves

A design conversation contains more than decisions. It contains the problem that motivated the work, the experience someone wants to improve, constraints that rule out attractive alternatives, and deliberate limits on what the change should do.

Those details can disappear when the conversation is reduced to a few ADRs or a delivery checklist:

- **A glossary** defines shared terms, not the purpose of an initiative.
- **ADRs** explain particular consequential decisions. A set of narrow decisions does not necessarily explain the larger outcome they serve.
- **A specification** describes required behavior and constraints. It may contain an excellent motivation section—or bury it under requirements.
- **Tasks and user stories** make work actionable, but a long list is a poor introduction to the overall intention.
- **A transcript** retains the conversation but asks every colleague to reconstruct it, including abandoned directions and unresolved guesses.

The answer is not more ADRs, an exhaustive story matrix, or a mandatory new document for every edit. It is a clear **intent anchor**: an authoritative explanation of purpose, desired outcome, direction, and boundaries that survives the conversation.

## Reuse first

If an approved solution brief, feature document, or spec introduction already answers those questions, use it. The skill should name and link that source, not create a competing `intent.md`.

When no adequate artifact exists, follow the project's documentation convention; the fallback is `docs/intent/<slug>.md`. For a small self-explanatory change, a short issue or task rationale may be enough. A document should earn its place by helping someone understand or judge the work.

| Artifact | Its main job |
|---|---|
| Intent anchor | Explain the problem, desired outcome, direction, and boundaries |
| Specification | Define required behavior and constraints |
| ADR | Explain a particular consequential decision and its trade-offs |
| Plan/tasks | Organize delivery |
| Verification contract | Define the evidence needed for acceptance |
| Commit/PR explanation | Explain the reason for the concrete change being reviewed |

These can link to each other. They should not repeat the same full account in several places.

## How it works with grilling

Start with an ordinary request:

> I want players to keep using supported old saves after upgrading. Help me reason about the compatibility boundary and keep the purpose understandable to someone who misses this discussion.

The coordinator can use `grill-with-docs` for unresolved design, retaining terminology and ADRs. Alongside that conversation, `capture-intent` records the emerging purpose when writing is authorized. In read-only planning mode, it drafts the brief in the conversation and identifies where it should later live.

It should not interview you again merely to fill another template. Approval of the intent belongs with design approval. Already approved decisions remain approved unless material new evidence changes them.

The result should communicate:

- The concrete problem and affected people, including developers or operators for architectural work.
- The desired outcome and observable signs of success.
- The proposed direction and the reasons it fits.
- Important boundaries and non-goals, with reasons.
- What is established, what is proposed, and what remains uncertain.
- Where to find the relevant decisions and delivery details.

Use a few representative scenarios when they clarify the experience. Do not fabricate personas, interview evidence, numeric targets, or dozens of stories to make the artifact look complete.

## Make the shape visible

Use ordinary Mermaid `flowchart` or `sequenceDiagram` syntax where a picture clarifies boundaries, responsibilities, or interactions. The intention is C4-like clarity, not a requirement to use Mermaid's experimental C4 syntax or produce every C4 level.

One diagram should answer one reader question. Label relationships with meaningful interactions. A sequence diagram can explain ordering when a static boundary view cannot. Follow the project's or user's existing Mermaid convention; a generic example is not a new styling standard.

A short example in the codebase's familiar language can make an interface or behavior concrete—C# in a C# project, for instance. Mark an example **illustrative** unless its API is an agreed contract. Do not silently turn explanatory code into an implementation requirement.

The [skill's save-compatibility example](../skills/capture-intent/EXAMPLE.md) combines concise rationale, ordinary Mermaid, and an illustrative C# shape. Rendering should use an existing approved tool when available; absent rendering evidence, say it is unverified rather than installing tools or uploading private diagrams automatically.

## Keep the explanation useful over time

Link the intent anchor from the spec and task handoffs. Review the implementation against the approved outcomes and boundaries, not only individual checklist items. Use the same rationale when [writing commits and PRs](write-commit-and-pr.md).

When intent materially changes, identify the affected decisions, requirements, and tasks, then confirm the new scope. Preserve historical ADRs through new decisions or supersession links; do not rewrite old reasoning to make it agree with whatever the code now does.

For a substantial brief, one bounded fresh-reader review can ask: “Can I explain the purpose, outcome, boundaries, and key trade-offs without the transcript?” Address concrete gaps, not every possible question. A reader check is not a second design interview or a new mandatory approval stage.

## Compatible with optional PM techniques

Research synthesis, hypotheses, opportunity trees, or a stakeholder solution brief can contribute evidence and clarify choices. They are optional activities, not prerequisites or a second workflow. If a selected PM skill produces a sufficient approved brief, that artifact can be the intent anchor.

The core installation adds `capture-intent` without additional third-party dependencies. It preserves the existing grilling and ADR process; it does not install another PM framework. The [skill instructions](../skills/capture-intent/SKILL.md) define the compact agent procedure.
