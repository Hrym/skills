#!/usr/bin/env python3
"""Copy catalogue-selected skills. Python 3.10+, standard library only."""

import argparse
import json
import os
from pathlib import Path, PurePosixPath, PureWindowsPath
import re
import shutil
import subprocess
import sys
import tempfile


class InstallError(Exception):
    """An actionable planning or installation error."""


def arguments():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalogue", type=Path,
                        default=Path(__file__).resolve().parents[1] / "catalogue.json")
    parser.add_argument("--group", action="append",
                        help="Union of supplied groups; core only when no --group is supplied")
    parser.add_argument("--list", action="store_true", help="List purposes without fetching")
    parser.add_argument("--source", action="append", default=[], metavar="ID=PATH",
                        help="Local repository root (repeatable; last value per ID wins)")
    parser.add_argument("--destination", type=Path,
                        default=Path.home() / ".agents" / "skills")
    parser.add_argument("--offline", action="store_true", help="Never fetch sources")
    parser.add_argument("--apply", action="store_true", help="Write; otherwise preview only")
    parser.add_argument("--replace", action="store_true", help="Back up differing targets")
    parser.add_argument("--backup-dir", type=Path,
                        default=Path.home() / ".hrym" / "skill-backups",
                        help="Backup root outside destination and directories named skills")
    return parser.parse_args()


def relative_path(value):
    if (not isinstance(value, str) or not value or "\\" in value or
            PurePosixPath(value).is_absolute() or PureWindowsPath(value).drive or
            ".." in PurePosixPath(value).parts):
        raise InstallError(f"Expected a repository-relative path without '..': {value!r}")
    return value


def load_catalogue(path):
    catalogue = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(catalogue, dict) or catalogue.get("version") != 1:
        raise InstallError("Catalogue must have version: 1")
    for section in ("sources", "skills", "groups"):
        entries = catalogue.get(section)
        if not isinstance(entries, dict):
            raise InstallError(f"Catalogue {section} must be an object")
        for name in entries:
            if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", name):
                raise InstallError(f"Invalid {section} name: {name!r}")
    for source_id, source in catalogue["sources"].items():
        if not isinstance(source, dict) or any(
                not isinstance(source.get(key), str) or not source[key]
                for key in ("url", "ref", "license")):
            raise InstallError(f"Source {source_id} needs url, ref and license strings")
        relative_path(source["license"])
    for name, skill in catalogue["skills"].items():
        if not isinstance(skill, dict) or any(
                not isinstance(skill.get(key), str) or not skill[key]
                for key in ("source", "path", "description")):
            raise InstallError(f"Skill {name} needs source, path and description strings")
        if skill["source"] not in catalogue["sources"]:
            raise InstallError(f"Unknown source for skill {name}: {skill['source']}")
        relative_path(skill["path"])
    selections = [(f"Skill {n} requires", s.get("requires"))
                  for n, s in catalogue["skills"].items()]
    selections += [(f"Group {n}", members) for n, members in catalogue["groups"].items()]
    for context, members in selections:
        if not isinstance(members, list) or not all(isinstance(n, str) for n in members):
            raise InstallError(f"{context} must be a list of skill names")
        for name in members:
            if name not in catalogue["skills"]:
                raise InstallError(f"{context}: unknown skill {name}")
    return catalogue


def select_skills(catalogue, groups):
    selected = set()

    def visit(name):
        if name in selected:
            return
        selected.add(name)
        for dependency in catalogue["skills"][name]["requires"]:
            visit(dependency)

    for group in groups:
        if group not in catalogue["groups"]:
            raise InstallError(f"Unknown group: {group}")
        for name in catalogue["groups"][group]:
            visit(name)
    return sorted(selected)


def fetch_source(source_id, source, root):
    root.mkdir(parents=True)
    environment = dict(os.environ, GIT_TERMINAL_PROMPT="0")
    commands = [
        ("init", ["init", "--quiet"]),
        ("fetch", ["fetch", "--quiet", "--depth", "1", "--", source["url"], source["ref"]]),
        ("checkout", ["checkout", "--quiet", "--detach", "FETCH_HEAD"]),
        ("revision", ["rev-parse", "HEAD"]),
    ]
    for phase, command in commands:
        try:
            result = subprocess.run(["git", "-C", str(root), *command],
                                    env=environment, capture_output=True, text=True)
        except OSError as error:
            raise InstallError(f"Git could not run for source {source_id}; install Git or "
                               f"use --source {source_id}=PATH") from error
        if result.returncode:
            # Git stderr/command arguments may contain private URLs or credentials.
            raise InstallError(f"Git {phase} failed for source {source_id} "
                               f"(exit {result.returncode}). Check the URL, ref and preconfigured "
                               f"Git credentials, or use --source {source_id}=PATH. "
                               "Git output omitted to avoid exposing credentials.")
    print(f"Source {source_id}: resolved Git revision {result.stdout.strip()}")
    return root


