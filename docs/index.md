# Proyecto I: ecuación de calor en dos dimensiones

**FS-0432 — Física Computacional, Universidad de Costa Rica**

Este sitio reúne la documentación del proyecto: el fundamento físico, el método numérico FTCS, las implementaciones en Python y C++ con OpenMP, los resultados y la bitácora del equipo.

La ecuación que se resuelve es

$$
\frac{\partial u}{\partial t} = \kappa\left(\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2}\right),
$$

y el esquema explícito FTCS actualiza cada nodo interior con

$$
u_{j,i}^{n+1} = u_{j,i}^{n} + r_x\left(u_{j,i+1}^{n} - 2u_{j,i}^{n} + u_{j,i-1}^{n}\right) + r_y\left(u_{j+1,i}^{n} - 2u_{j,i}^{n} + u_{j-1,i}^{n}\right),
$$

con $r_x = \kappa\,\Delta t/\Delta x^2$ y $r_y = \kappa\,\Delta t/\Delta y^2$. El método es estable si $r_x + r_y \le 1/2$.

## Integrantes

| Nombre | Carné | Responsabilidad |
|---|---|---|
| Fernando Rodríguez Blanco | C26548 | Python |
| Orlando Ismael Benavides Renault | C11025 | Markdown, README, reporte y bitácora |
| Samuel Rojas Baldi | C36852 | YAML, scripts y documentación web |
| Eytan Sequeira Mora | C07458 | C++, ejecutable y CSV |

## Navegación

| Sección | Contenido |
|---|---|
| [Integrantes y estado](equipo_falta.md) | Integrantes, estado y ejecución |
| [Método](explanation.md) | Ecuación, discretización, estabilidad |
| [Tutorial](tutorials_falta.md) | Reproducir los experimentos |
| [Referencia](reference_falta.md) | Parámetros, arreglos y funcionamiento |
| [Resultados y validación](resultados_falta.md) | Análisis físico y comprobaciones |
| [Datos, gráficas y CSV](resultados.md) | Salidas de `scripts/validar_calor.py`, CSV descargables y figuras |
| [Paralelismo](paralelismo_falta.md) | C++/OpenMP y protocolo de medición |
| [Reporte](reporte_falta.md) | Síntesis académica |
| [Bitácora](bitacora_falta.md) | Historial Git y registro de trabajo |

## Generar este sitio

Desde la raíz del repositorio:

```bash
python -m pip install -r requirements-docs.txt
mkdocs serve      # vista previa en http://127.0.0.1:8000
mkdocs build      # genera el sitio estático en site/
```

Las fórmulas se escriben con `$...$` y `$$...$$`; la extensión `pymdownx.arithmatex` las prepara y MathJax 3 (configurado en `docs/javascripts/mathjax.js`) las dibuja en el navegador. MathJax se carga desde un CDN, por lo que se necesita conexión para ver las ecuaciones.
