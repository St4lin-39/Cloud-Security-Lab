# Cloud Security Lab

# Detection Engine

## 1. Introduction

The Detection Engine is the analytical core of Cloud Security Lab.

Its primary responsibility is to evaluate every incoming security event, execute all available detection rules, enrich the resulting alerts with contextual information, suppress duplicated alerts, and correlate multiple attack techniques into higher-level security incidents.

Unlike traditional detection mechanisms that simply generate alerts, Cloud Security Lab implements a complete detection pipeline inspired by the workflow followed by modern Security Information and Event Management (SIEM) platforms.

Version 1.0 follows a fully rule-based detection approach, providing deterministic and transparent detection logic while maintaining a modular architecture that facilitates future expansion.

---

# 2. Detection Philosophy

Cloud Security Lab adopts a rule-based detection strategy for several reasons:

- Deterministic detection decisions.
- Transparent detection logic.
- Low computational cost.
- Ease of maintenance.
- High modularity.
- Extensibility for future detection techniques.

Each detection rule represents a specific malicious behavior.

Whenever a rule is satisfied, the system generates a standardized alert that is subsequently enriched, validated, correlated, and stored.

---

# 3. Detection Pipeline

Every generated event follows the processing pipeline shown below.

```text
Event

↓

Detection Engine

↓

Detection Rules

↓

Alert Factory

↓

Confidence Engine

↓

Risk Engine

↓

Alert Manager

↓

Correlation Engine

↓

Alert Storage

↓

Power BI
```

Each stage performs a single responsibility, following the Separation of Concerns principle.

---

# 4. Detection Rules

The Detection Engine currently implements four independent detectors.

Each detector operates independently through the Detection Registry, allowing new rules to be incorporated without modifying existing implementations.

---

## 4.1 Brute Force Detection

### Objective

Detect multiple failed authentication attempts against the same user account within a configurable time window.

### Detection Logic

The detector counts recent `LOGIN_FAILED` events associated with the same username.

If the number of failed attempts exceeds the configured threshold, a Brute Force alert is generated.

### Configuration

- Threshold: 5 failed attempts.
- Time Window: 5 minutes.

### Generated Alert

```text
BRUTE_FORCE_ATTEMPT
```

---

## 4.2 Resource Enumeration Detection

### Objective

Identify users attempting to access an unusually large number of protected resources within a short period of time.

This behavior is commonly associated with reconnaissance activities preceding more sophisticated attacks.

### Detection Logic

The detector counts the number of distinct resources accessed by the same user.

If the configured threshold is exceeded, the detector generates an alert.

### Configuration

- Threshold: 6 unique resources.
- Time Window: 15 minutes.

### Generated Alert

```text
RESOURCE_ENUMERATION
```

---

## 4.3 Credential Stuffing Detection

### Objective

Detect authentication attempts against multiple user accounts originating from the same IP address.

This behavior typically indicates the use of credentials leaked from previous data breaches.

### Detection Logic

The detector counts the number of different usernames targeted by the same IP address.

If the threshold is exceeded, a Credential Stuffing alert is generated.

### Configuration

- Threshold: 5 users.
- Time Window: 10 minutes.

### Generated Alert

```text
CREDENTIAL_STUFFING
```

---

## 4.4 Password Spraying Detection

### Objective

Detect the use of a single password against multiple user accounts.

Password spraying differs from brute force because the attacker attempts a single common password across many accounts instead of many passwords against one account.

### Detection Logic

The detector identifies how many different usernames attempted authentication using the same password within the configured time window.

If the number exceeds the configured threshold, the detector generates a Password Spraying alert.

### Configuration

- Threshold: 5 users.
- Time Window: 10 minutes.

### Generated Alert

```text
PASSWORD_SPRAYING
```

---

# 5. Alert Factory

The Alert Factory is responsible for constructing standardized alert objects.

Rather than allowing each detector to manually populate every alert field, all alerts are generated through a centralized factory that ensures structural consistency across the platform.

The Alert Factory retrieves static metadata from the Alert Metadata repository and combines it with dynamic information calculated during the detection process.

