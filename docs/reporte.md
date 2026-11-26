# Reporte de avance: solución numérica de la ecuación de calor en dos dimensiones

**Universidad de Costa Rica — FS-0432 Física Computacional**  
**Profesor:** Marlon Brenes 

## Integrantes y aportes

| Nombre completo | Carné | Aporte / responsabilidad |
|---|---|---|
| Fernando Rodríguez Blanco | C26548 | Implementación en Python, deploy del repositorio |
| Orlando Ismael Benavides Renault | C11025 | Documentación, README, reporte y bitácora |
| Samuel Rojas Baldi | C36852 | Configuración YAML (`.yml`), scripts y recursos de documentación web |
| Eytan Sequeira Mora | C07458 | Implementación C++ y publicación de ejecutable y CSV |

## Resumen

Se estudia computacionalmente la difusión térmica en una placa bidimensional mediante el método FTCS. El repositorio incluye una implementación en Python, un escenario de punto caliente central y otro de fronteras caliente/fría, y visualizaciones a cuatro tiempos distintos. Se verifica analíticamente que los parámetros satisfacen la condición de estabilidad. Como aporte complementario de documentación se desarrolló un script independiente que reproduce los casos y valida convergencia contra una solución analítica, obteniendo orden cercano a dos al acoplar el refinamiento espacial y temporal. El 13 de noviembre Eytan incorporó `heat.cpp`, `heat.exe` y los dos CSV de resultados; el código C++ contiene paralelismo OpenMP.
## 1. Introducción y objetivos

La ecuación de calor describe el transporte difusivo de energía térmica. El objetivo general es resolverla sobre un dominio bidimensional, explorar la dependencia temporal respecto a las condiciones iniciales y de frontera y comparar las implementaciones computacionales. Los objetivos específicos son derivar FTCS, implementar Python y C++, visualizar mapas de temperatura, verificar estabilidad y exactitud.

## 2. Fundamento y metodología

El modelo es $u_t=\kappa(u_{xx}+u_{yy})$, con $\kappa=c^2$ en la notación del enunciado. Se considera una placa conductora con longitud $L$, que para el caso de este proyecto se le asignó un valor de 1. El espacio se divide en 20 intervalos por lado y el tiempo en pasos de 0.0001; $\kappa=1$. Cada nuevo estado se calcula con el stencil de cinco puntos del [método numérico](explanation.md), usando un estado anterior y otro nuevo para no alterar dependencias. Los coeficientes son $r_x=r_y=0.04$, y su suma 0.08 cumple el límite 0.5 para garantizar la estabilidad del método. El algoritmo almacena 4 instantáneas a 0.01, 1, 5 y 15. En el primer caso el interior y los bordes se inicializan a 25, salvo el centro a 100. En el segundo el interior está a 25 y los bordes izquierdo/derecho a 100/0, con filas extremas a 25.

## 3. Implementación y recursos

`heat.py` contiene `heat_ftcs_2D`, NumPy para matrices y Matplotlib para visualizar. El repositorio incluye dos gráficas PNG. Se realizan 150 000 pasos por caso y 361 actualizaciones interiores por paso. Se usa memoria proporcional al número de nodos, manteniendo dos estados y cuatro instantáneas.

El 13 de noviembre, el commit [`50693a1`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/50693a1ccc0b00f6b8b4b81f16bafd447de81546) incorporó `heat.cpp`, `heat.exe`, `resultados_punto.csv` y `resultados_gradiente.csv`. C++ usa `std::vector<std::vector<double>>`, reproduce los dos casos y paraleliza tanto el cálculo interior como el almacenamiento de instantáneas mediante directivas `#pragma omp parallel for collapse(2)`. Se copia `Tp` sobre `T` después de cada paso. El código permite implementar el paralelismo de memoria compartida a la función `heat_ftcs_2D`. Consultar [referencia](reference.md), [tutorial](tutorials.md) y [paralelismo](paralelismo.md).

## 4. Resultados y discusión

La reproducción independiente documentada en el avance previo muestra que la temperatura central del punto caliente baja desde prácticamente el instante inicial y se aproxima a 25°; el caso con fronteras diferentes converge a un estado estacionario no uniforme, con centro cercano a 37.5°. La prueba de convergencia con una solución seno-seno muestra errores máximos de 3.18248e-3 (M=10) y 4.93386e-5 (M=80); los órdenes estimados son cercanos a 2. Esas pruebas corresponden a un script complementario anterior y no a una ejecución completa del código original.

Los dos CSV publicados por Eytan registran, en el nodo central y los tiempos 0.01, 1, 5 y 15, las series 26.5265, 25, 25, 25 (`punto`) y 25.0336, 37.5, 37.5, 37.5 (`gradiente`). Los resultados son compatibles con la reproducción independiente dentro del redondeo presentado. Véanse [resultados y validación](resultados.md). Conviene usar una escala de colores fija y muestrear más temprano el punto caliente.

## 5. Conclusiones de avance

FTCS permite estudiar la dinámica térmica con una discretización explícita sencilla y estable para los parámetros actuales. Las fronteras determinan el estado estacionario y deben distinguirse de las condiciones iniciales. La evidencia disponible cubre Python, C++, dos CSV y visualización; las comprobaciones adicionales refuerzan la metodología, con una comparación cruzada ya publicada en la PR #1 que identifica una diferencia de frontera localizada. OpenMP está presente en el código y permite optimizar la implementación del código.

## Referencias y reproducibilidad

1. Marlon Brenes, *Temas para proyectos finales*, FS-0432, sección I, p. 1, documento `Proyectos_I_2026_FS_0432.pdf`.
2. [Repositorio del proyecto, snapshot b9c78fe](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/tree/b9c78fe0e526a7b547f26aa88c961998b368fd78).
3. [Código Python original](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/blob/b9c78fe0e526a7b547f26aa88c961998b368fd78/heat.py) y [commit C++ de Eytan](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/50693a1ccc0b00f6b8b4b81f16bafd447de81546).
4. [Resultados y datos CSV](resultados.md), distinguiendo los archivos publicados por Eytan de las comprobaciones complementarias documentadas previamente.
