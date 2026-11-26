# Referencia del código

> **Estado al 20/11/2026:** interfaces Python, C++ y script de Samuel documentados. Están disponibles pruebas numéricas, datos comparativos y el validador.

Fuentes: [heat.py](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/blob/main/heat.py) y [heat.cpp](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/blob/main/heat.cpp). La incorporación de C++ corresponde al commit [`50693a1`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/50693a1ccc0b00f6b8b4b81f16bafd447de81546).

## `heat_ftcs_2D(Th, Tc, Tm, kappa, L, M, h, t_end, initial='punto', T_hot=100.0)`

| Parámetro | Significado |
|---|---|
| `Th`, `Tc` | Temperatura del borde caliente/frío en `gradiente` |
| `Tm` | Temperatura base y de bordes restantes |
| `kappa` | Difusividad térmica |
| `L` | Lado de la placa cuadrada |
| `M` | Número de intervalos por eje |
| `h` | Paso temporal |
| `t_end` | Tiempo final solicitado |
| `initial` | `punto` o `gradiente` |
| `T_hot` | Temperatura del nodo central, por defecto 100 |

**Retorno:** `T_res`, arreglo NumPy de forma `(M+1, M+1, 4)`, con índices espaciales `[j,i]` e índice temporal `k`. Los tiempos son fijos: 0.01, 1, 5, 15. `its=round(t_end/h)`; se guardan estados cuando el índice temporal coincide con `round(tiempo/h)`, aunque se pueden cambiar en el programa para estudiar otros instantes.

**Dependencias:** NumPy; Matplotlib para gráficas fuera de la función. En `punto`, la función usa las coordenadas globales `x`, `y`, no las calcula internamente. La importación de `heat.py` ejecuta ambos casos.

## Arreglos

| Objeto | Uso |
|---|---|
| `T` | Estado anterior y fronteras |
| `Tp` | Estado nuevo; conserva bordes |
| `T_res` | Instantáneas |
| `x,y,X,Y` | Coordenadas y malla de visualización |

## Código complementario propuesto

`../scripts/validar_calor.py`: `inicializar(M, caso)` prepara los escenarios; `evolucionar(T, kappa, dx, dy, dt, pasos)` ejecuta FTCS vectorizado con verificación de estabilidad y fronteras fijas; `main()` genera CSV y ejecuta pruebas. Es una herramienta independiente de validación, no un reemplazo de `heat.py`.

## Función C++ `heat_ftcs_2D`

```cpp
std::vector<std::vector<std::vector<double>>> heat_ftcs_2D(
    double Th, double Tc, double Tm, double kappa, double L,
    int M, double h, double t_end, const std::string& initial,
    const std::vector<double>& x, std::vector<double>& y,
    double T_hot = 100.0);
```

| Parámetro | Significado y tipo |
|---|---|
| `Th`, `Tc`, `Tm` | Temperaturas de frontera y de referencia; `double`. |
| `kappa` | Difusividad térmica; `double`. |
| `L` | Lado de la placa cuadrada; `double`. |
| `M` | Intervalos espaciales por eje; `int`. |
| `h`, `t_end` | Incremento temporal y tiempo final solicitado; `double`. |
| `initial` | Escenario `punto` o `gradiente`; referencia constante a cadena. |
| `x`, `y` | Coordenadas de la malla; referencias a vectores de `double`. El código no modifica `y`, aunque su parámetro no está declarado `const`. |
| `T_hot` | Temperatura inicial del punto central; `double`, valor por defecto 100. |

**Retorno:** vector tridimensional `T_res[j][i][k]` de dimensiones `(M+1) × (M+1) × 4`, con cuatro instantáneas para los tiempos 0.01, 1, 5 y 15. Las matrices `T` y `Tp` se representan con vectores anidados. El método utiliza diferencias finitas FTCS y dos regiones paralelas OpenMP, una para actualizar los nodos interiores y otra para almacenar estados.

## Programa C++ `main()` y archivos generados

El programa establece los parámetros `Th=100`, `Tc=0`, `Tm=25`, `kappa=1`, `L=1`, `M=20`, `h=0.0001` y `t_end=15`, genera coordenadas uniformes y ejecuta ambos casos. Imprime en consola la temperatura central para cuatro instantes y guarda:

- `resultados_punto.csv`: columnas `Tiempo, j, i, Temperatura`.
- `resultados_gradiente.csv`: las mismas columnas para el segundo escenario.

Cada CSV tiene cuatro bloques de 441 nodos, uno por instante, además de la fila de cabecera. `heat.exe` es el ejecutable incluido en GitHub.

## Comparación

Las dos implementaciones usan la misma fórmula FTCS y los mismos parámetros nominales. En C++ se copia la matriz completa mediante `T = Tp` en cada paso; en Python se utiliza `T[:, :] = Tp[:, :]`. La comparación automatizada nodo a nodo ya fue incorporada con `scripts/validar_calor.py` en la PR #1 y documenta una diferencia localizada en la esquina `(j=20,i=0)` del caso gradiente.


## Actualización de interfaces y archivos — integración del 20/11/2026

El archivo [`scripts/validar_calor.py`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/blob/main/scripts/validar_calor.py) ya existe en `main`, incorporado por la [pull request #1](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/pull/1). Este apartado actualiza el estado documental de la referencia sin sustituir las especificaciones anteriores de `heat.py` y `heat.cpp`.

| Función / recurso | Entrada principal | Retorno o propósito |
|---|---|---|
| `inicializar(M, caso, ...)` | Intervalos, tipo de escenario y parámetros térmicos | Matriz NumPy inicial `(M+1,M+1)` |
| `verificar_estabilidad(kappa, dx, dy, dt)` | Difusividad y pasos | Suma `r_x+r_y`; lanza `ValueError` si excede `0.5` |
| `paso_ftcs(T, rx, ry)` | Matriz y coeficientes | Matriz nueva con bordes fijos |
| `evolucionar(T, kappa, dx, dy, dt, pasos, guardar_en=())` | Estado y parámetros temporales | Matriz final y diccionario de instantáneas |
| `simular_escenario(caso)` | `punto` o `gradiente` | Arreglo `(21,21,4)` para el caso actual |
| `cargar_heat_py()` | Código original `heat.py` | Función extraída por AST sin ejecutar sus gráficas |
| `exportar_matrices(ruta, T_res)` | Ruta y arreglo de resultados | CSV con columnas `Tiempo, j, i, Temperatura` |
| `leer_csv_cpp(ruta)` | Ruta a CSV de C++ | Arreglo `(21,21,4)` |
| `convergencia(...)` | Mallas, tiempo y factor temporal | Filas con error máximo y orden observado |

El script acepta `--original` para ejecutar las comparaciones contra `heat.py` y `--sin-figuras` para omitir la producción de imágenes. Escribe salidas en `resultados/`, replica los CSV publicados para la web en `docs/datos/` y guarda figuras en `docs/img/`. La página [`docs/resultados.md`](resultados.md) contiene el inventario y los enlaces para consultar esos recursos.

