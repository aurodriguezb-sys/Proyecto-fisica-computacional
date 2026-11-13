# Referencia del código

> **Estado: borrador — falta información.** Documentar funciones, interfaces y archivos C++ y scripts de Samuel cuando estén disponibles.

Fuente: [heat.py original](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/blob/b9c78fe0e526a7b547f26aa88c961998b368fd78/heat.py).

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

**Retorno:** `T_res`, arreglo NumPy de forma `(M+1, M+1, 4)`, con índices espaciales `[j,i]` e índice temporal `k`. Los tiempos son fijos: 0.01, 1, 5, 15. `its=round(t_end/h)`; se guardan estados cuando el índice temporal coincide con `round(tiempo/h)`.

**Dependencias:** NumPy; Matplotlib para gráficas fuera de la función. En `punto`, la función usa las coordenadas globales `x`, `y`, no las calcula internamente. La importación de `heat.py` ejecuta ambos experimentos porque no tiene guardia `if __name__ == '__main__':`.

## Arreglos

| Objeto | Uso |
|---|---|
| `T` | Estado anterior y fronteras |
| `Tp` | Estado nuevo; conserva bordes |
| `T_res` | Instantáneas |
| `x,y,X,Y` | Coordenadas y malla de visualización |

## Limitaciones y mejoras propuestas

- Validar `M`, `L`, `h`, `kappa`, `initial` y estabilidad antes de iterar.
- Construir las coordenadas dentro de la función, recibir tiempos de salida y validar que sean alcanzables; si no, quedan instantáneas de ceros sin advertencia.
- Separar simulación de visualización y usar una guardia de ejecución para permitir importar funciones.
- Emplear intercambio de búferes en lugar de copiar toda la matriz cada paso; comparar resultados.
- Documentar unidades, tratamiento de esquinas y fronteras. Fijar escalas de color comparables para mostrar la evolución.
- Valorar clase de configuración o simulador si mejora modularidad; no afirmar que ya se usa OOP.

## Código complementario propuesto

`../scripts/validar_calor.py`: `inicializar(M, caso)` prepara los escenarios; `evolucionar(T, kappa, dx, dy, dt, pasos)` ejecuta FTCS vectorizado con verificación de estabilidad y fronteras fijas; `main()` genera CSV y ejecuta pruebas. Es una herramienta independiente de validación, no un reemplazo de `heat.py`.
