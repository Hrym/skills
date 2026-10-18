# Environment setup reference

## Installation versus configuration

The Python installer copies skills. It does not configure OpenCode, remove plugins, install Python/Git, log in to providers, or execute downloaded skill scripts. The setup agent performs approved configuration merging separately using `setup-opencode-routing`. That setup asks separately about opt-in Deep even if Astra workers are approved; preserve previously explicit Deep choices unless the user asks to change them. Project tracker/domain setup is a third explicit step, not a side effect of copying skills.

The complete distribution is this directory: `SKILL.md`, this reference, `catalogue.json`, `scripts/install.py`, and `LICENSE`. It can be installed independently; other recommended skills come from declared source repositories, not assumed sibling directories.

## Prerequisites and commands

Python 3.10+; no pip/npm dependencies. Git is required only for source fetching. OpenCode and confirmed provider access are needed for subsequent agent use, not for copying offline skills. On Windows use a real Python installation (`python --version` or `py -3 --version`); Git Bash does not bundle Python.

From a repository checkout:

```bash
python3 skills/setup-development-environment/scripts/install.py --list
python3 skills/setup-development-environment/scripts/install.py
python3 skills/setup-development-environment/scripts/install.py --apply
```

Use `python` or `py -3` instead of `python3` when appropriate on Windows. The script defaults to `core` only when no `--group` is supplied. For both groups, use `--group core --group planning`. Repeated groups form a union; dependencies are included automatically. `--list` never fetches sources. Preview may fetch into temporary storage but does not modify the destination.

For maintaining skills, select `--group core --group authoring` (add `--group planning` if needed). `authoring` adds only Matt's `writing-for-agents` and its resources. It requires no Superpowers plugin, secondary TDD skill, Node package, or external renderer. Skill execution may use the host's already available tools; an authoring installation is not authorization to edit installed/global skills.

## Sources and offline mode

`catalogue.json` defines source IDs, Git URLs/revisions, relative skill paths, dependencies, purposes, and groups. The Hrym and Matt core sources retain their existing refs; four optional source roots are pinned separately (including a distinct Matt optional revision). Remote fetching reports the resolved commit. Update a trusted catalogue's `ref` to an approved commit if exact repeatability is required.

The default Hrym source uses SSH and may require repository access. The script recognizes its own Hrym checkout automatically. A copied skill or exported repository without `.git` must be given `--source hrym=PATH`; do not infer a repository from an arbitrary parent directory. The checkout containing the installer and catalogue is still needed for offline use. `--source` overrides point to repository roots, not the installed flat skills directory. Existing local files take precedence and are reported as local/unverified, even when a catalogue contains a remote pin. They are not pulled or rewritten. `--offline` means only that source repositories will not be fetched; it is not a claim that the host has no public Internet and does not block approved internal trackers, Git/package services, or model endpoints.

```bash
python3 skills/setup-development-environment/scripts/install.py \
  --source hrym=/media/sources/hrym-skills \
  --source matt=/media/sources/matt-core-skills \
  --source matt-optional=/media/sources/matt-optional-skills \
  --source github-awesome-copilot=/media/sources/awesome-copilot \
  --source anthropic=/media/sources/anthropic-skills \
  --source microsoft-playwright-cli=/media/sources/playwright-cli \
  --destination "$HOME/.agents/skills" --offline
```

Add `--apply` after reviewing. On Windows, quote Python-compatible paths, for example `--source "matt=C:/Skill Sources/matt-skills"`. In Git Bash, `cygpath -m "$HOME/.agents/skills"` can produce a Windows path when passing an explicit destination. Otherwise the default is Python's home directory plus `.agents/skills`.

Local roots must contain the paths and source licenses named by the catalogue, including the two separate Matt revisions and their categorized `skills/engineering/`, `skills/productivity/`, and `skills/in-progress/` directories. Transfer complete trusted repository snapshots for convenience; the example supplies all six source roots explicitly. An export without Git metadata works because offline installation copies files only. Offline mode never fetches missing material; it reports the required `--source` argument. Offline installation does not supply an offline model endpoint or credentials. Approved internal trackers and services may remain available in an Internet-isolated environment; do not assert they are usable without checking prerequisites and access.

`--catalogue PATH` selects an alternative trusted catalogue with the same schema. Use it for reviewed mirrors, revisions, or a different source layout. Do not solve missing content by silently modifying the approved group selection.

## Conflicts, updates, and backups

