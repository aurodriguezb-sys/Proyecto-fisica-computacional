# Proyecto-fisica-computacional
Repositorio en el cual se desarrolla y expone la solución al proyecto del curso Física Computacional.

## Ecuación de calor en dos dimensiones

Este proyecto estudia la evolución de la temperatura en una placa mediante la solución numérica de la ecuación de calor bidimensional. Se utiliza el método de diferencias finitas FTCS y se analizan dos escenarios térmicos mediante mapas de colores. La primera implementación se realizó en Python. Posteriormente, el 13 de noviembre de 2026, Eytan incorporó la versión C++ con directivas OpenMP, el ejecutable `heat.exe` y los archivos CSV de los dos escenarios.

## Integrantes

| Nombre completo | Carné | Aporte / responsabilidad |
|---|---|---|
| Fernando Rodríguez Blanco | C26548 | Implementación en Python, deploy del repositorio |
| Orlando Ismael Benavides Renault | C11025 | Documentación, README, reporte y bitácora |
| Samuel Rojas Baldi | C36852 | Configuración YAML (`.yml`), scripts y soporte de documentación web |
| Eytan Sequeira Mora | C07458 | Implementación en C++ y publicación de `heat.cpp`, `heat.exe` y dos CSV |

**Profesor:** Marlon Brenes.

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
