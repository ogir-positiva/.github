# 🏢 OGIR - Positiva

Organización privada que centraliza los repositorios de código fuente utilizados para el desarrollo, operación y soporte de soluciones tecnológicas con impacto en procesos **financieros, de datos, gestión de riesgos y cumplimiento normativo**.

El acceso a esta organización es **restringido y controlado**.

---

## 🎯 Alcance y objetivo

Esta organización tiene como propósito:

- Centralizar el código fuente de soluciones internas
- Asegurar y el mantener el SistemaIntegral de Gestion de Riesgos `SIAR` 
- Asegurar la aplicación de estándares técnicos y de seguridad
- Garantizar trazabilidad, control de cambios y segregación de funciones
- Facilitar procesos de auditoría, control interno y cumplimiento regulatorio
- Reducir riesgos operativos, tecnológicos y de información

---

## 🧱 Clasificación de repositorios

Los repositorios se organizan de acuerdo con su naturaleza y riesgo operativo:

### 🔹 Aplicaciones
Repositorios que soportan procesos de la operación:
- APIs y servicios backend
- Automatizaciones de procesos
- Herramientas de uso general 
- Procesos batch y event-driven
- Pipelines de datos, reportes regulatorios y analítica

### 🔹 Infraestructura como código (IaC)
Repositorios destinados exclusivamente a:
- Definición de infraestructura mediante Terraform
- Gestión de proyectos cloud, redes, IAM y servicios
- Separación estricta por ambientes (desarrollo / producción)
- Control de cambios sobre componentes de infraestructura

### 🔹 Gestion de Riesgos
Repositorios con código de metodologias y processos del `SIAR`  :
- Metodologias de Gestion de Riesgos
- Automatizacion de procesos de la gestión de Riesgos 

### 🔹 Apñlicaciones de IA 
Repositorios con código para aplicacionde IA a procesos, análitica y gestión de riesgos   :
- Modelos personalizados 
- Esquemas de agentes
- Otros 

### 🔹 Componentes compartidos
Repositorios con código reutilizable para:
- Logging corporativo
- Manejo de errores y excepciones
- Seguridad y control de accesos
- Utilidades comunes transversales

---

## 🧩 Lineamientos técnicos y de control

Todos los repositorios de esta organización deben cumplir, como mínimo, con los siguientes lineamientos:

- Arquitectura limpia (Clean Architecture / Hexagonal) o equivalente, con separación de responsabilidades
- Separación de capas (dominio, aplicación, infraestructura)
- Versionamiento semántico y control de dependencias
- Gestión centralizada de configuración y secretos
- Logging estructurado orientado a trazabilidad y auditoría
- Manejo explícito de errores y eventos relevantes
- Principio de mínimo privilegio en accesos y permisos (IAM)

---

## 🔄 Gestión de cambios y control de versiones

La gestión de cambios se rige por los siguientes controles:

- Rama principal protegida (`main`)
- Desarrollo únicamente mediante ramas controladas
- Uso obligatorio de Pull Requests
- Revisión técnica previa a la integración de cambios
- Evidencia de cambios mediante historial de commits y PRs
- Automatización de pruebas y despliegues cuando aplique

---

## 🔐 Seguridad de la información

- Prohibido el almacenamiento de credenciales o secretos en el código
- Uso obligatorio de servicios de gestión de secretos
- Control de accesos basado en roles
- Segregación de funciones entre desarrollo, revisión y despliegue
- Registro de eventos relevantes para análisis posterior y auditoría

---

## 📚 Documentación y evidencia

Cada repositorio debe contar con documentación mínima que incluya:

- Descripción funcional del componente
- Alcance y criticidad del proceso soportado
- Instrucciones de despliegue o ejecución
- Consideraciones de seguridad y cumplimiento
- Dependencias relevantes

Esta documentación constituye **evidencia de control** para procesos de auditoría.

---

## ⚠️ Uso interno y confidencialidad

El contenido de esta organización es **confidencial** y de uso exclusivo.  
Cualquier uso, reproducción o distribución no autorizada constituye un incumplimiento a las políticas internas de seguridad de la información.

---

## 📬 Responsabilidad y gobierno

Responsable del gobierno técnico:  
**Equipo de Arquitectura / Ingeniería**

Los responsables funcionales de cada repositorio se definen en su documentación específica.
