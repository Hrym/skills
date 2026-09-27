# Routing design

The goal is **lower cost per correctly completed task**, not maximum delegation or the lowest-priced model on every request. The setup combines stable agent roles, environment-specific model bindings, and a coordinator responsible for integration.

The [user guide](setup-opencode-routing.md) covers installation and the shipped role table. This document explains the policy: why work is divided this way, where the approach can fail, and what to measure before changing it.

## Separate roles from models

A role describes responsibility and permissions: discover sources, implement a bounded change, run checks, or advise on architecture. A model binding selects the available model for that role. Keeping those concepts separate makes the setup portable without pretending every environment has the same capabilities.

The quality-first example uses GPT-6 Luna for economical bounded work, GPT-5.6 Sol for standard coordination and ordinary implementation, GPT-6 Sol for dense-source research, and optional confirmed GPT-6 Astra for difficult design and correctness questions. These are role-specialized starting points, not a universal capability ranking. If Astra is unavailable, a fresh standard-model advisor offers separate context and independent checking—not an upgrade in underlying capability. Users prioritizing price may evaluate GPT-6 Sol for standard coordination/implementation instead, based on their own workloads.

The coordinator selects from configured agents. It does not switch its own model merely by recommending another one. Configuration, recommendation, runtime self-report, and recorded execution metadata are different kinds of evidence.

## Decide whether to delegate before selecting a worker

A new worker needs instructions, tool definitions, an assignment, and a handoff. For an obvious edit already in the coordinator's context, those costs can exceed the cost of acting directly. Conversely, answering a small question may require substantial discovery that benefits from an isolated, cheaper context.

Delegate sustained, bounded work or work that benefits from context isolation. Batch related changes sharing one outcome. Route by ambiguity and correctness risk rather than line count: a short concurrency fix can be harder than a large mechanical edit.

Direct tool concurrency is a separate choice. Independent reads or safe commands can run together without additional agents, but their outputs are still interpreted by the coordinator. Do not overlap writes, shared build state, or operations whose inputs depend on earlier results.

## Use explicit escalation triggers

“Ask for help when unsure” is insufficient because the coordinator can be confidently wrong. Architecture consultation is triggered by changes to shared interfaces, persistence formats, subsystem boundaries, concurrency/lifecycle constraints, competing designs, contradictory architectural evidence, or repeated failed fixes. Dense conflicts among source qualifications can go to the researcher without involving the architect.

The advisor receives original constraints and relevant evidence, not merely the coordinator's favored solution. Use a stronger primary coordinator when task decomposition and integration are themselves globally difficult. A separate advisor is not mandatory when an equally capable coordinator can handle the design directly, unless independent review or context isolation is required.

When no stronger model exists, narrow the question, gather decisive evidence, and return unresolved choices to the user. Escalation is not a license to retry unavailable models or speculate through a long sequence of fixes.

## Keep delegation flat and permissions explicit

One coordinator owns requirements, task boundaries, conflicts, verification, and integration. Workers return blockers rather than creating their own delegation trees. This makes scope and escalation easier to reason about and reduces repeated handoffs.

Plan delegates only to read-only `explore`, `researcher`, and `architect`. Implementation, verification, evidence interpretation, and architecture advice are separate roles because they need different permissions. In particular, a worker with a “just advise” instruction but editing tools is not the same boundary as a read-only advisor.

Permissions do not replace operational judgment. A verification worker's shell can create artifacts or modify files even when edit tools are disabled. Custom tools need their own review. These controls are not a filesystem sandbox.

## Keep noisy verification out of the coordinator when useful

Large build/test logs can dominate a conversation. A verification worker can inspect them and return exact commands, exit codes, completion status, test totals, decisive failures, and log locations instead of the entire transcript.

Reduce output first: use concise reporters and targeted log inspection while preserving the full log when practical. Retain real exit status through pipelines. A truncated preview or timed-out command cannot establish success. Verify a stable working tree and rerun affected checks after edits.

A slow command with three lines of output may be better run directly; a fast command with thousands of lines may benefit from isolation. The relevant cost is not just elapsed command time or tool-call count.

Delegation moves work to another context rather than eliminating it. Net savings depend on startup instructions, worker reasoning, summary size, retries, caching, and the harness's transcript handling. Repeated context may receive cache discounts, so included tokens are not necessarily charged at the full input rate on every request. See [OpenAI prompt caching](https://developers.openai.com/api/docs/guides/prompt-caching) for its conditions.

