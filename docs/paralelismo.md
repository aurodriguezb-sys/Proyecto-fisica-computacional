# Paralelismo de memoria compartida — implementación y evaluación pendiente

> **Estado: implementación disponible; evaluación pendiente.** Las directivas OpenMP están en `heat.cpp`. Faltan entorno de prueba, número de hilos y tiempos medidos para cuantificar aceleración y eficiencia.

**Estado:** Eytan incorporó `heat.cpp` y `heat.exe` el 13 de noviembre de 2026 (commit [`50693a1`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/50693a1ccc0b00f6b8b4b81f16bafd447de81546)). Se distingue a continuación la implementación efectiva de las optimizaciones sugeridas.

## 1. Justificación

En un paso de FTCS, cada nodo interior de `Tp` se calcula únicamente a partir de `T`. Las escrituras no se superponen; los nodos pueden procesarse en paralelo. Los pasos temporales sí son dependientes y requieren que todas las actualizaciones terminen antes de intercambiar los búferes.

## 2. Implementación publicada en C++ y OpenMP

El código `heat.cpp` utiliza `std::vector<std::vector<double>>` para las matrices `T` y `Tp`, así como para el almacenamiento tridimensional de instantáneas `T_res`. En cada paso temporal paraleliza los índices interiores `j` e `i` mediante `#pragma omp parallel for collapse(2) shared(T, Tp, rx, ry, M)`. Cada hilo escribe posiciones distintas de `Tp` y lee el estado anterior `T`, por lo que el esquema es compatible con la independencia espacial del método FTCS.

Al finalizar el bucle paralelo se dispone de una barrera implícita de OpenMP y se ejecuta `T = Tp`, que copia la matriz completa antes de continuar al siguiente paso. Para guardar una instantánea seleccionada se emplea otra directiva `#pragma omp parallel for collapse(2) shared(T_res, T, M, k)`; cada hilo escribe un elemento diferente. No se ha documentado todavía cuántos hilos se utilizaron ni el rendimiento alcanzado.

El código conserva los bordes asignados en las dos matrices y actualiza únicamente los nodos interiores. El paso temporal depende de la finalización del anterior: no se pueden paralelizar pasos temporales sucesivos sin cambiar el algoritmo.

## 3. Esquema de actualización observado

```cpp
// Extracto simplificado del procedimiento utilizado en heat.cpp.
for (int n = 1; n <= its; ++n) {
    #pragma omp parallel for collapse(2) shared(T, Tp, rx, ry, M)
    for (int j = 1; j < M; ++j) {
        for (int i = 1; i < M; ++i) {
            Tp[j][i] = T[j][i] + rx * (T[j][i+1] - 2*T[j][i] + T[j][i-1])
                                  + ry * (T[j+1][i] - 2*T[j][i] + T[j-1][i]);
        }
    }
    T = Tp;
    // Si corresponde, guardar instantánea en T_res.
}
```

El segundo bucle paralelo de almacenamiento no se reproduce aquí; permanece en el código fuente. Con GCC y soporte OpenMP, el comando de compilación previsto es `g++ -O3 -std=c++17 -fopenmp heat.cpp -o heat` en Linux, o `-o heat.exe` en Windows. Se debe comprobar la compilación y ejecución en el equipo utilizado. Con la malla original de 21 × 21 nodos, la creación frecuente de regiones paralelas puede costar más que el trabajo realizado.

## 4. Posibles optimizaciones adicionales

- Almacenar las matrices en un vector contiguo indexado mediante `j*(M+1)+i` para mejorar la localidad de memoria y reducir indirecciones.
- Evaluar el intercambio de búferes `T.swap(Tp)` en lugar de la copia `T = Tp`, manteniendo las condiciones de frontera correctas.
- Comparar `collapse(2)` con un paralelismo por filas y `schedule(static)`; evitar que la carga de trabajo sea menor que el costo de la región paralela.
- Evaluar una región paralela persistente que reduzca el costo de crear regiones en cada paso, respetando las barreras antes del intercambio.

Estas son propuestas; no se atribuyen a la versión de Eytan ni se reportan como cambios ya aplicados.

## 5. Protocolo de rendimiento

Para cada malla (por ejemplo 128, 256, 512, 1024 intervalos), definir pasos y `dt` estables, fijar igual trabajo entre configuraciones, registrar CPU, núcleos, RAM, SO, compilador y flags. Probar 1, 2, 4, 8 hilos o hasta los disponibles, calentar y repetir al menos cinco veces. Reportar mediana de segundos, dispersión, $S_p=T_1/T_p$ y $E_p=S_p/p$. Comparar primero C++ con 1 hilo contra C++ con varios hilos y, por separado, contra Python. Medir preferiblemente solo el cálculo, sin operaciones de escritura de CSV, y verificar antes el error máximo frente a una referencia. La presencia de OpenMP no permite afirmar aceleración: la malla, las copias, el overhead y el ancho de banda pueden limitarla.

| M | Hilos | Mediana (s) | Aceleración | Eficiencia | Error vs referencia |
|---:|---:|---:|---:|---:|---:|
| [M] | [p] | [medir] | [calcular] | [calcular] | [medir] |
