# Bitácora del desarrollo

**Proyecto:** Ecuación de calor en dos dimensiones  
**Curso:** FS-0432 Física Computacional — Universidad de Costa Rica  
**Profesor:** Marlon Brenes  
**Última actualización:** 20 de noviembre de 2026 (hora de Costa Rica, UTC−6)

> Documento de seguimiento en progreso. Se distinguen las actividades registradas en WhatsApp, los avances publicados en GitHub, los avances comunicados que todavía no se han verificado y las tareas pendientes. Los archivos de documentación adoptan nombres definitivos, mientras que los pendientes científicos se mantienen identificados.

## 1. Integrantes y distribución del trabajo

| Integrante | Carné | Responsabilidad | Estado al 16 de noviembre |
|---|---|---|---|
| Fernando Rodríguez Blanco | C26548 | Implementación en Python, simulaciones y gráficas | `heat.py` y dos gráficas publicados el 9 de noviembre. |
| Orlando Ismael Benavides Renault | C11025 | Archivos Markdown, README, reporte y bitácora | Publicó la documentación de avance el 12 de noviembre; actualización documental tras la publicación de C++. |
| Samuel Rojas Baldi | C36852 | Configuración YAML (`mkdocs.yml`), scripts, `mathjax.js` y apoyo en datos según los acuerdos | La PR #1 integró `mkdocs.yml`, MathJax, el script de validación y CSV complementarios. Los CSV originales de C++ publicados el 13 de noviembre forman parte del commit de Eytan. |
| Eytan Sequeira Mora | C07458 | Implementación en C++ | Publicó `heat.cpp`, `heat.exe`, `resultados_punto.csv` y `resultados_gradiente.csv` en el commit `50693a1` del 13 de noviembre. |

La optimización mediante paralelismo de memoria compartida es un requisito del proyecto. El código `heat.cpp` incorporado por Eytan contiene directivas OpenMP para actualizar los nodos y almacenar las instantáneas. Faltan mediciones verificables de aceleración y eficiencia.

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

**Publicación en GitHub y dificultad técnica:** Orlando utilizó HTTPS después de problemas con SSH. Windows rechazó los nombres de tres archivos `:Zone.Identifier` del repositorio. Se recuperaron los archivos originales y se publicó la documentación. En el segundo commit documental se eliminaron únicamente esos tres metadatos incompatibles, sin eliminar `heat.py`, las gráficas originales ni el README original. El historial de GitHub confirma los commits documentales que se detallan a continuación, seguidos de la entrega C++ de Eytan.

### 13 de noviembre de 2026 — Incorporación de C++ y de los archivos de resultados

**Evidencia en GitHub:** Eytan publicó en la rama `main` el commit [`50693a1`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/50693a1ccc0b00f6b8b4b81f16bafd447de81546), con fecha de autor del 13 de noviembre a las 16:16 en Costa Rica (22:16 UTC). El commit incorpora cuatro archivos:

- `heat.cpp`: solución FTCS para los escenarios `punto` y `gradiente`. Presenta dos bucles con `#pragma omp parallel for collapse(2)`: uno para actualizar los nodos interiores y otro para copiar las instantáneas.
- `heat.exe`: ejecutable de Windows incorporado al repositorio. No se ha verificado de forma independiente su compilación ni su ejecución.
- `resultados_punto.csv`: temperaturas de la placa para los cuatro tiempos de observación.
- `resultados_gradiente.csv`: temperaturas de la placa bajo fronteras térmicas diferentes.

**Revisión de datos:** en el nodo central, a los tiempos 0.01, 1, 5 y 15, el CSV de punto caliente muestra 26.5265, 25, 25 y 25; el de gradiente muestra 25.0336, 37.5, 37.5 y 37.5. Son consistentes, dentro del redondeo mostrado, con los resultados independientes previamente documentados; la comparación integral nodo a nodo se incorporó posteriormente mediante la PR #1, documentada en las entradas del 19–20 de noviembre.

**Resultado y pendientes:** C++ y las directivas OpenMP están publicados. Falta documentar una compilación reproducible, verificar resultados cruzados completos y medir tiempo, aceleración y eficiencia con diferentes números de hilos. En la fecha de esa entrega todavía no figuraban `mkdocs.yml` ni los scripts de validación; Samuel los incorporó posteriormente en la PR #1.

## 3. Historial verificable de GitHub