This design significantly reduces duplicated code while simplifying future maintenance.

---

# 6. Alert Enrichment

Before an alert is stored, Cloud Security Lab enriches it with additional contextual information.

This enrichment process transforms a simple detection into a structured security incident that is significantly more useful for analysts.

Every generated alert currently includes:

- Severity
- Confidence Score
- Risk Score
- Status
- Description
- Recommendation
- MITRE ATT&CK Tactic
- MITRE ATT&CK Technique

These attributes provide valuable context that facilitates investigation, prioritization, and visualization.

---

## 6.1 Severity

Severity represents the intrinsic impact of the detected attack technique.

Each alert type is assigned a predefined severity level.

Current levels include:

- LOW
- MEDIUM
- HIGH
- CRITICAL

Severity remains static for each attack type.

---

## 6.2 Confidence Engine

The Confidence Engine estimates how confident the system is that the observed behavior corresponds to malicious activity.

Unlike severity, confidence is calculated dynamically based on the available evidence.

For example:

- Number of failed login attempts.
- Number of accessed resources.
- Number of affected user accounts.

The result is expressed as a percentage between 0 and 100.

Higher confidence indicates stronger evidence supporting the detection.

---

## 6.3 Risk Engine

The Risk Engine calculates a Risk Score that assists analysts in prioritizing incidents.

Risk Score combines:

- Attack Severity
- Detection Confidence

using a weighted formula.

This provides a single numerical value representing the operational priority of the incident.

Unlike severity, Risk Score varies depending on the confidence associated with the detection.

---

# 7. Alert Suppression

Repeated attack attempts can generate hundreds of identical alerts, increasing operational noise.

To prevent unnecessary duplication, every generated alert passes through the Alert Manager.

The Alert Manager checks whether an equivalent alert already exists for the same source IP within a configurable cooldown period.

If a recent alert is found, the new alert is discarded.

### Configuration

Cooldown:

- 5 minutes.

---

# 8. Correlation Engine

Individual alerts often represent isolated attack techniques.

Enterprise SIEM platforms typically correlate multiple alerts to identify more sophisticated attack campaigns.

Cloud Security Lab implements this concept through the Correlation Engine.

The current implementation generates a Multi-Stage Attack alert whenever the same source IP produces all of the following alerts within the configured correlation window:

- Brute Force
- Resource Enumeration
- Credential Stuffing

### Generated Alert

```text
MULTI_STAGE_ATTACK
```

This represents a simplified implementation of multi-stage attack correlation.

---

# 9. Detection Pipeline Integration

The Detection Pipeline orchestrates every stage of the detection workflow.

For each incoming event, the pipeline performs the following operations:

1. Execute all registered detection rules.
2. Generate standardized alerts using the Alert Factory.
3. Calculate Confidence Score.
4. Calculate Risk Score.
5. Process alerts through the Alert Manager.
6. Store only non-suppressed alerts.
7. Execute alert correlation.
8. Process correlated alerts through the Alert Manager.
9. Store correlated alerts.
10. Return all valid alerts for visualization.

This orchestration layer keeps the architecture modular while allowing each component to evolve independently.

---

# 10. Current Limitations

Version 1.0 intentionally focuses on deterministic rule-based detection.

The following capabilities are planned for future versions:

- Incident Classification
- Asset Criticality
- Threat Intelligence Integration
- Impossible Travel Detection
- Privilege Escalation Detection
- Data Exfiltration Detection
- Lateral Movement Detection
- User and Entity Behavior Analytics (UEBA)
- Machine Learning-based Detection

---

# 11. Future Evolution

The Detection Engine was designed around a modular architecture that facilitates continuous expansion.

Future versions aim to incorporate:

- Behavioral analytics.
- Advanced correlation.
- Dynamic risk assessment.
- MITRE ATT&CK coverage expansion.
- Machine Learning.
- SOAR integrations.
- Cloud-native security telemetry.

The current implementation establishes a scalable foundation that progressively evolves Cloud Security Lab toward the architecture and analytical capabilities commonly found in enterprise SIEM platforms.