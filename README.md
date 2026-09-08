# DSAN — Decentralized Sovereign Agent Network

**Open architectural framework for sovereign digital entities**

DSAN (Decentralized Sovereign Agent Network) is an open architectural framework for representing, governing, and operating **sovereign digital entities** in distributed computational environments.

The architecture defines how concepts such as **identity, presence, intent, authority, authorization, state, delegation, communication, execution, evidence, trust, and governance** can be represented and coordinated without requiring a single centralized authority.

DSAN is intentionally **technology-independent**. Specific implementations may use different operating systems, hardware, cryptographic mechanisms, databases, networks, or application stacks.

---

## 1. Architectural Purpose

DSAN addresses a fundamental problem in distributed computing:

> How can a digital entity maintain a coherent identity, authority, state, presence, and ability to act across multiple computational environments while preserving verifiability, control, and continuity?

The architecture therefore separates concepts that are frequently conflated in conventional systems:

* identity is not presence;
* presence is not authority;
* authority is not authorization;
* authorization is not execution;
* execution is not evidence;
* a physical device is not the sovereign entity;
* software infrastructure does not itself constitute sovereignty.

These distinctions form the foundation of DSAN.

---

## 2. Core Architectural Model

The DSAN architecture is organized around a **Sovereign Digital Entity** and the mechanisms through which that entity manifests and operates computationally.

```text
                  SOVEREIGN DIGITAL ENTITY
                             │
                             │ operational manifestation
                             ▼
                          GUARDIAN
                             │
                   ┌─────────┴─────────┐
                   │                   │
                   ▼                   ▼
              GuardianOS             Totem
                   │             optional physical
                   │                 anchor
                   │
                   ▼
                DSAN CORE
                   │
          protocols / state /
       authorization / evidence
                   │
                   ▼
              DSAN NETWORK
                   │
          ┌────────┴────────┐
          ▼                 ▼
        DREX            RadSecure
```

This diagram represents **architectural relationships**, not a mandatory execution pipeline.

A DSAN implementation may use only a subset of these components depending on its context.

---

## 3. Sovereign Digital Entity

The **Sovereign Digital Entity** is the fundamental conceptual reference of the architecture.

Sovereignty belongs to the entity.

The entity may possess:

* a sovereign identity;
* persistent or evolving state;
* authority;
* intent;
* presence;
* delegated authority;
* relationships of trust;
* authorization capabilities;
* communication capabilities;
* controlled execution capabilities.

The entity is not equivalent to any particular device, software process, cryptographic key, or network node.

Implementations may represent the entity through different technical mechanisms while preserving the architectural distinction between the entity and its computational manifestations.

---

## 4. Guardian

The **Guardian** is the operational unit through which a sovereign digital entity acts within a computational environment.

The Guardian is therefore neither:

* the sovereign entity itself;
* the source of sovereignty;
* the operating system;
* the physical Totem;
* nor the DSAN network.

The Guardian provides an operational boundary through which identity, state, authority, authorization, execution, and protection mechanisms may be coordinated.

A Guardian may operate entirely in software or may be associated with physical infrastructure.

---

## 5. GuardianOS

**GuardianOS** is the computational environment responsible for supporting and protecting the operational Guardian.

It may provide mechanisms for:

* secure initialization;
* execution control;
* local state management;
* authorization enforcement;
* cryptographic operations;
* interaction with physical anchors;
* protected services;
* communication;
* hardware abstraction;
* recovery and controlled evolution.

GuardianOS is an **implementation layer**.

It does not define the sovereignty of the entity and does not replace the DSAN architectural model.

---

## 6. Totem

The **Totem** is an optional physical sovereignty anchor.

It provides a possible physical boundary through which a sovereign entity can establish or reinforce relationships between computational authority and a controlled physical environment.

A Totem may participate in:

* physical authorization;
* presence verification;
* secure interaction;
* protected key operations;
* execution release;
* local autonomy;
* recovery or revocation mechanisms.

The Totem is **not the sovereign entity** and does not independently create authority.

Its use is contextual and operation-dependent.

A DSAN implementation does not necessarily require a physical Totem.

---

## 7. GuardianRing

A **GuardianRing** is one possible wearable implementation of a Totem.

The term describes a physical implementation, not a separate architectural source of sovereignty.

Other physical implementations may exist, including dedicated devices or other secure hardware configurations.

The architecture therefore distinguishes:

```text
Sovereign Entity
        │
     Guardian
        │
   GuardianOS
        │
      Totem
        │
 GuardianRing
   (one possible
   implementation)
```

---

## 8. Identity, Presence, Intent and Authority

DSAN explicitly separates four related concepts.

### Identity

Represents **who or what the entity is** within the system.

