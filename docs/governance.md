# DSAN Governance

**DSAN — Decentralized Sovereign Agent Network**

## 1. Purpose

This document defines the governance principles for the DSAN ecosystem.

Governance exists to preserve:

* architectural coherence;
* protocol integrity;
* implementation interoperability;
* security;
* traceability;
* controlled evolution;
* compatibility;
* responsible maintenance.

Governance does not constitute or replace the sovereignty of entities operating within DSAN.

---

# 2. Governance Is Not Sovereignty

The fundamental distinction is:

```text id="gvr001"
Sovereignty
     ≠
Governance
```

Sovereignty belongs to the Sovereign Digital Entity.

Governance establishes rules for maintaining and evolving the technological and organizational environment through which sovereign entities may operate.

Governance therefore does not:

* create sovereign entities;
* acquire their authority;
* become the source of their identity;
* automatically authorize their actions;
* replace their Guardians;
* replace their authorization mechanisms.

---

# 3. Governance Scope

DSAN governance applies to the ecosystem itself.

It may cover:

* architecture;
* specifications;
* protocols;
* reference implementations;
* documentation;
* interoperability;
* security practices;
* release management;
* compatibility;
* repositories;
* contribution processes;
* versioning;
* deprecation;
* recovery;
* incident response.

Domain-specific applications may establish additional governance mechanisms appropriate to their own operational environments.

---

# 4. Architectural Authority

The architectural definition establishes the conceptual boundaries of the DSAN ecosystem.

The **Guardian System Definition** provides the architectural definition of the Guardian-centered model.

The `DSAN-Ecosystem` repository translates those architectural concepts into publicly accessible documentation, principles, and specifications.

Implementation repositories should not silently redefine fundamental architectural concepts.

When an implementation requires a change to concepts such as:

* Sovereign Entity;
* Guardian;
* GuardianOS;
* Totem;
* Identity;
* Presence;
* Authority;
* Authorization;
* Delegation;
* State;
* Execution;

the change should be treated as an architectural change.

---

# 5. Governance Layers

DSAN governance can be understood as several related layers:

```text id="gvr002"
Architectural Governance
        │
        ▼
Protocol Governance
        │
        ▼
Implementation Governance
        │
        ▼
Repository Governance
        │
        ▼
Application Governance
```

Each layer has a different scope.

### Architectural Governance

Maintains the conceptual integrity of DSAN.

### Protocol Governance

Maintains protocol definitions, semantics, compatibility, and evolution.

### Implementation Governance

Maintains reference implementations and their technical evolution.

### Repository Governance

Controls contribution, review, releases, documentation, and repository maintenance.

### Application Governance

Controls domain-specific deployments and operational policies.

---

# 6. Separation of Architectural and Implementation Decisions

An implementation detail must not automatically become an architectural requirement.

For example, an implementation may use:

* a specific consensus mechanism;
* a specific ledger;
* a specific cryptographic algorithm;
* a specific microcontroller;
* a physical Totem;
* a particular database;
* a particular operating system.

These choices do not automatically become mandatory DSAN architectural requirements.

Conversely, architectural invariants should not be removed merely because a particular implementation does not currently support them.

---

# 7. Protocol Evolution

DSAN protocols may evolve as implementation experience and research produce new requirements.

Protocol changes should be:

* documented;
* versioned;
* reviewed;
* tested where applicable;
* evaluated for compatibility;
* accompanied by migration guidance when necessary.

Changes that affect interoperability should receive particular attention.

---

# 8. Versioning

DSAN specifications and implementations should use explicit version identifiers.

Versioning should distinguish at least:

```text id="gvr003"
Architecture Version
Protocol Version
Implementation Version
Application Version
```

These versions are related but independent.

An implementation version change does not necessarily constitute an architectural change.

Likewise, an architectural revision may affect multiple implementations without requiring identical software versions.

---

# 9. Backward Compatibility

Where practical, DSAN protocol evolution should preserve backward compatibility.

When compatibility cannot be maintained, the change should specify:

* affected versions;
* affected interfaces;
* migration requirements;
* deprecated mechanisms;
* transition period;
* expected behavior after deprecation.

Compatibility must not override security requirements.

A vulnerable or invalid mechanism may require immediate deprecation despite compatibility costs.

---

# 10. Deprecation

A protocol, interface, implementation mechanism, or repository component may be deprecated when it is:

