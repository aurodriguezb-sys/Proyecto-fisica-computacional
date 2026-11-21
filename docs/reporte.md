# Reporte de avance: solución numérica de la ecuación de calor en dos dimensiones

> **Estado al 20/11/2026:** integrados Python, C++, validación de Samuel y resultados. Restan las mediciones reproducibles de rendimiento, el acuerdo sobre la esquina discrepante y la confirmación de la fecha oficial de presentación.

**Universidad de Costa Rica — FS-0432 Física Computacional**  
**Profesor:** Marlon Brenes (autor del enunciado)  
**Fecha de revisión:** 20 de noviembre de 2026  
**Estado:** reporte documental consolidado; la evaluación de aceleración OpenMP permanece pendiente.

## Integrantes y aportes

| Nombre completo | Carné | Aporte / responsabilidad |
|---|---|---|
| Fernando Rodríguez Blanco | C26548 | Implementación en Python |
| Orlando Ismael Benavides Renault | C11025 | Documentación, README, reporte y bitácora |
| Samuel Rojas Baldi | C36852 | Configuración YAML (`.yml`), scripts y recursos de documentación web |
| Eytan Sequeira Mora | C07458 | Implementación C++ y publicación de ejecutable y CSV |

Los nombres, carnés y responsabilidades se registran según la información proporcionada por el grupo. Los cuatro carnés están registrados. Las responsabilidades son asignaciones de trabajo, no certificaciones de tareas terminadas. Los commits de la cuenta `aurodriguezb-sys` documentan cambios del repositorio, pero no se ha confirmado su correspondencia con un integrante.

## Resumen

Se estudia computacionalmente la difusión térmica en una placa bidimensional mediante diferencias finitas explícitas (FTCS). El avance del repositorio incluye una implementación en Python, un escenario de punto caliente central y otro de fronteras caliente/fría, y visualizaciones a cuatro tiempos. Se verifica analíticamente que los parámetros satisfacen la condición de estabilidad. Como aporte complementario de documentación se desarrolló un script independiente que reproduce los casos y valida convergencia contra una solución analítica, obteniendo orden cercano a dos al acoplar el refinamiento espacial y temporal. El 13 de noviembre Eytan incorporó `heat.cpp`, `heat.exe` y los dos CSV de resultados; el código C++ contiene paralelismo OpenMP. La exactitud cruzada completa y la aceleración todavía no se han medido de manera reproducible.

## 1. Introducción y objetivos

La ecuación de calor describe el transporte difusivo de energía térmica. El objetivo general es resolverla sobre un dominio bidimensional, explorar la dependencia temporal respecto a las condiciones iniciales y de frontera y comparar las implementaciones computacionales. Los objetivos específicos son derivar FTCS, implementar Python y C++, visualizar mapas de temperatura, verificar estabilidad y exactitud, y evaluar aceleración por paralelismo de memoria compartida. El enunciado solicita también uso apropiado de memoria, optimización, documentación, colaboración Git y principios de programación orientada a objetos cuando sean pertinentes.

## 2. Fundamento y metodología

El modelo es $u_t=\kappa(u_{xx}+u_{yy})$, con $\kappa=c^2$ en la notación del enunciado. Se considera un cuadrado unitario con condiciones Dirichlet. El espacio se divide en 20 intervalos por lado y el tiempo en pasos de 0.0001; $\kappa=1$. Cada nuevo estado se calcula con el stencil de cinco puntos del [método numérico](explanation.md), usando un estado anterior y otro nuevo para no alterar dependencias. Los coeficientes son $r_x=r_y=0.04$, y su suma 0.08 cumple el límite 0.5. El algoritmo almacena 4 instantáneas a 0.01, 1, 5 y 15. En el primer caso el interior y los bordes se inicializan a 25, salvo el centro a 100. En el segundo el interior está a 25 y los bordes izquierdo/derecho a 100/0, con filas extremas a 25. No se debe interpretar esta frontera como aislamiento perfecto.

