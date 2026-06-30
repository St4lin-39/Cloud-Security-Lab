# Cloud Security Lab

# Dashboard Guide

## 1. Introduction

Cloud Security Lab includes a collection of dashboards developed in Power BI to transform security events and alerts into meaningful information for security analysis.

Each dashboard page was designed to answer specific questions that a security analyst would typically ask during an investigation.

Together, these pages provide a comprehensive understanding of the system's behavior, help identify suspicious patterns, and support structured incident analysis.

---

# 2. Dashboard Philosophy

The dashboards follow a progressive analysis approach.

Instead of presenting all information simultaneously, each page is designed to answer a specific set of analytical questions.

The recommended analysis workflow is as follows:

```text id="yqotng"
Executive Overview

↓

IP Analysis

↓

User Analysis

↓

Resource Analysis

↓

Incident Investigation
```

This approach allows the analyst to move from a high-level overview of the environment to the detailed investigation of a specific incident.

---

# 3. Executive Overview

## Objective

Provide a high-level overview of the current state of the system.

This page answers questions such as:

* How many events have been generated?
* How many alerts have been generated?
* Which alert types are the most common?
* Which event types occur most frequently?

### KPIs

* Total Events
* Total Alerts
* Active Users
* Active IPs

### Visualizations

* Alerts by type.
* Events by type.

This page serves as the starting point for any security analysis.

---

# 4. IP Analysis

## Objective

Identify the IP addresses with the highest level of activity within the system.

This page answers questions such as:

* Which IP address generates the most events?
* Which IP address generates the highest number of alerts?
* Is there an unusually active IP address?

### Visualizations

* Events by IP address.
* Alerts by IP address.
* IP address summary table.

This view helps identify potential sources of attacks.

---

# 5. User Analysis

## Objective

Analyze the behavior of users recorded in the generated events.

This page answers questions such as:

* Which users generate the highest level of activity?
* Which users have the highest number of failed authentication attempts?
* Which users are associated with generated alerts?

### Visualizations

* Events by user.
* Failed authentication attempts by user.
* User summary table.

This information helps identify potentially compromised accounts or accounts involved in attack simulations.

---

# 6. Resource Analysis

## Objective

Analyze the resources accessed by users during attack simulations.

This page answers questions such as:

* Which resources receive the highest number of access attempts?
* Which resources are most frequently involved in suspicious events?
* Is there evidence of reconnaissance activity targeting specific resources?

### Visualizations

* Most accessed resources.
* Events by resource.
* Resources categorized by event type.
* Resource summary table.

This view is particularly useful for analyzing reconnaissance and resource enumeration attacks.

---

# 7. Incident Investigation

## Objective

Provide a dedicated view for incident investigation.

This page allows analysts to review the events and alerts generated during a simulation in chronological order.

It answers questions such as:

* What happened first?
* Which alerts were generated?
* Which IP address was involved?
* Which users participated?
* What was the sequence of the incident?

### Visualizations

* Chronological event table.
* Chronological alert table.
* Incident summary indicators.
* Slicers for filtering by IP address or user.

This page represents the most detailed level of the analysis process.

---

# 8. Analytical Workflow

The dashboard was designed to be used following the workflow below:

1. Review the overall system activity in the Executive Overview.
2. Identify relevant IP addresses using the IP Analysis page.
3. Analyze the users involved through the User Analysis page.
4. Review the affected resources using the Resource Analysis page.
5. Reconstruct the incident through the Incident Investigation page.

This workflow reflects a simplified investigation methodology commonly used in Security Operations Centers (SOCs).

---

# 9. Current Scope

The current dashboards represent the capabilities available in version 1.0.

Their primary objective is to facilitate the understanding of the events generated during the attack simulations implemented in the laboratory.

They are not intended to replace the capabilities of commercial SIEM platforms, but rather to provide a foundation for future enhancements.

---

# 10. Future Improvements

Future versions will incorporate additional visualization capabilities, including:

* Geographic maps.
* Advanced time-series analysis.
* Incident risk assessment.
* Alert severity visualization.
* MITRE ATT&CK Mapping.
* Threat Hunting dashboards.
* Executive dashboards.
* Detection Engine performance metrics.

These enhancements will significantly increase the analytical capabilities of the platform.