* obsolete;
* insecure;
* incompatible with the architecture;
* superseded by a better mechanism;
* no longer maintained;
* unsuitable for current operational requirements.

Deprecation should be documented whenever practical.

Deprecated mechanisms should not silently remain presented as current architectural requirements.

---

# 11. Security Governance

Security governance establishes processes for identifying, evaluating, communicating, and mitigating security issues.

It should address:

* vulnerability reporting;
* dependency management;
* cryptographic practices;
* credential handling;
* secrets management;
* release integrity;
* access control;
* incident response;
* security documentation.

Security claims must be supported by appropriate evidence.

Governance must not transform an unverified implementation into a claim of certification or formal security assurance.

---

# 12. Secrets and Credentials

Repositories must not intentionally contain operational secrets.

Examples include:

* private cryptographic keys;
* passwords;
* API credentials;
* production tokens;
* database credentials;
* signing secrets;
* confidential deployment configuration.

Development repositories should use appropriate mechanisms such as:

```text id="gvr004"
.env
.env.example
secret managers
development credentials
test fixtures
```

Test credentials must be clearly identified and must not be reused in production environments.

Previously exposed secrets should be treated as compromised until properly evaluated and rotated.

---

# 13. Repository Governance

Each repository within the DSAN ecosystem should define, as appropriate:

* its purpose;
* ownership or maintainership;
* license;
* contribution process;
* security reporting process;
* supported versions;
* release process;
* dependencies;
* architectural role.

Repositories should not make claims about capabilities that their implementation does not demonstrate.

---

# 14. Open and Restricted Components

The DSAN ecosystem may contain components with different access and licensing models.

For example:

```text id="gvr005"
Open Architecture
       │
       ├── Open reference implementations
       │
       ├── Experimental implementations
       │
       └── Restricted domain applications
```

An open DSAN architecture does not imply that every implementation or application must be open source.

Licensing decisions belong to the individual project and its applicable legal framework.

---

# 15. Domain Application Governance

Applications such as healthcare, financial, industrial, or governmental systems may require additional governance.

Such governance may address:

* regulatory requirements;
* institutional policies;
* data protection;
* clinical or operational safety;
* auditing;
* accountability;
* deployment authorization;
* domain-specific security.

Domain governance supplements DSAN governance.

It does not redefine the underlying DSAN architecture without an explicit architectural change.

---

# 16. Intellectual Property

The DSAN ecosystem may contain intellectual property associated with:

* software;
* documentation;
* protocols;
* research;
* hardware;
* inventions;
* domain applications.

Open licensing of one component does not automatically grant rights to unrelated proprietary components.

Patent, copyright, trademark, confidentiality, and contractual matters must be handled according to the applicable legal framework.

Repository documentation should avoid making legal claims that are broader than the rights actually granted.

---

# 17. Contributions

Contributions should preserve the architectural integrity of the ecosystem.

A contribution should preferably identify whether it affects:

```text id="gvr006"
Documentation
Protocol
Architecture
Implementation
Security
Application
```

Architectural changes should not be merged as ordinary implementation changes without appropriate review.

Contributors should document relevant compatibility or migration implications.

---

# 18. Architectural Change Process

A proposed architectural change should answer at least:

1. What architectural concept is changing?
2. Why is the change necessary?
3. Which existing principles are affected?
4. Which repositories are affected?
5. Does interoperability change?
6. Does security behavior change?
7. Does the change invalidate existing implementations?
8. Is migration required?
9. What version should identify the change?

This prevents implementation evolution from producing uncontrolled architectural drift.

---

# 19. Review

Changes should receive a level of review proportional to their impact.

A practical classification is:

| Change                                 | Typical review                        |
| -------------------------------------- | ------------------------------------- |
| Typographical/documentation correction | Maintainer review                     |
| Non-breaking implementation change     | Technical review                      |
| Protocol change                        | Protocol review                       |
| Security-sensitive change              | Security review                       |
| Architectural change                   | Architectural review                  |
| Breaking ecosystem change              | Architectural + implementation review |

The review process may evolve as the ecosystem grows.

---

# 20. Release Governance

Releases should distinguish between:

* experimental releases;
* development releases;
* reference releases;
* application releases;
* production releases.

A release should not be described as production-ready merely because source code exists.

Where applicable, release documentation should identify:

* version;
* changes;
* known issues;
* compatibility;
* security considerations;
* migration requirements.

---

# 21. Experimental and Research Work

