"""Validación y exportación de resultados de la ecuación de calor 2D (FTCS).


Este script es una herramienta independiente de validación. No modifica
``heat.py`` ni ``heat.cpp``. Hace lo siguiente:

1. Reproduce los dos escenarios de ``heat.py`` (punto caliente central y
   gradiente) con una versión vectorizada de la misma fórmula FTCS y los
   exporta a CSV con el mismo formato que los CSV de C++
   (``Tiempo, j, i, Temperatura``).
2. Compara nodo a nodo esas matrices con ``resultados_punto.csv`` y
   ``resultados_gradiente.csv`` (salida de ``heat.cpp``), si existen.
3. Ejecuta dos pruebas: la versión vectorizada contra un bucle escalar
   equivalente (100 pasos) y un campo uniforme que debe permanecer constante.
4. Estudia la convergencia contra la solución analítica
   u = sin(pi x) sin(pi y) exp(-2 pi^2 kappa t).
5. Si Matplotlib está instalado, guarda figuras para la documentación.

Opcionalmente, con ``--original``, ejecuta la propia función
``heat_ftcs_2D`` de ``heat.py`` (extraída sin ejecutar las gráficas) y
compara sus resultados con la versión vectorizada. Es lento (bucles de
Python), del orden de minutos.

Uso, desde la raíz del repositorio::

    python scripts/validar_calor.py
    python scripts/validar_calor.py --original

Salidas en ``resultados/`` (y una copia en ``docs/datos/`` para el sitio
MkDocs; figuras en ``docs/img/``).
"""

import argparse
import ast
import csv
import shutil
import sys
from pathlib import Path

import numpy as np

RAIZ = Path(__file__).resolve().parent.parent
DIR_RESULTADOS = RAIZ / "resultados"
DIR_DOCS_DATOS = RAIZ / "docs" / "datos"
DIR_DOCS_IMG = RAIZ / "docs" / "img"

# Parámetros de heat.py y heat.cpp
TH, TC, TM = 100.0, 0.0, 25.0
T_HOT = 100.0
KAPPA = 1.0
L = 1.0
M = 20
H = 0.0001
T_END = 15.0
TIEMPOS = [0.01, 1.0, 5.0, 15.0]


# ---------------------------------------------------------------------------
# Núcleo numérico
# ---------------------------------------------------------------------------

def inicializar(M, caso, L=L, Th=TH, Tc=TC, Tm=TM, T_hot=T_HOT):
    """Matriz inicial (M+1)x(M+1) con las mismas condiciones que heat.py.

    Índices T[j, i]: j recorre y (filas), i recorre x (columnas).
    """
    T = np.full((M + 1, M + 1), Tm, dtype=float)
    if caso == "punto":
        x = np.linspace(0, L, M + 1)
        i = int(np.argmin(np.abs(x - L / 2)))
        j = i
        T[j, i] = T_hot
        T[:, 0] = Tm
        T[:, M] = Tm
        T[0, :] = Tm
        T[M, :] = Tm
    elif caso == "gradiente":
        # Mismo orden que heat.py: las filas 0 y M sobrescriben las esquinas.
        T[:, 0] = Th
        T[:, M] = Tc
        T[0, :] = Tm
        T[M, :] = Tm
    elif caso == "uniforme":
        pass
    else:
        raise ValueError(f"caso desconocido: {caso!r}")
    return T


def verificar_estabilidad(kappa, dx, dy, dt):
    """FTCS 2D es estable si kappa*dt*(1/dx^2 + 1/dy^2) <= 1/2."""
    r = kappa * dt * (1 / dx**2 + 1 / dy**2)
    if r > 0.5:
        raise ValueError(f"FTCS inestable: kappa*dt*(1/dx²+1/dy²) = {r:.4f} > 0.5")
    return r


def paso_ftcs(T, rx, ry):
    """Un paso FTCS vectorizado; las fronteras quedan fijas."""
    Tp = T.copy()
    Tp[1:-1, 1:-1] = (T[1:-1, 1:-1]
                      + rx * (T[1:-1, 2:] - 2 * T[1:-1, 1:-1] + T[1:-1, :-2])
                      + ry * (T[2:, 1:-1] - 2 * T[1:-1, 1:-1] + T[:-2, 1:-1]))
    return Tp


def evolucionar(T, kappa, dx, dy, dt, pasos, guardar_en=()):
    """Avanza ``pasos`` pasos FTCS. Devuelve (T_final, {paso: copia de T})."""
    verificar_estabilidad(kappa, dx, dy, dt)
    rx = kappa * dt / dx**2
    ry = kappa * dt / dy**2
    guardar_en = set(guardar_en)
    instantaneas = {}
    T = T.copy()
    for n in range(1, pasos + 1):
        T = paso_ftcs(T, rx, ry)
        if n in guardar_en:
            instantaneas[n] = T.copy()
    return T, instantaneas


