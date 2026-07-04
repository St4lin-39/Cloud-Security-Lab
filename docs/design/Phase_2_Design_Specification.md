# Cloud Security Lab

# Phase 2 Design Specification

## 1. Introduction

This document defines the architectural and functional objectives of **Cloud Security Lab Version 2.0**.

Version 1.0 successfully established the foundation of the platform by implementing a modular event processing pipeline, a rule-based Detection Engine, alert suppression, event correlation, PostgreSQL persistence, and interactive Power BI dashboards.

The purpose of Version 2.0 is not to redesign the existing architecture, but to improve its analytical capabilities by reducing false positives, enriching contextual information, and introducing more realistic detection and correlation mechanisms inspired by enterprise SIEM platforms.

---

# 2. Motivation

The current implementation performs event correlation primarily using the source IP address.

While this approach is sufficient for demonstrating the correlation workflow, it introduces limitations commonly found in real-world environments.

For example, multiple users may legitimately share the same public IP address due to:

* Network Address Translation (NAT)
* Corporate proxies
* VPN gateways
* Cloud environments
* Shared workstations

In these scenarios, correlating alerts solely by IP address may incorrectly associate unrelated user activities, increasing the likelihood of false positive incidents.

Version 2.0 aims to address these limitations.

---

# 3. Objectives

The primary objectives of Version 2.0 are:

* Reduce false positives during alert correlation.
* Increase contextual awareness within the Detection Engine.
* Introduce severity and risk-based analysis.
* Expand the detection capabilities of the platform.
* Prepare the architecture for future SIEM-oriented features.

---

# 4. Planned Improvements

The second version will focus on four major areas.

## 4.1 Correlation Engine v2

The Correlation Engine will be redesigned to use multiple contextual attributes instead of relying exclusively on source IP addresses.

The initial correlation context will include:

* Username
* Source IP
* Time Window

Future versions may also incorporate:

* Hostname
* Device Identifier
* User Agent
* Geolocation
* Session Identifier

This enhancement will significantly reduce false positives generated in shared network environments.

---

## 4.2 Detection Engine Improvements

The Detection Engine will be expanded with additional detection rules, including:

* Password Spraying Detection
* Impossible Travel Detection
* Lateral Movement Detection
* Privilege Escalation Detection
* Data Exfiltration Detection

Each new detector will remain independent to preserve the modular architecture established in Version 1.0.

---

## 4.3 Severity Classification

Alerts will include a severity level representing their operational importance.

The initial severity levels will be:

* Low
* Medium
* High
* Critical

Severity values will later be used for dashboard prioritization and risk calculations.

---

## 4.4 Risk Scoring

A Risk Scoring mechanism will be introduced to quantify the overall threat level associated with detected behaviors.

Rather than relying solely on individual alerts, the system will progressively accumulate risk based on multiple suspicious activities.

This approach more closely resembles the analytical workflow implemented by modern SIEM platforms.

---

# 5. Architectural Impact

The overall architecture will remain modular.

Most improvements will extend existing components instead of replacing them.

The primary architectural modifications will affect:

* Detection Engine
* Correlation Engine
* Alert Model
* Database Schema
* Power BI Dashboards

The event generation process will remain unchanged.

---

# 6. Expected Benefits

The implementation of Version 2.0 is expected to provide:

* Lower false positive rates.
* More accurate incident correlation.
* Richer analytical context.
* Better dashboard prioritization.
* A stronger foundation for future Machine Learning integration.
* Increased similarity to enterprise SIEM platforms.

---

# 7. Implementation Strategy

Development will be carried out incrementally.

The proposed implementation order is:

1. Correlation Engine v2.
2. Severity Classification.
3. Risk Scoring.
4. Database updates.
5. Power BI enhancements.
6. New Detection Rules.

Each phase will remain functional before moving to the next one.

---

# 8. Long-Term Vision

Version 2.0 represents the transition from a basic educational detection laboratory toward a more realistic security analysis platform.

The architectural decisions introduced during this phase will serve as the foundation for future capabilities such as MITRE ATT&CK Mapping, Threat Hunting, User and Entity Behavior Analytics (UEBA), Machine Learning, Cloud integrations, and SOAR functionality.
