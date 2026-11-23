---
name: capture-intent
description: Use when a feature or architecture change needs a durable purpose and boundary for colleagues who will not have the discovery transcript, or when material new evidence changes an existing intent.
license: MIT
---

# Capture intent

Keep the **why** legible without the conversation. This is a purpose anchor, not another interview, plan, or approval ceremony. Follow project documentation conventions first.

## Locate the anchor

Read the task, approved brief/spec introduction, glossary, and ADRs. Reuse and link an artifact that explains purpose, outcome, boundaries, and tradeoffs; a trivial change may need only its task rationale. Otherwise follow the project's location convention, defaulting to `docs/intent/<slug>.md`. Link authoritative specs, ADRs, and tasks instead of copying them. ADRs explain decisions and their history; glossaries define terms, not overall purpose.

## Write the minimum useful brief

Capture the concrete problem and audience (including affected maintainers or operators), desired outcome, direction and rationale, boundaries and non-goals with reasons, observable success signals, and key uncertainties. Distinguish user-provided evidence, approved decisions, and proposals; never fabricate interviews, measurements, or targets. Use representative scenarios only where they clarify scope or tradeoffs. Adapt the prose; headings are optional. [An illustrative brief](EXAMPLE.md) is neither template nor contractual API.

Make durable decision prose understandable without the interview: name the question or issue, the settled outcome, and the key conditions and known rationale. Keep proposals, deferrals, and missing rationale explicit. Use the existing spec, outline, issue, or ADR that owns the decision; link it from the intent anchor rather than duplicating it. Q IDs are optional traceability, not substitutes for meaning; references that require the question must link to saved question text. No full transcript or exhaustive duplicate Q&A log is required. When a decision changes, reconcile the current summary and mark or link superseded history so its former status cannot read as current.

When authorized, capture emerging purpose incrementally. In read-only mode, draft in conversation and identify its destination; do not edit. Existing approval counts: check intent alongside design approval, without an extra gate. For unresolved design, recommend the configured workflow (e.g. `grill-with-docs` where installed); if settled, record without restarting questioning. Product-management techniques are optional evidence sources, not required stages or dependencies.

## Use visuals selectively

If one focused view clarifies scope, boundary, responsibilities, or directional interactions, use the project's or user's Mermaid convention. Until one is supplied, ordinary Mermaid `flowchart` or `sequenceDiagram` syntax is enough; label interactions and do not invent a styling standard. Examples of code should use the project's language and be marked illustrative unless an API is approved. Use only an existing approved renderer; otherwise state that rendering is unverified. No external upload is needed.

## Reconcile and stop

When intent materially shifts, identify affected design, ADRs, specs, and tasks; ask for an impact and approval check before treating the change as approved. Add a new decision or supersession link where needed instead of rewriting old rationale to fit code. For substantial briefs, a bounded fresh-reader pass can expose missing purpose or ambiguous boundaries without interviewing anew. Stop when a colleague can explain purpose, outcome, boundaries, and tradeoffs without the transcript, and missing decisions are explicit. Report what was reused or written and what remains uncertain.
