# Levantamiento de Información del Proyecto SGI

En el presente documento se hace un levantamiento completo del estado actual del sistema SGI, su arquitectura, tecnologías utilizadas, módulos principales y flujos de trabajo. Este levantamiento servirá como base para futuras mejoras y migraciones tecnológicas.

El sistema tiene una arquitectura basada en capas y éstas a su vez se estructuran en  módulos, cada uno de los m,ódulos usan el patrón MVC (Modelo-Vista-Controlador) para organizar la lógica de negocio, la presentación y el acceso a datos. El sistema está construido en dos grandes capas:
- El Backend en PHP con CodeIgniter, junto con una solución en Django con Python.
- En la base de datos, se utiliza MySQL como motor de persistencia.
- Tiene un subsistema de log de eventos y un sistema de gestión de usuarios con roles y permisos.


## Tecnologías Principales y Versiones
- **Backend:** PHP >= 5.3.7 ; django >= 2.2
- **Servidor Web:** Apache HTTP Server 2.2
- **Framework:** CodeIgniter 2.1.5
- **Base de datos:** MySQL 5.5
- **Frontend:** Vuejs 2.6, Bootstrap 3, HTML4
- **Gestión de dependencias:** composer (PHP) ; pip (Python)
- **Motor de plantillas:** Twig 1.0; jinja2
- **Control de versiones:** Git, GitHub

## Estructura y Módulos Principales (`app/src`)
- `config`: Archivos de configuración del sistema
- `controllers`: Controladores principales de la aplicación (lógica de negocio y rutas)
- `helpers`: Funciones auxiliares reutilizables
- `hooks`: Extensiones para eventos del ciclo de vida
- `libraries`: Librerías personalizadas de la aplicación para manejo de funcionalidades específicas
- `models`: Modelos de datos para acceso a base de datos mediante ORM
- `views-active`: Aplicación de vistas activas para la interfaz de usuario VueJS
- `third_party`: Librerías de terceros  Vistas basadas en Twig y Jinja2
- `test`: Pruebas del sistema Pytest y PHP Unit
- `reports`: modulo de reportes y visualización de datos, análisis de costos, stocks, pedidos activos etc
- `sap-importacion`: modulo de importación de datos desde SAP
- `costings`: modulo de prorrateo de costos y cálculo de costos totales y parciales con cuadre de libro mayor
- `expenses`: modulo de manejo de gastos y costos de importación
- `tributes`: modulo de manejo de impuestos y términos de comercio internacional (Incoterms, Monedas, Politicas)
- `almagro-import`: modulo de importación de datos desde almagro
- `labels`: Módulo de automatización de activación de etiquetas fiscales
- `system-layer-1`: Núcleo del sistema escrito en el framework CodeIgniter usando PHP 5.5
- `system-layer-2`: Núcleo del framework escrito en Django con Python
- `logs`, `cache`: Logs de acciones de usuario y cacheo de datos

---

## Arquitectura General del Sistema

El sistema APPImportaciones implementa una arquitectura basada en capas y módulos. La solución se estructura en dos capas principales:

- **Backend CodeIgniter; Django:** expone varios servicios API y gestiona la lógica de negocio y acceso a datos.
- **Frontend VUEJS, Twig y Jinja2:** provee la interfaz de usuario y la lógica cliente, consumiendo los servicios del backend vía HTTP/JSON.

### Flujo de Peticiones y Enrutamiento

1. **Servidor Web (Apache):** Todas las peticiones HTTP pasan por reglas de reescritura en `.htaccess`, que redirigen las solicitudes a `index.php` si no corresponden a archivos estáticos.
2. **Front Controller:** Inicializa el entorno, define constantes de rutas y carga el núcleo de CodeIgniter y Django.
3. **Router:** Determina el controlador y método a ejecutar según la URL.
4. **Controlador:** Ejecuta la lógica de negocio, interactúa con los modelos y genera la respuesta (JSON para la SPA o renderizado de vistas con Twig).
5. **Frontend VUEJS:** Consume los endpoints del backend, actualiza la interfaz y gestiona la navegación SPA.

