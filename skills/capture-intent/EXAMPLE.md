# Illustrative intent anchor: save-file compatibility

This hypothetical C# project has an approved request to allow the next version to read older save files. The text and code below illustrate intent documentation, **not** an approved API or a mandated format.

Players with older saves need to continue their games after upgrading; maintainers need to know why the loader tolerates legacy fields. The desired outcome is that supported older saves load without changing the current save format. The proposed direction is to translate older payloads at the loading boundary, keeping game logic focused on the current model. This isolates compatibility behavior and leaves room to retire it deliberately when support policy changes.

Scope is reading documented legacy versions. Rewriting every historical file on disk is out of scope because upgrade should not modify a player's data simply by opening it. Recovery of corrupt or unknown-version files remains an explicit product decision, not a promise of best-effort parsing. A useful success signal is that representative supported legacy fixtures load to the current model while current-version saves remain unchanged; which legacy versions are supported is still to be confirmed against the approved spec. Link the version policy, decision record, and task here when they exist rather than copying their details.

One focused boundary view, only if it helps readers:

```mermaid
flowchart LR
    File[Save file] -->|read version and payload| Loader[Compatibility loader]
    Loader -->|translate supported legacy format| Model[Current save model]
    Model -->|restore state| Game[Game logic]
```

Illustrative C# shape, **not** an approved contractual API:

```csharp
// Example only: actual method names and supported versions come from the project spec.
CurrentSave LoadSave(Stream source)
{
    var envelope = ReadEnvelope(source);
    return envelope.Version == CurrentVersion
        ? ReadCurrent(envelope)
        : TranslateSupportedLegacy(envelope);
}
```

The diagram is plain Mermaid; rendering has not been verified here. If an adequate approved solution brief already says all this, link it rather than creating another file.
