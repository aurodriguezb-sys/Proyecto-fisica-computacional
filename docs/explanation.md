# Explicación del método numérico

> **Estado: completo para el alcance del método FTCS y la implementación Python revisada.** No documenta una implementación C++ todavía no disponible.

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
5. Copiar `Tp` a `T` y guardar instantáneas seleccionadas.
6. Dibujar mapas mediante `contourf`.

El doble búfer evita modificar valores que aún se requieren en la misma iteración. El costo temporal es $O(N_t M^2)$ y el almacenamiento $O(M^2)$ para dos estados y cuatro instantáneas. En la configuración actual, son 54 150 000 actualizaciones interiores por caso. Dos matrices de 441 valores `float64` ocupan 7056 bytes; las cuatro instantáneas ocupan 14112 bytes, sin contar objetos y figuras.

## 5. Validación

Una solución analítica con fronteras cero es $u(x,y,t)=\sin(\pi x)\sin(\pi y)e^{-2\pi^2\kappa t}$ sobre el cuadrado unitario. Permite cuantificar error y convergencia. Se incluye una comprobación independiente en `scripts/validar_calor.py`; consultar [resultados](resultados_falta.md). No estaba implementada en `heat.py` original.