## 3. Implementación y recursos

`heat.py` contiene `heat_ftcs_2D`, NumPy para matrices y Matplotlib para visualizar. El repositorio incluye dos gráficas PNG. Se realizan 150 000 pasos por caso y 361 actualizaciones interiores por paso. Se usa memoria proporcional al número de nodos, manteniendo dos estados y cuatro instantáneas.

El 13 de noviembre, el commit [`50693a1`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/50693a1ccc0b00f6b8b4b81f16bafd447de81546) incorporó `heat.cpp`, `heat.exe`, `resultados_punto.csv` y `resultados_gradiente.csv`. C++ usa `std::vector<std::vector<double>>`, reproduce los dos casos y paraleliza tanto el cálculo interior como el almacenamiento de instantáneas mediante directivas `#pragma omp parallel for collapse(2)`. Se copia `Tp` sobre `T` después de cada paso. El código permite estudiar memoria compartida, pero el repositorio no contiene una serie reproducible de tiempos ni una demostración cuantitativa de aceleración. Se proponen validación de parámetros, reducción de copias y pruebas de eficiencia; no se presentan como mejoras ya implementadas. Consultar [referencia](reference.md), [tutorial](tutorials.md) y [paralelismo](paralelismo.md).

## 4. Resultados y discusión

La reproducción independiente documentada en el avance previo muestra que la temperatura central del punto caliente baja a 26.526536 en t=0.01 y se aproxima a 25; el caso con fronteras diferentes converge a un estado estacionario no uniforme, con centro cercano a 37.5. La prueba de convergencia con una solución seno-seno muestra errores máximos de 3.18248e-3 (M=10) y 4.93386e-5 (M=80); los órdenes estimados son cercanos a 2. Esas pruebas corresponden a un script complementario anterior y no a una ejecución completa del código original.

Los dos CSV publicados por Eytan registran, en el nodo central y los tiempos 0.01, 1, 5 y 15, las series 26.5265, 25, 25, 25 (`punto`) y 25.0336, 37.5, 37.5, 37.5 (`gradiente`). Los resultados son compatibles con la reproducción independiente dentro del redondeo presentado, pero no equivalen a una comparación automatizada de todas las matrices. Véanse [resultados y validación](resultados.md). Conviene usar una escala de colores fija y muestrear más temprano el punto caliente. No se dispone de mediciones de aceleración; no puede concluirse una ganancia de rendimiento.

## 5. Desarrollo del proyecto y trabajo futuro

La distribución de trabajo comunicada por el grupo asigna Python a Fernando, la documentación Markdown a Orlando, C++ a Eytan y YAML y scripts de documentación a Samuel. Los CSV presentes se publicaron junto con C++ en el commit de Eytan; esto distingue una entrega verificable de asignaciones previas relacionadas con datos.

El historial Git registra la creación del README el 31/10/2026, la publicación de Python y gráficas el 09/11/2026 y la incorporación de C++, el ejecutable y dos CSV el 13/11/2026 (hora de Costa Rica). La [bitácora](bitacora.md) enlaza los commits y distingue actividades reportadas de entregas verificables. La siguiente etapa es compilar el código en un entorno reproducible, comparar todas las salidas de Python y C++ y medir los tiempos con diferentes cantidades de hilos. El protocolo se encuentra en [paralelismo](paralelismo.md).

## 6. Conclusiones de avance

FTCS permite estudiar la dinámica térmica con una discretización explícita sencilla y estable para los parámetros actuales. Las fronteras determinan el estado estacionario y deben distinguirse de las condiciones iniciales. La evidencia disponible cubre Python, C++, dos CSV y visualización; las comprobaciones adicionales refuerzan la metodología, con una comparación cruzada ya publicada en la PR #1 que identifica una diferencia de frontera localizada. OpenMP está presente en el código y debe evaluarse experimentalmente. Para cerrar la evaluación de rendimiento se requiere medir aceleración y eficiencia, documentar el entorno y comprobar la construcción del sitio web ya incorporado, además de confirmar los requisitos de presentación.