### Integración Frontend-Backend

- **Comunicación:** El frontend VueJs se comunica con el backend CodeIgniter usando peticiones HTTP AJAX, recibiendo y enviando datos en formato JSON.
- **Plantillas:** El backend utiliza Twig y Jinja2 para el renderizado de vistas cuando es necesario, aunque la mayor parte de la interfaz se gestiona como SPA.
- **Directivas y Servicios:** VueJs define módulos, controladores, factories y directivas personalizadas para la lógica de presentación y consumo de datos.

### Stack Tecnológico y Dependencias

| Capa                | Tecnología                | Propósito                                     | Configuración principal      | Descripción breve |
|---------------------|--------------------------|-----------------------------------------------|-----------------------------|-------------------|
| Servidor Web        | Apache HTTP Server       | Manejo de peticiones y archivos estáticos     | `.htaccess` (URL rewriting) | Servidor web principal que recibe todas las solicitudes y aplica reglas de reescritura para el enrutamiento centralizado. |
| Backend Layer1      | CodeIgniter 2            | Framework MVC, ruteo, controladores           | `index.php` (bootstrap)     | Motor principal de la lógica de negocio Manejo de Importaciones, expone APIs y gestiona la interacción con la base de datos. |
| Backend Layer2      | Django 2                  | Framework MTV, ruteo, controladores           | `manage.py` (bootstrap)     | Motor principal de la lógica de negocio Manejo de costos para Costeo y Reportes, expone APIs y gestiona la interacción con la base de datos. |
| Motor de plantillas | Twig2/Jinja2                     | Renderizado de vistas en servidor             | Dependencia Composer/Pip        | Permite generar vistas HTML desde el backend usando plantillas reutilizables y seguras. |
| Frontend            | VueJs 1.x            | SPA, ruteo y data binding                     | Módulo `cordovezApp`        | Framework JS para construir la interfaz de usuario dinámica y gestionar la navegación SPA. |
| UI/Estilo           | Bootstrap   | Interfaz administrativa             | Archivos CSS/JS             | Frameworks de diseño visual y componentes para una UI moderna y adaptable. |
| Visualización       | Flot, Morris Charts      | Gráficas y reportes                           | Archivos JS                 | Librerías JS para visualización de datos y generación de gráficos en reportes. |
| Dependencias PHP    | Composer                 | Gestión de dependencias PHP                   | `composer.json`             | Herramienta para instalar y actualizar librerías PHP requeridas por el proyecto. |
| Dependencias Python | Pip                      | Gestión de dependencias Python                | `requirements.txt`         | Herramienta para instalar y actualizar librerías Python requeridas por el proyecto. |
| Dependencias Front  | Bower (histórico)        | Gestión de dependencias frontend              | `bower.json`                | Herramienta (ya en desuso) para gestión de librerías JS/CSS del frontend. |

---
## Tabla de Módulos MCV

