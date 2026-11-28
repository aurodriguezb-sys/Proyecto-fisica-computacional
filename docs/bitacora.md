# Bitácora del desarrollo

**Proyecto:** Ecuación de calor en dos dimensiones  
**Curso:** FS-0432 Física Computacional — Universidad de Costa Rica  
**Profesor:** Marlon Brenes  
**Última actualización:** 26 de noviembre de 2026

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

Las entradas son una síntesis del chat del equipo, complementada con el historial de GitHub.

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

Se acordó iniciar una reunión por Zoom para acordar la división y organización de las tareas del proyecto.

**Actividades y acuerdos registrados:**

- Fernando creó el repositorio del proyecto e invitó a los demás integrantes como colaboradores. El primer commit de GitHub, `d0f4080`, corresponde a la creación del README inicial.
- Se planteó confirmar la distribución de trabajo el lunes siguiente.
- Se acordó que cada integrante realizaría commits y pushes de su aporte.
- Se indicó que la documentación debía explicar las funciones del código, sus parámetros, tipos de datos y valores de retorno, siguiendo el estilo de la Tarea 2.

**Resultado:** se estableció el repositorio compartido y se definió una referencia para el formato de documentación.

### 2 de noviembre de 2026 — Definición del dominio físico

Fernando comunicó que, según lo indicado por el profesor, se podían escoger dimensiones iguales, $a=b=L$, y que el equipo debía elegir varias condiciones iniciales para estudiar la evolución temporal.

**Decisión:** trabajar con un dominio cuadrado y considerar distintos escenarios térmicos. Esto coincide con el código Python posteriormente publicado.

### 9 de noviembre de 2026 — Elección de FTCS y primera implementación

Se propuso el método FTCS explícito (Forward Time, Centered Space) para resolver la ecuación diferencial y se ofreció a implementarlo en Python. Eytan se ofreció a desarrollar C++ e indicó, a partir de una consulta al profesor, que el reporte debía integrarse en la documentación explicando qué se hizo y por qué. Orlando se ofreció a elaborar el README y el reporte.

El mismo día Fernando subió el código Python y las gráficas de dos escenarios. El commit `b9c78fe` confirma la incorporación de:

- `heat.py`: método FTCS explícito, malla cuadrada de 21 × 21 nodos, dos matrices de temperatura y cuatro instantes de salida.
- `grafica_punto_caliente_central.png`: evolución de una temperatura localizada en el centro, con bordes a temperatura fija.
- `grafica_gradiente.png`: evolución con borde izquierdo caliente, borde derecho frío y bordes superior e inferior a temperatura media.

### 12 de noviembre de 2026 — Seguimiento, responsabilidades y documentación


- Orlando revisó el repositorio para preparar los Markdown, solicitó los nombres y carnés del equipo y consultó quién se encargaría de `mkdocs.yml`, los scripts de validación y los CSV. Informó que gran parte de su documentación estaba preparada.
- Fernando confirmó que en ese momento solo estaba publicado Python y comunicó que Eytan tenía dificultades de conexión con la fibra óptica.
- Eytan confirmó que el código C++ ya estaba desarrollado, aunque todavía no podía subirlo. Orlando le solicitó compartirlo por WhatsApp para avanzar con la documentación; la exportación no contiene el código ni una respuesta que confirme su envío.
- Fernando solicitó a Samuel hacerse cargo de MkDocs. Orlando pidió también `mathjax.js` y los CSV. Samuel aceptó ambas solicitudes.

**Trabajo documental:** se preparó una explicación de FTCS, estabilidad numérica, condiciones iniciales y de frontera, referencias de la implementación Python, tutoriales, resultados, propuesta de paralelismo, reporte y bitácora. Se prepararon comprobaciones numéricas complementarias con una implementación independiente; estas no se consideran validación conjunta del código original ni trabajo terminado de Samuel.

**Publicación en GitHub y dificultad técnica:** Orlando utilizó HTTPS después de problemas con SSH. Windows rechazó los nombres de tres archivos `:Zone.Identifier` del repositorio. Se recuperaron los archivos originales y se publicó la documentación. En el segundo commit documental se eliminaron únicamente esos tres metadatos incompatibles, sin eliminar `heat.py`, las gráficas originales ni el README original. El historial de GitHub confirma los commits documentales que se detallan a continuación, seguidos de la entrega C++ de Eytan.

