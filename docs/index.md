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
<<<<<<< HEAD
| [Integrantes y estado](equipo.md) | Integrantes, estado y ejecución |
| [Método](explanation.md) | Ecuación, discretización, estabilidad |
| [Tutorial](tutorials.md) | Reproducir los experimentos |
| [Referencia](reference.md) | Parámetros, arreglos y funcionamiento |
| [Resultados y validación](resultados.md) | Análisis físico y comprobaciones |
| [Datos, gráficas y CSV](resultados.md) | Salidas de `scripts/validar_calor.py`, CSV descargables y figuras |
| [Paralelismo](paralelismo.md) | C++/OpenMP y protocolo de medición |
| [Reporte](reporte.md) | Síntesis académica |
| [Bitácora](bitacora.md) | Historial Git y registro de trabajo |
=======
| [Integrantes y estado](equipo_falta.md) | Integrantes, estado y ejecución |
| [Método](explanation.md) | Ecuación, discretización, estabilidad |
| [Tutorial](tutorials_falta.md) | Reproducir los experimentos |
| [Referencia](reference_falta.md) | Parámetros, arreglos y funcionamiento |
| [Resultados y validación](resultados_falta.md) | Análisis físico y comprobaciones |
| [Datos, gráficas y CSV](resultados.md) | Salidas de `scripts/validar_calor.py`, CSV descargables y figuras |
| [Paralelismo](paralelismo_falta.md) | C++/OpenMP y protocolo de medición |
| [Reporte](reporte_falta.md) | Síntesis académica |
| [Bitácora](bitacora_falta.md) | Historial Git y registro de trabajo |
>>>>>>> 6f3633991a747fd67dd0bcf6d6dedc773b5460db

## Generar este sitio

Desde la raíz del repositorio:

```bash
python -m pip install -r requirements-docs.txt
mkdocs serve      # vista previa en http://127.0.0.1:8000
mkdocs build      # genera el sitio estático en site/
```

Las fórmulas se escriben con `$...$` y `$$...$$`; la extensión `pymdownx.arithmatex` las prepara y MathJax 3 (configurado en `docs/javascripts/mathjax.js`) las dibuja en el navegador. MathJax se carga desde un CDN, por lo que se necesita conexión para ver las ecuaciones.
<<<<<<< HEAD

---

## Complemento académico y seguimiento de Orlando

> **Alcance del complemento documental:** los cuatro aportes ya están incorporados a `main`; todavía falta medir rendimiento OpenMP y acordar el tratamiento de las esquinas en el caso de gradiente.

**FS-0432 — Física Computacional, Universidad de Costa Rica**

### Integrantes

| Nombre | Carné | Responsabilidad |
|---|---|---|
| Fernando Rodríguez Blanco | C26548 | Python |
| Orlando Ismael Benavides Renault | C11025 | Markdown, README, reporte y bitácora |
| Samuel Rojas Baldi | C36852 | YAML, scripts y documentación web |
| Eytan Sequeira Mora | C07458 | C++, ejecutable y CSV |

### Objetivo

Simular la distribución de temperatura en una placa y documentar el método, implementación, resultados, validación y optimización. El enunciado de Marlon Brenes exige Python, C++, visualización y paralelismo de memoria compartida.

### Navegación

| Sección | Contenido |
|---|---|
| [Integrantes y estado](equipo.md) | Integrantes, estado y ejecución |
| [Método](explanation.md) | Ecuación, discretización, estabilidad |
| [Tutorial](tutorials.md) | Reproducir los experimentos |
| [Referencia](reference.md) | Parámetros, arreglos y funcionamiento |
| [Bitácora](bitacora.md) | Historial Git y registro de trabajo |
| [Resultados](resultados.md) | Análisis físico y comprobaciones nuevas |
| [Paralelismo](paralelismo.md) | Plan C++/OpenMP y protocolo de medición |
| [Reporte](reporte.md) | Síntesis académica |

El proyecto se encuentra en desarrollo. `heat.py`, `heat.cpp`, `heat.exe` y los dos CSV de resultados están publicados en `main`; la [bitácora](bitacora.md) registra sus commits. Se separan los resultados disponibles de las pruebas de rendimiento y las propuestas todavía no ejecutadas.


### Actualización de navegación — 20/11/2026

La [pull request #1](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/pull/1) incorporó la portada de Samuel y la configuración [`mkdocs.yml`](https://github.com/aurodriguezb-sys/Proyecto-fisica-computacional/blob/main/mkdocs.yml). En esta consolidación, la información documental de Orlando se incorpora como complemento de la misma página, sin eliminar el aporte de Samuel.

| Nueva sección integrada | Ruta |
|---|---|
| Portada del sitio | [Inicio](index.md) |
| Tablas, pruebas, mapas y archivos descargables | [Datos, gráficas y CSV](resultados.md) |
| Informe numérico consolidado | [Resultados y validación](resultados.md) |
| Registro histórico actualizado | [Bitácora](bitacora.md) |

La navegación activa de MkDocs incluye la documentación anterior de Orlando y las páginas nuevas de Samuel. Los pendientes principales son la evaluación cuantitativa de OpenMP y la decisión sobre el tratamiento de las esquinas de frontera.
=======
>>>>>>> 6f3633991a747fd67dd0bcf6d6dedc773b5460db