def evolucionar_escalar(T, kappa, dx, dy, dt, pasos):
    """Bucle escalar equivalente a heat.py, para comparar con la versión vectorizada."""
    rx = kappa * dt / dx**2
    ry = kappa * dt / dy**2
    T = T.copy()
    Tp = T.copy()
    n_filas, n_cols = T.shape
    for _ in range(pasos):
        for j in range(1, n_filas - 1):
            for i in range(1, n_cols - 1):
                Tp[j, i] = (T[j, i] + rx * (T[j, i + 1] - 2 * T[j, i] + T[j, i - 1])
                            + ry * (T[j + 1, i] - 2 * T[j, i] + T[j - 1, i]))
        T[:, :] = Tp[:, :]
    return T


def simular_escenario(caso):
    """Instantáneas del escenario ``caso`` en TIEMPOS, como arreglo (M+1, M+1, 4)."""
    dx = dy = L / M
    pasos = round(T_END / H)
    pasos_guardado = [round(t / H) for t in TIEMPOS]
    _, inst = evolucionar(inicializar(M, caso), KAPPA, dx, dy, H, pasos, pasos_guardado)
    return np.stack([inst[n] for n in pasos_guardado], axis=-1)


# ---------------------------------------------------------------------------
# Ejecución opcional del heat.py original
# ---------------------------------------------------------------------------

def cargar_heat_py():
    """Extrae ``heat_ftcs_2D`` de heat.py sin ejecutar las gráficas."""
    fuente = (RAIZ / "heat.py").read_text(encoding="utf-8")
    arbol = ast.parse(fuente)
    funcion = next(n for n in arbol.body
                   if isinstance(n, ast.FunctionDef) and n.name == "heat_ftcs_2D")
    modulo = ast.Module(body=[funcion], type_ignores=[])
    # heat.py usa x e y globales dentro de la función.
    espacio = {"np": np,
               "x": np.linspace(0, L, M + 1),
               "y": np.linspace(0, L, M + 1)}
    exec(compile(modulo, "heat.py", "exec"), espacio)
    return espacio["heat_ftcs_2D"]


# ---------------------------------------------------------------------------
# Entrada/salida
# ---------------------------------------------------------------------------

def escribir_csv(ruta, encabezado, filas):
    ruta.parent.mkdir(parents=True, exist_ok=True)
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(encabezado)
        w.writerows(filas)


def exportar_matrices(ruta, T_res):
    """Mismo formato que heat.cpp: Tiempo, j, i, Temperatura."""
    filas = []
    for k, t in enumerate(TIEMPOS):
        for j in range(T_res.shape[0]):
            for i in range(T_res.shape[1]):
                filas.append([f"{t:g}", j, i, f"{T_res[j, i, k]:.10g}"])
    escribir_csv(ruta, ["Tiempo", "j", "i", "Temperatura"], filas)


def leer_csv_cpp(ruta):
    """Lee un CSV de heat.cpp y lo devuelve como arreglo (M+1, M+1, 4)."""
    datos = np.genfromtxt(ruta, delimiter=",", skip_header=1)
    T = np.full((M + 1, M + 1, len(TIEMPOS)), np.nan)
    for t, j, i, temp in datos:
        k = int(np.argmin([abs(t - tt) for tt in TIEMPOS]))
        T[int(j), int(i), k] = temp
    return T


# ---------------------------------------------------------------------------
# Pruebas y convergencia
# ---------------------------------------------------------------------------

def prueba_escalar_vs_vectorizado(pasos=100, tol=1e-12):
    dx = dy = L / M
    resultados = []
    for caso in ("punto", "gradiente"):
        T0 = inicializar(M, caso)
        T_vec, _ = evolucionar(T0, KAPPA, dx, dy, H, pasos)
        T_esc = evolucionar_escalar(T0, KAPPA, dx, dy, H, pasos)
        err = float(np.max(np.abs(T_vec - T_esc)))
        resultados.append((f"escalar_vs_vectorizado_{caso}", err, tol, err <= tol))
    return resultados


def prueba_campo_uniforme(pasos=1000, tol=1e-12):
    dx = dy = L / M
    T0 = inicializar(M, "uniforme")
    T, _ = evolucionar(T0, KAPPA, dx, dy, H, pasos)
    err = float(np.max(np.abs(T - TM)))
    return [("campo_uniforme_constante", err, tol, err <= tol)]