All selected sources/payloads and target conflicts are checked before destination writes. Entire skill directories, empty directories, supporting files, and a source-root `SOURCE-LICENSE` are retained. `SOURCE-LICENSE` is reserved for that attribution; a differing existing source file of that name is an error.

Identical payloads are left unchanged. A differing directory aborts installation by default; preview it first, then use `--replace --apply` only after approval. Symlink targets and non-directory targets are not replaced by this installer. Handle such installations through their owning manager or an explicit manual migration.

Replacement moves old directories into uniquely named backups under `~/.hrym/skill-backups/` before copying new payloads. `--backup-dir PATH` overrides the root; it must be outside the destination and directories named `skills` so backups are not mistaken for active skills. Account for any custom discovery paths as well. Unrelated installed skills are untouched. Review output for actual backup paths.

Preflight avoids ordinary partial installation from missing sources/conflicts, but multi-directory writes are not crash-atomic. On a write failure, inspect the reported installed and backup paths before retrying. To undo, restore the applicable backups and remove only newly installed directories you intended to remove; do not overwrite subsequent local edits. Configuration changes require their separate configuration backup. Restart after changes.

## Upgrade an existing installation

Updating this repository does not update installed skills or active application configuration. The repository is the source of truth for its managed skills and prompts; install them exactly unless an explicit override is approved. Application configuration retains environment-specific bindings and settings. Upgrade these separately.

1. **Inspect:** identify the installed skill destination, selected groups, source revisions, and local edits. Locate active OpenCode configuration and discovery scopes, including project overrides and environment-selected configuration directories. Record the currently resolved prompts, model bindings, permissions, and enabled agents without exposing credentials.
2. **Preview:** select trusted source revisions and preview the same groups, sources, destination, and offline/online mode intended for installation. Use `--replace` without `--apply` to preview replacements. Compare installed files against the previous source revision where available to distinguish local edits from upstream changes. For local edits or unexplained differences, stop and ask whether to replace with the source version, approve an explicit override, or incorporate the change into the repository first. Do not silently merge; directory replacement is not a merge.
3. **Back up and install:** obtain approval before `--replace --apply`. Use the installer's external backup location described above and record actual paths. Back up application configuration and active prompts separately, outside skill discovery. Preserve unrelated skills; symlink-managed installations must use their owning manager or an approved manual migration. Inspect partial failures before retrying.
4. **Migrate configuration:** use the updated `setup-opencode-routing` skill and its SETUP.md migration notes for changes applicable to the installed version. Install approved managed prompts from the repository and verify their contents match, recording any explicit overrides. Update approved configuration references without replacing the entire configuration. Preserve unrelated settings, model bindings, effort settings, permissions, and explicit `deep` choices unless their changes are separately approved. Installing new templates does not activate them.
5. **Verify:** inspect skill discovery and resolved configuration from each affected project. Run `opencode debug config` and `opencode debug agent NAME` for Build, Plan, and enabled `deep`, plus any changed workers. Check prompt content, file references, models, and effective permissions. Parsing alone does not establish provider access or behavioral compliance; paid calls need permission. Inspect debug output locally for secrets before sharing it.
6. **Restart and report:** quit/restart OpenCode and begin a fresh conversation. Report source revisions, installed versus configured changes, preserved customizations, backup paths, checks, and remaining gaps. On failure, restore only the applicable skill and configuration backups after checking for subsequent edits; do not delete unrelated resources.

Apply migration notes only when their stated condition holds. Do not replay historical migrations on every upgrade.

## Workflow migration

The recommended profile is explicit: the configured coordinator selects `grill-with-docs` for unresolved design when useful, presents an appropriately sized spec/checklist and verification contract, uses `execute-approved-work` for authorized delivery, Matt's `tdd` at agreed seams, and independent standards/spec review at a meaningful delivery boundary. The developer can start with an ordinary request. Missing optional planning skills call for a disclosed local draft, not a blocked small task; publishing through installed upstream planning skills needs separate authorization. Plan remains read-only until the user switches to Build for implementation.

`capture-intent` retains the overarching purpose alongside grilling and ADRs, reusing an adequate existing brief/spec introduction. It creates no mandatory second interview or document. `write-commit-and-pr` drafts rationale-first Git commit messages and PR descriptions from actual changes and approved intent; writing text grants no publishing/mutation permission. Both are local skills with no added third-party dependencies. If another installed writing skill claims the same task, select the intended owner explicitly rather than stacking formats or approval loops.