| Módulo / Funcionalidad          | Descripción Detallada |
|---------------------------------|----------------------|
| Pedidos de importación          | Sistema completo de gestión y registro de pedidos de importación que permite crear, modificar y seguir el estado de cada pedido desde su creación hasta su entrega. Incluye validaciones de datos, cálculo automático de costos preliminares, asignación de proveedores y generación de documentos asociados. |
| Productos                       | Catálogo centralizado y sistema de administración de productos que maneja información completa de cada artículo incluyendo códigos, descripciones, categorías, precios, especificaciones técnicas, imágenes y datos de importación. Permite búsquedas avanzadas y filtros por múltiples criterios. |
| Proveedores                     | Módulo integral de gestión de proveedores y contactos que administra toda la información comercial, financiera y logística de los socios comerciales. Incluye historial de transacciones, evaluación de desempeño, datos bancarios, contactos clave y documentación legal. |
| Usuarios                        | Sistema robusto de gestión y autenticación de usuarios que maneja perfiles personalizados, roles específicos, permisos granulares y sesiones seguras. Controla el acceso a diferentes módulos según el nivel de autorización y mantiene registro de actividades por usuario. |
| Reportes                        | Módulo avanzado de generación y visualización de reportes que incluye análisis de costos, gastos operativos, pagos realizados, facturas procesadas y estados financieros. Ofrece múltiples formatos de exportación, gráficos interactivos y filtros personalizables por fechas, categorías y otros parámetros. |
| Detalle de pedidos              | Sistema especializado de consulta y seguimiento detallado que permite visualizar toda la información específica de cada pedido realizado, incluyendo productos, cantidades, costos, estados de avance, documentación asociada y historial completo de cambios. |
| Facturas informativas           | Módulo especializado para la consulta y gestión de facturas informativas ICE que maneja toda la documentación fiscal requerida, cálculos de impuestos específicos, validaciones tributarias y generación de reportes para autoridades competentes. |
| Pagos de facturas               | Sistema integral de gestión y seguimiento de pagos que controla el detalle completo de todas las transacciones financieras, estados de pago, fechas de vencimiento, métodos de pago utilizados y conciliación bancaria automática. |
| Gastos iniciales                | Módulo de registro y control de gastos iniciales de importación que documenta todos los costos previos al proceso principal incluyendo trámites, permisos, inspecciones, transporte inicial y gastos administrativos preliminares. |
| Nacionalización                 | Sistema especializado para el registro y seguimiento de gastos de nacionalización que maneja todos los costos asociados con los procesos aduaneros, impuestos de importación, tasas portuarias, almacenaje y trámites de liberación de mercancías. |
| Importación desde SAP           | Módulo de integración y sincronización que facilita la importación automatizada de datos desde sistemas externos SAP, incluyendo validación de formatos, transformación de datos, manejo de errores y reportes de inconsistencias para mantener la integridad de la información. |
| Impuestos y términos            | Sistema completo de gestión de impuestos y términos de comercio internacional que administra Incoterms, tipos de cambio de monedas, políticas comerciales, cálculos tributarios específicos y normativas aduaneras vigentes según regulaciones locales e internacionales. |
| Procesos parciales              | Módulo de control y seguimiento de procesos parciales de importación que permite dividir grandes importaciones en lotes menores, realizar seguimiento independiente de cada parte y consolidar información para reportes unificados del proceso completo. |
| Relación pedido-factura         | Sistema de trazabilidad que establece y mantiene las relaciones entre pedidos y facturas correspondientes, permitiendo consultas cruzadas, validación de correspondencia, detección de discrepancias y generación de reportes de conciliación. |
| Pedidos recibidos Almagro       | Módulo especializado para el seguimiento y control de pedidos que han llegado a la bodega Almagro, incluyendo verificación de inventario, control de calidad, registro de recepción, actualización de estados y notificaciones automáticas a los responsables. |
| Home / Dashboard                | Página principal e interfaz de control central del sistema que presenta resúmenes ejecutivos, indicadores clave de rendimiento, alertas importantes, accesos rápidos a funciones principales y visualización de datos críticos en tiempo real. |
| Perfil de usuario               | Módulo de gestión personal que permite a cada usuario visualizar y editar su información personal, preferencias del sistema, configuración de notificaciones, cambio de contraseñas y personalización de la interfaz según sus necesidades específicas. |

*Nota: Esta tabla describe la funcionalidad principal de cada módulo del sistema. Para detalles técnicos específicos sobre controladores, modelos y vistas, revisar la documentación técnica del código fuente en las carpetas correspondientes de `controllers`, `models` y `views`.*

*Nota: Los módulos están organizados siguiendo el patrón MVC (Modelo-Vista-Controlador) y las vistas se encuentran estructuradas por carpetas temáticas dentro del directorio `views` (base, errors, forms, pages, reports, scripts, sections).*

---

## Tablas y Descripciones de Arquitectura y Flujos

### 1. Flujo General del Sistema