Repositorio: [Proyecto-fisica-computacional](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional). Rama `main`, revisada hasta el commit `50693a1` del 13 de noviembre de 2026.

| Fecha y hora CR | Fecha y hora UTC | Autor GitHub | Commit | Cambios |
|---|---|---|---|---|
| 31 oct., 17:52 | 31 oct., 23:52 | `aurodriguezb-sys` | [`d0f4080`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/d0f4080b08f9f83703466aaa005ff95e1b9bb2a6) | Creación del README inicial. |
| 9 nov., 22:39 | 10 nov., 04:39 | `aurodriguezb-sys` | [`b9c78fe`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/b9c78fe0e526a7b547f26aa88c961998b368fd78) | Código Python, dos gráficas y metadatos asociados. |
| 12 nov., 19:32 | 13 nov., 01:32 | `Benavides-Renault` | [`a4f2b23`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/a4f2b23fb867276bf897206014f84de17f23ee54) | README de avance, index y equipo. |
| 12 nov., 19:35 | 13 nov., 01:35 | `Benavides-Renault` | [`cc3a7e4`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/cc3a7e4b9374415a8ae09cdcc6e8b5df1fd2545b) | Siete Markdown restantes; eliminación de tres metadatos `:Zone.Identifier`. Mensaje registrado: `COMMIT_EDITMSG`. |
| 12 nov., 19:44 | 13 nov., 01:44 | `Benavides-Renault` | [`974dc1a`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/974dc1a9704da2e56f1a5f751d550319007d263f) | Actualización de reporte y bitácora con responsabilidades. |
| 12 nov., 19:52 | 13 nov., 01:52 | `Benavides-Renault` | [`e4f3323`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/e4f33239) | Actualización documental. |
| 12 nov., 19:53 | 13 nov., 01:53 | `Benavides-Renault` | [`22e9e86`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/22e9e86a) | Ampliación de bitácora: reuniones y acuerdos. |
| 12 nov., 19:55 | 13 nov., 01:55 | `Benavides-Renault` | [`ec0a24d`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/ec0a24d7) | Actualización de `bitacora.md`. |
| 13 nov., 16:16 | 13 nov., 22:16 | `eytanyared` | [`50693a1`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/50693a1ccc0b00f6b8b4b81f16bafd447de81546) | Publicación de `heat.cpp`, `heat.exe` y dos CSV. |

Los mensajes del grupo y el historial respaldan la atribución de Python a Fernando y la documentación a Orlando. Los commits indican publicación de cambios, no la duración del trabajo. La distribución inicial propuesta en cuatro commits documentales no coincide con el historial real: hasta el 12 de noviembre se registraron seis commits documentales de Orlando, incluidas correcciones posteriores.

## 4. Estado de los requisitos y próximos pasos

| Requisito / actividad | Estado | Próximo paso |
|---|---|---|
| Metodología numérica | FTCS implementado en Python y C++ | Comparar salida completa de ambas implementaciones bajo las mismas condiciones. |
| Python | Publicado | Validar el código original y acordar casos de prueba comunes. |
| C++ | `heat.cpp` y `heat.exe` publicados el 13 de noviembre por Eytan | Compilar en un entorno documentado, verificar el ejecutable y comparar con Python. |
| Condiciones iniciales y fronteras | Dos escenarios publicados | Confirmar si se requieren condiciones iniciales adicionales bajo fronteras iguales. |
| Mapas de colores | Dos gráficas publicadas | Revisar escalas de color y consistencia entre implementaciones. |
| MkDocs, MathJax y scripts | Pendientes de integración; los CSV publicados son del commit de Eytan | Incorporar los archivos de configuración de Samuel y comprobar la generación del sitio. |
| Paralelismo de memoria compartida | Directivas OpenMP presentes en `heat.cpp` | Medir tiempos de ejecución con 1, 2, 4 y más hilos según el equipo; calcular aceleración y eficiencia. |
| Reporte y bitácora | Markdown publicados; actualización tras el commit de Eytan | Añadir pruebas reproducibles de rendimiento y conclusiones finales cuando existan datos. |

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
- Historial público de [commits de `main`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commits/main/), incluido el commit [`50693a1`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/50693a1ccc0b00f6b8b4b81f16bafd447de81546).
- Enunciado del proyecto I del curso FS-0432 y documentación del equipo.


## 7. Seguimiento posterior — entrega de Samuel e integración al repositorio

### 19 de noviembre de 2026 — Entrega de documentación web y herramientas de validación