def resolve_sources(args, catalogue, names, temporary):
    overrides = {}
    for value in args.source:
        source_id, separator, path = value.partition("=")
        if not separator or not path or source_id not in catalogue["sources"]:
            raise InstallError("--source requires a known source ID and repository root: ID=PATH")
        overrides[source_id] = Path(path).expanduser().resolve()
    script = Path(__file__).resolve()
    checkout = script.parents[3]
    own_catalogue = checkout / "skills/setup-development-environment/catalogue.json"
    if ((checkout / ".git").exists() and args.catalogue.resolve() == own_catalogue and
            script == checkout / "skills/setup-development-environment/scripts/install.py"):
        overrides.setdefault("hrym", checkout)
    required = sorted({catalogue["skills"][name]["source"] for name in names})
    if args.offline:
        missing = [name for name in required if name not in overrides]
        if missing:
            raise InstallError("Offline: missing local sources; provide " +
                               " ".join(f"--source {name}=PATH" for name in missing))
    sources = {}
    for source_id in required:
        if source_id in overrides:
            root = overrides[source_id]
            if not root.is_dir():
                raise InstallError(f"Local source {source_id} is not a directory: {root}")
            print(f"Source {source_id}: {root} (local, unverified)")
            sources[source_id] = root
        else:
            sources[source_id] = fetch_source(source_id, catalogue["sources"][source_id],
                                              temporary / "sources" / source_id)
    return sources


def snapshot(root):
    """Byte-equivalent payload, including empty directories, not timestamps."""
    contents = {}

    def failed(error):
        raise error

    for directory, dirs, files in os.walk(root, onerror=failed):
        base = Path(directory)
        for name in dirs:
            contents[(base / name).relative_to(root)] = None
        for name in files:
            contents[(base / name).relative_to(root)] = (base / name).read_bytes()
    return contents


def install(args, catalogue, temporary):
    args.destination = args.destination.expanduser().resolve()
    args.backup_dir = args.backup_dir.expanduser().resolve()
    if args.replace and (args.backup_dir.is_relative_to(args.destination) or
                         any(p.name.casefold() == "skills" for p in
                             (args.backup_dir, *args.backup_dir.parents))):
        raise InstallError("Backup directory must be outside the destination and skill-discovery "
                           f"trees (directories named 'skills'): {args.backup_dir}")
    names = select_skills(catalogue, args.group or ["core"])
    sources = resolve_sources(args, catalogue, names, temporary)

    plan = []
    for name in names:
        skill = catalogue["skills"][name]
        root = sources[skill["source"]]
        source = root / skill["path"]
        if not (source / "SKILL.md").is_file():
            raise InstallError(f"Missing SKILL.md: {source / 'SKILL.md'}")
        staged = temporary / "payloads" / name
        shutil.copytree(source, staged)
        license_path = root / catalogue["sources"][skill["source"]]["license"]
        attribution = staged / "SOURCE-LICENSE"
        if attribution.exists() and (not attribution.is_file() or
                                     attribution.read_bytes() != license_path.read_bytes()):
            raise InstallError(f"Reserved SOURCE-LICENSE conflicts with source resource: "
                               f"{source / 'SOURCE-LICENSE'}")
        shutil.copyfile(license_path, attribution)
        target = args.destination / name
        if target.is_symlink() or (target.exists() and not target.is_dir()):
            raise InstallError(f"Target conflict (not a regular directory): {target}")
        unchanged = target.is_dir() and snapshot(target) == snapshot(staged)
        action = "unchanged" if unchanged else "replace" if target.exists() else "install"
        plan.append((action, staged, target))
        print(f"{action}: {target}")

    conflicts = [str(target) for action, _, target in plan if action == "replace"]
    if conflicts and not args.replace:
        raise InstallError("Target conflicts; use --replace to back up and replace: " +
                           ", ".join(conflicts))
    if not args.apply:
        print("Preview only; use --apply to write.")
        return
    backup_session = None
    for action, staged, target in plan:
        if action == "unchanged":
            continue
        backup = None
        try:
            if action == "replace":
                args.backup_dir.mkdir(parents=True, exist_ok=True)
                if backup_session is None:
                    backup_session = Path(tempfile.mkdtemp(prefix="replacement-",
                                                          dir=args.backup_dir))
                backup = backup_session / target.name
                shutil.move(str(target), str(backup))
                print(f"Backup: {target} -> {backup}", flush=True)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(staged, target)
            print(f"Installed: {target}", flush=True)
        except (OSError, shutil.Error) as error:
            raise InstallError(f"Writing {target} failed: {error}. Backup path: {backup}. "
                               "Earlier installs/backups remain; inspect these paths before retrying.") from error


def main():
    args = arguments()
    try:
        catalogue = load_catalogue(args.catalogue)
        if args.list:
            for name, members in sorted(catalogue["groups"].items()):
                print(f"Group {name}: {', '.join(members)}")
            for name, skill in sorted(catalogue["skills"].items()):
                print(f"{name}: {skill['description']}")
            return 0
        with tempfile.TemporaryDirectory(prefix="skill-install-") as temporary:
            install(args, catalogue, Path(temporary))
    except (InstallError, OSError, ValueError, shutil.Error) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