`finish-approved-work` owns an authorized Git integration/cleanup operation. It uses the feature-wide message, confirms scope and ownership, preserves unique notes, and keeps resources on failure. This is distinct from drafting. `execute-approved-work` owns implementation status (DONE/DONE_WITH_CONCERNS/NEEDS_CONTEXT/BLOCKED), review acceptance, and a durable local recovery record; report completion never substitutes for acceptance evidence.

The `.worktree/` repository-local default is overridable. Establish Git exclusions without an automatic preparatory commit; use existing policy or an appropriate local `.git/info/exclude` while a reviewed shared ignore rule is pending. Keep runtime progress outside removable worktrees, following project convention or primary checkout `.hrym/work/<initiative>/progress.md`. In Plan these remain in-chat drafts, not file writes. Branch/worktree permissions do not authorize dependency installs, pulls, or publishing.

Use `diagnosing-bugs` for non-obvious failures/performance work, not every clear regression. Selected-profile customization: reuse known reproductions, keep hypotheses plausible rather than padding a count, bound stress/instrumentation to authority and useful evidence, and stop no-progress retries. The upstream HITL Bash template is an optional last resort, not a mandatory shell workflow or automatic permission to instrument production. Supporting resources are copied, but copying is not execution.

The profile explicitly customizes the pinned upstream `to-spec`'s exhaustive-story instruction: use representative scenarios and appropriately scoped requirements unless the user asks for an exhaustive inventory. PM skills may be selected later as optional bounded analyses; do not install the whole collection or turn its prerequisites into another required workflow.

Do not stack `implement`, `implement-spec`, `subagent-driven-development`, or `executing-plans` under that adapter. Do not restart `brainstorming` after an approved design. The installer does not remove any of these from an existing environment. Obtain approval to remove the Superpowers bootstrap reference; inspect separately installed skills and any other plugin injecting workflow instructions. Preserve unrelated plugins and local skill edits.

The template explicitly denies competing workflow skills for Build/Plan through `permission.skill`, while leaving unrelated skills and other profiles alone. Read the exact rules in `templates/opencode.jsonc` from the router distribution; do not infer manual-only behavior from unsupported metadata. These rules select our execution/testing/finishing/writing owners instead of similarly purposed upstream orchestrators. If `deep` is enabled, copy the same skill rules as well as its task allowlist. Confirm effective permissions with the installed version. Removing a bootstrap and restricting skill loading are separate steps; neither proves all conflicting instructions are gone.

Matt's `resolving-merge-conflicts` is not manual-only. It can be useful under an explicitly authorized conflict-resolution workflow, but its raw instructions include staging everything and finishing. It is not part of core. Retain it outside this default flow or configure a deliberate recovery profile rather than silently nesting it under the finisher; preserve unrelated work under the selected profile's authority rules.

The compact standing policy in the router is necessary: a skill that loads only after a competing workflow has already taken control cannot reliably resolve that conflict retroactively. Explicit user choice of another workflow should be handled by switching profile or revising the selection, not running both.

## Recommended catalogue

Run `--list` for the exact selection and purposes. The catalogue contains 32 skills in 14 groups. `core` resolves to fourteen skills: environment setup, intent capture, execution, commit/PR writing, finishing, routing, grilling/domain helpers, TDD/interface-design reference, two-axis review, scoped diagnosis, and project-convention setup. Specialist groups are opt-in; their exact contents and dependencies are listed by the catalogue. `--all-groups` selects all defined groups and dependencies; preview and inspect it as the catalogue grows.

At meaningful completion, the coordinator may propose reusable improvements from evidence and expected repetition. Project-specific facts belong in project docs; mechanical repeats may deserve scripts; portable methods may deserve a skill. Prefer correcting an existing owner. Proposals are nonblocking and edits/deployment require approval; no automatic retrospective, transcript-to-skill dump, or installed-cache rewrites.

The installer treats sources as trusted content and does not execute their scripts. It preserves licenses, not a guarantee of skill quality. Review changes when updating a source revision; use the recorded pinned revision to prepare reproducible offline exports.

## Verification

Run `python3 -m unittest discover -s tests -v` from the repository (or `python -m unittest discover -s tests -v` on Windows). Tests use temporary fixtures and local Git repositories; no public-network calls or installed user changes. Python 3.10 syntax checks on a newer interpreter are not a Python 3.10 runtime test.

Check native skill/configuration discovery separately after approved configuration merging. Successful parsing does not establish account entitlement or actual model execution. Report the tested platform and any untested Windows/Git Bash or provider behavior.
