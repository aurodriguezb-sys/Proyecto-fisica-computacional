# Bitácora del desarrollo

> **Estado: borrador — falta información.** Registrar fecha y evidencia de las próximas sesiones y commits, y avances de los cuatro encargos.

## Integrantes

| Nombre completo | Carné | Aporte / responsabilidad |
|---|---|---|
| Fernando Rodríguez Blanco | C26548 | Implementación en Python |
| Orlando Ismael Benavides Renault | C11025 | Documentación, README, reporte y bitácora |
| Samuel Rojas Baldi | C36852 | Configuración YAML (`.yml`) y scripts |
| Eytan Sequeira Mora | C07458 | Implementación en C++ |

Los nombres, carnés y responsabilidades se registran según la información proporcionada por el grupo. Los cuatro carnés están registrados. Las responsabilidades son asignaciones de trabajo, no certificaciones de tareas terminadas. Los commits de la cuenta `aurodriguezb-sys` documentan cambios del repositorio, pero no se ha confirmado su correspondencia con un integrante.

## Distribución de responsabilidades

| Integrante | Encargo comunicado | Evidencia y estado |
|---|---|---|
| Fernando Rodríguez Blanco | Python | `heat.py` y dos PNG existen en el repositorio revisado; confirmar cambios posteriores y validación del programa original. |
| Orlando Ismael Benavides Renault | Archivos Markdown, README, reporte y bitácora | Documentación de avance preparada; revisión grupal y publicación pendientes. |
| Eytan Sequeira Mora | C++ | Código todavía no disponible en el repositorio revisado; estado de implementación pendiente de confirmar. |
| Samuel Rojas Baldi | YAML (`.yml`) y scripts | Responsabilidad asignada; falta conocer los archivos definitivos y verificar su integración. El script de validación de este paquete anterior es complementario y no se atribuye a Samuel. |

## 1. Historial verificable del repositorio

Fechas en hora de Costa Rica (UTC−6); se incluye UTC para reproducibilidad. Los commits prueban publicación de cambios, no las fechas exactas de todas las sesiones del equipo.

| Fecha CR | Fecha UTC | Autor GitHub | Evidencia | Actividad |
|---|---|---|---|---|
| 2026-10-31 17:52 | 2026-10-31 23:52 | `aurodriguezb-sys` | [`d0f4080`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/d0f4080b08f9f83703466aaa005ff95e1b9bb2a6) | Creación del README inicial; identificación del repositorio del curso. |
| 2026-11-09 22:39 | 2026-11-10 04:39 | `aurodriguezb-sys` | [`b9c78fe`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/b9c78fe0e526a7b547f26aa88c961998b368fd78) | Publicación de `heat.py` y dos gráficas de los escenarios. |

Al revisar `main` el 12 de noviembre de 2026, se encontraron dos commits, una rama y ninguna issue/PR en las consultas realizadas. No se encontró evidencia de C++ ni OpenMP. El nombre real y carné del autor no se deducen de su cuenta.

## 2. Registro de la preparación documental (no publicado)

**2026-11-12 — preparación del aporte de documentación.** Se revisó el enunciado y el código, se derivó FTCS, se verificó la condición de estabilidad, se identificaron las fronteras Dirichlet y se preparó una estructura documental. Se desarrolló y ejecutó un script independiente de validación con dos CSV. Este trabajo es nuevo y debe revisarse con el grupo antes de incorporarlo al repositorio. No equivale a un commit existente ni a una sesión presencial del equipo.

**2026-11-12 — actualización de integrantes y estado del proyecto.** Se registran los cuatro integrantes y tres carnés comunicados por el grupo. En ese momento, el carné de Eytan quedaba pendiente de confirmar (completado en la actualización posterior del mismo día). El grupo indica que el código C++ aún no está incorporado a GitHub; no se ha revisado su contenido ni su estado fuera del repositorio. Esta actualización corresponde a la documentación preparada, no a una sesión presencial ni a un commit publicado.

**2026-11-12 — actualización del carné faltante.** Se incorpora C07458, comunicado por el grupo, para Eytan Sequeira Mora. Los cuatro integrantes quedan identificados con su carné. Esta actualización documental no corresponde a un commit publicado.

**Actualización de la distribución de trabajo (comunicada por el grupo; sin fecha de reunión registrada).** Orlando se encarga de los `.md`; Fernando de Python; Eytan de C++; Samuel de los `.yml` y scripts. Se registra como acuerdo de responsabilidades, no como evidencia de implementación completada. No se atribuyen los commits existentes a una persona concreta sin confirmación.

## 3. Plantilla para futuras entradas

### AAAA-MM-DD — [Título de la sesión]

- Participantes: [nombres]
- Objetivo: [qué se intentó resolver]
- Actividades realizadas: [cambios concretos]
- Evidencia: [commit, archivo, comando, gráfico o datos]
- Resultados: [mediciones reales]
- Dificultades: [problema y diagnóstico]
- Decisiones: [qué se acordó y por qué]
- Próximo paso y responsable: [tarea]

## 4. Pendientes

Confirmar los avances efectivos y las sesiones fuera de Git; incorporar C++ al repositorio, verificar el paralelismo (OpenMP u otra técnica) y realizar mediciones; revisar resultados y documentación en conjunto. No inventar sesiones ni atribuir cambios a una persona sin evidencia.