### 13 de noviembre de 2026 — Incorporación de C++ y de los archivos de resultados

**Evidencia en GitHub:** Eytan publicó en la rama `main` el commit [`50693a1`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/50693a1ccc0b00f6b8b4b81f16bafd447de81546). El commit incorpora cuatro archivos:

- `heat.cpp`: solución FTCS para los escenarios `punto` y `gradiente`. Presenta dos bucles con `#pragma omp parallel for collapse(2)`: uno para actualizar los nodos interiores y otro para copiar las instantáneas.
- `heat.exe`: ejecutable de Windows incorporado al repositorio. No se ha verificado de forma independiente su compilación ni su ejecución.
- `resultados_punto.csv`: temperaturas de la placa para los cuatro tiempos de observación.
- `resultados_gradiente.csv`: temperaturas de la placa bajo fronteras térmicas diferentes.

**Revisión de datos:** en el nodo central, a los tiempos 0.01, 1, 5 y 15, el CSV de punto caliente muestra 26.5265, 25, 25 y 25; el de gradiente muestra 25.0336, 37.5, 37.5 y 37.5. Son consistentes, dentro del redondeo mostrado, con los resultados independientes previamente documentados; la comparación integral nodo a nodo se incorporó posteriormente mediante la PR #1, documentada en las entradas del 19–20 de noviembre.

## 3. Estado de los requisitos y próximos pasos

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

## 4. Seguimiento posterior — entrega de Samuel e integración al repositorio

### 19 de noviembre de 2026 — Entrega de documentación web y herramientas de validación

**Evidencia:** el commit [`de7cbd0`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/de7cbd0a7235d17ab5fe96f2af6c804c1ee2c5c6), fue publicado por Samuel.

**Elementos incorporados en la rama de trabajo:** `mkdocs.yml`, `requirements-docs.txt`, `docs/index.md`, `docs/resultados.md`, `docs/javascripts/mathjax.js`, `scripts/validar_calor.py`, imágenes en `docs/img/` y datos CSV en `resultados/` y `docs/datos/`. El script reproduce los dos escenarios FTCS, compara matrices con los CSV de C++, verifica la invariancia de un campo uniforme, compara el método escalar con el vectorizado y calcula convergencia frente a una solución analítica. Su opción `--original` permite contrastar con la función de `heat.py` sin ejecutar sus ventanas de gráficos.

### 20 de noviembre de 2026 — Aprobación e integración de la pull request #1

**Evidencia:** [pull request #1](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/pull/1), titulada *Agregar MkDocs, MathJax, script de validación y CSV (Samuel Rojas)*, fusionada a `main` mediante [`6f363399`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/6f3633991a747fd67dd0bcf6d6dedc773b5460db). La fusión incorporó 30 archivos nuevos y no eliminó archivos existentes de la rama `main`.

**Revisión documental posterior:** los registros publicados en `resultados/pruebas.csv` muestran cinco pruebas aprobadas: equivalencia escalar/vectorizada para cada caso, conservación de campo uniforme y comparación de `heat.py` con la versión vectorizada para ambos escenarios. En `resultados/convergencia.csv`, el orden estimado tiende a 2 al refinar la malla con `dt` proporcional a `dx²`. La comparación C++/Python registra una diferencia máxima de 75 en el escenario de gradiente por el tratamiento de la esquina `(j=20,i=0)`; fuera de ese punto, las diferencias son compatibles con el redondeo de los CSV.

## 5. Poblicación del repositorio por medio de GitHub Pages

### 21 de noviembre de 2026

Se realizó el deploy del repositorio por medio de GitHub Pages, en el cual se presenta el proyecto, y se puede accesar por medio del siguiente link:
https://aurodriguezb-sys.github.io/Proyecto-fisica-computacional/

### 26 de noviembre de 2026

Se agregó una gráfica adicional a la sección de resultados, en `resultados.md`. Además, se pulieron diversos aspectos de formato y redacción en los diferentes archivos del repositorio. 