## Discover cheaply; verify decisive evidence

For routine contextual lookup, the coordinator reads directly. Broad straightforward local-document or web discovery goes to Luna `explore` for an evidence index. Dense specification or web-source interpretation goes directly to GPT-6 Sol `researcher` for a bounded answer and decision-ready evidence:

- The claim or question being supported.
- URL/section or file/line range.
- A short excerpt preserving relevant headings, table headers, and qualifiers.
- Source authority and version/date or local revision, applicability, exceptions, conflicts, and caveats.
- Search scope, access gaps, uncertainty, and important original passages for the coordinator to inspect.

The coordinator opens decisive original passages before relying on them. For consequential decisions it independently checks for omitted exceptions and conflicting evidence. A relevant-source shortlist reduces reading cost but cannot establish completeness. Inaccessible material remains unverified.

No compulsory Luna → researcher → coordinator → Astra chain: source volume alone does not justify architecture advice. Consult `architect` for difficult architectural implications when warranted. Researcher cannot delegate or escalate itself; it reports blockers. This separates discovery, verification, and interpretation without automatically adding stages or test ceremony.

## Treat effort as a setting, not a capability label

The supplied variants use low effort for focused discovery/log triage, medium for ordinary coordination and bounded implementation, and high for complex reasoning. They are hypotheses to evaluate on representative work, not universal optima.

Higher effort is not a fixed token budget, free additional quality, or equivalence to a stronger model. OpenAI bills reasoning tokens as output tokens. Provider integrations may expose different variants, and a textual instruction to think harder does not demonstrate a changed API setting. See the [reasoning guide](https://developers.openai.com/api/docs/guides/reasoning) and [OpenCode configuration schema](https://opencode.ai/config.json).

Avoid adding a worker for every model/effort combination. First identify a recurring failure or inefficiency. Add Terra or another alternative only if matched-task trials show a repeatable quality, latency, cost, or access benefit. Obtain approval before paid experiments or changing provider/account assumptions.

## Keep runtime prompts compact

Use concise grammatical instructions and evidence-bearing handoffs. Remove repeated explanations and process recaps, not uncertainty, conditions, negations, exact errors, or useful progress updates. Runtime workers need their role contract, not the entire setup guide or conversation history.

The harness, tool definitions, loaded skills, and task material also consume context. Compressing a prompt helps, but starting many tiny sessions or rereading a large log can outweigh those savings. Review worker results proportionately rather than repeating their entire process.

## Preserve workflow obligations

Generic worker requests map to the appropriate configured role rather than unconditionally to `general`. Workflow ownership is explicit: approved design is not re-interviewed, the execution adapter coordinates delivery, and workers do not start additional orchestrators. Native OpenCode delegation needs no orchestration plugin.

The verification contract carries observable behavior, public test boundaries, required cases/checks, non-goals, scope-reopening conditions, and completion criteria. It lets the coordinator and reviewers distinguish material gaps from optional improvements. See [staying in control](staying-in-control.md) for practical examples.

Passing tests do not establish every requirement. Cheap execution followed by an expensive full reconstruction may erase savings; skipping review to avoid that cost sacrifices the goal. The useful middle ground is bounded assignments, concrete evidence, and targeted independent review where required.

## Evaluate outcomes, not routing activity

Separate four checks:

1. **Configuration:** files parse and roles, variants, and permissions resolve correctly.
2. **Access:** the intended provider/account can invoke the selected model.
3. **Execution:** available session/provider metadata establishes what actually ran.
4. **Outcome:** representative tasks finish correctly at acceptable cost and latency.

A route passing the first check does not establish the others. Model descriptions and prices help choose candidates; they do not prove that this combination beats alternatives.

When evaluating a change, keep tasks, tools, context, and acceptance criteria comparable. Record correct completion, review findings, retries, user intervention, elapsed time, and total billed usage including reasoning and caching. Preserve failures as well as successes. Do not infer completed-task savings from token prices alone.

Use current [OpenAI pricing](https://developers.openai.com/api/docs/pricing) or [Copilot pricing](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing) for the actual provider/product. Avoid freezing a price table into permanent routing rules.
