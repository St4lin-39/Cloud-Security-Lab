# Cloud Security Lab

# Enhancement 002

# Detection Engine Refactor Design

## Status

**Design**

---

# 1. Introduction

The first version of Cloud Security Lab implements a rule-based Detection Engine where every detector is invoked explicitly.

This approach was intentionally selected to maximize readability while building the initial version of the laboratory.

As the number of supported detection rules increases, however, this design becomes progressively harder to maintain.

Enhancement 002 introduces the architectural design required to support an extensible Detection Engine capable of incorporating future detectors with minimal code modifications.

---

# 2. Current Architecture

The current Detection Engine follows the structure below.

```text
Event

↓

Brute Force Detector

↓

Resource Enumeration Detector

↓

Credential Stuffing Detector

↓

Alerts
```

Each detector is executed manually inside the Detection Engine.

Whenever a new detector is implemented, the Detection Engine itself must also be modified.

---

# 3. Problem Statement

Although the current implementation is perfectly adequate for version 1.0, it introduces several long-term maintenance challenges.

Every new detector requires modifications to the Detection Engine.

As additional capabilities are introduced, the Detection Engine becomes increasingly coupled to every detection rule implemented by the system.

This violates the Open/Closed Principle, one of the fundamental SOLID principles.

The engine should remain closed for modification while remaining open for extension.

---

# 4. Proposed Architecture

Future versions will introduce a Detection Registry responsible for maintaining the list of available detectors.

The Detection Engine will no longer know which detectors exist.

Instead, it will simply iterate through the registry.

The proposed architecture becomes:

```text
Event

↓

Detection Engine

↓

Detection Registry

↓

Detector 1

Detector 2

Detector 3

...

Detector N

↓

Alerts
```

---

# 5. Detection Registry

The Detection Registry acts as the central catalogue of available detection modules.

Each detector registers itself once.

The Detection Engine simply executes every registered detector sequentially.

This architecture removes the need to modify the Detection Engine whenever a new detector is created.

---

# 6. Benefits

The proposed architecture provides multiple advantages.

## Scalability

New detectors can be incorporated without modifying the engine itself.

---

## Lower Coupling

The Detection Engine no longer depends on individual detection rules.

---

## Maintainability

Each detector remains completely independent.

Individual rules can evolve without affecting other modules.

---

## Extensibility

Future versions may dynamically enable or disable detectors based on configuration.

---

## Testability

Each detector can be tested independently from the Detection Engine.

---

# 7. Future Integration

The Detection Registry will support future capabilities including:

* Password Spraying Detection
* Impossible Travel Detection
* Privilege Escalation Detection
* Lateral Movement Detection
* UEBA
* Machine Learning Detectors
* Threat Intelligence Rules

without requiring structural modifications to the Detection Engine.

---

# 8. Implementation Strategy

This enhancement introduces only the architectural design.

The actual implementation will be performed incrementally during version 2.0.

The first detector to use the new architecture will be Password Spraying Detection.

This approach minimizes implementation risk while preserving compatibility with version 1.0.
