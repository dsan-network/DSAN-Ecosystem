# DSAN Architecture

**DSAN — Decentralized Sovereign Agent Network**

## 1. Purpose

This document describes the architectural organization of the DSAN ecosystem and the relationships among its principal components.

It complements the **Guardian System Definition** and provides an architectural reference for implementations, simulations, protocols, and domain applications within the DSAN ecosystem.

This document defines architectural relationships and responsibilities. It does not prescribe a single implementation, programming language, operating system, hardware platform, database, or network technology.

---

# 2. Architectural Foundation

The fundamental reference of DSAN is the **Sovereign Digital Entity**.

A sovereign entity may manifest computationally through one or more operational components while maintaining a conceptual distinction between the entity itself and the infrastructure through which it acts.

The principal relationship is:

```text
Sovereign Digital Entity
            │
            ▼
         Guardian
            │
      ┌─────┴─────┐
      ▼           ▼
 GuardianOS     Totem
                  │
            optional physical
                 anchor
```

The DSAN Core and DSAN Network provide mechanisms and environments through which these entities, Guardians, and applications may interact.

```text
                Sovereign Digital Entity
                           │
                           ▼
                        Guardian
                           │
                    ┌──────┴──────┐
                    ▼             ▼
               GuardianOS       Totem
                    │
                    ▼
                 DSAN Core
                    │
                    ▼
               DSAN Network
                    │
             ┌──────┴──────┐
             ▼             ▼
           DREX        RadSecure
```

This representation describes **architectural relationships**, not a mandatory execution sequence.

---

# 3. Architectural Entities

## 3.1 Sovereign Digital Entity

The Sovereign Digital Entity is the conceptual owner of sovereignty within the architecture.

The entity may possess:

* sovereign identity;
* authority;
* intent;
* state;
* presence;
* delegated capabilities;
* trust relationships;
* authorization capabilities.

Sovereignty is not created by a software process, cryptographic key, physical device, or network.

These mechanisms provide representations, controls, evidence, and operational capabilities associated with the entity.

---

# 4. Guardian

The Guardian is the operational unit through which a sovereign digital entity acts within a computational environment.

The Guardian provides a boundary between the sovereign entity and the computational environment in which its operations occur.

The Guardian may coordinate:

* identity;
* presence;
* intent;
* authority;
* authorization;
* state;
* delegation;
* communication;
* execution;
* evidence.

The Guardian is not equivalent to the sovereign entity.

```text
Sovereign Entity
       │
       │ sovereignty
       ▼
    Guardian
       │
       │ operational manifestation
       ▼
Computational Environment
```

A Guardian may be implemented entirely in software or may interact with physical infrastructure.

---

# 5. GuardianOS

GuardianOS is the computational environment that supports and protects the operational Guardian.

Its implementation may provide:

* secure boot;
* protected execution;
* local state;
* cryptographic services;
* authorization enforcement;
* communication;
* hardware abstraction;
* secure services;
* recovery mechanisms;
* controlled software evolution.

GuardianOS is therefore an implementation environment and enforcement boundary.

It does not itself constitute sovereignty.

---

# 6. Totem

The Totem is an optional physical sovereignty anchor.

A Totem may establish a controlled relationship between a sovereign entity and a physical environment.

Depending on the implementation, a Totem may participate in:

* physical presence;
* physical authorization;
* secure key operations;
* protected execution release;
* local autonomy;
* recovery;
* revocation-related operations.

The Totem does not create sovereignty and does not independently constitute the sovereign entity.

Its participation is determined by the requirements of the operation and implementation.

Therefore:

```text
Totem
  ≠
Sovereignty
```

and:

```text
Totem
  ≠
Guardian
```

---

# 7. GuardianRing

GuardianRing is a possible wearable implementation of the Totem concept.

It is therefore an implementation of a physical anchor rather than an independent architectural entity.

Other physical implementations may be used without changing the underlying architecture.

```text
Totem
  │
  ├── GuardianRing
  ├── dedicated hardware
  └── other physical implementations
```

---

# 8. DSAN Core

The DSAN Core represents the logical and protocol mechanisms required to support DSAN operations.

Depending on implementation, the Core may provide mechanisms for:

* event representation;
* identity verification;
* authorization;
* state management;
* delegation;
* evidence;
* policy evaluation;
* cryptographic verification;
* synchronization;
* auditability;
* deterministic processing.

The Core should not be interpreted as the sovereign entity.

Likewise, a specific implementation of the Core does not necessarily implement every DSAN architectural concept.

The `dsan-core` repository is therefore an implementation/reference environment rather than the complete definition of DSAN.

---

# 9. DSAN Network

The DSAN Network represents the distributed computational environment through which sovereign entities, Guardians, nodes, applications, and other participants may interact.

The network may provide:

* communication;
* synchronization;
* discovery;
* distributed state exchange;
* evidence propagation;
* trust relationships;
* interoperability.

DSAN does not require a particular networking technology.

A DSAN Network may be implemented using conventional networks, peer-to-peer systems, institutional networks, edge environments, or other distributed infrastructures.

