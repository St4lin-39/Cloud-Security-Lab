# Cloud Security Lab

# Enhancement 001

# Detection Engine Refactor

## Status

**Completed**

---

# 1. Overview

During the development of Cloud Security Lab v1.0, the Detection Engine successfully demonstrated the implementation of a rule-based detection pipeline capable of identifying multiple attack patterns.

Although the overall architecture proved to be stable, several opportunities for improvement were identified while validating the behavior of the detection pipeline under more realistic attack simulations.

Rather than representing implementation defects, these findings reflect the natural evolution of the project as additional scenarios were evaluated.

Enhancement 001 documents the first architectural refinement introduced in version 2.0.

---

# 2. Motivation

The first version of the Detection Engine was intentionally designed to prioritize simplicity and readability.

Each detector was implemented independently, allowing the project to clearly demonstrate how rule-based security detection works.

However, after validating the complete pipeline, several aspects were identified that could be improved before introducing additional detection capabilities.

These improvements focus on maintainability, extensibility, and long-term scalability rather than changing the existing detection logic.

---

# 3. Identified Improvements

The following opportunities were identified during the review process.

## Detection Engine Scalability

The Detection Engine currently invokes every detector explicitly.

Although this approach is perfectly acceptable for three detection rules, future versions will incorporate additional detectors, increasing the amount of repetitive code.

The architecture will therefore evolve toward a more modular detection registration model.

---

## Detection Rule Standardization

Each detector currently performs similar operations:

* Query historical events.
* Apply a configurable threshold.
* Evaluate a configurable time window.
* Generate an alert.

Future implementations should maintain a consistent structure across all detectors, simplifying maintenance and reducing duplicated logic.

---

## Correlation Engine Validation

Several alternative correlation strategies were evaluated, including user-based correlation to reduce potential false positives in NAT environments.

After evaluating different scenarios, the project intentionally retained the original IP-based correlation model for version 1.0.

This decision was made because the current laboratory does not yet collect sufficient contextual information—such as session identifiers, device fingerprints, hostnames, or geolocation—to reliably distinguish different actors behind the same public IP address.

Future versions will revisit this limitation as richer contextual data becomes available.

---

# 4. Architectural Decision

No changes were introduced to the existing detection logic.

Instead, Enhancement 001 establishes the architectural foundation required for future detectors while preserving backward compatibility with version 1.0.

This approach minimizes implementation risk while allowing the Detection Engine to evolve incrementally.

---

# 5. Expected Benefits

Enhancement 001 prepares the Detection Engine for:

* Easier integration of new detection rules.
* Reduced maintenance effort.
* More consistent detector implementations.
* Improved readability.
* Greater scalability as the project grows.

---

# 6. Impact

This enhancement does not modify the external behavior of Cloud Security Lab.

Existing detection rules continue to operate exactly as implemented in version 1.0.

The improvement focuses exclusively on preparing the internal architecture for future expansion.

---

# 7. Future Work

The architectural improvements introduced in Enhancement 001 will serve as the foundation for upcoming detection capabilities, including:

* Password Spraying Detection
* Impossible Travel Detection
* Privilege Escalation Detection
* Lateral Movement Detection
* Risk Scoring
* Advanced Correlation Rules

These features will be implemented throughout the remaining milestones of version 2.0.
