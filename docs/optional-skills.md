# Optional skill groups

The catalogue is authoritative for source revisions, upstream paths, dependencies, and group membership. Third-party optional payloads are fetched as complete, unmodified upstream skill directories; they are not locally adapted or vendored. The separate Hrym-authored `research-handoff` skill does not modify upstream research. Default selection is `core`. When any `--group` is supplied, only those groups and their dependencies are selected: core is not added implicitly. Preview is the default; add `--apply` only after reviewing. `--all-groups` selects every group plus dependencies, and its contents grow with the catalogue.

| Exact group | Added skills | Source |
|---|---|---|
| `planning` | `to-spec`, `to-tickets` | Matt (core revision) |
| `authoring` | `writing-for-agents` | Matt (core revision) |
| `communication` | `wait-what` | Matt optional revision |
| `research` | `research`, `research-handoff` | Matt optional revision; Hrym handoff for question-only or approved repository context |
| `large-planning` | `wayfinder` | Matt optional revision; dependencies include `research`, `prototype`, `grilling`, `domain-modeling`, and `setup-matt-pocock-skills` |
| `dotnet` | `dotnet-best-practices`, `csharp-async`, `aspnet-minimal-api-openapi` | GitHub awesome-copilot |
| `dotnet-testing` | `csharp-xunit` | GitHub awesome-copilot |
| `java-testing` | `java-junit` | GitHub awesome-copilot |
| `js-ts-testing` | `javascript-typescript-jest` | GitHub awesome-copilot |
| `frontend-design` | `frontend-design` | Anthropic |
| `browser-testing` | `playwright-cli` | Microsoft |
| `documentation` | `documentation-writer` | GitHub awesome-copilot |
| `long-form-writing` | `writing-shape` | Matt optional revision |

Wayfinder also includes `research` and `prototype` as dependencies; `prototype` has no standalone group. The optional groups do not include the held `improve-codebase-architecture`, `web-design-guidelines`, or `docs-sync-audit` entries. The architecture skill is held pending a decision about bundling its mandatory CDN assets. The web design guidelines wrapper's license notice remains unresolved; [approved reference locations](reference-sources.md) describe the internal hosting approach without installing that wrapper. The documentation audit helper needs a user decision. These are held, not cancelled. React performance guidance is separately deferred.

## Source-specific notes

Use upstream skill instructions as shipped; do not use this catalogue to imply modifications or forks.

- `dotnet-best-practices` prescribes MSTest, FluentAssertions, Moq, and particular architecture conventions. These are not universal catalogue requirements. State the target project's choices in its instructions; for example, select xUnit guidance where that project uses xUnit, without changing defaults for other projects.
- `csharp-async` recommends `Task.FromException` instead of throwing in async task-returning methods. This needs qualification: ordinary `async Task` methods capture thrown exceptions in their returned task; `Task.FromException` can be appropriate for non-async wrappers returning a task. The upstream text is not patched here.
- `java-junit` says `@BeforeAll` and `@AfterAll` must be static. That is the default per-method lifecycle rule; non-static methods are permitted with an effective `PER_CLASS` lifecycle. The upstream text omits that exception and is not patched here.
- `javascript-typescript-jest` recommends resetting mocks between tests. Clearing calls, resetting implementations, and restoring spies have different effects; choose according to the project's test lifecycle. The upstream text does not make this distinction and is not patched here.

These are caveats about upstream material, not changes to it. Record relevant project choices in the project's instructions rather than assuming this human guide is automatically loaded. There is no universal xUnit choice; follow the target project's version and conventions. Nor does this catalogue require a local-only tracker: tracker prerequisites and availability depend on the selected skill and environment. Vanilla Wayfinder/research/prototype instructions include delegation, publication, or commit steps; selecting them does not grant those permissions or override host restrictions. Licensing questions about React performance material remain unresolved and separate.

## Selection examples

Preview core plus large planning (core is explicit):

```bash
python3 skills/setup-development-environment/scripts/install.py --group core --group large-planning
```

For offline use, retain the checkout/export with the installer and catalogue, and stage complete source roots for every selected source. This example explicitly supplies all six source roots; exports need no Git metadata:

```bash
python3 skills/setup-development-environment/scripts/install.py \
  --group core --group large-planning \
  --source hrym=/media/sources/hrym-skills \
  --source matt=/media/sources/matt-core-skills \
  --source matt-optional=/media/sources/matt-optional-skills \
  --source github-awesome-copilot=/media/sources/awesome-copilot \
  --source anthropic=/media/sources/anthropic-skills \
  --source microsoft-playwright-cli=/media/sources/playwright-cli --offline
```

`--offline` means only that the installer will not fetch missing skill sources. It does not assert that the host has no public Internet or that approved internal trackers, Git/package services, or model endpoints are unavailable (or available). Check access and prerequisites; do not claim every command ran without them. Offline copying itself does not require Git. Review the preview and conflicts, then repeat with the same arguments plus `--apply` only after approval. Installing browser guidance does not stage its runtime or authorize fetching it.

For cross-environment research, use `research-handoff`: it asks whether repositories/files can be shared unless already specified. Question-only is a normal supported mode when code cannot cross the boundary. It drafts a portable request and helps evaluate returned evidence; it never synchronizes or transmits anything. See [the examples](../skills/research-handoff/EXAMPLE.md).

The catalogue currently contains 32 skills in 14 groups. Use `--list` for the current selection and dependencies; group contents may change.
