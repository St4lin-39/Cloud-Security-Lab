# Cloud Security Lab

# Detection Engine

## 1. Introduction

El Detection Engine constituye el núcleo analítico de Cloud Security Lab.

Su responsabilidad consiste en evaluar cada evento generado por el sistema, aplicar un conjunto de reglas de detección previamente definidas y determinar si dicho evento forma parte de un comportamiento potencialmente malicioso.

A diferencia de soluciones basadas en inteligencia artificial o modelos estadísticos, la versión 1.0 implementa un motor completamente basado en reglas (Rule-Based Detection), permitiendo comprender de forma transparente el proceso de toma de decisiones y facilitar la incorporación de nuevas capacidades en futuras versiones.

---

# 2. Detection Philosophy

Cloud Security Lab adopta un enfoque de detección basado en reglas por las siguientes razones:

* Simplicidad en la implementación.
* Facilidad para explicar cada decisión tomada por el sistema.
* Resultados determinísticos.
* Bajo costo computacional.
* Alta facilidad de mantenimiento.
* Base sólida para incorporar técnicas más avanzadas en futuras versiones.

Cada regla representa un comportamiento considerado sospechoso dentro del contexto del laboratorio.

Cuando una regla se cumple, el motor genera una alerta que posteriormente será procesada por el sistema de supresión y correlación.

---

# 3. Detection Pipeline

El flujo de procesamiento de un evento sigue la siguiente secuencia:

```text
Event

↓

Detection Engine

↓

Detection Rules

↓

Alert Manager

↓

Correlation Engine

↓

Alert Storage

↓

Power BI
```

Cada componente posee una responsabilidad específica, permitiendo mantener una arquitectura desacoplada y fácilmente extensible.

---

# 4. Detection Rules

Actualmente el sistema implementa tres reglas principales de detección.

---

## 4.1 Brute Force Detection

### Objective

Detectar múltiples intentos fallidos de autenticación realizados contra una misma cuenta desde una misma dirección IP dentro de una ventana temporal determinada.

### Detection Logic

La regla consulta el historial reciente de eventos asociados al usuario y dirección IP.

Si el número de eventos LOGIN_FAILED supera el umbral configurado, se genera una alerta.

### Configuration

* Threshold: 5 intentos.
* Time Window: 5 minutos.

### Generated Alert

```text
BRUTE_FORCE_ATTEMPT
```

---

## 4.2 Resource Enumeration Detection

### Objective

Detectar usuarios que intentan acceder a una cantidad inusual de recursos diferentes en un corto período de tiempo.

Este comportamiento suele estar asociado con procesos de reconocimiento realizados antes de un ataque más complejo.

### Detection Logic

La regla contabiliza la cantidad de recursos distintos accedidos por un usuario.

Cuando el número supera el umbral configurado, se genera una alerta.

### Configuration

* Threshold: 10 recursos únicos.
* Time Window: 15 minutos.

### Generated Alert

```text
RESOURCE_ENUMERATION
```

---

## 4.3 Credential Stuffing Detection

### Objective

Detectar intentos fallidos de autenticación sobre múltiples cuentas utilizando una misma dirección IP.

Este patrón suele indicar el uso de credenciales filtradas previamente obtenidas en otras plataformas.

### Detection Logic

La regla identifica cuántos usuarios diferentes presentan eventos LOGIN_FAILED provenientes de una misma dirección IP.

Cuando la cantidad supera el umbral establecido, el sistema genera una alerta.

### Configuration

* Threshold: 5 usuarios.
* Time Window: 10 minutos.

### Generated Alert

```text
CREDENTIAL_STUFFING
```

---

# 5. Alert Suppression

La generación continua de eventos similares puede producir un elevado número de alertas idénticas, dificultando el análisis por parte del operador.

Para reducir este problema, Cloud Security Lab incorpora un mecanismo de supresión de alertas.

Antes de almacenar una nueva alerta, el sistema verifica si ya existe una alerta equivalente para la misma dirección IP dentro de un período de enfriamiento configurado.

Si existe una alerta reciente, la nueva alerta es descartada.

### Objective

Reducir el ruido operacional y evitar la duplicación innecesaria de alertas.

### Configuration

Cooldown: 5 minutos.

---

# 6. Correlation Engine

La detección de una única regla no siempre representa un ataque completo.

Por este motivo, el sistema incorpora un Correlation Engine encargado de analizar las alertas previamente generadas.

Cuando una misma dirección IP presenta simultáneamente los siguientes comportamientos:

* Brute Force
* Resource Enumeration
* Credential Stuffing

el sistema interpreta que existe evidencia suficiente para considerar la actividad como un ataque de múltiples etapas.

En consecuencia, genera una nueva alerta de mayor nivel.

### Generated Alert

```text
MULTI_STAGE_ATTACK
```

Este enfoque permite representar una aproximación simplificada a los mecanismos de correlación utilizados por plataformas SIEM empresariales.

---

# 7. Detection Pipeline Integration

El Detection Pipeline coordina el funcionamiento de todos los componentes del sistema.

Para cada evento recibido realiza las siguientes operaciones:

1. Ejecutar el Detection Engine.
2. Procesar cada alerta mediante el Alert Manager.
3. Almacenar únicamente las alertas no suprimidas.
4. Ejecutar el Correlation Engine.
5. Procesar la alerta correlacionada mediante el Alert Manager.
6. Almacenar la alerta correlacionada cuando corresponda.
7. Retornar todas las alertas válidas para su visualización.

Este flujo garantiza que únicamente las alertas relevantes lleguen a la capa de análisis.

---

# 8. Current Limitations

La versión 1.0 implementa únicamente un subconjunto de técnicas de detección.

Actualmente no se encuentran implementadas capacidades como:

* Password Spraying Detection.
* Impossible Travel Detection.
* Lateral Movement Detection.
* Privilege Escalation Detection.
* Data Exfiltration Detection.
* User and Entity Behavior Analytics (UEBA).
* Machine Learning.
* Anomaly Detection.
* Threat Intelligence Integration.

Estas capacidades forman parte del roadmap de evolución del proyecto.

---

# 9. Future Evolution

El Detection Engine fue diseñado con una arquitectura modular que permite incorporar nuevas reglas sin modificar las existentes.

Las próximas versiones buscarán ampliar el motor mediante:

* Nuevos detectores basados en comportamiento.
* Correlación avanzada.
* Puntuación de riesgo (Risk Scoring).
* Integración con MITRE ATT&CK.
* Detección basada en Machine Learning.
* Integración con plataformas SOAR.

La arquitectura actual proporciona una base sólida para evolucionar desde un laboratorio académico hacia una plataforma de análisis de seguridad considerablemente más cercana a las soluciones utilizadas en la industria.