| Paso | Descripción técnica | Descripción breve |
|------|---------------------|-------------------|
| 1 | El usuario accede a la aplicación desde su navegador. | Inicio de la interacción del usuario con el sistema. |
| 2 | El servidor Apache recibe la petición y aplica las reglas de `.htaccess`. | Apache decide si la petición es para un recurso estático o para la aplicación. |
| 3 | Si la petición no es para un archivo estático, se redirige a `index.php` (Front Controller). | Se centraliza el manejo de todas las rutas en un solo punto de entrada. |
| 4 | `index.php` inicializa CodeIgniter, configura rutas y el entorno. | El framework se prepara para procesar la petición. |
| 5 | El router de CodeIgniter determina el controlador y método adecuado según la URL. | Se resuelve qué lógica de negocio ejecutar. |
| 6 | El controlador ejecuta la lógica de negocio, consulta/actualiza modelos y genera la respuesta (JSON para VueJs o vista Twig). | Se procesa la petición y se prepara la respuesta para el usuario. |
| 7 | El usuario recibe la respuesta en su navegador y la interfaz se actualiza según corresponda. | El usuario visualiza la información o el resultado de su acción. |
| 8 | `manage.py` inicializa el entorno de Django para módulos de costeo y reportes. | Django se prepara para procesar peticiones relacionadas con análisis de costos. |
| 9 | Nginx actúa como servidor de capa para Django, dirigiendo peticiones de costeo y reportes. | El servidor web gestiona las solicitudes específicas del subsistema Django. |
| 10 | El ORM de Django maneja las consultas y actualizaciones de base de datos para análisis financiero. | Django gestiona los datos de costeo mediante su sistema de mapeo objeto-relacional. |


### 2. Componentes Principales del Sistema

| Componente           | Descripción técnica                                                                 | Descripción breve |
|----------------------|-----------------------------------------------------------------------------------|-------------------|
| Navegador Web        | Punto de acceso para el usuario final.                                            | Donde el usuario interactúa con la aplicación. |
| Apache               | Servidor web que gestiona peticiones y aplica reglas de reescritura.              | Recibe las solicitudes y dirige el tráfico. |
| Nginx                | Servidor proxy reverso que dirige peticiones de Django y maneja el balanceo de carga. | Gestiona el tráfico específico del subsistema Django. |
| VueJs (SPA)      | Framework frontend para la interfaz y lógica de usuario.                         | Construye y actualiza la interfaz de usuario. |
| Bootstrap          | Frameworks de diseño y componentes visuales responsivos.                      | Da estilo y estructura visual a la aplicación. |
| CodeIgniter          | Framework backend PHP (MVC) que expone APIs y lógica de negocio.                 | Procesa la lógica y responde a las peticiones. |
| Django               | Framework backend Python (MTV) que gestiona costeo, reportes y análisis financiero. | Procesa análisis de costos y genera reportes avanzados. |
| Twig                 | Motor de plantillas PHP para renderizar vistas tradicionales.                    | Permite generar HTML dinámico desde el backend. |
| Jinja2               | Motor de plantillas Python para renderizar vistas Django.                        | Genera vistas HTML dinámicas desde Django. |
| Modelos PHP          | Acceso y gestión de datos desde la base de datos.                                | Consultan y actualizan la información en la BD. |
| Django ORM           | Sistema de mapeo objeto-relacional de Django para gestión de datos.              | Gestiona consultas y actualizaciones de datos de costeo. |
| MySQL                | Base de datos relacional para persistencia de información.                       | Almacena todos los datos del sistema. |

---
## 3. Propuesta Técnica

### 3.1 Estrategia de Continuidad y Mantenimiento

- **Auditoría de código** para detectar funciones obsoletas o incompatibles.
- **Actualización de código** para asegurar compatibilidad con nuevas versiones de dependencias.
- **Documentación técnica** completa de todos los módulos funcionales.
- **Pruebas unitarias** y de integración en los módulos críticos.

### 3.2 Estrategia de Actualización Tecnológica

