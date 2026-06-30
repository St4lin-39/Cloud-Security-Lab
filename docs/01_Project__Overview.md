# Cloud Security Lab

## Project Overview

## 1. Introduction

Cloud Security Lab es una plataforma desarrollada para simular, detectar y analizar eventos de seguridad en entornos empresariales mediante un motor de detección basado en reglas y un sistema de visualización construido con Power BI.

El proyecto fue diseñado con un enfoque modular para representar el flujo básico de funcionamiento de un SIEM (Security Information and Event Management), permitiendo generar eventos, ejecutar reglas de detección, correlacionar alertas y visualizar los resultados a través de dashboards interactivos.

Aunque actualmente se trata de un laboratorio educativo, la arquitectura fue diseñada para evolucionar progresivamente hacia una plataforma más cercana a un entorno de producción, incorporando nuevas capacidades de detección, correlación, análisis de comportamiento y respuesta automática.

---

# 2. Motivation

Los sistemas modernos generan millones de eventos diariamente provenientes de servidores, aplicaciones, dispositivos de red y servicios en la nube.

Analizar manualmente esta cantidad de información resulta inviable, por lo que las organizaciones utilizan plataformas SIEM capaces de transformar eventos en alertas accionables para los analistas de seguridad.

Cloud Security Lab nace con el objetivo de comprender y construir los componentes principales de este tipo de plataformas, implementándolos desde cero para entender su funcionamiento interno en lugar de depender únicamente de herramientas comerciales.

---

# 3. Objectives

## General Objective

Diseñar e implementar una plataforma modular capaz de simular eventos de seguridad, detectar patrones de ataque, correlacionar alertas y presentar la información mediante dashboards interactivos.

## Specific Objectives

* Simular diferentes escenarios de ataque mediante un generador de eventos.
* Implementar un motor de detección basado en reglas configurables.
* Reducir ruido mediante mecanismos de supresión de alertas.
* Correlacionar múltiples alertas para identificar ataques de mayor complejidad.
* Almacenar eventos y alertas en PostgreSQL.
* Visualizar la información mediante Power BI.
* Diseñar una arquitectura preparada para futuras capacidades de Threat Hunting, Machine Learning y SOAR.

---

# 4. Current Features (Version 1.0)

La versión 1.0 implementa las siguientes funcionalidades:

* Event Generator
* Attack Runner
* Detection Engine
* Brute Force Detection
* Resource Enumeration Detection
* Credential Stuffing Detection
* Alert Suppression
* Correlation Engine
* Multi-Stage Attack Detection
* PostgreSQL como almacenamiento principal
* SQLAlchemy como ORM
* Dashboards analíticos desarrollados en Power BI

---

# 5. Technologies

## Backend

* Python
* SQLAlchemy
* PostgreSQL

## Data Analysis

* Microsoft Power BI

## Development Tools

* Git
* GitHub

---

# 6. Current Architecture

La arquitectura del proyecto está dividida en componentes independientes con responsabilidades claramente definidas.

Flujo general:

1. El Attack Runner ejecuta una simulación.
2. El Event Generator produce eventos.
3. Los eventos son almacenados en PostgreSQL.
4. El Detection Engine evalúa cada evento.
5. Las alertas pasan por el proceso de supresión.
6. El Correlation Engine analiza ataques de múltiples etapas.
7. Las alertas finales son almacenadas.
8. Power BI consume la información para su análisis.

---

# 7. Current Project Status

Versión actual:

**Cloud Security Lab v1.0**

Estado:

* Backend funcional.
* Motor de detección operativo.
* Correlación de alertas implementada.
* Dashboard analítico en Power BI.
* Arquitectura preparada para futuras ampliaciones.

---

# 8. Future Evolution

Las siguientes versiones incorporarán nuevas capacidades, entre ellas:

* Nuevas reglas de detección.
* Integración con MITRE ATT&CK.
* Threat Hunting.
* User and Entity Behavior Analytics (UEBA).
* Machine Learning para detección de anomalías.
* Automatización mediante SOAR.
* Integración con entornos Cloud.
* Integración con Windows Event Logs.
* Integración con Syslog y dispositivos de red.

---

# 9. Project Philosophy

Cloud Security Lab no busca únicamente generar alertas.

Su objetivo principal es representar el ciclo completo de análisis de eventos de seguridad:

**Generación de eventos → Detección → Supresión → Correlación → Visualización → Investigación**

Esta filosofía permitirá que el proyecto evolucione progresivamente hacia una plataforma de análisis de seguridad mucho más cercana a las soluciones utilizadas actualmente en la industria.