### Presence

Represents whether and how the entity is currently manifested or reachable within a particular computational context.

### Intent

Represents what the entity seeks or authorizes as an intended action or state transition.

### Authority

Represents the legitimate capacity of the entity to determine or influence actions within an applicable scope.

These concepts may interact, but none should be treated as interchangeable.

---

## 9. Authorization

Authorization is the contextual mechanism through which a proposed operation is evaluated against the applicable authority, state, policy, delegation, and security conditions.

Authorization does not create sovereignty.

A conceptual authorization decision may depend on:

```text
Identity
   +
Presence
   +
Intent
   +
Authority
   +
State
   +
Delegation
   +
Context
   +
Policy
   +
Security conditions
   ↓
Authorization Decision
```

Different DSAN implementations may realize these mechanisms differently.

---

## 10. Authorization Artifact

An **Authorization Artifact** is a verifiable representation of an authorization decision or authorization state.

Depending on the implementation, it may contain or reference:

* the authorized entity;
* operation or capability;
* contextual constraints;
* validity conditions;
* delegation information;
* cryptographic evidence;
* expiration;
* revocation state;
* provenance.

The artifact allows downstream components to verify that an operation has received the required authorization without assuming that authorization itself constitutes sovereignty.

---

## 11. Sovereign State

A sovereign entity may maintain a state that evolves over time.

State may include:

* operational status;
* authorization status;
* delegated capabilities;
* trust relationships;
* revocation information;
* pending operations;
* synchronization state;
* evidence;
* recovery information.

State continuity is particularly important in distributed and intermittently connected environments.

Offline operation does not imply unrestricted autonomy.

A previously revoked or expired authority must not automatically become valid merely because a node is temporarily disconnected.

---

## 12. Sovereign Presence

Presence is treated independently from identity and authorization.

A digital entity may be:

* cryptographically identifiable but not currently present;
* present but not authorized for a specific operation;
* authorized for an operation but not physically anchored;
* physically anchored without that anchor itself being the sovereign entity.

Presence mechanisms may be implemented through software, cryptographic protocols, network relationships, physical interaction, or combinations of these mechanisms.

---

## 13. Sovereign Delegation

Delegation allows an entity to transfer or derive a bounded capability from an existing authority.

Delegation should be:

* explicit;
* scoped;
* verifiable;
* time-bounded when appropriate;
* revocable;
* traceable.

Derived authority cannot exceed the authority from which it originates.

Revocation of the originating authority must propagate according to the applicable protocol and consistency model.

---

## 14. Sovereign Communication

DSAN communication mechanisms allow sovereign entities and their Guardians to exchange information while preserving:

* identity;
* provenance;
* authorization context;
* integrity;
* confidentiality where required;
* state consistency;
* delegation constraints.

Communication is therefore not merely message transport.

It is part of the mechanism through which sovereign relationships are maintained across distributed environments.

---

## 15. Execution

Execution represents the actual realization of an authorized operation within a computational environment.

DSAN maintains the distinction:

```text
Authority
    ≠
Authorization
    ≠
Execution
```

A system may therefore determine that an entity has authority without automatically executing an operation.

Likewise, an authorization decision may be subject to additional execution-time conditions.

Individual implementations may introduce mechanisms such as policy validation, consensus, physical authorization, local security checks, or other enforcement mechanisms.

These are implementation choices rather than universal architectural requirements.

---

## 16. Evidence and Auditability

DSAN supports the concept of **verifiable evidence** associated with relevant operations and state transitions.

Evidence may include:

* signed events;
* authorization artifacts;
* execution records;
* state transitions;
* provenance;
* timestamps;
* cryptographic hashes;
* audit records.

An implementation may use append-only ledgers, Merkle structures, distributed logs, databases, or other mechanisms to preserve evidence.

No particular storage technology is mandated by the architecture.

---

## 17. Distributed and Offline Operation

DSAN is designed to support distributed environments in which connectivity, synchronization, or centralized availability may be limited.

A node may therefore maintain local capabilities and state while disconnected.

However:

> **Offline operation does not imply unrestricted sovereignty.**

Local autonomy must remain bounded by:

* previously established authority;
* authorization constraints;
* validity periods;
* revocation mechanisms;
* local security policy;
* synchronization rules.

Reconnection must not be treated as a mechanism for resurrecting invalid authority.

---

## 18. Trust

Trust relationships within DSAN are contextual and verifiable.

Trust may exist between:

* sovereign entities;
* Guardians;
* computational nodes;
* applications;
* physical anchors;
* institutional environments.

Trust does not automatically imply authority.

Likewise, authority does not necessarily imply unrestricted trust.

