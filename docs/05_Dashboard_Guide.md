# Cloud Security Lab

# Dashboard Guide

## 1. Introduction

Cloud Security Lab incorpora un conjunto de dashboards desarrollados en Power BI con el objetivo de transformar eventos y alertas en información útil para el análisis de seguridad.

Cada página del dashboard fue diseñada para responder preguntas específicas que normalmente realizaría un analista durante una investigación.

En conjunto, estas páginas permiten comprender el comportamiento general del sistema, identificar patrones sospechosos y analizar incidentes de forma estructurada.

---

# 2. Dashboard Philosophy

Los dashboards siguen una filosofía de análisis progresivo.

En lugar de mostrar toda la información simultáneamente, cada página responde un conjunto específico de preguntas.

El flujo recomendado de análisis es el siguiente:

```text
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

Este enfoque permite pasar desde una visión general del entorno hasta el análisis detallado de un incidente concreto.

---

# 3. Executive Overview

## Objective

Proporcionar una visión general del estado actual del sistema.

Esta página responde preguntas como:

* ¿Cuántos eventos se han generado?
* ¿Cuántas alertas existen?
* ¿Qué tipos de alertas predominan?
* ¿Qué tipos de eventos ocurren con mayor frecuencia?

### KPIs

* Total Events
* Total Alerts
* Active Users
* Active IPs

### Visualizations

* Alertas por tipo.
* Eventos por tipo.

Esta página representa el punto de entrada para cualquier proceso de análisis.

---

# 4. IP Analysis

## Objective

Identificar las direcciones IP con mayor actividad dentro del sistema.

Esta página responde preguntas como:

* ¿Qué IP genera más eventos?
* ¿Qué IP concentra la mayor cantidad de alertas?
* ¿Existe una dirección IP especialmente activa?

### Visualizations

* Eventos por dirección IP.
* Alertas por dirección IP.
* Tabla resumen de direcciones IP.

Esta vista facilita la identificación de posibles orígenes de ataques.

---

# 5. User Analysis

## Objective

Analizar el comportamiento de los usuarios registrados en los eventos.

Esta página responde preguntas como:

* ¿Qué usuarios generan mayor actividad?
* ¿Qué usuarios presentan mayor cantidad de intentos fallidos?
* ¿Qué usuarios aparecen asociados a alertas?

### Visualizations

* Eventos por usuario.
* Intentos fallidos por usuario.
* Tabla de usuarios.

Esta información permite identificar cuentas potencialmente comprometidas o utilizadas durante simulaciones de ataque.

---

# 6. Resource Analysis

## Objective

Analizar los recursos accedidos por los usuarios durante las simulaciones.

Esta página responde preguntas como:

* ¿Qué recursos reciben más accesos?
* ¿Qué recursos participan con mayor frecuencia en eventos sospechosos?
* ¿Existe un patrón de reconocimiento sobre determinados recursos?

### Visualizations

* Recursos más accedidos.
* Eventos por recurso.
* Recursos clasificados por tipo de evento.
* Tabla de recursos.

Esta vista resulta especialmente útil para analizar ataques de reconocimiento y enumeración de recursos.

---

# 7. Incident Investigation

## Objective

Proporcionar una vista orientada a la investigación de incidentes.

Esta página permite revisar cronológicamente los eventos y alertas generados durante una simulación.

Responde preguntas como:

* ¿Qué ocurrió primero?
* ¿Qué alertas fueron generadas?
* ¿Qué dirección IP estuvo involucrada?
* ¿Qué usuarios participaron?
* ¿Cuál fue la secuencia del incidente?

### Visualizations

* Tabla cronológica de eventos.
* Tabla cronológica de alertas.
* Indicadores generales del incidente.
* Segmentadores para filtrar por IP o usuario.

Esta página representa el nivel más detallado del proceso de análisis.

---

# 8. Analytical Workflow

El dashboard fue diseñado para ser utilizado siguiendo el siguiente flujo de trabajo:

1. Revisar la actividad general en Executive Overview.
2. Identificar direcciones IP relevantes mediante IP Analysis.
3. Analizar los usuarios involucrados en User Analysis.
4. Revisar los recursos afectados en Resource Analysis.
5. Reconstruir el incidente utilizando Incident Investigation.

Este flujo refleja una metodología simplificada de investigación utilizada en centros de operaciones de seguridad (SOC).

---

# 9. Current Scope

Los dashboards actuales representan el estado de la versión 1.0.

Su objetivo principal consiste en facilitar la comprensión de los eventos generados por las simulaciones implementadas en el laboratorio.

No pretenden sustituir las capacidades de plataformas SIEM comerciales, sino servir como base para futuras ampliaciones.

---

# 10. Future Improvements

Las próximas versiones incorporarán nuevas capacidades de visualización, entre ellas:

* Mapas geográficos.
* Tendencias temporales avanzadas.
* Riesgo por incidente.
* Severidad de alertas.
* MITRE ATT&CK Mapping.
* Dashboards de Threat Hunting.
* Dashboards ejecutivos.
* Métricas de rendimiento del Detection Engine.

Estas mejoras permitirán incrementar significativamente la capacidad analítica del sistema.
