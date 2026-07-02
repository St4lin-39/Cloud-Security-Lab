# Cloud Security Lab

A modular cybersecurity laboratory designed to simulate cyberattacks, detect malicious behaviors, correlate security events, and visualize security incidents through interactive dashboards.

Cloud Security Lab was developed from scratch with the objective of understanding how modern Security Information and Event Management (SIEM) platforms process, analyze, and correlate security events while maintaining a clean, scalable, and extensible architecture.

---

# Overview

Cloud Security Lab simulates security events generated during different attack scenarios and processes them through a modular Detection Engine capable of identifying suspicious behaviors using rule-based detection techniques.

Detected threats are processed by an Alert Manager, correlated into higher-level security incidents, stored in PostgreSQL, and finally visualized through interactive Power BI dashboards.

Rather than replicating the full functionality of commercial SIEM platforms, Cloud Security Lab focuses on demonstrating their internal architecture and core analytical workflow in a transparent and educational manner.

---

# Features

Current Version (v1.0)

* Rule-Based Detection Engine
* Brute Force Detection
* Resource Enumeration Detection
* Credential Stuffing Detection
* Alert Suppression
* Multi-Stage Attack Correlation
* PostgreSQL Data Persistence
* SQLAlchemy ORM
* Interactive Power BI Dashboards
* Modular Software Architecture
* Technical Documentation

---

# Project Architecture

The platform follows a sequential security event processing workflow.

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
Correlation Engine
      │
      ▼
PostgreSQL (Alerts)
      │
      ▼
Power BI
```

Each component performs a single, well-defined responsibility, promoting scalability, maintainability, and future extensibility.

---

# Technology Stack

Backend

* Python
* SQLAlchemy

Database

* PostgreSQL

Business Intelligence

* Microsoft Power BI

Development

* Git
* GitHub
* Visual Studio Code

---

# Project Structure

```text
Cloud-Security-Lab/

├── app/
├── config/
├── database/
├── detection/
├── generator/
├── models/
├── repositories/
├── services/
├── simulations/
├── main.py
├── docs/
├── powerbi/
├── diagrams/          (Future)
│
├── requirements.txt
│
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

Activate the environment.

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

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

Create a PostgreSQL database and update the connection string inside the project configuration.

---

## Run the project

```bash
python main.py
```

The application will generate simulated security events, execute the Detection Engine, store alerts, and make the generated data available for Power BI analysis.

---

# Power BI Dashboard

The project includes interactive dashboards designed to facilitate security analysis.

Current dashboard pages include:

* Executive Overview
* IP Analysis
* User Analysis
* Resource Analysis
* Incident Investigation

These dashboards transform raw security events into meaningful visual insights that support investigation and decision-making.

---

# Documentation

Detailed technical documentation is available in the **docs/** directory.

Available documents include:

* Project Overview
* System Architecture
* Detection Engine
* Database Design
* Dashboard Guide
* Project Roadmap
* Lessons Learned

---

# Roadmap

### Version 1.0

Completed

* Rule-Based Detection
* Detection Engine
* PostgreSQL
* Power BI
* Correlation Engine

### Version 2.0

Advanced Detection

* Password Spraying Detection
* Risk Scoring
* Severity Classification
* Additional Detection Rules

### Version 3.0

Threat Hunting Platform

* MITRE ATT&CK Mapping
* IOC Detection
* Threat Hunting Dashboards
* Incident Management

### Version 4.0

Cloud Security

* AWS CloudTrail
* Azure Activity Logs
* Kubernetes Audit Logs
* Syslog Integration

### Version 5.0

Intelligent Detection

* Machine Learning
* Anomaly Detection
* User and Entity Behavior Analytics (UEBA)

### Version 6.0

SOAR

* Automated Response
* Firewall Integration
* Playbooks
* Response Workflows

---

# Current Status

Current Version:

**v1.0**

Project Status:

**Completed**

The first release establishes a complete modular foundation for future versions while demonstrating the internal workflow of a modern security monitoring platform.

---

# Future Goals

Cloud Security Lab will continue evolving by incorporating advanced detection techniques, cloud integrations, behavioral analytics, machine learning, and automated incident response capabilities.

The long-term objective is to build an educational and technical platform that closely reflects the architecture and operational principles of enterprise SIEM solutions while remaining fully transparent and accessible for learning purposes.

---

# License

This project is intended for educational and research purposes.

---

**Cloud Security Lab** is continuously evolving as part of an ongoing learning journey in software engineering and cybersecurity.
