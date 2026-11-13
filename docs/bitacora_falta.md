from pathlib import Path
p=Path('/mnt/data/bitacora_falta.md')
s="""# Bitácora del desarrollo

**Proyecto:** Ecuación de calor en dos dimensiones  
**Curso:** FS-0432 Física Computacional — Universidad de Costa Rica  
**Profesor:** Marlon Brenes  
**Última actualización:** 12 de noviembre de 2026 (hora de Costa Rica, UTC−6)

> Documento de seguimiento en progreso. Se distinguen las actividades registradas en WhatsApp, los avances publicados en GitHub, los avances comunicados que todavía no se han verificado y las tareas pendientes. Se mantiene el sufijo `_falta` mientras no se complete el proyecto.

## 1. Integrantes y distribución del trabajo

| Integrante | Carné | Responsabilidad | Estado al 12 de noviembre |
|---|---|---|---|
| Fernando Rodríguez Blanco | C26548 | Implementación en Python, simulaciones y gráficas | `heat.py` y dos gráficas publicados el 9 de noviembre. |
| Orlando Ismael Benavides Renault | C11025 | Archivos Markdown, README, reporte y bitácora | Diez archivos Markdown publicados; documentación en revisión y actualización. |
| Samuel Rojas Baldi | C36852 | Configuración YAML (`mkdocs.yml`), scripts, `mathjax.js` y archivos `.csv` | Aceptó encargarse de MkDocs, MathJax y CSV el 12 de noviembre; scripts asignados según la distribución comunicada por el grupo. Archivos definitivos e integración por verificar. |
| Eytan Sequeira Mora | C07458 | Implementación en C++ | Comunicó el 12 de noviembre que el código está desarrollado, pero no pudo publicarlo por dificultades de conexión. Código y pruebas pendientes de revisión. |

La optimización mediante paralelismo de memoria compartida es un requisito del proyecto. La conversación no confirma quién será su responsable definitivo ni que ya se haya implementado.

## 2. Registro cronológico del proceso

Las fechas y horas se expresan en hora local de Costa Rica. Las entradas son una síntesis del chat del equipo, complementada con el historial de GitHub. No constituyen transcripciones literales ni actas de asistencia.

### 1 y 11 de octubre de 2026 — Organización del canal de comunicación

- El 1 de octubre se creó el grupo de WhatsApp para coordinar el proyecto.
- El 11 de octubre Orlando se incorporó mediante el enlace de invitación.
- No se registran en estas fechas avances de implementación.

### 26 de octubre de 2026 — Planificación inicial

**Objetivo:** acordar cómo dividir el proyecto y organizar la colaboración.

Orlando consultó cuándo comenzar y cómo repartir las tareas. Fernando compartió los requisitos y propuso cuatro bloques: código Python, código C++, condiciones iniciales y visualización con optimización de memoria compartida, y documentación del repositorio.

Orlando planteó utilizar commits individuales para que quedaran registradas las contribuciones, compartir un único repositorio y coordinar una llamada por Zoom o Discord. Fernando respaldó la propuesta de incorporar las partes de cada integrante al repositorio común.

**Resultado:** se estableció una propuesta de organización, todavía sin una asignación definitiva de todas las tareas.

### 30 de octubre de 2026 — Coordinación de la primera reunión

Orlando propuso realizar una reunión virtual durante el fin de semana o la semana siguiente y creó una encuesta para elegir entre sábado y domingo. Fernando indicó su disponibilidad.

**Resultado:** quedó encaminada la coordinación de la reunión del día siguiente.

### 31 de octubre de 2026 — Reunión, repositorio y formato de documentación

Se acordó iniciar una reunión por Zoom a las 18:30. El enlace se compartió a las 18:34. Orlando informó que perdió temporalmente la conexión a Internet; cuando volvió, a las 18:49, los compañeros indicaron que la reunión estaba terminando. No se dispone de un acta completa ni de una lista de asistentes confirmada.

**Actividades y acuerdos registrados:**

- Fernando creó el repositorio del proyecto e invitó a Orlando como colaborador. El primer commit de GitHub, `d0f4080`, corresponde a la creación del README inicial.
- Se planteó confirmar la distribución de trabajo el lunes siguiente.
- Se acordó que cada integrante realizaría commits y pushes de su aporte.
- Se indicó que la documentación debía explicar las funciones del código, sus parámetros, tipos de datos y valores de retorno, siguiendo el estilo de la Tarea 2.
- Orlando compartió una referencia de su Tarea 2 y posteriormente un prototipo de sitio sobre la ecuación de calor, generado con ayuda de IA, para consultar si el formato era apropiado. Fernando compartió su propia documentación de la Tarea 2 y consideró que el prototipo seguía el formato esperado.

**Resultado:** se estableció el repositorio compartido y se definió una referencia para el formato de documentación. El prototipo externo era una propuesta, no el sitio oficial terminado del grupo.

### 2 de noviembre de 2026 — Definición del dominio físico

Fernando comunicó que, según lo indicado por el profesor, se podían escoger dimensiones iguales, $a=b=L$, y que el equipo debía elegir varias condiciones iniciales para estudiar la evolución temporal.

**Decisión:** trabajar con un dominio cuadrado y considerar distintos escenarios térmicos. Esto coincide con el código Python posteriormente publicado.

### 4 de noviembre de 2026 — Exploración del método numérico

Fernando propuso utilizar el método de Gauss-Seidel estudiado en clase.

**Resultado:** fue una alternativa considerada. El chat no registra una implementación de Gauss-Seidel ni una comparación experimental de métodos. La implementación posterior adoptó FTCS explícito.

### 9 de noviembre de 2026 — Elección de FTCS y primera implementación

A las 15:36 Fernando propuso el método FTCS explícito (Forward Time, Centered Space) para resolver la ecuación diferencial y se ofreció a implementarlo en Python. Eytan se ofreció a desarrollar C++ e indicó, a partir de una consulta al profesor, que el reporte debía integrarse en la documentación explicando qué se hizo y por qué. Orlando se ofreció a elaborar el README y el reporte; Fernando estuvo de acuerdo.

Se discutió como objetivo de trabajo intentar terminar el proyecto para el fin de semana; no constituye una fecha oficial de entrega.

**Avance publicado:** a las 22:41 Fernando informó que había subido el código Python y las gráficas de dos escenarios. El commit `b9c78fe` confirma la incorporación de:

- `heat.py`: método FTCS explícito, malla cuadrada de 21 × 21 nodos, dos matrices de temperatura y cuatro instantes de salida.
- `grafica_punto_caliente_central.png`: evolución de una temperatura localizada en el centro, con bordes a temperatura fija.
- `grafica_gradiente.png`: evolución con borde izquierdo caliente, borde derecho frío y bordes superior e inferior a temperatura media.

**Nota física:** el segundo escenario cambia principalmente las condiciones de frontera, aunque en el chat se describió como una segunda condición inicial. Ambos escenarios deben diferenciarse al redactar el reporte.

**Próximos pasos:** revisión de Python, elaboración de C++ y documentación del método.

### 10 de noviembre de 2026 — Acceso al repositorio

Eytan solicitó el enlace HTTPS del repositorio y Fernando lo compartió.

**Resultado:** se facilitó el acceso al repositorio común para continuar la implementación. No se registran nuevos resultados de simulación en esa fecha.

### 12 de noviembre de 2026 — Seguimiento, responsabilidades y documentación

**Revisión y coordinación (17:37–18:38):**

- Orlando revisó el repositorio para preparar los Markdown, solicitó los nombres y carnés del equipo y consultó quién se encargaría de `mkdocs.yml`, los scripts de validación y los CSV. Informó que gran parte de su documentación estaba preparada.
- Fernando confirmó que en ese momento solo estaba publicado Python y comunicó que Eytan tenía dificultades de conexión con la fibra óptica.
- Eytan confirmó que el código C++ ya estaba desarrollado, aunque todavía no podía subirlo. Orlando le solicitó compartirlo por WhatsApp para avanzar con la documentación; la exportación no contiene el código ni una respuesta que confirme su envío.
- Fernando solicitó a Samuel hacerse cargo de MkDocs. Orlando pidió también `mathjax.js` y los CSV. Samuel aceptó ambas solicitudes a las 18:37–18:38 y compartió su nombre y carné.
- Se completó la identificación de los cuatro integrantes, incluido el carné de Eytan (C07458).
- Orlando consultó si debía publicar en una rama separada. Fernando indicó a las 18:28 que podía subir directamente a `main` y corregir posteriormente mediante nuevos commits.

**Trabajo documental:** se preparó una explicación de FTCS, estabilidad numérica, condiciones iniciales y de frontera, referencias de la implementación Python, tutoriales, resultados, propuesta de paralelismo, reporte y bitácora. Se prepararon comprobaciones numéricas complementarias con una implementación independiente; estas no se consideran validación conjunta del código original ni trabajo terminado de Samuel.

**Publicación en GitHub y dificultad técnica:** Orlando utilizó HTTPS después de problemas con SSH. Windows rechazó los nombres de tres archivos `:Zone.Identifier` del repositorio. Se recuperaron los archivos originales y se publicó la documentación. En el segundo commit documental se eliminaron únicamente esos tres metadatos incompatibles, sin eliminar `heat.py`, las gráficas originales ni el README original. El historial de GitHub confirma los tres commits documentales que se detallan a continuación.

## 3. Historial verificable de GitHub

Repositorio: [Proyecto-fisica-computacional](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional). Rama `main`, consultada el 12 de noviembre de 2026.

| Fecha y hora CR | Fecha y hora UTC | Autor GitHub | Commit | Cambios |
|---|---|---|---|---|
| 31 oct., 17:52 | 31 oct., 23:52 | `aurodriguezb-sys` | [`d0f4080`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/d0f4080b08f9f83703466aaa005ff95e1b9bb2a6) | Creación del README inicial. |
| 9 nov., 22:39 | 10 nov., 04:39 | `aurodriguezb-sys` | [`b9c78fe`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/b9c78fe0e526a7b547f26aa88c961998b368fd78) | Código Python, dos gráficas y metadatos asociados. |
| 12 nov., 19:32 | 13 nov., 01:32 | `Benavides-Renault` | [`a4f2b23`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/a4f2b23fb867276bf897206014f84de17f23ee54) | README de avance, index y equipo. |
| 12 nov., 19:35 | 13 nov., 01:35 | `Benavides-Renault` | [`cc3a7e4`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/cc3a7e4b9374415a8ae09cdcc6e8b5df1fd2545b) | Siete Markdown restantes; eliminación de tres metadatos `:Zone.Identifier`. Mensaje registrado: `COMMIT_EDITMSG`. |
| 12 nov., 19:44 | 13 nov., 01:44 | `Benavides-Renault` | [`974dc1a`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/974dc1a9704da2e56f1a5f751d550319007d263f) | Actualización de reporte y bitácora con responsabilidades. |

Los mensajes del grupo y el historial respaldan la atribución de Python a Fernando y la documentación a Orlando. Los commits indican publicación de cambios, no la duración del trabajo. La distribución inicial propuesta en cuatro commits documentales no coincide con el historial real: se registran tres commits de Orlando hasta esta revisión.

## 4. Estado de los requisitos y próximos pasos

| Requisito / actividad | Estado | Próximo paso |
|---|---|---|
| Metodología numérica | FTCS implementado en Python | Revisar estabilidad y documentar el algoritmo de C++ cuando esté disponible. |
| Python | Publicado | Validar el código original y acordar casos de prueba comunes. |
| C++ | Desarrollado según Eytan; no publicado en la revisión | Incorporar el código, compilar, ejecutar y comparar con Python. |
| Condiciones iniciales y fronteras | Dos escenarios publicados | Confirmar si se requieren condiciones iniciales adicionales bajo fronteras iguales. |
| Mapas de colores | Dos gráficas publicadas | Revisar escalas de color y consistencia entre implementaciones. |
| MkDocs, MathJax, scripts y CSV | Responsabilidad de Samuel; integración pendiente de verificar | Incorporar archivos, configurar navegación y comprobar la generación del sitio y datos. |
| Paralelismo de memoria compartida | Sin implementación verificada | Acordar responsable, implementar y medir tiempos, aceleración y eficiencia. |
| Reporte y bitácora | Markdown publicados, en actualización | Incorporar evidencia de C++, rendimiento y conclusiones finales. |

## 5. Plantilla para futuras entradas

### AAAA-MM-DD — Título de la sesión

- Participantes:
- Objetivo:
- Actividades realizadas:
- Evidencia (commit, archivo, datos o gráfico):
- Resultados y mediciones:
- Dificultades:
- Decisiones:
- Próximo paso y responsable:

## 6. Fuentes del registro

- Exportación del grupo de WhatsApp, mensajes del 1 de octubre al 12 de noviembre de 2026. Se sintetiza el contenido pertinente; no se reproducen teléfonos, correos, enlaces privados de reunión ni mensajes de voz o imágenes omitidos.
- Historial público de [commits de `main`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commits/main/).
- Enunciado del proyecto I del curso FS-0432 y documentación del equipo.

"""
p.write_text(s,encoding='utf-8')
print(p, p.stat().st_size, len(s.splitlines()))
