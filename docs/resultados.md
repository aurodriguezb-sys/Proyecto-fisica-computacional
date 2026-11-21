# Datos, gráficas y CSV

Esta página reúne los archivos de datos del proyecto y las salidas del script de validación `scripts/validar_calor.py` (aporte de Samuel Rojas). El análisis físico detallado está en [Resultados y validación](resultados_falta.md).

## Cómo regenerar los datos

Desde la raíz del repositorio:

```bash
python -m pip install numpy matplotlib
python scripts/validar_calor.py             # unos segundos
python scripts/validar_calor.py --original  # además ejecuta heat_ftcs_2D de heat.py (≈1–2 min)
```

El script no modifica `heat.py`, `heat.cpp` ni los CSV de C++. Escribe sus salidas en `resultados/`, copia los CSV a `docs/datos/` y las figuras a `docs/img/` para que este sitio las publique. Matplotlib es opcional: sin él solo se omiten las figuras.

Qué hace:

1. Reproduce los dos escenarios de `heat.py` (`M = 20`, `h = 1e-4`, `t_end = 15`, tiempos 0.01, 1, 5 y 15) con una versión vectorizada de la misma fórmula FTCS y verifica la estabilidad antes de iterar.
2. Exporta las matrices con el mismo formato que los CSV de C++ (`Tiempo, j, i, Temperatura`).
3. Compara nodo a nodo esas matrices con `resultados_punto.csv` y `resultados_gradiente.csv` de `heat.cpp`.
4. Comprueba la versión vectorizada contra un bucle escalar (100 pasos) y que un campo uniforme permanezca constante. Con `--original` también compara contra la función `heat_ftcs_2D` del propio `heat.py`.
5. Mide la convergencia contra la solución analítica $u = \sin(\pi x)\sin(\pi y)\,e^{-2\pi^2\kappa t}$.

## Archivos CSV

| Archivo | Origen | Contenido |
|---|---|---|
| [resultados_punto.csv](datos/resultados_punto.csv) | `heat.cpp` (Eytan) | Punto caliente central, 4 instantes × 441 nodos |
| [resultados_gradiente.csv](datos/resultados_gradiente.csv) | `heat.cpp` (Eytan) | Borde caliente y borde frío, 4 instantes × 441 nodos |
| [python_punto.csv](datos/python_punto.csv) | `validar_calor.py` | Punto caliente, versión vectorizada, mismo formato que C++ |
| [python_gradiente.csv](datos/python_gradiente.csv) | `validar_calor.py` | Gradiente, versión vectorizada, mismo formato que C++ |
| [heat_py_punto.csv](datos/heat_py_punto.csv) | `heat.py` vía `--original` | Punto caliente calculado con la función original de Python |
| [heat_py_gradiente.csv](datos/heat_py_gradiente.csv) | `heat.py` vía `--original` | Gradiente calculado con la función original de Python |
| [resumen_ftcs.csv](datos/resumen_ftcs.csv) | `validar_calor.py` | Temperatura central, máximo y media nodal por instante |
| [comparacion_cpp.csv](datos/comparacion_cpp.csv) | `validar_calor.py` | Diferencias Python − C++ por escenario e instante |
| [pruebas.csv](datos/pruebas.csv) | `validar_calor.py` | Resultado de las pruebas automáticas |
| [convergencia.csv](datos/convergencia.csv) | `validar_calor.py` | Error máximo y orden estimado por malla |

## Resumen en el nodo central

| Tiempo | Punto: centro | Punto: máximo | Gradiente: centro | Gradiente: media nodal |
|---:|---:|---:|---:|---:|
| 0.01 | 26.526536 | 26.526536 | 25.033626 | 30.657058 |
| 1 | 25.000000 | 25.000000 | 37.500000 | 37.386621 |
| 5 | 25.000000 | 25.000000 | 37.500000 | 37.386621 |
| 15 | 25.000000 | 25.000000 | 37.500000 | 37.386621 |

La media nodal incluye los nodos de frontera; no es una integral de energía ponderada.

## Pruebas automáticas

| Prueba | Error máximo | Tolerancia | Resultado |
|---|---:|---:|---|
| Vectorizado vs. bucle escalar, punto (100 pasos) | 0 | 1e-12 | Aprobada |
| Vectorizado vs. bucle escalar, gradiente (100 pasos) | 0 | 1e-12 | Aprobada |
| Campo uniforme constante (1000 pasos) | 0 | 1e-12 | Aprobada |
| `heat.py` original vs. vectorizado, punto (150 000 pasos) | 0 | 1e-9 | Aprobada |
| `heat.py` original vs. vectorizado, gradiente (150 000 pasos) | 0 | 1e-9 | Aprobada |

La versión vectorizada reproduce exactamente las matrices de `heat.py`, de modo que `python_*.csv` y `heat_py_*.csv` contienen los mismos valores.

## Comparación nodo a nodo con C++

Diferencia absoluta máxima entre la versión Python y los CSV de `heat.cpp`:

| Tiempo | Punto | Gradiente (sin la esquina `j = 20`, `i = 0`) |
|---:|---:|---:|
| 0.01 | 4.9e-5 | 5.0e-5 |
| 1 | 2.0e-9 | 5.0e-5 |
| 5 | 2.1e-12 | 5.0e-5 |
| 15 | 2.1e-12 | 5.0e-5 |

Las diferencias del orden de $10^{-5}$ se explican por el redondeo a 6 cifras significativas con que `heat.cpp` escribe los CSV. **Hallazgo:** en el escenario de gradiente hay una sola diferencia de 75 en la esquina inferior izquierda (`j = 20`, `i = 0`): `heat.py` la deja en `Tm = 25` y `heat.cpp` en `Th = 100`, porque C++ asigna los cuatro bordes dentro del mismo bucle y el orden de las asignaciones cambia el valor de esa esquina. La esquina no interviene en el esténcil de cinco puntos, así que no afecta a ningún nodo interior; solo cambia el valor guardado (y la media nodal). Conviene que el grupo acuerde qué valor usar en las esquinas.

## Convergencia con la solución analítica

Cuadrado unitario, fronteras cero, $\kappa = 1$, $u_0 = \sin(\pi x)\sin(\pi y)$, error máximo nodal a $t = 0.1$ con $\Delta t \approx 0.2\,\Delta x^2$ (ajustado para llegar exactamente al tiempo final). El orden se estima como $\log_2(E_M/E_{2M})$.

| M | Error máximo | Orden estimado |
|---:|---:|---:|
| 10 | 3.18248e-3 | — |
| 20 | 7.90884e-4 | 2.0086 |
| 40 | 1.97428e-4 | 2.0021 |
| 80 | 4.93386e-5 | 2.0005 |

![Convergencia del error máximo](img/convergencia.png)

El orden tiende a 2, como se espera de FTCS cuando $\Delta t \propto \Delta x^2$.

## Mapas de temperatura

Figuras generadas por `validar_calor.py` con una escala de colores fija por escenario, para que los cuatro instantes se puedan comparar entre sí:

![Punto caliente central](img/mapa_punto.png)

![Borde caliente y borde frío](img/mapa_gradiente.png)

Gráficas originales de `heat.py` publicadas por el grupo (escala de colores independiente en cada panel):

![Punto caliente central, heat.py](img/grafica_punto_caliente_central.png)

![Gradiente, heat.py](img/grafica_gradiente.png)