Se propone actualizar progresivamente el sistema a una arquitectura moderna, por fases:

#### Fase 1: Aseguramiento de calidad y refactorización

- Actualización de PHP al menos a 7.4
- Actualizacion de Python a 3.10
- Migración a CodeIgniter 4 o Laravel
- Actualización de dependencias a versiones estables
- Actualización a Django 5.2 
- Actualización de librerías frontend a Vue.js 3.x
- Migración de Twig a Jinja2 para el backend Django
- Migración de MySQL a PostgreSQL
- Migracion de Servidor a Fedora Server 48
- Actualizacion de Apache HTTP Server a 2.4
- Actualizacion de Nginx a 1.24

#### Fase 2: Reemplazo del Frontend SPA

- Migración de VueJs a Vue.js 3.x
- Rediseño de componentes SPA con arquitectura modular y responsive
- Migración progresiva de vistas Twig a componentes frontend

#### Fase 3: Integración y mejora de base de datos

- Optimización de queries y modelos
- Implementación de caché a nivel de base de datos para etiquetas fiscales
- Implementación de migraciones y seeds con herramientas modernas
- Refuerzo en políticas de seguridad y validaciones SQL

---

## 5. Plan de Trabajo Propuesto

| Fase               | Actividades principales                                              | Duración estimada |
|--------------------|----------------------------------------------------------------------|-------------------|
| Levantamiento      | Auditoría técnica, análisis de dependencias y mapeo funcional        | 2 semanas         |
| **1. Correcciones críticas** | **Corrección de cierre de pedidos en módulo de costeo, arreglo de activación de etiquetas SafeTrack y validación de rangos** | **5 semanas** |
| **2. Actualización de servidor y entorno** | Actualización de sistema operativo, dependencias globales, configuración de Docker y servicios base (nginx, PostgreSQL/MySQL, Python, Node.js, etc.) | **1 semana** |
| **3. Modernización de conectores SAP** | Actualizar y/o reescribir conectores para integración segura y eficiente con SAP (RFC, API REST, etc.) | **3 semanas** |
| **4. Migración de base de datos** | Migración de MySQL a PostgreSQL, ajuste de modelos, migración y validación de datos | **2 semanas** |
| **5. Refactorización del Backend** | Actualización a PHP 7.4+, modernización de CodeIgniter 2 → 4, pruebas de compatibilidad y ajuste del core | **8 semanas** |
| **6. Modernización del Frontend** | Nuevo frontend con Vue.js 3.x, componentes modernos, consumo de servicios existentes | **8 semanas** |
| **7. Despliegue y Puesta en Producción** | Configuración del ambiente productivo, migración de datos en vivo, capacitación del equipo, documentación | **1 semana** |
| **8. Implementación Cálculo de Impuestos Multi-Producto** | **Desarrollo de módulo para cálculo de impuestos y costeo de productos diferentes a licores en botella** | **8 semanas** |
| Pruebas QA         | QA, validación funcional con usuarios clave                          | 2 semanas         |

### 5.1 Detalle de Correcciones Críticas (Fase Prioritaria)

#### 5.1.1 Corrección de Cierre de Pedidos - Módulo de Costeo
- **Problema:** Error en el flujo de cierre de pedidos donde el sistema no completa el proceso correctamente, dejando pedidos abiertos cuando deberían estar cerrados
- **Solución propuesta:** 
  - Revisar y corregir la lógica de transición de estados en el controlador de costeo
  - Implementar validaciones adicionales antes del cierre
  - Agregar logs detallados para rastrear el proceso de cierre
- **Impacto:** Alto - afecta la gestión operativa de pedidos

#### 5.1.2 Corrección de Activación de Etiquetas SafeTrack
- **Problema:** Las etiquetas rechazadas por el sistema SafeTrack quedan encoladas en estado de error sin posibilidad de reprocessamiento
- **Solución propuesta:**
  - Implementar un mecanismo de reintento automático para etiquetas rechazadas
  - Crear un proceso de limpieza de cola de errores
  - Agregar interfaz administrativa para gestión manual de etiquetas en error
