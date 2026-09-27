"""Installer contract tests: real CLI, isolated sources, no public network."""

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SCRIPT = (Path(__file__).resolve().parents[1] / "skills" /
          "setup-development-environment" / "scripts" / "install.py")


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="skill installer ")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "export with spaces"
        self.destination = self.root / "installed skills"
        self.backups = self.root / "saved skills"
        self.catalogue = self.root / "catalogue.json"
        self.home = self.root / "home"
        self.home.mkdir()
        self.environment = dict(os.environ, HOME=str(self.home),
                                USERPROFILE=str(self.home),
                                PYTHONDONTWRITEBYTECODE="1")
        self.write(self.source / "LICENSE", "Fixture license\n")
        for name in ("alpha", "helper", "optional"):
            self.write(self.source / "skills" / name / "SKILL.md", f"# {name}\n")
        self.write(self.source / "skills/alpha/references/guide.md", "Guide\n")
        self.write(self.source / "skills/alpha/scripts/never-run.py",
                   "raise RuntimeError('source scripts must not run')\n")
        (self.source / "skills/alpha/empty").mkdir()
        self.data = {
            "version": 1,
            "sources": {"fixture": {"url": str(self.root / "missing remote"),
                                     "ref": "main", "license": "LICENSE"}},
            "skills": {
                name: {"source": "fixture", "path": f"skills/{name}",
                       "description": f"Purpose of {name}",
                       "requires": ["helper"] if name == "alpha" else []}
                for name in ("alpha", "helper", "optional")
            },
            "groups": {"core": ["alpha"], "planning": ["optional"]},
        }
        self.save_catalogue()

    def write(self, path, text):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def save_catalogue(self):
        self.catalogue.write_text(json.dumps(self.data), encoding="utf-8")

    def run_cli(self, *args, local=True, offline=True, script=SCRIPT,
                catalogue=True, destination=True):
        command = [sys.executable, str(script)]
        if catalogue:
            command += ["--catalogue", str(self.catalogue)]
        if destination:
            command += ["--destination", str(self.destination)]
        if local:
            command += ["--source", f"fixture={self.source}"]
        if offline:
            command += ["--offline"]
        return subprocess.run(command + list(args), cwd=self.root,
                              env=self.environment, text=True, capture_output=True)

    def assert_ok(self, result):
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def tree(self, root):
        return {str(p.relative_to(root)): p.read_bytes() if p.is_file() else None
                for p in root.rglob("*")}

    def test_preview_and_apply_copy_full_payload_and_dependencies(self):
        dependency_source = self.root / "another export"
        self.write(dependency_source / "skills/helper/SKILL.md", "# From another source\n")
        self.write(dependency_source / "LICENSE", "Dependency license\n")
        self.data["sources"]["dependency"] = dict(self.data["sources"]["fixture"])
        self.data["skills"]["helper"]["source"] = "dependency"
        self.save_catalogue()
        override = ("--source", f"dependency={dependency_source}")
        preview = self.run_cli(*override)
        self.assert_ok(preview)
        self.assertIn("alpha", preview.stdout)
        self.assertIn("helper", preview.stdout)
        self.assertIn("unverified", preview.stdout.lower())
        self.assertFalse(self.destination.exists())
        self.assert_ok(self.run_cli("--apply", *override))
        self.assertEqual({p.name for p in self.destination.iterdir()},
                         {"alpha", "helper"})
        alpha = self.destination / "alpha"
        self.assertEqual((alpha / "references/guide.md").read_text(), "Guide\n")
        self.assertTrue((alpha / "empty").is_dir())
        self.assertEqual((alpha / "scripts/never-run.py").read_text(),
                         "raise RuntimeError('source scripts must not run')\n")
        self.assertEqual((alpha / "SOURCE-LICENSE").read_text(), "Fixture license\n")
        self.assertEqual((self.destination / "helper/SKILL.md").read_text(),
                         "# From another source\n")
        self.assertEqual((self.destination / "helper/SOURCE-LICENSE").read_text(),
                         "Dependency license\n")

    def test_repeated_apply_leaves_unchanged_payload_untouched(self):
        self.assert_ok(self.run_cli("--apply"))
        before = self.tree(self.destination)
        skill = self.destination / "alpha/SKILL.md"
        os.utime(skill, (1000000000, 1000000000))
        result = self.run_cli("--apply")
        self.assert_ok(result)
        self.assertIn("unchanged", result.stdout.lower())
        self.assertEqual(self.tree(self.destination), before)
        self.assertEqual(skill.stat().st_mtime, 1000000000)
        self.assertFalse((self.home / ".hrym").exists())

    def test_conflict_aborts_all_writes_and_preserves_unrelated_skills(self):
        self.write(self.destination / "helper/SKILL.md", "Local changes\n")
        self.write(self.destination / "unrelated/SKILL.md", "Keep me\n")
        before = self.tree(self.destination)
        result = self.run_cli("--apply")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.tree(self.destination), before)
        self.assertIn("conflict", result.stderr.lower())
        self.assertFalse((self.home / ".hrym").exists())

    def test_replace_preserves_backup_outside_discovery_and_preview_is_read_only(self):
        self.assert_ok(self.run_cli("--apply"))
        self.write(self.destination / "alpha/SKILL.md", "Local changes\n")
        self.write(self.destination / "alpha/local.txt", "Personal notes\n")
        before = self.tree(self.destination / "alpha")
        for unsafe in (self.destination / "backups", self.home / ".agents/skills/backups"):
            with self.subTest(unsafe=unsafe):
                result = self.run_cli("--apply", "--replace", "--backup-dir", str(unsafe))
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(self.tree(self.destination / "alpha"), before)
                self.assertFalse(unsafe.exists())
        options = ("--replace", "--backup-dir", str(self.backups))
        self.assert_ok(self.run_cli(*options))
        self.assertFalse(self.backups.exists())
        self.assertEqual(self.tree(self.destination / "alpha"), before)
        result = self.run_cli("--apply", *options)
        self.assert_ok(result)
        copies = list(self.backups.rglob("alpha"))
        self.assertEqual(len(copies), 1)
        self.assertEqual(self.tree(copies[0]), before)
        self.assertIn(str(copies[0]), result.stdout)
        self.assertEqual((self.destination / "alpha/SKILL.md").read_text(), "# alpha\n")
        self.assertFalse((self.destination / "alpha/local.txt").exists())
        self.write(self.destination / "alpha/SKILL.md", "Another edit\n")
        self.assert_ok(self.run_cli("--apply", "--replace"))
        default_backups = list((self.home / ".hrym/skill-backups").rglob("alpha/SKILL.md"))
        self.assertEqual(len(default_backups), 1)
        self.assertEqual(default_backups[0].read_text(), "Another edit\n")

    def test_list_prints_groups_and_purposes_without_resolving_sources(self):
        result = self.run_cli("--list", local=False, offline=False)
        self.assert_ok(result)
        for text in ("core", "planning", "Purpose of alpha", "Purpose of optional"):
            self.assertIn(text, result.stdout)
        self.assertFalse(self.destination.exists())

    def test_offline_and_missing_payload_fail_before_any_destination_writes(self):
        # No Git executable is available, even if an offline regression tries fetching.
        self.environment["PATH"] = ""
        missing = self.run_cli("--apply", local=False)
        self.assertNotEqual(missing.returncode, 0)
        self.assertIn("offline", missing.stderr.lower())
        self.assertIn("--source fixture=", missing.stderr)
        self.assertFalse(self.destination.exists())
        for relative in ("skills/helper/SKILL.md", "LICENSE"):
            with self.subTest(missing=relative):
                path = self.source / relative
                original = path.read_text()
                path.unlink()
                result = self.run_cli("--apply")
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(str(path), result.stderr)
                self.assertNotIn("Traceback", result.stderr)
                self.assertFalse(self.destination.exists())
                self.write(path, original)
        # Adding source attribution must not silently discard a supplied resource.
        self.write(self.source / "skills/helper/SOURCE-LICENSE", "Existing resource\n")
        collision = self.run_cli("--apply")
        self.assertNotEqual(collision.returncode, 0)
        self.assertIn("SOURCE-LICENSE", collision.stderr)
        self.assertFalse(self.destination.exists())

    def test_invalid_selection_and_escaping_path_fail_clearly_without_writes(self):
        invalid_group = self.run_cli("--apply", "--group", "unknown")
        self.assertNotEqual(invalid_group.returncode, 0)
        self.assertIn("unknown", invalid_group.stderr)
        self.assertNotIn("Traceback", invalid_group.stderr)
        self.data["skills"]["alpha"]["requires"] = ["missing-dependency"]
        self.save_catalogue()
        invalid_dependency = self.run_cli("--apply")
        self.assertNotEqual(invalid_dependency.returncode, 0)
        self.assertIn("missing-dependency", invalid_dependency.stderr)
        self.assertNotIn("Traceback", invalid_dependency.stderr)
        self.data["skills"]["alpha"]["requires"] = []
        self.data["skills"]["alpha"]["path"] = "../outside"
        self.write(self.root / "outside/SKILL.md", "Must not install\n")
        self.save_catalogue()
        result = self.run_cli("--apply")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("path", result.stderr.lower())
        self.assertFalse(self.destination.exists())

    def test_checkout_detection_requires_own_catalogue_and_git_marker(self):
        script = self.source / "skills/setup-development-environment/scripts/install.py"
        script.parent.mkdir(parents=True)
        shutil.copyfile(SCRIPT, script)
        self.data["sources"]["hrym"] = self.data["sources"].pop("fixture")
        for skill in self.data["skills"].values():
            skill["source"] = "hrym"
        self.save_catalogue()
        shutil.copyfile(self.catalogue, script.parent.parent / "catalogue.json")
        (self.source / ".git").mkdir()
        self.assert_ok(self.run_cli("--apply", script=script, local=False,
                                    catalogue=False, destination=False))
        self.assertTrue((self.home / ".agents/skills/alpha/SKILL.md").is_file())
        self.assertFalse(self.destination.exists())
        # A different selected catalogue must not silently bind to this checkout.
        external = self.run_cli(script=script, local=False)
        self.assertNotEqual(external.returncode, 0)
        self.assertIn("--source hrym=", external.stderr)
        (self.source / ".git").rmdir()
        installed = self.run_cli(script=script, local=False, catalogue=False)
        self.assertNotEqual(installed.returncode, 0)
        self.assertIn("--source hrym=", installed.stderr)

    @unittest.skipUnless(shutil.which("git"), "Git needed for local revision fixture")
    def test_group_union_and_exact_remote_revision_using_local_git(self):
        def git(*args):
            result = subprocess.run(
                ["git", "-c", "user.name=Fixture", "-c", "user.email=fixture@example.test",
                 *args], cwd=self.source, env=self.environment, text=True, capture_output=True)
            self.assert_ok(result)
            return result.stdout.strip()

        git("init", "--quiet")
        git("add", ".")
        git("commit", "--quiet", "-m", "First fixture")
        first = git("rev-parse", "HEAD")
        self.write(self.source / "skills/alpha/SKILL.md", "Newer, not selected\n")
        git("add", ".")
        git("commit", "--quiet", "-m", "Second fixture")
        self.data["sources"]["fixture"].update(url=self.source.as_uri(), ref=first)
        self.save_catalogue()
        preview = self.run_cli(local=False, offline=False)
        self.assert_ok(preview)
        self.assertIn(first, preview.stdout)
        self.assertFalse(self.destination.exists())
        planning = self.run_cli("--apply", "--group", "planning", local=False, offline=False)
        self.assert_ok(planning)
        self.assertEqual({p.name for p in self.destination.iterdir()}, {"optional"})
        union = self.run_cli("--apply", "--group", "planning", "--group", "core",
                             "--group", "planning", local=False, offline=False)
        self.assert_ok(union)
        self.assertIn(first, union.stdout)
        self.assertEqual({p.name for p in self.destination.iterdir()},
                         {"alpha", "helper", "optional"})
        self.assertEqual((self.destination / "alpha/SKILL.md").read_text(), "# alpha\n")


if __name__ == "__main__":
    unittest.main()
