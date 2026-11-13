# Resultados y validación

> **Estado: borrador — falta información.** Añadir resultados de C++, comparación Python/C++, pruebas del programa original y mediciones de rendimiento.

## 1. Evidencia original

El repositorio contiene dos figuras PNG y `heat.py`, que genera cuatro instantáneas por escenario. Véanse [punto caliente](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/blob/main/grafica_punto_caliente_central.png) y [gradiente](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/blob/main/grafica_gradiente.png). Se verifica su presencia en Git; la interpretación siguiente se basa en el código y en la reproducción numérica independiente, no en una inspección visual de los PNG originales.

## 2. Resultados complementarios (ejecutados el 12/11/2026)

El script `scripts/validar_calor.py` implementa la misma fórmula FTCS y las mismas fronteras, con operaciones vectorizadas NumPy. No se ejecutó el `heat.py` completo original ni se midió su rendimiento. Se comparó la fórmula vectorizada con un bucle escalar equivalente durante 100 pasos (tolerancia absoluta 1e-12), y se verificó que un campo uniforme permanece constante. Ambas pruebas pasaron.

| Tiempo | Punto: centro | Gradiente: centro | Gradiente: media nodal |
|---:|---:|---:|---:|
| 0.01 | 26.526536 | 25.033626 | 30.657058 |
| 1 | 25.000000 | 37.500000 | 37.386621 |
| 5 | 25.000000 | 37.500000 | 37.386621 |
| 15 | 25.000000 | 37.500000 | 37.386621 |

Los valores están redondeados. La media nodal incluye bordes; no es una integral de energía con ponderación espacial. En el punto caliente, el máximo inicial de 100 desciende rápidamente por la difusión y las fronteras a 25. En el gradiente, la temperatura se aproxima a un estado estacionario no uniforme, sostenido por temperaturas fijas. Los valores extremos de la matriz permanecen 0 y 100 por las fronteras. La configuración tiene un único nodo caliente, cuya extensión física cambia al refinar la malla; para comparar refinamientos del caso real conviene una mancha de ancho físico fijo.

## 3. Convergencia con solución analítica

Sobre el cuadrado unitario con fronteras cero y $\kappa=1$, se empleó $u_0=\sin(\pi x)\sin(\pi y)$ y $u(t)=u_0e^{-2\pi^2t}$. Se calculó el error máximo nodal a $t=0.1$, con $\Delta t=0.2\Delta x^2$ (ajustado para coincidir con el tiempo final). El orden estimado es $\log_2(E_M/E_{2M})$.

| M | Error máximo | Orden estimado |
|---:|---:|---:|
| 10 | 3.18248e-3 | — |
| 20 | 7.90884e-4 | 2.0086 |
| 40 | 1.97428e-4 | 2.0021 |
| 80 | 4.93386e-5 | 2.0005 |

Se observa orden cercano a dos con el refinamiento acoplado $\Delta t\propto\Delta x^2$, consistente con FTCS. Esto verifica el script complementario en ese caso suave, no constituye una prueba exhaustiva del programa original ni de la futura implementación C++.

## 4. Pendientes experimentales

Comparar la salida real de Python y C++ con tolerancia, generar mapas con una escala fija por escenario, incluir tiempos iniciales y más instantes tempranos, documentar unidades y probar fronteras Neumann si se desea aislamiento. Medir tiempos, aceleración y eficiencia de OpenMP con mallas suficientemente grandes. No existen mediciones de rendimiento verificadas en el repositorio original.