- **Impacto:** Medio - afecta el flujo de etiquetado y trazabilidad

#### 5.1.3 Corrección de Validación de Rangos
- **Problema:** El sistema falla completamente cuando encuentra errores de validación de rangos, impidiendo continuar con el registro
- **Solución propuesta:**
  - Implementar manejo de excepciones robusto en validaciones de rango
  - Crear mecanismo de validación no bloqueante con alertas informativas
  - Permitir omisión controlada de validaciones con registro de auditoría
- **Impacto:** Alto - bloquea funcionalidades críticas del sistema

---

## 6. Consideraciones Finales

- Este sistema presenta una arquitectura robusta para su época, pero debe adaptarse a los estándares actuales para garantizar su mantenibilidad y seguridad.
- Se recomienda priorizar las fases de refactorización y actualización tecnológica, manteniendo los flujos actuales durante la transición.
- La estructura modular actual permite trabajar por componentes, lo que facilita un plan de modernización progresiva sin afectar la operación.

---

## 7. Recomendaciones

- Migrar hacia una arquitectura basada en componentes reutilizables (Vue/React).
- Sustituir Bower por npm/yarn y Composer actualizado.
- Unificar estilos visuales con TailwindCSS o Bootstrap 5.
- Actualizar a PHP 7.4+ y Python 3.10+.
- Implementar un sistema de gestión de dependencias moderno (Composer, Pip).
- Implementar pruebas automatizadas (PHPUnit + Cypress).
- Mantener una documentación viva del sistema y sus dependencias.
- Usar una base de datos moderna y escalable como PostgreSQL.

---

## 8. Propuesta Económica - Sistema SGI

### 8.1 Propuesta Económica Consolidada

| # | Actividad | Descripción Detallada | Duración | Costo (USD) |
|---|-----------|----------------------|----------|-------------|
| **1** | **🚨 Correcciones Críticas (PRIORITARIO)** | **Corrección inmediata de cierre de pedidos en costeo, activación de etiquetas SafeTrack y validación de rangos** | **5 semanas** | **$1,950** |
| **2** | **Actualización de Servidor y Entorno** | Migración a Docker, configuración de nginx, actualización de SO, setup de PostgreSQL, Python 3.9+, Node.js | 1 semana | **$550** |
| **3** | **Modernización de Conectores SAP** | Reescritura de conectores RFC legacy, implementación de APIs REST modernas, testing de integración | 3 semanas | **$900** |
| **4** | **Migración de Base de Datos** | Migración completa MySQL → PostgreSQL, optimización de esquemas, migración de datos, validación de integridad | 2 semanas | **$800** |
| **5** | **Refactorización del Backend** | Actualización PHP 5.3 → 7.4+, modernización de CodeIgniter 2 → 4, implementación de APIs REST, pruebas unitarias | 8 semanas | **$2,000** |
| **6** | **Modernización del Frontend** | Migración Vue.js 1.x → 3.x, componentes modernos, interfaz responsiva, integración con nuevas APIs | 8 semanas | **$2,000** |
| **7** | **Despliegue y Puesta en Producción** | Configuración del ambiente productivo, migración de datos en vivo, capacitación del equipo, documentación | 1 semana | **$650** |
| **8** | **💼 Implementación Cálculo de Impuestos Multi-Producto** | **Desarrollo de módulo para cálculo de impuestos y costeo de productos diferentes a licores en botella: licores a granel, aguas tónicas y accesorios** | **8 semanas** | **$2,200** |
| | **SUBTOTAL DESARROLLO** | | **36 semanas** | **$11,050** |
| | **Capacitación Post-Implementación** | 20 horas de capacitación al equipo técnico, incluye manual de usuario | 1 semana | **$450** |
| | **Garantía y Soporte (3 meses)** | Soporte técnico post-producción, corrección de bugs | 3 meses | **$0** |
| | | | | |
| | **🎯 COSTO TOTAL DEL PROYECTO** | | **~10 meses** | **🔥 $11,500** |

