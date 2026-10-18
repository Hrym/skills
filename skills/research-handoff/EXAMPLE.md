# Illustrative research handoffs

These fictional examples show two sharing boundaries. They are not a required format; adapt the brief to the question and approved material.

## Question-only

**Purpose:** Understand the required retry behavior before choosing a transaction boundary.

**Question:** For PostgreSQL 16, which isolation levels can produce serialization failures, and what retry boundary does the official documentation recommend? Cite primary documentation and identify version-specific limits and uncertainty.

**Scope:** Public documentation only. Do not infer this project's implementation. No repository or private material is available. If the question cannot be answered without implementation evidence, say what evidence is missing and stop.

**Report:** Give source URLs, document/version, relevant quoted qualifiers and applicability, and enough cited excerpt to let the originating agent verify the finding offline. State which sources were actually consulted.

## Approved files

**Purpose/decision:** Determine whether the current parser handles documented format version 2 consistently with the upstream specification.

**Material approved for transfer:** Repository `sample-parser`, revision `r123`; `src/reader.ts` and `docs/format.md`. Also include the user-approved, sanitized diff `reader-change.diff` (uncommitted changes only). No other files or repository contents are in scope.

**Question and scope:** Compare those files and the supplied diff with primary upstream documentation for format version 2. Report applicable requirements, citations, quoted qualifiers, and uncertainty. Do not propose edits as approved work.

**Report:** Identify the exact supplied material and sources actually used, cite source URLs and versions with checkable excerpts, and separate evidence from recommendations. The originating agent will check findings against its current local checkout before drawing conclusions.
