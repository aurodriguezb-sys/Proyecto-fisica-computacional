# Proyecto-fisica-computacional
Repositorio en el cual se desarrolla y expone la solución al proyecto del curso Física Computacional.

---

## Ecuación de calor en dos dimensiones

> **Estado al 20 de noviembre de 2026:** Python, C++/OpenMP, MkDocs y el validador están publicados. Las pruebas numéricas y los resultados de convergencia se encuentran en el repositorio. Continúan pendientes los ensayos de rendimiento de OpenMP y la revisión del tratamiento de las esquinas.

**Proyecto final de Física Computacional — FS-0432 | Universidad de Costa Rica**

Este proyecto estudia la evolución de la temperatura en una placa mediante la solución numérica de la ecuación de calor bidimensional. Se utiliza el método de diferencias finitas FTCS y se analizan dos escenarios térmicos mediante mapas de colores. La primera implementación se realizó en Python. Posteriormente, el 13 de noviembre de 2026, Eytan incorporó la versión C++ con directivas OpenMP, el ejecutable `heat.exe` y los archivos CSV de los dos escenarios. La presencia de paralelismo en el código está verificada; su aceleración todavía no se ha medido en un entorno documentado.

## Integrantes

| Nombre completo | Carné | Aporte / responsabilidad |
|---|---|---|
| Fernando Rodríguez Blanco | C26548 | Implementación en Python |
| Orlando Ismael Benavides Renault | C11025 | Documentación, README, reporte y bitácora |
| Samuel Rojas Baldi | C36852 | Configuración YAML (`.yml`), scripts y soporte de documentación web |
| Eytan Sequeira Mora | C07458 | Implementación en C++ y publicación de `heat.cpp`, `heat.exe` y dos CSV |

Los nombres, carnés y responsabilidades se registran según la información proporcionada por el grupo. Los cuatro carnés están registrados. Las responsabilidades son asignaciones de trabajo, no certificaciones de tareas terminadas. Los commits de la cuenta `aurodriguezb-sys` documentan cambios del repositorio, pero no se ha confirmado su correspondencia con un integrante.

**Profesor:** Marlon Brenes (autor del enunciado suministrado).

## Problema y objetivos

Resolver $\partial_t u=\kappa(\partial_{xx}u+\partial_{yy}u)$ en una región rectangular, estudiar el efecto de las condiciones iniciales y de frontera, visualizar la solución, implementar el método en Python y C++ y evaluar la aceleración en memoria compartida.

## Documentación

- [Inicio](docs/index.md)
- [Fundamento físico y método numérico](docs/explanation.md)
- [Tutorial de ejecución](docs/tutorials.md)
- [Referencia de código](docs/reference.md)
- [Bitácora del proyecto](docs/bitacora.md)
- [Resultados y validación](docs/resultados.md)
- [Paralelismo y optimización](docs/paralelismo.md)
- [Reporte académico](docs/reporte.md)

## Ejecutar

Desde la raíz del repositorio original, con Python y las dependencias instaladas:

```bash
python -m pip install numpy matplotlib
python heat.py
```

El programa Python muestra dos figuras de Matplotlib; cierre la primera para continuar. El programa original no guarda automáticamente los PNG. El repositorio también contiene `heat.cpp`, que se puede compilar con GCC y OpenMP:

```bash
g++ -O3 -std=c++17 -fopenmp heat.cpp -o heat
./heat
```

En Windows se puede usar `-o heat.exe` y ejecutar `heat.exe` o `.\heat.exe`, según la terminal. La ejecución C++ escribe `resultados_punto.csv` y `resultados_gradiente.csv` en el directorio de trabajo. El script de validación `scripts/validar_calor.py` ya forma parte del repositorio; consultar el [tutorial](docs/tutorials.md).

## Estado

| Hito | Avance |
|---|---|
| Método numérico y Python | Implementados |
| Condiciones iniciales distintas | Parcial: punto caliente e interior uniforme con fronteras asimétricas |
| Visualización temporal | Cuatro instantáneas por caso |
| C++ | `heat.cpp` y `heat.exe` publicados por Eytan el 13 de noviembre |
| Paralelismo | OpenMP presente en `heat.cpp`; falta medir aceleración y eficiencia |
| Documentación | Sitio MkDocs, MathJax, script de validación, datos y gráficas publicados en la PR #1 |

Fuente: [repositorio del grupo](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional), rama `main`, revisada hasta el merge [`6f363399`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/6f3633991a747fd67dd0bcf6d6dedc773b5460db), del 20 de noviembre de 2026 (Costa Rica). Revisar los datos personales antes de publicar.

## Integración de esta entrega

La consolidación documental unifica el README descriptivo y las páginas de documentación, sin alterar `heat.py`, `heat.cpp`, `heat.exe`, los CSV ni las gráficas. Los documentos utilizan nombres definitivos sin sufijos provisionales. Se conservan los aportes previos del equipo y se indican por separado los experimentos de rendimiento aún no realizados.


## Actualización de integración — 20 de noviembre de 2026

La [pull request #1](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/pull/1) incorporó el trabajo de Samuel Rojas Baldi al repositorio principal mediante el [merge `6f363399`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/6f3633991a747fd67dd0bcf6d6dedc773b5460db). Este registro complementa el estado de avance descrito arriba; las notas anteriores se conservan como evidencia del momento en que fueron redactadas.

| Recurso incorporado | Uso actual |
|---|---|
| `mkdocs.yml` y `requirements-docs.txt` | Configuración y dependencias del sitio MkDocs. |
| `docs/index.md` | Portada de Samuel y contenido documental de Orlando integrados en una sola página. |
| `docs/javascripts/mathjax.js` | Renderización de fórmulas mediante MathJax 3. |
| `scripts/validar_calor.py` | Simulación vectorizada, pruebas de consistencia, comparación con CSV C++ y convergencia. |
| `docs/resultados.md`, `docs/datos/`, `docs/img/` | Presentación de tablas, datos descargables y gráficos. |
| `resultados/` | Salidas numéricas generadas y publicadas para reproducibilidad. |

**Comandos actuales desde la raíz del repositorio:**

```bash
python -m pip install numpy matplotlib -r requirements-docs.txt
python scripts/validar_calor.py
mkdocs serve
```

Para contrastar también con la función original de `heat.py` puede utilizarse `python scripts/validar_calor.py --original` (ejecución más lenta). El nuevo registro `resultados/pruebas.csv` informa cinco comprobaciones satisfactorias; `resultados/comparacion_cpp.csv` identifica una discrepancia de 75 unidades en la esquina `(j=20,i=0)` del caso `gradiente`. No se han publicado mediciones de aceleración o eficiencia de OpenMP; consultar [resultados](docs/resultados.md) y [paralelismo](docs/paralelismo.md).
