# Turn useful experience into reusable guidance

Some work teaches a method worth repeating. Some exposes a defect in an existing instruction. Preserve those lessons in the smallest useful form—without turning every completed task into a retrospective or blocking delivery on optional improvements.

## When to propose an improvement

Good candidates include a non-obvious technique intended to recur, repeated user corrections, a recurring expensive search, or new evidence that contradicts existing guidance. One well-understood solution can be enough to propose reusable guidance when repetition is intended; distinguish demonstrated behavior from assumptions about other environments.

A useful proposal says what happened, what evidence matters, why the lesson transfers, where it belongs, and what bounded check would support the change. It should not merely suggest “make this a skill” because a session was long.

## Choose the right artifact

| Learning | Usually belongs in |
|---|---|
| Project fact, trade-off, or decision | Project documentation or ADR |
| Local navigation or convention | A concise agent instruction or linked reference |
| Deterministic repeated operation | Script, check, or existing tool |
| Portable judgment or procedure | A skill |
| Correction to an existing method | The existing skill/reference, not a second owner |
| Tentative incident explanation | A note with uncertainty until evidence supports broader guidance |

A skill teaches when and how to apply a technique. It is not a chronological story about how one bug was fixed. Keep incident evidence where useful, then extract the transferable conditions, actions, limits, and stopping criteria. Sanitize examples and preserve applicable attribution.

## Authoring support

The optional `authoring` group installs **Matt's `writing-for-agents`** and its supporting reference files. It helps with clear triggers, information hierarchy, concise instructions, and completion criteria. It does not add Superpowers, another TDD owner, a renderer, or another model tier.

```bash
python3 skills/setup-development-environment/scripts/install.py \
  --group core --group authoring
```

Use the same source/offline options as your installation. This previews; add `--apply` only after approval. On Windows use your Python 3.10+ command, such as `python` or `py -3`.

## Update deliberately

1. Find the existing owner and authoritative source. Prefer a correction or useful pointer over another skill with overlapping triggers.
2. Propose the specific change, evidence, expected reuse, and a proportionate check.
3. After approval, edit the maintained repository, preserving scope and unrelated work.
4. Check the intended outcome. Behavioral guidance can use a bounded representative scenario; reference-only changes may need structural, link, or native-loading checks. Static reading is not an executed behavior test.
5. Report what changed, what was checked, and what remains uncertain. Committing and updating an installed environment remain separately authorized actions.

Do not silently modify globally installed skills, plugin caches, or a source revision just to make the current task easier. Deployment should be reviewable and repeatable through the setup process. A more extensive authoring experiment can be useful, but it needs a defined question and budget—not automatic loops until every imagined edge case is covered.

## Example

Suppose several workers retry a task after a tool permission denial, wasting time without new evidence. A useful improvement is a specific recovery rule: identify the missing capability, preserve partial work, and request an allowed next action instead of trying a stronger model as a permission bypass.

The evidence might be a sanitized worker report and a small scenario showing the wrong recovery decision. The reusable artifact is the corrected worker-recovery instruction, not a new document retelling the session. The original feature can still be accepted while that improvement is proposed as follow-up work.
