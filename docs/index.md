# Proyecto I: Ecuación de calor en dos dimensiones

**FS-0432 — Física Computacional**  
**Universidad de Costa Rica**

## Introducción

El presente proyecto consiste en el estudio y la simulación numérica de la distribución de temperatura en una placa bidimensional mediante la ecuación del calor. Para ello, se implementa el método de diferencias finitas explícito FTCS (*Forward Time, Centered Space*), utilizando los lenguajes de programación Python y C++, incorporando paralelización mediante OpenMP en esta última implementación para optimizar la ejecución del programa.

Se busca analizar la evolución temporal de la temperatura bajo distintas condiciones iniciales y de frontera, estudiar la estabilidad y convergencia del método numérico, y comparar los resultados obtenidos mediante ambas implementaciones. Asimismo, se pretende evaluar el aprovechamiento del paralelismo para mejorar el rendimiento computacional de la solución.

## Modelo físico

La evolución de la temperatura en la placa se describe mediante la ecuación del calor en dos dimensiones:

\[
\frac{\partial u}{\partial t}
=
\kappa
\left(
\frac{\partial^2 u}{\partial x^2}
+
\frac{\partial^2 u}{\partial y^2}
\right),
\]

donde \(u(x,y,t)\) representa la temperatura en cada punto de la placa y \(\kappa\) corresponde a la difusividad térmica del material.

Para resolver esta ecuación se utiliza el esquema FTCS, que aproxima las derivadas espaciales mediante diferencias centradas y la derivada temporal mediante una diferencia hacia adelante.

## Integrantes del proyecto

| Nombre | Carné | Responsabilidad / aportación |
|---|---|---|
| Fernando Rodríguez Blanco | C26548 | Python, organización de index.md y deploy |
| Orlando Ismael Benavides Renault | C11025 | Markdown, README, reporte y bitácora |
| Samuel Rojas Baldi | C36852 | YAML, scripts y documentación web |
| Eytan Sequeira Mora | C07458 | C++, ejecutable y CSV |

## Organización de la documentación

La documentación del proyecto se estructura en seis apartados principales. En primer lugar, se presenta una introducción al problema físico y a los objetivos del trabajo. A continuación, se desarrolla el fundamento teórico de la ecuación del calor y se describen las condiciones iniciales y de frontera consideradas. Posteriormente, se explica el método numérico FTCS, incluyendo su discretización, algoritmo y condición de estabilidad.

En los siguientes apartados se presentan los resultados obtenidos, acompañados de gráficas y análisis de su comportamiento, así como los detalles de las implementaciones desarrolladas en Python y C++ con OpenMP. Finalmente, se proporciona acceso al repositorio y a los recursos necesarios para reproducir los experimentos y consultar el desarrollo del proyecto.