The architecture therefore favors explicit relationships and verifiable evidence over implicit trust assumptions.

---

## 19. Governance

Governance defines the rules by which an implementation or network maintains architectural coherence.

Governance may address:

* protocol evolution;
* authorization policies;
* participation rules;
* software evolution;
* security requirements;
* auditability;
* recovery;
* revocation;
* interoperability;
* compatibility;
* dispute and exception handling.

Governance does not create sovereignty.

It governs the mechanisms through which sovereignty is represented and exercised within a given environment.

---

## 20. Technology Independence

DSAN does not require a specific technology stack.

Implementations may use:

* embedded systems;
* secure elements;
* conventional servers;
* cloud infrastructure;
* edge computing;
* distributed databases;
* blockchain or distributed ledgers;
* cryptographic protocols;
* mobile devices;
* IoT devices;
* enterprise systems.

The architectural concepts must remain distinguishable from their technological implementations.

For example:

```text
Totem
    ≠
ESP32

GuardianOS
    ≠
a particular operating system

DSAN Core
    ≠
a particular programming language

DSAN Network
    ≠
a particular blockchain
```

---

## 21. Ecosystem Repositories

The DSAN ecosystem is organized by architectural responsibility.

| Repository               | Role                                                                     |
| ------------------------ | ------------------------------------------------------------------------ |
| **DSAN-Ecosystem**       | Architecture, principles, protocols, documentation and public reference  |
| **dsan-core**            | Experimental/reference implementation of selected DSAN mechanisms        |
| **GuardianOS**           | Guardian computational environment and physical-reference implementation |
| **DSAN Simulator**       | Simulation, experimentation and educational research                     |
| **DSAN-DREX-ENTERPRISE** | Enterprise/domain application based on DSAN concepts                     |
| **RadSecure**            | Healthcare/domain application based on DSAN concepts                     |

Domain applications are **not part of the architectural core**.

They demonstrate how DSAN concepts can be applied to specific operational environments.

---

## 22. Implementation Maturity

DSAN distinguishes architectural maturity from implementation maturity.

A concept may be:

* **Conceptual** — formally defined but not implemented;
* **Experimental** — implemented for research or testing;
* **Reference** — implemented to demonstrate an architectural mechanism;
* **Application** — integrated into a domain-specific system;
* **Production** — deployed under operational requirements and appropriate validation.

The existence of source code does not by itself imply production readiness, certification, formal verification, or security certification.

---

## 23. Security Philosophy

Security within DSAN is based on layered and contextual controls.

Relevant mechanisms may include:

* cryptographic identity;
* protected execution;
* authorization;
* delegation;
* revocation;
* physical anchoring;
* state integrity;
* provenance;
* auditability;
* secure communication;
* recovery.

No individual mechanism should be interpreted as providing absolute security.

Security claims must remain proportional to the implementation, threat model, testing, and evidence available.

---

## 24. Research Direction

DSAN provides a foundation for research into:

* sovereign digital identity;
* distributed authorization;
* autonomous digital agents;
* edge sovereignty;
* physical-digital trust boundaries;
* authorization artifacts;
* decentralized governance;
* offline-capable systems;
* provenance-aware execution;
* sovereign state management;
* secure human-machine interaction;
* distributed institutional systems.

The architecture is intentionally open to different implementations and research directions.

---

## 25. Relationship to the Guardian System Definition

The **Guardian System Definition** provides the architectural definition of the Guardian-centered model used by this ecosystem.

The repositories in this organization should implement, demonstrate, or apply the architecture without redefining its fundamental ontology independently.

The distinction is intentional:

```text
Guardian System Definition
            │
            ▼
     Architectural model
            │
            ▼
      DSAN-Ecosystem
            │
     ┌──────┼─────────┐
     ▼      ▼         ▼
   Core  GuardianOS  Simulator
     │
   ┌─┴─────────────┐
   ▼               ▼
 DREX           RadSecure
```

---

## 26. Fundamental Principle

The DSAN architecture can be summarized as follows:

> **Sovereignty belongs to the entity; the Guardian manifests it operationally; GuardianOS protects and executes; the Totem may anchor it physically; DSAN Core structures its mechanisms and relationships; the DSAN Network enables distributed interaction; and governance preserves coherence and continuity.**

---

## 27. Status

DSAN is an evolving open architecture and research ecosystem.

Individual repositories may have different levels of maturity and different licensing or access conditions.

The architectural repository should therefore not be interpreted as a declaration that every component of the ecosystem is production-ready.

---

## License

The **DSAN-Ecosystem** repository is distributed under the **Apache License 2.0**.

See [`LICENSE`](LICENSE) for the complete license text.

Copyright © 2026 Alessandro Turok da Silva Collares.
