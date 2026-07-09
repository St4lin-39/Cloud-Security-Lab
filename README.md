# Cloud Security Lab

A modular cybersecurity laboratory designed to simulate cyberattacks, detect malicious behaviors, correlate security events, and visualize security incidents through interactive dashboards.

Cloud Security Lab was developed from scratch to understand how modern **Security Information and Event Management (SIEM)** platforms process, enrich, correlate, and visualize security events while maintaining a clean, scalable, and extensible software architecture.

Rather than replicating the complexity of enterprise SIEM solutions, this project focuses on implementing their core analytical workflow in a transparent, educational, and modular way.

---

# Overview

Cloud Security Lab simulates realistic attack scenarios that generate security events, which are processed through a modular Detection Engine capable of identifying malicious behaviors using rule-based detection techniques.

Detected threats are enriched with contextual metadata, processed by an Alert Manager, correlated into higher-level security incidents, stored in PostgreSQL, and finally visualized through interactive Power BI dashboards.

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

## Alert Processing

- Alert Enrichment
- Severity Classification
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

Cloud Security Lab follows a sequential security event processing pipeline.

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
Alert Manager
      │
      ▼
Alert Enrichment
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

Every module performs a single responsibility, promoting scalability, maintainability, and future extensibility.

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
- Generate enriched alerts.
- Perform alert correlation.
- Store all information inside PostgreSQL.

The generated data can then be explored through the included Power BI dashboards.

---

# Power BI Dashboards

Cloud Security Lab includes interactive dashboards designed to support security analysis and incident investigation.

Current dashboards include:

- Executive Overview
- IP Analysis
- User Analysis
- Resource Analysis
- Incident Investigation

Future releases will introduce:

- MITRE ATT&CK Dashboard
- Threat Hunting Dashboard
- IOC Dashboard
- Risk Scoring Dashboard

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
- Alert Enrichment
- Severity Classification
- Detection Registry
- Alert Metadata
- Improved Modular Architecture

---

## Version 3.0

In Progress

- MITRE ATT&CK Mapping
- IOC Detection
- Threat Hunting
- Risk Scoring
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

**Core Detection Platform Completed**

Cloud Security Lab currently provides a complete modular platform capable of simulating multiple cyberattack scenarios, detecting malicious behavior through rule-based analytics, enriching alerts with contextual metadata, suppressing duplicate alerts, correlating multiple detections into higher-level incidents, persisting information into PostgreSQL, and visualizing security data through Power BI.

---

# Future Goals

Future versions of Cloud Security Lab aim to progressively incorporate capabilities commonly found in enterprise security platforms, including:

- MITRE ATT&CK integration
- Threat Hunting
- IOC detection
- Cloud telemetry ingestion
- Behavioral analytics
- Machine Learning
- SOAR automation

The long-term objective is to build an educational platform that closely resembles the internal architecture and analytical workflow of modern SIEM solutions while remaining fully transparent and suitable for learning.

---

# License

This project is intended for educational and research purposes.

---

**Cloud Security Lab** is continuously evolving as part of an ongoing learning journey in software engineering, cloud security, and cybersecurity.