def convergencia(mallas=(10, 20, 40, 80), t_final=0.1, factor=0.2):
    """Error máximo nodal contra sin(pi x) sin(pi y) exp(-2 pi^2 kappa t).

    dt = factor*dx^2, ajustado para que un número entero de pasos llegue a t_final.
    """
    filas = []
    error_previo = None
    for Mi in mallas:
        dx = dy = 1.0 / Mi
        pasos = int(np.ceil(t_final / (factor * dx**2)))
        dt = t_final / pasos
        x = np.linspace(0, 1, Mi + 1)
        X, Y = np.meshgrid(x, x)
        u0 = np.sin(np.pi * X) * np.sin(np.pi * Y)
        u, _ = evolucionar(u0, KAPPA, dx, dy, dt, pasos)
        exacta = u0 * np.exp(-2 * np.pi**2 * KAPPA * t_final)
        error = float(np.max(np.abs(u - exacta)))
        orden = np.log2(error_previo / error) if error_previo else None
        filas.append((Mi, dx, dt, pasos, error, orden))
        error_previo = error
    return filas


# ---------------------------------------------------------------------------
# Figuras (opcionales)
# ---------------------------------------------------------------------------

def guardar_figuras(escenarios, conv):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("Matplotlib no está instalado: se omiten las figuras.")
        return []

    DIR_DOCS_IMG.mkdir(parents=True, exist_ok=True)
    x = np.linspace(0, L, M + 1)
    X, Y = np.meshgrid(x, x)
    rutas = []
    titulos = {"punto": "Punto caliente central", "gradiente": "Borde caliente y borde frío"}
    for caso, T_res in escenarios.items():
        fig, ejes = plt.subplots(2, 2, figsize=(9, 7.5), layout="constrained")
        # Escala de colores fija por escenario para comparar instantes.
        vmin, vmax = float(T_res.min()), float(T_res.max())
        niveles = np.linspace(vmin, vmax, 21)
        for k, ax in enumerate(ejes.flat):
            mapa = ax.contourf(X, Y, T_res[:, :, k], levels=niveles, cmap="hot")
            ax.set_title(f"t = {TIEMPOS[k]:g}")
            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.set_aspect("equal")
        fig.colorbar(mapa, ax=ejes, label="Temperatura")
        fig.suptitle(f"{titulos[caso]} (escala fija)")
        ruta = DIR_DOCS_IMG / f"mapa_{caso}.png"
        fig.savefig(ruta, dpi=120)
        plt.close(fig)
        rutas.append(ruta)

    Ms = np.array([f[0] for f in conv], dtype=float)
    errores = np.array([f[4] for f in conv])
    fig, ax = plt.subplots(figsize=(6, 4.5))
    ax.loglog(Ms, errores, "o-", label="Error máximo FTCS")
    ax.loglog(Ms, errores[0] * (Ms[0] / Ms) ** 2, "--", label=r"Referencia $\propto M^{-2}$")
    ax.set_xlabel("M (intervalos por lado)")
    ax.set_ylabel("Error máximo nodal")
    ax.set_title(r"Convergencia, $\Delta t = 0.2\,\Delta x^2$, $t = 0.1$")
    ax.grid(True, which="both", alpha=0.3)
    ax.legend()
    fig.tight_layout()
    ruta = DIR_DOCS_IMG / "convergencia.png"
    fig.savefig(ruta, dpi=120)
    plt.close(fig)
    rutas.append(ruta)
    return rutas


