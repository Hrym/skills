# Offline installation, updates, and troubleshooting

## Offline installation

Bring complete trusted source roots with their required licenses. The [catalogue](../skills/setup-development-environment/catalogue.json) records all source revisions and required paths. The Matt core and optional skills are distinct revisions and require separate roots. A local source override itself is reported as unverified.

Source roots are repositories, not flat installed skill collections. Matt's selected skills span `skills/engineering/`, `skills/productivity/`, and `skills/in-progress/`. Do not copy only visible `SKILL.md` files: referenced documents, templates, scripts, and upstream licenses belong with them. Export complete pinned source trees; Git metadata is not required.

Linux, from the Hrym export:

```bash
python3 skills/setup-development-environment/scripts/install.py \
  --source hrym=/media/sources/hrym-skills \
  --source matt=/media/sources/matt-core-skills \
  --source matt-optional=/media/sources/matt-optional-skills \
  --source github-awesome-copilot=/media/sources/awesome-copilot \
  --source anthropic=/media/sources/anthropic-skills \
  --source microsoft-playwright-cli=/media/sources/playwright-cli \
  --offline
```

Windows with Git Bash:

```bash
python skills/setup-development-environment/scripts/install.py \
  --source "hrym=C:/Skill Sources/hrym-skills" \
  --source "matt=C:/Skill Sources/matt-core-skills" \
  --source "matt-optional=C:/Skill Sources/matt-optional-skills" \
  --source "github-awesome-copilot=C:/Skill Sources/awesome-copilot" \
  --source "anthropic=C:/Skill Sources/anthropic-skills" \
  --source "microsoft-playwright-cli=C:/Skill Sources/playwright-cli" \
  --offline
```

The checkout or export containing the installer and catalogue is still required locally. The examples explicitly override all six catalogue sources; source exports need no `.git` metadata. Review, then repeat the same command with `--apply`. Add `--destination PATH` if necessary; otherwise Python's home directory determines `.agents/skills`. Explicit groups do not add `core` implicitly. For optional planning, include both `--group core --group planning`.

For example, a staged installer/catalogue checkout and all six source roots can be used with fetching disabled:

```bash
python3 skills/setup-development-environment/scripts/install.py --list
python3 skills/setup-development-environment/scripts/install.py \
  --group core --group large-planning \
  --source hrym=/media/sources/hrym-skills \
  --source matt=/media/sources/matt-core-skills \
  --source matt-optional=/media/sources/matt-optional-skills \
  --source github-awesome-copilot=/media/sources/awesome-copilot \
  --source anthropic=/media/sources/anthropic-skills \
  --source microsoft-playwright-cli=/media/sources/playwright-cli --offline
```

The command previews. Repeat with `--apply` only after inspecting the selection and conflicts. See [all optional groups](optional-skills.md). Installing skills installs no packages or runtimes; it also does not mean all installed skills are loaded in every conversation.

`--offline` means only that the installer does not fetch missing skill sources; it does not describe public Internet availability or disable approved internal trackers, Git/package services, or model endpoints. It does not attempt network fallback and does not require Git for copying exported roots. It fails with the source/path that is missing. Offline skill installation does not create a local model endpoint or account credentials. Check actual prerequisites/access before assuming internal services are available.

Copying a skill does not authorize network access, model selection, or acquisition of sensitive artifacts. For externally hosted reference material, configure [approved reference locations](reference-sources.md); this guide does not provision application tools or runtimes. If research requires unavailable sources, the optional `research-handoff` skill supports a human-mediated question-only or repository-aware request.

## Source revisions and private repositories

The default Hrym Git URL uses SSH and can require repository access; configure Git authentication separately or use a local source. The default Hrym `main` reference moves. To pin a release, use a reviewed catalogue with an exact ref through `--catalogue PATH`. Matt core, Matt optional, and the other optional source revisions are pinned separately.

Online retrieval reports its resolved commit. Preview can download into temporary storage even though the destination remains untouched. Git failures report the source and operation while withholding raw Git output that may contain private URLs or credentials. Diagnose access locally; do not paste secrets into an agent conversation.

## Updates and conflicts

Use an updated trusted checkout/catalogue and preview again. Identical payloads are left untouched. Existing differing directories produce conflicts rather than being overwritten, including when an older manual installation lacks the installer's `SOURCE-LICENSE` attribution.

Inspect the differences. If replacement is intended, use:

```bash
python3 skills/setup-development-environment/scripts/install.py --replace --apply
```

Include the same source/group/offline options used in the reviewed preview. Replacement moves the old directory into a unique backup under `~/.hrym/skill-backups/`. The command prints the actual path. Override the root with `--backup-dir PATH` outside discovery locations; do not put backups under a directory named `skills` or a custom recursive skill-discovery path.

Unrelated installed skills are not removed. Symlink-managed installations need their own manager or an explicit manual migration; the installer refuses to replace those targets. Multi-directory writes are not crash-atomic. On an I/O failure, inspect the reported affected paths and backups before retrying.

Updating skill files does not automatically change OpenCode configuration. Rerun the setup skill to review configuration changes, and restart OpenCode afterward.

## Rollback

Restore the relevant old directories from the reported backups and remove only newly installed skills you intend to remove. Preserve later edits. Removing the setup skill does not undo the configuration it helped create; restore or selectively merge your separate config backup as described in the [routing guide](setup-opencode-routing.md#undo-the-setup).

Keep backup directories outside skill discovery so old and current copies are not loaded together. Restart and check effective discovery/configuration after rollback.

## Troubleshooting

| Symptom | Check |
|---|---|
| Python command missing or too old | Install Python 3.10+; try `python` or `py -3` on Windows. Git Bash alone is insufficient. |
| Git fetch fails | Verify source access and revision using preconfigured Git credentials, or supply `--source ID=PATH`. |
| Offline source/path missing | Match the catalogue's repository layout and include licenses/resources. Do not drop `--offline` silently. |
| Skill does not appear | Check the actual discovery directory, name/frontmatter, permissions, duplicate names, and restart state. |
| Agent repeats discovery or starts another orchestrator | Inspect bootstrap plugins and all discovered skill copies; select one workflow owner and resolve conflicts explicitly. |
| Config accepts a model but calls fail | Model catalogue visibility does not establish account access. Confirm access rather than retrying unavailable models. |
| Variant has no effect | Check provider/model support and explicit session overrides; a request to “think harder” is not an API setting. |

## Platform checklist

Supported targets are Linux and Windows with Git Bash. Test on the actual platform before claiming it was verified. From this repository:

```bash
python -m unittest discover -s tests -v
python skills/setup-development-environment/scripts/install.py --list
```

Use `python3` on Linux if appropriate. Tests create temporary fixtures and exercise a local Git revision without public-network access. The Git-dependent test is skipped when Git is absent. Confirm preview leaves a chosen temporary destination untouched, paths with spaces work, and repeated fixture installation is unchanged. Check OpenCode discovery/configuration separately after approved setup.

A newer Python interpreter can check Python 3.10 syntax, but that is not a Python 3.10 runtime test. Linux success does not establish Windows/Git Bash behavior. Report untested environments plainly rather than adding speculative compatibility claims.
