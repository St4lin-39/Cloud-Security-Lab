# Cloud Security Lab

# Database Design

## 1. Introduction

La base de datos constituye el componente encargado de almacenar toda la información generada durante la ejecución de Cloud Security Lab.

Su diseño busca mantener una separación clara entre los eventos producidos por el sistema y las alertas derivadas del proceso de detección, permitiendo conservar tanto la información original como el resultado del análisis realizado por el Detection Engine.

La versión 1.0 utiliza PostgreSQL como sistema gestor de bases de datos y SQLAlchemy como ORM para abstraer las operaciones de persistencia.

---

# 2. Design Philosophy

El modelo de datos fue diseñado siguiendo los siguientes principios:

* Normalización de la información.
* Separación entre datos crudos y datos procesados.
* Facilidad para consultas analíticas.
* Escalabilidad.
* Compatibilidad con herramientas de Business Intelligence.

Cada entidad representa una etapa diferente dentro del flujo de procesamiento de seguridad.

---

# 3. Database Model

Actualmente el sistema se compone de dos entidades principales:

```text
Events
    │
    ▼
Detection Engine
    │
    ▼
Alerts
```

Los eventos representan la actividad registrada.

Las alertas representan el resultado del análisis realizado sobre dichos eventos.

---

# 4. Events Table

La tabla **Events** almacena todos los eventos generados por el sistema.

Cada registro representa una acción individual ejecutada por un usuario o una dirección IP.

Ejemplos:

* Intento de autenticación.
* Acceso a un recurso.
* Evento generado durante una simulación.

Los eventos nunca son modificados una vez almacenados.

Esto permite conservar el historial completo para posteriores análisis.

### Información almacenada

* Identificador.
* Usuario.
* Dirección IP.
* Tipo de evento.
* Recurso accedido.
* Fecha y hora.

---

# 5. Alerts Table

La tabla **Alerts** almacena únicamente los eventos que fueron considerados sospechosos por el Detection Engine.

Cada alerta representa una conclusión obtenida tras analizar uno o varios eventos.

Las alertas contienen información resumida sobre el comportamiento detectado.

### Información almacenada

* Identificador.
* Tipo de alerta.
* Usuario.
* Dirección IP.
* Volumen de intentos.
* Fecha y hora.

---

# 6. Why Separate Events and Alerts?

Uno de los principios fundamentales del proyecto consiste en mantener separados los datos originales de los resultados del proceso de análisis.

Esta decisión proporciona múltiples ventajas.

## Conservación del historial

Todos los eventos permanecen disponibles incluso cuando no generan ninguna alerta.

## Reprocesamiento

Nuevas reglas pueden ejecutarse sobre eventos históricos sin necesidad de generar nuevamente la información.

## Auditoría

Es posible explicar exactamente qué eventos originaron una determinada alerta.

## Escalabilidad

Permite incorporar nuevos motores de detección sin modificar el modelo principal.

---

# 7. Repository Layer

El acceso a la base de datos se encuentra completamente desacoplado mediante el patrón Repository.

Cada entidad posee su propio repositorio responsable exclusivamente de realizar operaciones de persistencia.

Actualmente existen:

* Event Repository
* Alert Repository

Este enfoque evita que la lógica de negocio interactúe directamente con SQLAlchemy.

---

# 8. Database Workflow

El flujo de información dentro de la base de datos puede resumirse de la siguiente manera:

```text
Attack Runner

↓

Event Generator

↓

Events Table

↓

Detection Engine

↓

Alerts Table

↓

Power BI
```

La información fluye únicamente en una dirección.

No existen modificaciones sobre eventos previamente almacenados.

---

# 9. Analytical Queries

El modelo fue diseñado para facilitar consultas analíticas utilizadas posteriormente en Power BI.

Entre ellas:

* Eventos por usuario.
* Eventos por dirección IP.
* Eventos por recurso.
* Alertas por tipo.
* Alertas por usuario.
* Alertas por dirección IP.
* Correlación de ataques.
* Evolución temporal de incidentes.

Estas consultas permiten construir dashboards sin necesidad de modificar el modelo de datos.

---

# 10. Current Limitations

La versión 1.0 mantiene un modelo de datos intencionalmente sencillo.

Actualmente no existen entidades para:

* Incidentes.
* Activos.
* Dispositivos.
* Riesgo.
* Severidad.
* Usuarios del sistema.
* Casos de investigación.
* Inteligencia de amenazas.

Estas entidades podrán incorporarse en futuras versiones sin afectar la estructura existente.

---

# 11. Future Evolution

Las próximas versiones ampliarán el modelo incorporando nuevas entidades relacionadas con plataformas SIEM empresariales.

Entre ellas:

* Risk Score.
* Severity.
* Incident Management.
* MITRE ATT&CK Mapping.
* Threat Intelligence.
* Asset Inventory.
* User Profiles.
* Geolocation.
* Historical Correlation.

Estas ampliaciones permitirán incrementar la capacidad analítica del sistema sin modificar el flujo principal de procesamiento implementado en la versión 1.0.