# ---------------------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------------------

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--original", action="store_true",
                        help="ejecutar también heat_ftcs_2D de heat.py (lento)")
    parser.add_argument("--sin-figuras", action="store_true",
                        help="no generar las figuras PNG")
    args = parser.parse_args(argv)

    DIR_RESULTADOS.mkdir(exist_ok=True)
    generados = []

    # 1. Escenarios de heat.py, versión vectorizada
    print("Simulando escenarios (M=20, h=1e-4, t_end=15)...")
    escenarios = {caso: simular_escenario(caso) for caso in ("punto", "gradiente")}
    for caso, T_res in escenarios.items():
        ruta = DIR_RESULTADOS / f"python_{caso}.csv"
        exportar_matrices(ruta, T_res)
        generados.append(ruta)

    centro = M // 2
    resumen = []
    for k, t in enumerate(TIEMPOS):
        resumen.append([f"{t:g}",
                        f"{escenarios['punto'][centro, centro, k]:.6f}",
                        f"{escenarios['punto'][:, :, k].max():.6f}",
                        f"{escenarios['gradiente'][centro, centro, k]:.6f}",
                        f"{escenarios['gradiente'][:, :, k].mean():.6f}"])
    ruta = DIR_RESULTADOS / "resumen_ftcs.csv"
    escribir_csv(ruta, ["tiempo", "punto_centro", "punto_maximo",
                        "gradiente_centro", "gradiente_media_nodal"], resumen)
    generados.append(ruta)

    # 2. Comparación nodo a nodo con los CSV de heat.cpp
    comparacion = []
    for caso, T_res in escenarios.items():
        ruta_cpp = RAIZ / f"resultados_{caso}.csv"
        if not ruta_cpp.exists():
            print(f"No se encontró {ruta_cpp.name}; se omite la comparación con C++.")
            continue
        T_cpp = leer_csv_cpp(ruta_cpp)
        for k, t in enumerate(TIEMPOS):
            dif = np.abs(T_res[:, :, k] - T_cpp[:, :, k])
            comparacion.append([caso, f"{t:g}", f"{np.nanmax(dif):.3e}",
                                f"{np.nanmean(dif):.3e}", int(np.isnan(dif).sum())])
    if comparacion:
        ruta = DIR_RESULTADOS / "comparacion_cpp.csv"
        escribir_csv(ruta, ["caso", "tiempo", "dif_max_abs", "dif_media_abs",
                            "nodos_faltantes"], comparacion)
        generados.append(ruta)

    # 3. Pruebas
    pruebas = prueba_escalar_vs_vectorizado() + prueba_campo_uniforme()

    # Opcional: heat.py original
    if args.original:
        print("Ejecutando heat_ftcs_2D de heat.py (puede tardar varios minutos)...")
        heat_ftcs_2D = cargar_heat_py()
        for caso, T_res in escenarios.items():
            T_orig = heat_ftcs_2D(TH, TC, TM, KAPPA, L, M, H, T_END, initial=caso)
            exportar_matrices(DIR_RESULTADOS / f"heat_py_{caso}.csv", T_orig)
            generados.append(DIR_RESULTADOS / f"heat_py_{caso}.csv")
            err = float(np.max(np.abs(T_orig - T_res)))
            pruebas.append((f"heat_py_vs_vectorizado_{caso}", err, 1e-9, err <= 1e-9))

    ruta = DIR_RESULTADOS / "pruebas.csv"
    escribir_csv(ruta, ["prueba", "error_max", "tolerancia", "aprobada"],
                 [[n, f"{e:.3e}", f"{t:g}", "si" if ok else "no"] for n, e, t, ok in pruebas])
    generados.append(ruta)

    # 4. Convergencia
    conv = convergencia()
    ruta = DIR_RESULTADOS / "convergencia.csv"
    escribir_csv(ruta, ["M", "dx", "dt", "pasos", "error_max", "orden"],
                 [[Mi, f"{dx:.6g}", f"{dt:.6g}", p, f"{e:.6e}",
                   "" if o is None else f"{o:.4f}"] for Mi, dx, dt, p, e, o in conv])
    generados.append(ruta)

    # Copia para el sitio MkDocs
    DIR_DOCS_DATOS.mkdir(parents=True, exist_ok=True)
    for ruta in generados:
        shutil.copy2(ruta, DIR_DOCS_DATOS / ruta.name)
    # Datos y gráficas originales del grupo (heat.cpp y heat.py), sin modificarlos.
    for nombre in ("resultados_punto.csv", "resultados_gradiente.csv"):
        if (RAIZ / nombre).exists():
            shutil.copy2(RAIZ / nombre, DIR_DOCS_DATOS / nombre)
    DIR_DOCS_IMG.mkdir(parents=True, exist_ok=True)
    for nombre in ("grafica_punto_caliente_central.png", "grafica_gradiente.png"):
        if (RAIZ / nombre).exists():
            shutil.copy2(RAIZ / nombre, DIR_DOCS_IMG / nombre)

    if not args.sin_figuras:
        generados += guardar_figuras(escenarios, conv)

    # Informe en consola
    print("\nResumen (nodo central):")
    print(f"{'t':>6} {'punto':>12} {'gradiente':>12}")
    for fila in resumen:
        print(f"{fila[0]:>6} {fila[1]:>12} {fila[3]:>12}")
    if comparacion:
        print("\nComparación con heat.cpp (diferencia máxima absoluta):")
        for caso, t, dmax, _, falt in comparacion:
            print(f"  {caso:<10} t={t:<5} {dmax}" + (f" ({falt} nodos faltantes)" if falt else ""))
    print("\nConvergencia:")
    for Mi, _, _, _, e, o in conv:
        print(f"  M={Mi:<3} error={e:.5e}" + ("" if o is None else f" orden={o:.4f}"))
    print("\nPruebas:")
    for n, e, t, ok in pruebas:
        print(f"  [{'OK' if ok else 'FALLA'}] {n}: {e:.2e} (tol {t:g})")
    print("\nArchivos generados:")
    for ruta in generados:
        print(f"  {ruta.relative_to(RAIZ)}")

    return 0 if all(ok for *_, ok in pruebas) else 1


if __name__ == "__main__":
    sys.exit(main())
