# Architectural terminology — Digital Sovereign Entity (DSE)

**Status:** terminology alignment proposed in a draft migration PR, based on the DSAN manager's decision DEC-GRD-021 (alternative A), 2026-10-27.  
**Scope:** public architectural wording only. No runtime, protocol, identity, hardware or license changes.

## Canonical designation

**Digital Sovereign Entity (DSE)** is the canonical English term for the conceptual entity that holds sovereignty in the DSAN architecture.

**Sovereign Digital Entity** is the approved historical/descriptive alias for **the same concept**. The alias does **not** designate a second entity, actor, legal person, resource type or interoperable schema name.

The Portuguese explanatory translation **Entidade Digital Soberana (EDS)** is not a new protocol identifier.

## Preserved architectural boundaries

- A DSE is not the Guardian, GuardianOS, Totem, Guardian device, key, software process, account or network.
- Sovereign Identity represents a DSE but does not by itself grant authority.
- Authority does not equal contextual authorization or execution permission.
- Execution Intent does not confer approval; Execution Decision and Execution Release remain distinct from actual Execution.
- An evidence record, signature, hash or ledger entry does not create sovereign authority.
- Offline behavior remains bounded by previously established valid policy, delegation and revocation rules.

## Compatibility and history

The change is editorial and conceptual: it does not rename any API field, DID method, existing serialized message, software class, on-chain contract or database column.

The prior term remains searchable in **this alias mapping**. Readers of older citations or historical whitepapers should interpret it as *Digital Sovereign Entity (DSE)* under DEC-GRD-021, without retroactively rewriting historical publications. Technical consumers must be evaluated independently if later migrations touch wire-level identifiers.

## Affected current reference documentation

- [Main README](../README.md)
- [Architecture](architecture.md)
- [Architectural principles](principles.md)
- [Governance](governance.md)
- [Related work](../references/related-work.md)

Historical whitepapers remain unchanged. The files above preserve the architecture's semantics while making the chosen designation consistent.

**Decision vs implementation:** the manager approved the terminology choice; incorporating this documentation still requires a separate PR review and merge.