## Referencias y reproducibilidad

1. Marlon Brenes, *Temas para proyectos finales*, FS-0432, sección I, p. 1, documento `Proyectos_I_2026_FS_0432.pdf` suministrado al grupo. El PDF indica presentación el 6-7-2026 (20 minutos); esta fecha es anterior a los commits revisados, por lo que debe confirmarse la fecha aplicable al grupo actual.
2. [Repositorio del proyecto, snapshot b9c78fe](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/tree/b9c78fe0e526a7b547f26aa88c961998b368fd78).
3. [Código Python original](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/blob/b9c78fe0e526a7b547f26aa88c961998b368fd78/heat.py) y [commit C++ de Eytan](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/50693a1ccc0b00f6b8b4b81f16bafd447de81546).
4. [Resultados y datos CSV](resultados.md), distinguiendo los archivos publicados por Eytan de las comprobaciones complementarias documentadas previamente.


## 7. Integración y validación complementaria — 20 de noviembre de 2026

El avance posterior al reporte se formaliza mediante la [pull request #1](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/pull/1), propuesta con el commit [`de7cbd0`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/de7cbd0a7235d17ab5fe96f2af6c804c1ee2c5c6) de Samuel Rojas e incorporada a `main` por Orlando en el [merge `6f363399`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/6f3633991a747fd67dd0bcf6d6dedc773b5460db). La entrega incluye la configuración de MkDocs, la portada y la página de resultados, MathJax, imágenes y datos CSV, además de `scripts/validar_calor.py`. El aporte mejora la reproducibilidad de la documentación y añade comprobaciones automatizadas sin modificar las implementaciones originales de Python y C++.

### 7.1. Verificaciones numéricas publicadas

En `resultados/pruebas.csv` se registran cinco pruebas satisfactorias: equivalencia entre FTCS escalar y vectorizado en los dos escenarios (100 pasos), conservación de temperatura uniforme (1000 pasos) y comparación del código Python original con el vectorizado para ambos escenarios (150 000 pasos). Los errores máximos informados son cero bajo las tolerancias respectivas de `1e-12` y `1e-9`. Son evidencias registradas por el script del repositorio; deben reproducirse en el equipo de entrega para documentar el entorno.

El archivo `resultados/convergencia.csv` registra errores máximos aproximadamente `3.18248e-3`, `7.90884e-4`, `1.97428e-4` y `4.93386e-5` para `M=10,20,40,80`. Los órdenes estimados en los refinamientos sucesivos son `2.0086`, `2.0021` y `2.0005`, compatibles con convergencia de segundo orden cuando `dt` decrece proporcionalmente a `dx²`.

### 7.2. Comparación de Python y C++

La comparación de las matrices publicadas, para cada instante, muestra diferencias del orden de `5e-5` o menores en el punto caliente, compatibles con la escritura redondeada de los CSV de C++. Para `gradiente`, la diferencia máxima total es **75** porque la esquina `(j=20,i=0)` tiene valor 25 en Python y 100 en C++. Este hallazgo se explica por el orden diferente en que ambos códigos asignan las condiciones de frontera. Los nodos interiores conservan concordancia numérica dentro del redondeo; los promedios nodales de C++ que incluyen la esquina no coinciden exactamente con los de Python.

### 7.3. Alcances y pendientes

La publicación de la página [`datos y gráficas`](resultados.md) permite consultar las pruebas, las curvas de convergencia y los mapas de temperatura del proyecto. Sin embargo, no existen en `main` mediciones verificadas de aceleración y eficiencia de OpenMP. Por ello, el reporte sigue siendo un avance: resta normalizar la convención en las esquinas si el grupo decide corregir C++, ejecutar y registrar el proceso de construcción del sitio, comparar tiempos entre configuraciones y discutir las condiciones de frontera fijas frente al aislamiento térmico exigido en el enunciado.