Research repositories may contain:

* incomplete mechanisms;
* experimental protocols;
* simulations;
* prototypes;
* intentionally simplified security models;
* mechanisms under evaluation.

Research status should be explicitly identified.

Experimental results must not automatically be interpreted as production guarantees.

Likewise, conceptual security properties should not be presented as empirically demonstrated security unless supported by appropriate evidence.

---

# 22. Governance of Reference Implementations

Reference implementations exist to demonstrate or test architectural mechanisms.

A reference implementation may:

* implement only part of the architecture;
* use simplified mechanisms;
* expose experimental interfaces;
* prioritize clarity over production optimization.

Reference status therefore does not imply universal normative status.

The architecture remains conceptually independent from any single implementation.

---

# 23. Incident Response

Security or architectural incidents should be handled according to their scope.

Possible actions include:

* issue identification;
* containment;
* assessment;
* mitigation;
* disclosure;
* credential rotation;
* release correction;
* documentation update;
* protocol revision.

When an incident reveals an architectural weakness rather than merely an implementation defect, the appropriate architectural documentation should also be reviewed.

---

# 24. Revocation and Recovery Governance

Governance should define mechanisms for dealing with:

* compromised identities;
* invalid authorization;
* revoked delegation;
* compromised implementations;
* compromised hardware;
* protocol vulnerabilities;
* incompatible versions.

Recovery mechanisms should not silently restore authority that has been legitimately revoked.

Recovery restores valid operation; it does not resurrect invalid authority.

---

# 25. Governance and Offline Operation

Offline-capable implementations require explicit governance of state reconciliation.

Governance should define, where relevant:

* which state may be modified offline;
* which authorizations remain valid;
* expiration behavior;
* revocation propagation;
* conflict resolution;
* synchronization;
* recovery.

Offline operation must remain consistent with the applicable authority and security model.

---

# 26. Dispute and Exception Handling

Implementations may encounter exceptional conditions that are not completely represented by normal protocol flows.

Where appropriate, governance should define:

* exception categories;
* escalation procedures;
* temporary controls;
* evidence requirements;
* resolution procedures;
* post-incident review.

Exceptions should not silently redefine architectural principles.

A temporary operational workaround should remain distinguishable from a protocol or architectural change.

---

# 27. Transparency

The ecosystem should favor transparent documentation of:

* architectural decisions;
* protocol changes;
* security issues;
* breaking changes;
* deprecated mechanisms;
* known limitations.

Transparency improves interoperability and prevents incorrect assumptions about implementation capabilities.

---

# 28. Governance Invariants

The following principles should remain stable:

1. Governance does not create sovereignty.
2. Architecture defines concepts; implementations instantiate them.
3. Implementation details do not automatically become architectural requirements.
4. Architectural changes must be explicit.
5. Protocol changes must be versioned.
6. Security claims must be evidence-based.
7. Secrets must not be intentionally published.
8. Revocation must not be defeated by offline operation.
9. Recovery must not resurrect invalid authority.
10. Domain governance does not silently redefine DSAN architecture.
11. Open architecture does not require every implementation to be open source.
12. Licensing of one repository does not automatically determine licensing of another.
13. Reference implementations do not automatically constitute production systems.
14. Governance exists to preserve coherence, continuity, and responsible evolution.

---

# 29. Governance Model

The DSAN governance model can therefore be summarized as:

```text id="gvr007"
                 ARCHITECTURAL DEFINITION
                          │
                          ▼
                  ARCHITECTURAL GOVERNANCE
                          │
             ┌────────────┼────────────┐
             ▼            ▼            ▼
          Protocol    Security    Interoperability
          Governance  Governance   Governance
             │            │            │
             └────────────┼────────────┘
                          ▼
                 Implementation Governance
                          │
             ┌────────────┴────────────┐
             ▼                         ▼
        Open Projects            Restricted Projects
             │                         │
             └────────────┬────────────┘
                          ▼
                   Domain Applications
```

This model separates the governance of the ecosystem from the sovereignty of the entities operating within it.

---

# 30. Final Principle

The purpose of DSAN governance is not to control sovereign entities.

Its purpose is to ensure that the technological system through which sovereign entities operate remains:

* coherent;
* verifiable;
* interoperable;
* secure;
* evolvable;
* auditable;
* and architecturally consistent.

The fundamental distinction is therefore:

> **Governance governs the system. Sovereignty belongs to the entity.**

