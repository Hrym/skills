# Offline installation, updates, and troubleshooting

## Offline installation

Bring complete trusted snapshots of this repository and Matt's source repository, including their licenses. The [catalogue](../skills/setup-development-environment/catalogue.json) records the selected Matt revision and each required relative skill path. Export that revision on a connected machine when you need reproducibility; a local source override itself is reported as unverified.

Source roots are repositories, not flat installed skill collections. Matt's selected skills live under `skills/engineering/` and `skills/productivity/`. Do not copy only the visible `SKILL.md` files: referenced documents, templates, and scripts belong with them.

Linux, from the Hrym export:

```bash
python3 skills/setup-development-environment/scripts/install.py \
  --source hrym=/media/sources/hrym-skills \
  --source matt=/media/sources/matt-skills \
  --offline
```

Windows with Git Bash:

```bash
python skills/setup-development-environment/scripts/install.py \
  --source "hrym=C:/Skill Sources/hrym-skills" \
  --source "matt=C:/Skill Sources/matt-skills" \
  --offline
```

Review, then repeat with `--apply`. Add `--destination PATH` if necessary; otherwise Python's home directory determines `.agents/skills`. For optional planning, include both `--group core --group planning`.

Offline mode does not fetch missing sources, attempt network fallback, or require Git for copying. It fails with the source/path that is missing. Offline skill installation does not create a local model endpoint or account credentials. The agent application must separately have an inference route available in that environment.

## Source revisions and private repositories

The default Hrym Git URL uses SSH and can require repository access; configure Git authentication separately or use a local source. The default Hrym `main` reference moves. To pin a release, use a reviewed catalogue with an exact ref through `--catalogue PATH`. Matt's default revision is already pinned.

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
