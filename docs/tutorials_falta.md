# Tutorial de uso

> **Estado: borrador — falta información.** Añadir comandos reales de compilación y ejecución de C++, scripts y configuración YAML definitivos, y comprobar el sitio.

## 1. Obtener e instalar

```bash
git clone https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional.git
cd Proyecto-fisica-computacional
python -m pip install numpy matplotlib
python heat.py
```

El repositorio original no contiene un archivo de dependencias ni una interfaz de línea de comandos. Se necesita un entorno gráfico para ver `plt.show()`; cerrar la primera ventana permite avanzar a la segunda. No se requiere C++ para este avance.

## 2. Parámetros del experimento original

En `heat.py`, la sección de parámetros fija `Th=100`, `Tc=0`, `Tm=25`, `kappa=1`, `L=1`, `M=20`, `h=0.0001`, `t_end=15`. Las coordenadas se construyen con `np.linspace` y `np.meshgrid`. Los tiempos de salida son `[0.01, 1, 5, 15]`. Si se cambia `M` o `L`, las coordenadas globales y la condición de estabilidad deben mantenerse coherentes. Si se cambia `h` o `t_end`, revisar los tiempos de guardado dentro y fuera de la función.

## 3. Visualización

Cada escenario genera una figura de cuatro mapas de colores (`contourf`, 20 niveles, mapa `hot`). Los PNG ya presentes en el repositorio son [punto caliente](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/blob/main/grafica_punto_caliente_central.png) y [gradiente](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/blob/main/grafica_gradiente.png). El código no tiene `savefig`; para guardar, añadir `fig1.savefig(...)` o `fig2.savefig(...)` antes de `show`.

## 4. Comprobaciones complementarias

Tras integrar el script complementario del paquete completo anterior en la raíz (no incluido en esta entrega de docs):

```bash
python -m pip install numpy
python scripts/validar_calor.py
```

El script escribe `resultados/resumen_ftcs.csv` y `resultados/convergencia.csv`. Reproduce los escenarios con una versión independiente vectorizada, compara contra un bucle escalar de la fórmula por 100 pasos y verifica un campo constante. No importa ni modifica el `heat.py` original. Véase [resultados](resultados_falta.md).

## 5. C++ y OpenMP (pendiente)

No existe un ejecutable C++ en el commit revisado. El comando de compilación y el formato de entrada/salida se añadirán cuando se integre la implementación. Consultar [plan de paralelismo](paralelismo_falta.md).

## 6. Página de documentación (opcional)

El paquete completo anterior contiene una propuesta de `mkdocs.yml`; Samuel está a cargo de la configuración definitiva. La propuesta sirve para convertir los Markdown en un sitio navegable:

```bash
python -m pip install mkdocs pymdown-extensions
mkdocs serve
```

Abrir la dirección local indicada por MkDocs. `mkdocs build` genera el sitio en `site/`. Las fórmulas usan MathJax cargado desde CDN, por lo que requieren conexión para renderizarse. Esta entrega solo incluye archivos Markdown; Samuel se encargará de configurar los recursos del sitio. No se ha publicado un sitio remoto.