---

# 10. Identity

Identity establishes the referential identity of an entity within a DSAN environment.

Identity mechanisms may include:

* cryptographic keys;
* credentials;
* certificates;
* hardware-backed identity;
* other verifiable representations.

Identity establishes **who or what is being represented**.

It does not automatically establish:

* current presence;
* authority for every operation;
* authorization;
* execution permission.

---

# 11. Presence

Presence describes the manifestation or availability of an entity within a particular context.

Presence may be established through:

* software state;
* network interaction;
* cryptographic interaction;
* physical interaction;
* trusted hardware;
* combinations of these mechanisms.

Presence and identity are therefore distinct.

An entity may be identifiable without being considered present for a particular operation.

Likewise, presence does not automatically imply authorization.

---

# 12. Intent

Intent represents an intended operation, state transition, or objective associated with a sovereign entity.

Intent may be represented by:

* signed requests;
* commands;
* authorization requests;
* state transitions;
* application-level instructions.

Intent must be evaluated within the applicable authority, state, policy, delegation, and contextual constraints.

---

# 13. Authority

Authority represents the legitimate capacity of an entity to determine or influence actions within a defined scope.

Authority is distinct from authorization.

Conceptually:

```text
Authority
   │
   │ may permit
   ▼
Authorization
   │
   │ may permit
   ▼
Execution
```

Authorization therefore does not create the underlying authority.

---

# 14. Authorization

Authorization is the contextual evaluation of whether a proposed operation may proceed.

Relevant conditions may include:

* identity;
* presence;
* intent;
* authority;
* state;
* delegation;
* context;
* policy;
* security conditions;
* validity;
* revocation status.

An implementation may express the decision through an Authorization Artifact.

Authorization mechanisms are contextual and may vary among applications.

---

# 15. Authorization Artifact

An Authorization Artifact is a verifiable representation of an authorization decision or authorization state.

It may contain or reference:

* authorized entity;
* operation;
* capability;
* scope;
* constraints;
* validity period;
* delegation;
* cryptographic evidence;
* provenance;
* revocation information.

The artifact provides a mechanism for downstream components to verify authorization without treating the artifact itself as the source of sovereignty.

---

# 16. Sovereign State

State represents the evolving operational condition of a sovereign entity and its associated Guardian.

State may include:

* current operational status;
* authorization status;
* delegated capabilities;
* trust relationships;
* revocation information;
* pending operations;
* synchronization state;
* recovery state;
* evidence.

State transitions should be treated as verifiable operations where required by the implementation.

---

# 17. Delegation

Delegation permits authority or capability to be derived from another authoritative entity.

Delegation should be:

* explicitly established;
* scoped;
* verifiable;
* bounded;
* revocable;
* traceable.

Derived authority must remain within the scope of the originating authority.

The validity of delegated authority therefore depends on the continued validity of its source.

---

# 18. Communication

Communication provides the exchange mechanism between participating components.

A DSAN communication mechanism may preserve:

* identity;
* provenance;
* integrity;
* authorization context;
* confidentiality;
* state information;
* delegation constraints.

Communication should not be treated merely as transport when the exchanged information affects sovereign state or authority.

---

# 19. Execution

Execution represents the realization of an operation within a computational environment.

DSAN maintains a strict conceptual distinction:

```text
Authority
    ≠
Authorization
    ≠
Execution
```

A valid authority does not imply that every operation is authorized.

An authorization decision does not necessarily imply immediate execution.

Execution may additionally depend on:

* local security conditions;
* state;
* physical requirements;
* resource availability;
* policy;
* synchronization;
* implementation-specific controls.

---

# 20. Evidence

Evidence provides verifiable information about relevant events, decisions, state transitions, and executions.

Possible evidence mechanisms include:

* signed events;
* hashes;
* authorization artifacts;
* execution records;
* provenance;
* timestamps;
* audit records;
* append-only logs;
* Merkle structures;
* distributed ledgers.

DSAN does not require a blockchain or any particular ledger technology.

---

# 21. Trust

Trust represents a relationship or confidence model between participants.

Trust may exist between:

* sovereign entities;
* Guardians;
* nodes;
* applications;
* institutions;
* physical anchors.

Trust is contextual.

Trust does not automatically confer authority.

Authority does not automatically imply unrestricted trust.

Implementations should therefore define the scope and semantics of relevant trust relationships.

---

# 22. Offline and Local Autonomy

DSAN may operate in environments where network connectivity is intermittent or unavailable.

A Guardian or node may therefore retain locally valid state and capabilities.

However:

```text
Offline
  ≠
Unrestricted autonomy
```

Local operation remains constrained by:

* previously established authority;
* authorization validity;
* expiration;
* delegation scope;
* revocation;
* local policy;
* security state.

Reconnection must reconcile local state according to the applicable consistency and synchronization rules.

A revoked authority must not be resurrected merely because a node operated offline.

---

# 23. Governance

Governance maintains the rules and coherence of a DSAN implementation or network.

