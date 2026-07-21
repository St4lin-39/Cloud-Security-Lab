# Cloud Security Lab

A modular cybersecurity laboratory designed to simulate cyberattacks, detect malicious behaviors, enrich security alerts, correlate attack patterns, and visualize security incidents through interactive dashboards.

Cloud Security Lab was developed from scratch to understand how modern **Security Information and Event Management (SIEM)** platforms process, enrich, prioritize, correlate, and visualize security events while maintaining a clean, scalable, and extensible software architecture.

Rather than replicating the complexity of enterprise SIEM solutions, this project focuses on implementing their core analytical workflow in a transparent, educational, and modular way.

---

# Overview

Cloud Security Lab simulates realistic attack scenarios that generate security events, which are processed through a modular Detection Engine capable of identifying malicious behaviors using rule-based detection techniques.

Once an attack is detected, alerts are enriched with contextual metadata including severity, confidence, risk score, recommendations, and MITRE ATT&CK mappings. The alerts are then processed by an Alert Manager, correlated into higher-level security incidents, stored in PostgreSQL, and finally visualized through interactive Power BI dashboards.

The platform emphasizes software architecture, modularity, and cybersecurity concepts over infrastructure complexity, making it an ideal laboratory for learning and experimentation.

---

# Features

Current Version (**v2.0**)

## Attack Simulations

- Brute Force
- Resource Enumeration
- Credential Stuffing
- Password Spraying

## Detection Capabilities

- Rule-Based Detection Engine
- Brute Force Detection
- Resource Enumeration Detection
- Credential Stuffing Detection
- Password Spraying Detection

## Alert Enrichment

- Severity Classification
- Dynamic Confidence Scoring
- Dynamic Risk Scoring
- MITRE ATT&CK Mapping
- Alert Recommendations
- Alert Status Management

## Alert Processing

- Alert Factory
- Alert Suppression
- Multi-Stage Attack Correlation

## Data Layer

- PostgreSQL Persistence
- SQLAlchemy ORM
- Repository Pattern

## Visualization

- Interactive Power BI Dashboards

## Documentation

- Modular Software Architecture
- Technical Documentation
- System Design Documentation

---

# Detection Capabilities

| Attack | Detection Method | Status |
|---------|------------------|--------|
| Brute Force | Rule-Based | ✅ |
| Resource Enumeration | Rule-Based | ✅ |
| Credential Stuffing | Rule-Based | ✅ |
| Password Spraying | Rule-Based | ✅ |
| Multi-Stage Attack | Correlation Engine | ✅ |

---

# Project Architecture

Cloud Security Lab follows a modular security event processing pipeline.

```text
Attack Runner
      │
      ▼
Event Generator
      │
      ▼
PostgreSQL (Events)
      │
      ▼
Detection Engine
      │
      ▼
Alert Factory
      │
      ▼
Confidence Engine
      │
      ▼
Risk Engine
      │
      ▼
Alert Manager
      │
      ▼
Correlation Engine
      │
      ▼
PostgreSQL (Alerts)
      │
      ▼
Power BI
```

Each component performs a single responsibility, promoting scalability, maintainability, and future extensibility.

A complete architectural explanation is available in:

```
docs/System Architecture.md
```

---

# Technology Stack

## Backend

- Python
- SQLAlchemy

## Database

- PostgreSQL

## Business Intelligence

- Microsoft Power BI

## Development Tools

- Git
- GitHub
- Visual Studio Code

---

# Project Structure

```text
Cloud-Security-Lab/

├── config/
├── database/
├── detection/
├── entities/
├── generator/
├── models/
├── repositories/
├── services/
├── docs/
├── powerbi/
├── main.py
├── requirements.txt
└── README.md
```

---

# Getting Started

## Clone the repository

```bash
git clone https://github.com/your_username/Cloud-Security-Lab.git

cd Cloud-Security-Lab
```

---

## Create a virtual environment

```bash
python -m venv venv
```

Activate it.

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configure PostgreSQL

Create a PostgreSQL database and configure the connection parameters inside the project configuration.

---

## Run the project

```bash
python main.py
```

The platform will:

- Generate simulated attack events.
- Execute the Detection Engine.
- Enrich alerts with contextual metadata.
- Calculate Confidence Score.
- Calculate Risk Score.
- Suppress duplicated alerts.
- Perform alert correlation.
- Store alerts in PostgreSQL.

The generated information can then be explored through the included Power BI dashboards.

---

# Power BI Dashboards

Cloud Security Lab includes interactive dashboards designed to support security analysis and incident investigation.

Current dashboards include:

- Executive Overview
- Network Activity
- User Analysis
- Resource Analysis
- Attack Timeline
- Attack Investigation

Future releases will introduce:

- MITRE ATT&CK Dashboard
- Threat Hunting Dashboard
- IOC Dashboard

---

# Documentation

Detailed technical documentation is available under the **docs/** directory.

Current documentation includes:

- Project Overview
- System Architecture
- Detection Engine
- Database Design
- Dashboard Guide
- Development Roadmap
- Lessons Learned

---

# Development Roadmap

## Version 1.0

Completed

- Rule-Based Detection Engine
- PostgreSQL Integration
- Detection Pipeline
- Correlation Engine
- Power BI Dashboards

---

## Version 2.0

Completed

- Password Spraying Detection
- Alert Factory
- Detection Registry
- Alert Metadata
- Dynamic Confidence Scoring
- Dynamic Risk Scoring
- MITRE ATT&CK Mapping
- Improved Modular Architecture 

---

## Version 3.0

Planned

- Incident Classification
- Asset Criticality
- Threat Hunting
- IOC Detection
- Advanced Dashboards

---

## Version 4.0

Cloud Security

- AWS CloudTrail
- Azure Activity Logs
- Kubernetes Audit Logs
- Windows Event Logs
- Syslog Integration

---

## Version 5.0

Behavior Analytics

- User and Entity Behavior Analytics (UEBA)
- Machine Learning
- Anomaly Detection

---

## Version 6.0

SOAR

- Automated Incident Response
- Firewall Integration
- Security Playbooks
- Response Workflows

---

# Current Status

## Current Version

**v2.0**

## Project Status

**Detection, Alert Enrichment and Correlation Platform Completed**

Cloud Security Lab currently provides a modular security monitoring platform capable of simulating multiple cyberattack scenarios, detecting malicious behaviors through rule-based analytics, enriching alerts with contextual information, calculating confidence and risk scores, suppressing duplicate alerts, correlating multiple attack techniques into higher-level incidents, persisting data into PostgreSQL, and visualizing security information through Power BI.

---

# Future Goals

Future versions of Cloud Security Lab aim to progressively incorporate capabilities commonly found in enterprise security platforms, including:

- Threat Hunting
- IOC Detection
- Cloud Telemetry
- Behavioral Analytics
- Machine Learning
- SOAR Automation

The long-term objective is to build an educational platform that closely resembles the internal architecture and analytical workflow of modern SIEM platforms while remaining fully transparent and suitable for learning.

---

# License

This project is intended for educational and research purposes.

---

**Cloud Security Lab** is continuously evolving as part of an ongoing learning journey in software engineering, cloud security, and cybersecurity.