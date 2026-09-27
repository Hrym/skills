---
name: setup-development-environment
description: Use when installing or updating the recommended development skills, onboarding OpenCode on Windows or Linux, migrating overlapping workflows, or preparing a local-source/offline setup.
license: MIT
---

# Set up a development environment

Install only the selected skills; configure the application as a separate reviewed step. Python 3.10+ and its standard library are required. The initial application integration is OpenCode on Linux or Windows with Git Bash. Superpowers is not required.

## Inspect and agree

Read [SETUP.md](SETUP.md) and `catalogue.json`. Establish destination scope, sources, network access, available models, and existing skill/plugin/configuration locations. Use local discovery to settle facts; ask about choices. Never expose credentials or equate catalog visibility with model entitlement.

Recommend `core`; add `planning` for specs/tickets and `authoring` when maintaining skills. Authoring contains Matt's `writing-for-agents`, not another orchestration/TDD framework. The catalogue includes required resources. Do not install entire collections by default. Skill installation alone configures neither model access nor project conventions.

## Install skill files

Use `scripts/install.py --list`, then preview the selected groups and sources without `--apply`. Use the same Python 3.10+ executable for all commands. Paths are relative to this skill for the script/catalogue, not the current directory. Obtain approval before `--apply` or `--replace`.

Offline: supply repository roots with `--source ID=PATH --offline`; missing sources fail without fetching. Do not silently change to online mode. Online: use the catalogue's revisions and preconfigured Git access. A local source is reported as unverified, not falsely pinned. Preserve licenses. Differing installations conflict by default; explicit replacement makes backups outside discovery paths. Show actual actions and backup paths; never silently remove unrelated skills.

## Configure the selected workflow

Invoke `setup-opencode-routing` after agreeing the intended models and scope. Its standing coordinator prompt guides ordinary requests through decisions and scoped authorization: discovery only for unresolved design, implementation through `execute-approved-work`, behavioral testing through `tdd`, and meaningful independent review. An approved design is not re-interviewed. Workers do not restart orchestration. Keep required verification, but bound it with the contract. Installation alone does not activate this prompt; validate configuration and restart as instructed below.

The core supplies `capture-intent`, `write-commit-and-pr`, `finish-approved-work`, and scoped `diagnosing-bugs`. Retain purpose, ground change explanations in the actual diff, and keep drafting distinct from authorized integration. Use the configured worker-status/recovery contract and overridable `.worktree/` default. Preserve compact-story, bounded-diagnosis, and learning-checkpoint rules; no additional PM pipeline is required.

For this profile, propose removal of the Superpowers bootstrap/plugin and apply template Build/Plan skill denials only with approval. Preserve unrelated/auth plugins and other profiles. Denials do not stop a plugin injecting instructions. Inspect discovery locations for separate/duplicate copies; never rely on unsupported `disable-model-invocation`. Workers get narrow briefs and cannot delegate. Explain remaining conflicts instead of claiming isolation.

When project tracker/domain conventions are missing, use `setup-matt-pocock-skills` with approval. Offline projects may choose local Markdown tracking. Do not create remote issues/labels or overwrite project instructions as an installation side effect.

## Verify and hand off

Check installed skill discovery, resolved OpenCode models/variants/prompts, and effective permissions. Offline, use installed-version checks; mark unavailable external schema/access verification as unverified. Model calls cost money and need permission.

Report installed versus configured steps, selected sources/revisions, changes/backups, missing access, and remaining compatibility gaps. Quit/restart OpenCode and start a fresh conversation. Guide the developer through one bounded change before recommending more workflow machinery. Do not claim Windows runtime testing from Linux-only checks.
