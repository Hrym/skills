# Set up your development environment

The setup has three distinct steps: **install skill files**, **configure OpenCode**, and **configure project conventions**. The installer automates the first. The setup agent guides the other two after you approve the proposed changes.

## Prerequisites

- Python **3.10 or newer**, with no additional Python packages.
- OpenCode for agent use. The existing routing template has been exercised with OpenCode 1.18.30; validate the installed version's supported fields.
- Confirmed access to suitable models through your chosen provider. You do not need Astra; see [routing profiles](setup-opencode-routing.md#what-gets-configured).
- Git for downloading sources. Local exported sources need neither Git nor network access for copying.
- On Windows, Git Bash is available, but **Python must be installed separately**.

Check from a terminal:

```bash
# Linux
python3 --version
git --version
opencode --version
```

```bash
# Windows / Git Bash
python --version
# If Python is available through its Windows launcher instead:
py -3 --version
```

Use the working Python 3.10+ command consistently below. No administrator privileges are needed for a normal user-directory installation. Do not install prerequisites or change account credentials silently through an agent.

## Obtain the sources

Start from a trusted checkout or export of this repository. Commands below run from its root. The catalogue uses the local Hrym checkout automatically when it can identify it; otherwise supply `--source hrym=PATH`. Its remote Hrym URL uses SSH and may require repository access. Matt's repository is fetched at a pinned revision.

For restricted environments, use [offline installation](offline-and-updates.md#offline-installation) instead. Offline copying does not provide offline model inference.

## Inspect the selection and preview

```bash
python3 skills/setup-development-environment/scripts/install.py --list
python3 skills/setup-development-environment/scripts/install.py
```

On Windows, replace `python3` with `python` or `py -3`. The default `core` group resolves to fourteen skills, covering setup/routing, intent, design, bounded execution and diagnosis, verification/review, change writing, and authorized finishing. The [recommended profile](recommended-profile.md) explains ownership; the [catalogue](../skills/setup-development-environment/catalogue.json) is the authoritative selection/dependency map.

The optional `planning` group adds specification and ticket synthesis. Select both explicitly:

```bash
python3 skills/setup-development-environment/scripts/install.py --group core --group planning
```

If any `--group` is supplied, only those groups and their dependencies are selected; `core` is not added implicitly. Source directories are copied in full, with the source license. Unrelated installed skills are not removed.

For skill maintenance, use `--group core --group authoring` to add Matt's `writing-for-agents`. The authoring group introduces no Superpowers/TDD or renderer dependency. [Improvement proposals](improving-skills.md) are grounded in observed evidence and expected reuse; authoring is not an automatic phase after every task.

Preview is the default. It may download sources into temporary storage but never changes the skill destination. The output identifies `install`, `unchanged`, or `replace` targets. A differing existing directory is a conflict and needs review; see [updates](offline-and-updates.md#updates-and-conflicts).

## Install the approved selection

Repeat the reviewed command with `--apply`:

```bash
python3 skills/setup-development-environment/scripts/install.py --apply
```

Default destination: Python's home directory plus `.agents/skills`. Override it with `--destination PATH` when using another supported discovery location. On Windows, compare Python's home directory with OpenCode's effective paths; Git Bash's `$HOME` can differ.

Restart OpenCode after installing skills. The installer has not yet changed OpenCode's model configuration.

## Configure OpenCode with the setup skill

Back up the affected configuration directories first, keeping any credential-bearing backups outside Git. Start OpenCode and ask:

> Use setup-development-environment. The skills are installed. Configure my global OpenCode environment for the recommended workflow. GPT-6.1 Sol and GPT-6 Luna are available through my provider; Astra is not. Preserve unrelated settings and show the changes before applying them. Do not run paid model probes without asking.

State actual provider/model access rather than copying those names if they do not apply. The setup uses `setup-opencode-routing` to merge model bindings, prompts, variants, and permissions. It does not assume a model is usable merely because it appears in a catalogue.

### Migrating an existing workflow

The recommended profile needs no Superpowers plugin. If it is installed, the setup should identify its bootstrap/plugin entry and propose removing it **with your approval**, while preserving unrelated and authentication plugins. Separately installed Superpowers or other overlapping skills can still be discovered after plugin removal; inspect those too.

Select one owner per phase: the coordinator guides ordinary requests through approved design, execution/recovery, bounded TDD/diagnosis, independent review, and authorized finishing. Plan stays read-only until Build. The template's Build/Plan skill denials are deliberate profile changes: review them before applying, and apply matching rules to enabled `deep`. They restrict competing skill loading but cannot prevent a plugin from injecting instructions. Preserve unrelated agents/profiles; do not silently uninstall other skills or edit plugin caches.

Review the actual configuration changes, run native loading/permission checks, restart OpenCode, and start a fresh conversation. See [the routing guide](setup-opencode-routing.md#4-validate-and-activate) for commands. Unsupported fields or unverified model access must be reported, not hidden.

## Configure the project

Open the target project and ask:

> Use setup-matt-pocock-skills to inspect this project's tracker and domain-document conventions. Preserve existing AGENTS.md or CLAUDE.md content and show proposed changes first. Use local Markdown tracking if no issue service is available.

This is needed only when the conventions are missing or intentionally changing. Do not create a GitHub issue, labels, a PR, or a second instruction file just because the skill is installed. Tracker operations have their own tools and access prerequisites.

## Confirm a useful result

Expected result:

- Installed skills are discoverable, with supporting files and licenses.
- The intended workflow and role/model bindings load from the correct scope.
- Plan has only read-only delegates; workers cannot delegate further.
- Existing unrelated settings are intact and backup locations are known.
- `.worktree/` is the overridable local isolation default; multi-task progress is kept outside removable worktrees in an ignored project-local record. Creating a worktree does not authorize installs, pulls, or commits.
- Model entitlement and actual execution remain distinct from static configuration validation.

Now try [your first change](first-change.md). Start with a small task whose expected behavior you can judge. Do not begin by asking the agent to redesign an unfamiliar application.
