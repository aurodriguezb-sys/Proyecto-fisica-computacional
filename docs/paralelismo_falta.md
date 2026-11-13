# Paralelismo de memoria compartida — plan de implementación

> **Estado: borrador — falta información.** Confirmar técnica implementada, código, entorno, número de hilos y mediciones reales de aceleración.

**Estado:** propuesta, no código existente en el repositorio original.

## 1. Justificación

En un paso de FTCS, cada nodo interior de `Tp` se calcula únicamente a partir de `T`. Las escrituras no se superponen; los nodos pueden procesarse en paralelo. Los pasos temporales sí son dependientes y requieren que todas las actualizaciones terminen antes de intercambiar los búferes.

## 2. C++ y OpenMP

Usar `std::vector<double>` contiguo, índice `j*(M+1)+i`, dos matrices y fronteras copiadas en ambas. Paralelizar las filas interiores con OpenMP (`#pragma omp parallel for schedule(static)`), manteniendo el índice de columna en el bucle interno para accesos contiguos. La barrera implícita al final del bucle precede al intercambio `T.swap(Tp)`. No usar `nowait` sin sincronización equivalente. Se puede evaluar una región paralela persistente para reducir overhead, usando barreras y un solo hilo para intercambiar. No introducir una copia por nodo ni una matriz completa por hilo.

## 3. Pseudocódigo

```cpp
// Esquema ilustrativo, no programa compilable completo
for (int n = 0; n < pasos; ++n) {
    #pragma omp parallel for schedule(static)
    for (int j = 1; j < M; ++j) {
        for (int i = 1; i < M; ++i) {
            // Tp[j,i] = FTCS(T, j, i, rx, ry);
        }
    } // barrera implícita
    T.swap(Tp);
}
```

Compilación prevista con GCC: `g++ -O3 -std=c++17 -fopenmp heat.cpp -o heat`. El archivo y la interfaz todavía deben implementarse. Medir cálculo sin gráficas ni escritura de archivos, con mismos parámetros y precisión.

## 4. Protocolo de rendimiento

Para cada malla (por ejemplo 128, 256, 512, 1024 intervalos), definir pasos y `dt` estables, fijar igual trabajo entre configuraciones, registrar CPU, núcleos, RAM, SO, compilador y flags. Probar 1, 2, 4, 8 hilos o hasta los disponibles, calentar y repetir al menos cinco veces. Reportar mediana de segundos, dispersión, $S_p=T_1/T_p$ y $E_p=S_p/p$. Comparar primero con la versión C++ de un hilo y, aparte, con Python; no atribuir toda diferencia entre lenguajes al paralelismo. Verificar error máximo frente a referencia antes de medir. No prometer aceleración: el tamaño, overhead y ancho de banda pueden limitarla.

| M | Hilos | Mediana (s) | Aceleración | Eficiencia | Error vs referencia |
|---:|---:|---:|---:|---:|---:|
| [M] | [p] | [medir] | [calcular] | [calcular] | [medir] |