**Evidencia:** el commit [`de7cbd0`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/de7cbd0a7235d17ab5fe96f2af6c804c1ee2c5c6), con fecha de autor del 19 de noviembre a las 18:58 en Costa Rica (20 de noviembre, 00:58 UTC), fue publicado por la cuenta `Melrojas21`, correspondiente al aporte identificado en la pull request como trabajo de Samuel Rojas Baldi. Esta atribución se refiere a la entrega de GitHub y no constituye una medición del tiempo invertido.

**Elementos incorporados en la rama de trabajo:** `mkdocs.yml`, `requirements-docs.txt`, `docs/index.md`, `docs/resultados.md`, `docs/javascripts/mathjax.js`, `scripts/validar_calor.py`, imágenes en `docs/img/` y datos CSV en `resultados/` y `docs/datos/`. El script reproduce los dos escenarios FTCS, compara matrices con los CSV de C++, verifica la invariancia de un campo uniforme, compara el método escalar con el vectorizado y calcula convergencia frente a una solución analítica. Su opción `--original` permite contrastar con la función de `heat.py` sin ejecutar sus ventanas de gráficos.

### 20 de noviembre de 2026 — Aprobación e integración de la pull request #1

**Evidencia:** [pull request #1](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/pull/1), titulada *Agregar MkDocs, MathJax, script de validación y CSV (Samuel Rojas)*, fusionada a `main` mediante [`6f363399`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/6f3633991a747fd67dd0bcf6d6dedc773b5460db) el 20 de noviembre a las 18:13 de Costa Rica (21 de noviembre, 00:13 UTC). La fusión incorporó 30 archivos nuevos y no eliminó archivos existentes de la rama `main`.

**Revisión documental posterior:** los registros publicados en `resultados/pruebas.csv` muestran cinco pruebas aprobadas: equivalencia escalar/vectorizada para cada caso, conservación de campo uniforme y comparación de `heat.py` con la versión vectorizada para ambos escenarios. En `resultados/convergencia.csv`, el orden estimado tiende a 2 al refinar la malla con `dt` proporcional a `dx²`. La comparación C++/Python registra una diferencia máxima de 75 en el escenario de gradiente por el tratamiento de la esquina `(j=20,i=0)`; fuera de ese punto, las diferencias son compatibles con el redondeo de los CSV.

**Decisiones y alcance:** se conserva la redacción anterior de la bitácora como registro histórico. La integración de MkDocs y la validación automatizada cierra parte de los pendientes mencionados en entradas anteriores; no equivale a haber medido rendimiento de OpenMP. Quedan pendientes una decisión común sobre las esquinas de frontera, la ejecución documentada de `mkdocs build` en un entorno reproducible y la medición de tiempos, aceleración y eficiencia para diferentes hilos y mallas.

| Fecha y hora CR | Autor GitHub | Commit | Evidencia |
|---|---|---|---|
| 19 nov., 18:58 | `Melrojas21` | [`de7cbd0`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/de7cbd0a7235d17ab5fe96f2af6c804c1ee2c5c6) | Entrega del sitio MkDocs, script de validación, resultados y recursos. |
| 20 nov., 18:13 | `Benavides-Renault` (merge) | [`6f363399`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/6f3633991a747fd67dd0bcf6d6dedc773b5460db) | Integración de la pull request #1 en `main`. |


## 8. Consolidación de documentación — 20 de noviembre de 2026

**Objetivo:** establecer nombres definitivos de los Markdown y mantener una sola página de inicio y una sola de resultados, sin perder las contribuciones existentes.

**Trabajo documental preparado:** se integraron las páginas de documentación de Orlando con `docs/index.md` y `docs/resultados.md` de Samuel, se actualizaron los enlaces de navegación y se mantuvo la configuración técnica original de MkDocs. Se conservó el README inicial junto con la descripción ampliada del proyecto.

**Alcance verificable:** el merge `6f363399` incorporó la PR #1; la presente consolidación de nombres corresponde a una actualización documental posterior y no representa por sí misma mediciones de rendimiento ni cambios en `heat.py`, `heat.cpp`, `heat.exe` o los CSV. Su publicación en GitHub queda sujeta a que se aplique y confirme el commit correspondiente.

**Pendientes académicos:** pruebas reproducibles del rendimiento de OpenMP, tratamiento consistente de una esquina en el escenario de gradiente y revisión de las condiciones de frontera frente al requisito físico de aislamiento.
