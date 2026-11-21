# Explicación del método numérico

> **Estado al 20/11/2026:** fundamento FTCS, implementaciones y validación numérica documentados. Se identificó una diferencia de esquina en C++; siguen pendientes las mediciones de rendimiento de OpenMP.

## 1. Modelo físico

La temperatura $u(x,y,t)$ evoluciona en $[0,a]\times[0,b]$ según

$$\frac{\partial u}{\partial t}=c^2\left(\frac{\partial^2u}{\partial x^2}+\frac{\partial^2u}{\partial y^2}\right).$$

En `heat.py`, $\kappa=c^2$ es la difusividad térmica, con dimensiones longitud²/tiempo. No se especifican unidades físicas concretas en el programa. El calor difunde desde regiones más calientes hacia regiones más frías. El código usa una placa cuadrada de lado $L$ y no incluye fuentes volumétricas. Aunque el enunciado menciona aislamiento perfecto, los bordes del código son Dirichlet (temperatura fija), por lo que sí puede haber intercambio térmico a través de la frontera. Para una placa perfectamente aislada correspondería imponer flujo normal nulo (Neumann), no temperatura fija.

## 2. Discretización espacial y temporal

Se divide cada lado en $M$ intervalos y se almacenan $M+1$ nodos por dirección, incluyendo los bordes. $x_i=i\Delta x$, $y_j=j\Delta y$, $t_n=n\Delta t$, con $\Delta x=\Delta y=L/M$ en la implementación. `T[j,i]` representa el nodo $(x_i,y_j)$.

Usando diferencia hacia adelante en tiempo y centrada en espacio:

$$\frac{T^{n+1}_{j,i}-T^n_{j,i}}{\Delta t}=\kappa\left[\frac{T^n_{j,i+1}-2T^n_{j,i}+T^n_{j,i-1}}{\Delta x^2}+\frac{T^n_{j+1,i}-2T^n_{j,i}+T^n_{j-1,i}}{\Delta y^2}\right].$$

Despejando:

$$T^{n+1}_{j,i}=(1-2r_x-2r_y)T^n_{j,i}+r_x(T^n_{j,i-1}+T^n_{j,i+1})+r_y(T^n_{j-1,i}+T^n_{j+1,i}),$$

con $r_x=\kappa\Delta t/\Delta x^2$ y $r_y=\kappa\Delta t/\Delta y^2$.

El método FTCS es explícito: el valor nuevo depende solo del estado anterior. Es de primer orden temporal y segundo orden espacial para soluciones suficientemente suaves. La condición de estabilidad para difusividad positiva en una malla uniforme es $r_x+r_y\leq 1/2$. Se obtiene del factor de amplificación de Fourier $G=1-4r_x\sin^2(k_x\Delta x/2)-4r_y\sin^2(k_y\Delta y/2)$, al exigir $|G|\leq1$. Con $M=20$, $L=1$, $h=10^{-4}$, $\kappa=1$, los coeficientes son 0.04 y 0.04; su suma es 0.08.

## 3. Condiciones implementadas

**Punto caliente (`punto`):** se inicializa toda la matriz a 25, excepto el nodo central a 100. Los cuatro bordes se fijan a 25. El exceso térmico se dispersa y eventualmente sale a través de los bordes; la solución se aproxima a 25.

**Gradiente (`gradiente`):** el interior comienza a 25; borde izquierdo a 100, derecho a 0, superior e inferior a 25. Las esquinas quedan a 25 porque las filas se asignan después de las columnas. Aparece una distribución térmica no uniforme y se aproxima a un estado estacionario no constante. No es una placa aislada. No es un gradiente inicial lineal: son fronteras distintas con interior uniforme.

## 4. Algoritmo y memoria

1. Reservar `T` y asignar condiciones iniciales y de frontera.
2. Crear `Tp = T.copy()` y calcular los coeficientes.
3. Para cada paso, recorrer solamente los índices interiores `1..M-1`.
4. Calcular `Tp` leyendo exclusivamente `T`.
5. Copiar `Tp` a `T` y guardar instantáneas seleccionadas. La implementación C++ también utiliza esta copia completa; un intercambio de búferes sería una optimización futura.
6. Dibujar mapas mediante `contourf`.

El doble búfer evita modificar valores que aún se requieren en la misma iteración. El costo temporal es $O(N_t M^2)$ y el almacenamiento $O(M^2)$ para dos estados y cuatro instantáneas. En la configuración actual, son 54 150 000 actualizaciones interiores por caso. Dos matrices de 441 valores `float64` ocupan 7056 bytes; las cuatro instantáneas ocupan 14112 bytes, sin contar objetos y figuras.

## 5. Validación

Una solución analítica con fronteras cero es $u(x,y,t)=\sin(\pi x)\sin(\pi y)e^{-2\pi^2\kappa t}$ sobre el cuadrado unitario. Permite cuantificar error y convergencia. Se incluye una comprobación independiente en `scripts/validar_calor.py`; consultar [resultados](resultados.md). No estaba implementada en `heat.py` original.

## 6. Implementación C++ y paralelismo

El 13 de noviembre Eytan incorporó `heat.cpp`, `heat.exe` y los resultados CSV. La versión C++ utiliza matrices `std::vector<std::vector<double>>`, el mismo esquema explícito de cinco puntos y los mismos parámetros y tiempos observados en Python. Los nodos interiores se calculan con `#pragma omp parallel for collapse(2)`; otra región paralela guarda las instantáneas. El archivo `omp.h` y las directivas verifican el uso de la interfaz OpenMP en el código, pero no demuestran una mejora de tiempo sin mediciones comparativas. Los resultados y pendientes se detallan en [paralelismo](paralelismo.md) y [resultados](resultados.md).


## 7. Validación integrada en la pull request #1

La [integración de Samuel](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/pull/1) añadió `scripts/validar_calor.py`, que reproduce el esténcil FTCS de cinco puntos usando operaciones vectorizadas con NumPy y conserva las temperaturas impuestas en los bordes. El validador comprueba la condición de estabilidad antes de la evolución: con `L=1`, `M=20`, `h=0.0001` y `kappa=1`, se obtiene `r_x=r_y=0.04` y `r_x+r_y=0.08`, por debajo del límite `0.5`.

Se añadió un estudio con solución analítica `sin(pi*x)*sin(pi*y)*exp(-2*pi²*kappa*t)` y condiciones de Dirichlet homogéneas. Los errores máximos publicados para `M=10,20,40,80` son aproximadamente `3.18248e-3`, `7.90884e-4`, `1.97428e-4` y `4.93386e-5`, con orden observado cercano a 2 bajo refinamiento acoplado `dt≈0.2 dx²`. Estos resultados apoyan la consistencia del esquema para ese problema de prueba, sin convertirlo en una demostración de aislamiento térmico.

**Nota sobre la comparación C++/Python:** el validador localiza una diferencia en el nodo de esquina `(j=20,i=0)` del escenario `gradiente`: Python mantiene 25 mientras C++ guarda 100 por la secuencia de asignación de fronteras. Dado que el esténcil interior utiliza vecinos axiales y no esquinas, esa diferencia de esquina no cambia el cálculo de los nodos interiores en los escenarios actuales, pero sí la salida CSV y las medias que incluyen el borde. La discrepancia debe registrarse hasta que el grupo acuerde una convención uniforme para las esquinas.