Governance may cover:

* protocol evolution;
* participation;
* authorization policy;
* security requirements;
* interoperability;
* software evolution;
* audit;
* recovery;
* revocation;
* compatibility.

Governance governs the system.

It does not create sovereignty.

---

# 24. Architectural Relationships

The architecture should be understood as a graph of relationships rather than as a fixed linear pipeline.

For example:

```text
                    Identity
                       │
                       ▼
                    Presence
                       │
                       ▼
                     Intent
                       │
                       ▼
                    Authority
                       │
              ┌────────┴────────┐
              ▼                 ▼
            State          Delegation
              │                 │
              └────────┬────────┘
                       ▼
                    Context
                       │
                       ▼
                   Authorization
                       │
                       ▼
                    Execution
                       │
                       ▼
                    Evidence
```

This diagram represents conceptual dependencies.

It does **not** mean that every operation must traverse every element.

For example:

* some operations may not require a Totem;
* some may not require delegation;
* some may not require distributed consensus;
* some may operate entirely locally;
* some may require physical presence;
* others may be purely computational.

The architecture therefore supports contextual composition.

---

# 25. Security Boundary

Security mechanisms may exist at multiple boundaries:

```text
Sovereign Entity
       │
       ▼
    Guardian
       │
       ▼
 GuardianOS
       │
   ┌───┴────┐
   ▼        ▼
 Totem    Network
   │        │
   └───┬────┘
       ▼
   DSAN Core
       │
       ▼
 Applications
```

Each boundary may implement different controls.

The architecture does not assume that one mechanism provides complete security.

Security properties must therefore be evaluated against the specific implementation and threat model.

---

# 26. Implementation Independence

The following equivalences must not be assumed:

```text
Totem        ≠ ESP32
GuardianOS   ≠ a specific operating system
Guardian     ≠ a hardware device
DSAN Core    ≠ a programming language
DSAN Network ≠ a blockchain
Authorization ≠ cryptographic signature
Identity     ≠ private key
Evidence     ≠ blockchain ledger
```

Specific technologies may implement these concepts, but the concepts remain architecturally independent from their implementations.

---

# 27. Repository Boundaries

The architecture is reflected in the ecosystem repository structure.

```text
DSAN-Ecosystem
│
├── architecture
│
├── protocols
│
├── principles
│
└── governance
        │
        ├───────────────┐
        ▼               ▼
   dsan-core        GuardianOS
        │               │
        │             Totem
        │
        ├───────────────┐
        ▼               ▼
   Simulator          Applications
                         │
                  ┌──────┴──────┐
                  ▼             ▼
                DREX        RadSecure
```

The boundaries have the following purpose:

### DSAN-Ecosystem

Architectural and documentation authority.

### dsan-core

Reference/experimental implementation of selected logical mechanisms.

### GuardianOS

Guardian computational environment and associated physical-reference implementation.

### DSAN Simulator

Experimental and educational environment.

### DSAN-DREX-ENTERPRISE

Enterprise/domain implementation.

### RadSecure

Healthcare/domain implementation.

---

# 28. Architectural Invariants

The following distinctions should remain invariant across implementations:

1. Sovereignty belongs to the sovereign entity.
2. Guardian is an operational manifestation of the entity.
3. GuardianOS is an implementation environment.
4. Totem is an optional physical sovereignty anchor.
5. GuardianRing is one possible Totem implementation.
6. Identity is distinct from presence.
7. Authority is distinct from authorization.
8. Authorization is distinct from execution.
9. Delegated authority is bounded by originating authority.
10. Offline operation does not imply unrestricted autonomy.
11. Revocation must not be defeated by disconnection.
12. Governance does not create sovereignty.
13. Evidence provides verifiability but does not itself constitute authority.
14. Implementation technology does not redefine the architectural concept.

---

# 29. Architectural Summary

The DSAN architecture establishes a separation between:

```text
WHO
  → Identity

WHERE / HOW PRESENT
  → Presence

WHAT IS INTENDED
  → Intent

WHAT MAY BE DONE
  → Authority

WHETHER AN OPERATION MAY PROCEED
  → Authorization

WHAT ACTUALLY HAPPENED
  → Execution + Evidence

HOW AUTHORITY IS DERIVED
  → Delegation

HOW CONDITION EVOLVES
  → State

HOW PARTICIPANTS RELATE
  → Trust

HOW THE SYSTEM REMAINS COHERENT
  → Governance
```

The physical and computational architecture provides the mechanisms through which these concepts can be manifested:

```text
Sovereign Entity
        ↓
     Guardian
        ↓
   GuardianOS
        ↓
      Totem
   (optional)
        ↓
   DSAN mechanisms
        ↓
  Distributed environment
```

The exact composition depends on the operational context.

---

# 30. Architectural Principle

The central architectural principle is:

> **A sovereign digital entity is not defined by the technology through which it is represented. The architecture defines the relationships and constraints through which sovereignty can be manifested, verified, authorized, exercised, and preserved across computational environments.**
