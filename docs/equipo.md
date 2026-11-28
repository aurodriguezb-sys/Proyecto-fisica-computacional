# Integrantes y estado del proyecto

> **Estado: en actualización.** Se documentan los aportes publicados y se separan de los encargos todavía pendientes.

**Universidad de Costa Rica — FS-0432 Física Computacional**

| Nombre completo | Carné | Aporte / responsabilidad |
|---|---|---|
| Fernando Rodríguez Blanco | C26548 | Implementación en Python |
| Orlando Ismael Benavides Renault | C11025 | Documentación, README, reporte y bitácora |
| Samuel Rojas Baldi | C36852 | Configuración YAML (`.yml`), scripts y recursos de MkDocs |
| Eytan Sequeira Mora | C07458 | Implementación en C++ y publicación de ejecutable y CSV |

Los nombres, carnés y responsabilidades se registran según la información proporcionada por el grupo. Los cuatro carnés están registrados. Las responsabilidades son asignaciones de trabajo, no certificaciones de tareas terminadas. Los commits de la cuenta `aurodriguezb-sys` documentan cambios del repositorio, pero no se ha confirmado su correspondencia con un integrante.

## Distribución de responsabilidades

| Integrante | Encargo comunicado | Evidencia y estado |
|---|---|---|
| Fernando Rodríguez Blanco | Python | `heat.py` y dos PNG existen en el repositorio revisado; confirmar cambios posteriores y validación del programa original. |
| Orlando Ismael Benavides Renault | Archivos Markdown, README, reporte y bitácora | Seis commits documentales publicados el 12 de noviembre; actualización de la documentación tras el aporte de Eytan. |
| Eytan Sequeira Mora | C++ | El commit [`50693a1`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/50693a1ccc0b00f6b8b4b81f16bafd447de81546) incorpora `heat.cpp`, `heat.exe` y los dos CSV; código con OpenMP. |
| Samuel Rojas Baldi | YAML (`.yml`), scripts y recursos de documentación web | Responsabilidad asignada; `mkdocs.yml` y los scripts aún no constan en el repositorio. Aunque se habló de CSV como posible encargo, los dos CSV presentes se incorporaron en el commit de Eytan. |

## Estado del trabajo

Python y los mapas de temperatura están disponibles desde el 9 de noviembre. C++ y dos CSV están publicados desde el 13 de noviembre. El archivo `heat.cpp` contiene paralelismo OpenMP, pero todavía no existen en el repositorio mediciones suficientes para cuantificar la aceleración ni la eficiencia.

La documentación y el script independiente de validación descrito en el reporte se prepararon como aportes complementarios para revisión del grupo; el script ya fue incorporado por Samuel en la PR #1. Véase el [historial](bitacora.md) y el [reporte](reporte.md).


## Actualización de responsabilidades verificadas — 20/11/2026

La [pull request #1](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/pull/1) fue elaborada desde la rama `samuel-rojas` y posteriormente integrada en `main`. Por tanto, las referencias anteriores a `mkdocs.yml`, MathJax, scripts y archivos CSV **pendientes de incorporación** describen un estado histórico que ya fue superado.

| Integrante | Evidencia nueva | Estado posterior a la integración |
|---|---|---|
| Samuel Rojas Baldi | [Commit `de7cbd0`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/de7cbd0a7235d17ab5fe96f2af6c804c1ee2c5c6) y pull request #1 | Configuración de MkDocs y MathJax; script de validación; publicación de CSV, figuras y página de resultados. |
| Orlando Ismael Benavides Renault | [Merge `6f363399`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/6f3633991a747fd67dd0bcf6d6dedc773b5460db) | Integración de la pull request en la rama principal; documentación previa de avance conservada. |
| Eytan Sequeira Mora | [Commit `50693a1`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/50693a1ccc0b00f6b8b4b81f16bafd447de81546) | Fuente y ejecutable de C++ con OpenMP, además de los dos CSV originales, conservados intactos. |
| Fernando Rodríguez Blanco | [Commit `b9c78fe`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/b9c78fe0e526a7b547f26aa88c961998b368fd78) | Implementación Python y figuras originales, ahora comparadas por el nuevo validador. |

Los CSV publicados por Samuel son salidas de comparación y copias para el sitio; no se debe confundir su autoría con los dos CSV originales de Eytan.
