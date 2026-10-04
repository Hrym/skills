"""Bundled OpenCode routing profile, without provider calls or user config edits."""

import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
ROUTER = ROOT / "skills" / "setup-opencode-routing"


def agent_frontmatter(name):
    text = (ROUTER / "templates" / "agents" / f"{name}.md").read_text(encoding="utf-8")
    return dict(re.findall(r"^(model|variant|mode): (.+)$", text, re.MULTILINE))


class RoutingTemplateTests(unittest.TestCase):
    def test_no_astra_profile_bindings_and_effort(self):
        config = json.loads((ROUTER / "templates" / "opencode.jsonc").read_text(encoding="utf-8"))
        self.assertEqual(config["model"], "openai/gpt-6.1-sol")
        for name in ("build", "plan", "general"):
            with self.subTest(name=name):
                self.assertEqual(config["agent"][name]["model"], "openai/gpt-6.1-sol")
                self.assertEqual(config["agent"][name]["variant"], "medium")
        self.assertEqual(config["agent"]["explore"]["model"], "openai/gpt-6-luna")
        self.assertEqual(config["agent"]["explore"]["variant"], "medium")
        for name, model, variant in (
            ("researcher", "openai/gpt-6.1-sol", "medium"),
            ("architect", "openai/gpt-6.1-sol", "high"),
            ("implement-complex", "openai/gpt-6.1-sol", "high"),
            ("implement-small", "openai/gpt-6-luna", "medium"),
            ("verify", "openai/gpt-6-luna", "medium"),
        ):
            with self.subTest(name=name):
                self.assertEqual(agent_frontmatter(name)["model"], model)
                self.assertEqual(agent_frontmatter(name)["variant"], variant)

    def test_astra_worker_profile_uses_medium_without_changing_no_astra_high(self):
        """Catch applying one effort setting to both profiles during setup."""
        table = (ROUTER / "SKILL.md").read_text(encoding="utf-8")
        bindings = {}
        for line in table.splitlines():
            cells = [cell.strip() for cell in line.split("|")[1:-1]]
            if len(cells) == 3 and cells[0] in ("`architect`", "`implement-complex`"):
                bindings[cells[0]] = cells[1:]
        self.assertEqual(bindings, {
            "`architect`": ["GPT-6 Astra `medium`", "GPT-6.1 Sol `high`"],
            "`implement-complex`": ["GPT-6 Astra `medium`", "GPT-6.1 Sol `high`"],
        })
        for name in ("architect", "implement-complex"):
            with self.subTest(name=name):
                self.assertEqual(agent_frontmatter(name)["model"], "openai/gpt-6.1-sol")
                self.assertEqual(agent_frontmatter(name)["variant"], "high")

    def test_deep_is_disabled_by_default_and_opt_in_example_is_primary(self):
        config = json.loads((ROUTER / "templates" / "opencode.jsonc").read_text(encoding="utf-8"))
        self.assertEqual(config["agent"]["deep"], {"disable": True})
        reference = (ROUTER / "SETUP.md").read_text(encoding="utf-8")
        example = json.loads(reference.split("```json\n", 1)[1].split("\n```", 1)[0])
        self.assertEqual(example["mode"], "primary")
        self.assertIs(example["disable"], False)
        self.assertEqual(example["model"], "openai/gpt-6-astra")
        self.assertEqual(example["variant"], "medium")
        self.assertEqual(example["permission"]["task"], config["agent"]["build"]["permission"]["task"])
        self.assertEqual(example["permission"]["skill"], config["agent"]["build"]["permission"]["skill"])
        for name in ("build", "plan"):
            self.assertNotIn("deep", config["agent"][name]["permission"]["task"])
        self.assertNotIn("deep", example["permission"]["task"])


if __name__ == "__main__":
    unittest.main()
