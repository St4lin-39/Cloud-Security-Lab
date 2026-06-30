# Cloud Security Lab

# System Architecture

## 1. Architecture Overview

Cloud Security Lab fue diseñado siguiendo una arquitectura modular basada en la separación de responsabilidades (Separation of Concerns), donde cada componente cumple una función específica dentro del flujo de procesamiento de eventos de seguridad.

El objetivo principal de esta arquitectura es facilitar la escalabilidad, el mantenimiento y la incorporación de nuevas capacidades sin afectar el funcionamiento del sistema existente.

La plataforma sigue un flujo de procesamiento secuencial que transforma eventos de seguridad en información útil para el análisis.

---

# 2. High-Level Architecture

El flujo general del sistema es el siguiente:

```
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

Cada componente recibe información del anterior, la procesa y entrega el resultado al siguiente módulo.

---

# 3. Architecture Principles

La arquitectura fue diseñada bajo los siguientes principios:

* Separación de responsabilidades.
* Bajo acoplamiento entre componentes.
* Alta cohesión dentro de cada módulo.
* Reutilización de código.
* Escalabilidad.
* Facilidad de mantenimiento.
* Preparación para futuras integraciones.

Estos principios permiten agregar nuevas reglas de detección, nuevos tipos de ataques y nuevos motores de análisis sin modificar la estructura principal del sistema.

---

# 4. Components

## 4.1 Attack Runner

El Attack Runner representa el punto de entrada para las simulaciones.

Su responsabilidad consiste en ejecutar escenarios de ataque previamente definidos.

Actualmente implementa simulaciones para:

* Brute Force
* Resource Enumeration
* Credential Stuffing

Cada simulación genera múltiples eventos que posteriormente serán analizados por el sistema.

---

## 4.2 Event Generator

El Event Generator es responsable de construir eventos individuales de seguridad.

Cada evento representa una acción realizada por un usuario o una dirección IP dentro del sistema.

Su única responsabilidad consiste en crear eventos válidos y almacenarlos en la base de datos.

Este módulo no realiza ninguna detección.

---

## 4.3 Database Layer

La base de datos PostgreSQL actúa como el almacenamiento principal del sistema.

Actualmente existen dos entidades principales:

Events

Almacena toda la actividad generada durante las simulaciones.

Alerts

Almacena únicamente las alertas generadas por el motor de detección.

La separación entre eventos y alertas permite conservar el historial completo sin mezclar datos crudos con información procesada.

---

## 4.4 Detection Engine

El Detection Engine constituye el núcleo del sistema.

Su responsabilidad consiste en ejecutar todas las reglas de detección disponibles para cada evento recibido.

Actualmente implementa tres detectores independientes:

* Brute Force Detection
* Resource Enumeration Detection
* Credential Stuffing Detection

Cada detector funciona de forma completamente independiente.

Esto permite incorporar nuevas reglas sin modificar las existentes.

---

## 4.5 Alert Manager

No todas las alertas detectadas deben almacenarse.

Durante ataques repetitivos es común generar múltiples alertas idénticas que únicamente incrementan el ruido operacional.

El Alert Manager implementa mecanismos de supresión de alertas mediante ventanas de tiempo configurables.

Si una alerta equivalente ya fue registrada recientemente para la misma dirección IP, la nueva alerta es descartada.

Este mecanismo reduce significativamente la cantidad de información redundante.

---

## 4.6 Correlation Engine

El Correlation Engine representa el componente de mayor nivel analítico dentro de la arquitectura.

Su objetivo consiste en analizar las alertas previamente generadas para identificar patrones de ataque más complejos.

Actualmente implementa una correlación de múltiples etapas (Multi-Stage Attack), donde diferentes tipos de alertas son combinados para generar una alerta de mayor criticidad.

Este enfoque permite aproximarse al funcionamiento de plataformas SIEM utilizadas en entornos empresariales.

---

## 4.7 Power BI

Power BI constituye la capa de visualización del sistema.

Su función consiste en transformar los eventos y alertas almacenados en PostgreSQL en dashboards interactivos que facilitan el análisis por parte del usuario.

Actualmente el proyecto incorpora dashboards para:

* Executive Overview
* IP Analysis
* User Analysis
* Resource Analysis
* Incident Investigation

---

# 5. Layer Responsibilities

Cada capa posee responsabilidades claramente definidas.

| Layer              | Responsibility                   |
| ------------------ | -------------------------------- |
| Attack Runner      | Ejecutar escenarios de ataque    |
| Event Generator    | Generar eventos                  |
| Database           | Persistir información            |
| Detection Engine   | Detectar amenazas                |
| Alert Manager      | Reducir ruido mediante supresión |
| Correlation Engine | Correlacionar múltiples alertas  |
| Power BI           | Visualizar información           |

Esta separación permite que cada componente pueda evolucionar de forma independiente.

---

# 6. Scalability

La arquitectura fue diseñada pensando en futuras versiones.

Entre las capacidades previstas se encuentran:

* Nuevas reglas de detección.
* MITRE ATT&CK Mapping.
* Threat Hunting.
* User and Entity Behavior Analytics (UEBA).
* Machine Learning.
* SOAR.
* Integraciones Cloud.
* Integración con Windows Event Logs.
* Integración con Syslog.

La incorporación de estas funcionalidades no requiere modificar la arquitectura general, únicamente extender los componentes correspondientes.

---

# 7. Architectural Decisions

Durante el desarrollo se tomaron varias decisiones con el objetivo de mantener una arquitectura limpia y mantenible.

Entre ellas destacan:

* Uso del patrón Repository para desacoplar la lógica de negocio del acceso a datos.
* Implementación de un Detection Engine independiente de los generadores de eventos.
* Separación entre detección y correlación.
* Implementación de supresión de alertas para reducir ruido.
* Uso de Power BI como capa exclusiva de visualización.

Estas decisiones permiten mantener un sistema modular preparado para futuras ampliaciones.

---

# 8. Current Architecture Status

La arquitectura implementada corresponde a la primera versión funcional de Cloud Security Lab.

La versión 1.0 proporciona una base sólida para continuar incorporando capacidades propias de plataformas modernas de monitoreo y análisis de seguridad sin necesidad de rediseñar los componentes principales del sistema.