### 8.2 Opciones de Inversión


#### **⚡ Opción 1: Modernización Básica**
- **Incluye:** 
  - Punto 1 - Correcciones Críticas (PRIORITARIO)
  - Punto 2 - Actualización de Servidor y Entorno con Technologías Anteriores
  - Punto 4 - Migración de Base de Datos
  - Punto 3 - Modernización de Conectores SAP
- **Costo:** $4,950 (2,300 + 700 + 950 + 1,000)
- **Tiempo:** 12 semanas + 3 meses de garantía + soporte
- **Beneficio:** Sistema con correcciones críticas aplicadas y entorno actualizado con tecnologías anteriores, asegurando estabilidad y seguridad a corto plazo.

#### **🚀 Opción 2: Modernización Completa**
- **Incluye:** Todos los puntos del proyecto (1-8):
  - Punto 1 - Correcciones Críticas (PRIORITARIO)
  - Punto 2 - Actualización de Servidor y Entorno  
  - Punto 3 - Modernización de Conectores SAP
  - Punto 4 - Migración de Base de Datos
  - Punto 5 - Refactorización del Backend
  - Punto 6 - Modernización del Frontend
  - Punto 7 - Despliegue y Puesta en Producción
  - Punto 8 - Implementación Cálculo de Impuestos Multi-Producto
- **Costo:** $11,500
- **Tiempo:** 42 semanas + 12 meses de garantía + soporte
- **Beneficio:** Sistema completamente modernizado , seguro y preparado para los próximos 5-7 años, con un mantenimiento anual no considerado en la presente propuesta.

### 8.3 Modalidades de Pago

| Modalidad | Descripción | Beneficio |
|-----------|-------------|-----------|
| **Por Fases** | 30% adelanto + pagos por hitos | Control de avance |


### 8.4 Garantías Incluidas

- ✅ **12 meses** de garantía post-entrega en caso de correccion completa del sistema y 3 meses en caso de correcciones críticas
- ✅ **24h** de respuesta para bugs críticos
- ✅ **20 horas** de capacitación incluidas
- ✅ **Documentación técnica** completa
- ✅ **Código fuente** se entrega el código fuente con estándares modernos

---

## 9. Servicios Post-Venta y Mantenimiento

### 9.1 🔧 Mantenimiento Anual de Base de Datos

Ofrecemos un servicio opcional de mantenimiento anual especializado para garantizar el óptimo rendimiento y seguridad de su base de datos a largo plazo.

#### **Descripción del Servicio**
- **Costo Anual**: $500 USD por base de datos
- **Incluye**: Soporte técnico, optimización de rendimiento, actualizaciones de seguridad
- **Modalidad**: Servicio opcional post-implementación
- **Duración**: Contrato anual renovable

#### **Actividades Incluidas**
- ✅ **Optimización de consultas** - Análisis y mejora de queries lentos
- ✅ **Limpieza de datos obsoletos** - Eliminación de registros innecesarios y archivos temporales
- ✅ **Monitoreo de rendimiento** - Análisis mensual de performance y carga del sistema
- ✅ **Actualizaciones de seguridad** - Aplicación de parches y actualizaciones críticas
- ✅ **Análisis de crecimiento de datos** - Planificación de capacidad y escalabilidad
- ✅ **Ajustes de índices** - Optimización de índices para mejorar velocidad de consultas

#### **Beneficios del Mantenimiento**
- 🚀 **Rendimiento óptimo** - Sistema siempre funcionando a máxima velocidad
- 🔒 **Seguridad actualizada** - Protección contra vulnerabilidades emergentes
- 📊 **Visibilidad completa** - Reportes mensuales del estado del sistema
- 💾 **Datos protegidos** - Respaldos automáticos y verificados
- 📈 **Escalabilidad planificada** - Crecimiento controlado y predecible

*Este servicio está diseñado para mantener su inversión tecnológica en óptimas condiciones a largo plazo.*
