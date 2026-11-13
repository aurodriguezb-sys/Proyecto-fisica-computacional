# Ecuación de calor en dos dimensiones

> **Estado: borrador — falta información.** Incorporar enlaces y comandos definitivos de C++ y scripts; actualizar el estado del paralelismo.

**Proyecto final de Física Computacional — FS-0432 | Universidad de Costa Rica**

Este proyecto estudia la evolución de la temperatura en una placa mediante la solución numérica de la ecuación de calor bidimensional. Se utiliza el método de diferencias finitas FTCS y se analizan dos escenarios térmicos mediante mapas de colores. La implementación en Python constituye el avance inicial; el código C++ aún no se ha incorporado al GitHub, según la información del grupo; su estado de desarrollo fuera del repositorio no está confirmado. Tampoco se ha verificado la implementación de paralelismo de memoria compartida.

## Integrantes

| Nombre completo | Carné | Aporte / responsabilidad |
|---|---|---|
| Fernando Rodríguez Blanco | C26548 | Implementación en Python |
| Orlando Ismael Benavides Renault | C11025 | Documentación, README, reporte y bitácora |
| Samuel Rojas Baldi | C36852 | Configuración YAML (`.yml`), scripts y archivos de datos CSV (`.csv`) |
| Eytan Sequeira Mora | C07458 | Implementación en C++ |

Los nombres, carnés y responsabilidades se registran según la información proporcionada por el grupo. Los cuatro carnés están registrados. Las responsabilidades son asignaciones de trabajo, no certificaciones de tareas terminadas. Los commits de la cuenta `aurodriguezb-sys` documentan cambios del repositorio, pero no se ha confirmado su correspondencia con un integrante.

**Profesor:** Marlon Brenes (autor del enunciado suministrado).

## Problema y objetivos

Resolver $\partial_t u=\kappa(\partial_{xx}u+\partial_{yy}u)$ en una región rectangular, estudiar el efecto de las condiciones iniciales y de frontera, visualizar la solución, implementar el método en Python y C++ y evaluar la aceleración en memoria compartida.

## Documentación

- [Inicio](docs/index_falta.md)
- [Fundamento físico y método numérico](docs/explanation.md)
- [Tutorial de ejecución](docs/tutorials_falta.md)
- [Referencia de código](docs/reference_falta.md)
- [Bitácora del proyecto](docs/bitacora_falta.md)
- [Resultados y validación](docs/resultados_falta.md)
- [Paralelismo y optimización](docs/paralelismo_falta.md)
- [Reporte académico](docs/reporte_falta.md)

## Ejecutar

Desde la raíz del repositorio original, con Python y las dependencias instaladas:

```bash
python -m pip install numpy matplotlib
python heat.py
```

El programa muestra dos figuras de Matplotlib. Para cerrar la primera y continuar, cierre la ventana. El programa original no guarda automáticamente archivos PNG. Para reproducir las comprobaciones complementarias, integrar el script del paquete completo anterior y ejecutar `python scripts/validar_calor.py` (solo NumPy).

## Estado

| Hito | Avance |
|---|---|
| Método numérico y Python | Implementados |
| Condiciones iniciales distintas | Parcial: punto caliente e interior uniforme con fronteras asimétricas |
| Visualización temporal | Cuatro instantáneas por caso |
| C++ | Pendiente de incorporar a GitHub; estado fuera del repositorio no verificado |
| Paralelismo | Pendiente en el repositorio revisado |
| Documentación | Propuesta en este paquete |

Fuente: [repositorio original](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional), rama `main`, commit [`b9c78fe`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/commit/b9c78fe0e526a7b547f26aa88c961998b368fd78). Revisión: 12 de noviembre de 2026. Los resultados complementarios no estaban en ese commit. Revisar los datos personales antes de publicar.

## Integración de esta entrega

Esta entrega contiene exclusivamente archivos Markdown. No incluye `heat.py`, C++, `mkdocs.yml` ni scripts de simulación; conservar los originales y coordinar con Fernando, Eytan y Samuel. Los archivos `_falta.md` son borradores con pendientes explícitos. Al cerrarlos, quitar el sufijo y actualizar enlaces y navegación YAML; `docs/index.md` es el nombre habitual de la portada de MkDocs. No sustituir el README del repositorio hasta revisar el borrador.
