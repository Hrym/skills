# Hrym Skills

Reusable skills for a development workflow with clear requirements, bounded testing, and independent review. OpenCode is the first supported agent application, on Linux and Windows with Git Bash. Superpowers is not required.

**New to agent-assisted development? [Start here](docs/start-here.md).**

**Ready to install? [Set up your environment](docs/setup-development-environment.md).** The installer requires Python 3.10+, uses no pip/npm packages, and supports trusted local sources without network access.

## Available skills

| Skill | Purpose | Requirements |
|---|---|---|
| [setup-development-environment](skills/setup-development-environment/SKILL.md) | Install a selected skill catalogue and guide reviewed environment configuration | Python 3.10+; Git for remote sources; OpenCode for configuration |
| [capture-intent](skills/capture-intent/SKILL.md) | Preserve feature or architecture purpose without depending on a transcript or duplicating an existing brief | An agent with the relevant context and approved document access |
| [execute-approved-work](skills/execute-approved-work/SKILL.md) | Turn approved requirements into bounded implementation, verification, and independent review | An agent application with the needed execution/review capabilities |
| [write-commit-and-pr](skills/write-commit-and-pr/SKILL.md) | Draft Git commit messages and PR descriptions explaining why the change and approach are needed | Access to the intended diff and available rationale |
| [finish-approved-work](skills/finish-approved-work/SKILL.md) | Perform requested Git integration and owned-workspace cleanup without losing unrelated work or recovery notes | Git, the intended change, and explicit operation authority |
| [setup-opencode-routing](skills/setup-opencode-routing/SKILL.md) | Configure OpenCode models, worker roles (including read-only research), permissions, and reasoning defaults | OpenCode and confirmed model access |

### Quality-first OpenCode routing

Use inexpensive workers for bounded work, keep ordinary coordination on a standard model, and use a separate read-only researcher for dense source interpretation. Consult a stronger architectural advisor only when warranted and available. The setup keeps worker delegation flat, separates read-only advice from editing, and keeps large exploratory results and test logs out of the coordinator when useful.

This is an **agent-guided setup skill**, not an automatic runtime optimizer or a guarantee of lower bills. It adapts the example configuration to your available providers and preserves unrelated settings.

The [routing reference](docs/setup-opencode-routing.md) covers model/permission configuration. Read [the design rationale](docs/routing-design.md) for trade-offs and [staying in control](docs/staying-in-control.md) for avoiding duplicate workflows, unnecessary tests, and scope creep.

Keep the purpose readable with [intent capture](docs/capture-intent.md), then carry the reasoning into [commit messages and PR descriptions](docs/write-commit-and-pr.md). These skills complement grilling and ADRs without installing another documentation or PM framework.

The [recommended profile](docs/recommended-profile.md) identifies phase owners, optional planning/authoring groups, bounded debugging, and conflict controls. Multi-task work uses [recoverable progress](docs/progress-and-recovery.md); substantive implementation defaults to overridable repository-local `.worktree/` isolation. Finishing and message writing are separate authorized activities.

## Installing skills

The environment installer selects complete skill directories, dependencies, and license material from a [versioned catalogue](skills/setup-development-environment/catalogue.json). Preview from this checkout with:

```bash
python3 skills/setup-development-environment/scripts/install.py --list
python3 skills/setup-development-environment/scripts/install.py
```

On Windows use your Python command, typically `python` or `py -3`. Preview may fetch sources but does not change the installation destination. Use local `--source` roots and `--offline` for no-network installation. See the [setup guide](docs/setup-development-environment.md) before applying changes.

For maintaining skills, select `--group core --group authoring` to add Matt's `writing-for-agents`. [Improvement proposals](docs/improving-skills.md) are evidence-driven and nonblocking; they do not silently alter installed skills.

Installing a skill makes its instructions available; it does not automatically apply its configuration templates. Follow the individual user guide and review changes before accepting them.

## Maintaining this repository

- Keep each skill self-contained; installed skills must not depend on files elsewhere in this repository.
- Put user instructions in `docs/` and runtime/agent instructions with the skill.
- Validate model IDs, supported variants, permissions, and configuration loading against the intended environment. Never commit credentials, personal provider settings, debug output, or session logs.
- Preserve source citations and distinguish measured results from proposed defaults. A valid configuration is not proof of model access or task-quality improvements.

See [AGENTS.md](AGENTS.md) for repository-maintenance agent conventions and [the documentation index](docs/README.md) for user documentation. Local planning and orchestration artifacts are excluded from version control.

Installer checks: `python3 -m unittest discover -s tests -v` (or `python -m unittest discover -s tests -v` on Windows). They use temporary fixtures and local Git repositories, not the user's installed skills or public-network services. Linux validation does not establish Windows runtime compatibility; see the [platform checklist](docs/offline-and-updates.md#platform-checklist).

## License

[MIT](LICENSE). Third-party material and integration dependencies are identified in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
