import numpy as np
import matplotlib.pyplot as plt

def heat_ftcs_2D(Th, Tc, Tm, kappa, L, M, h, t_end,
                 initial='punto', T_hot=100.0):

    # matriz de temperaturas
    T = np.zeros((M + 1, M + 1), dtype=float)

    # condiciones iniciales
    T[:, :] = Tm

    if initial == 'punto':

        i = np.argmin(abs(x - L / 2))
        j = np.argmin(abs(y - L / 2))

        T[j, i] = T_hot

        # condiciones de frontera: todos los bordes a la misma temperatura
        T[:, 0] = Tm
        T[:, M] = Tm
        T[0, :] = Tm
        T[M, :] = Tm

    elif initial == 'gradiente':

        # condiciones de frontera del caso gradiente
        T[:, 0] = Th
        T[:, M] = Tc
        T[0, :] = Tm
        T[M, :] = Tm

    # matriz para las nuevas temperaturas
    Tp = T.copy()

    dx = L / M
    dy = L / M

    rx = (kappa * h) / dx**2
    ry = (kappa * h) / dy**2

    # tiempos para almacenar los resultados
    tiempos = [0.01, 1, 5, 15]

    T_res = np.zeros((M + 1, M + 1, len(tiempos)))

    # iteraciones
    its = round(t_end / h)

    for n in range(1, its + 1):

        for j in range(1, M):
            for i in range(1, M):

                Tp[j, i] = (T[j, i] + rx * (T[j, i+1] - 2*T[j, i] + T[j, i-1]) +
                            ry * (T[j+1, i] - 2*T[j, i] + T[j-1, i]))

        T[:, :] = Tp[:, :]
        for k in range(len(tiempos)):
            if n == round(tiempos[k] / h):
                T_res[:, :, k] = T

    return T_res


# parámetros

Th = 100.0
Tc = 0.0
Tm = 25.0
kappa = 1.0
L = 1.0
M = 20
h = 0.0001
t_end = 15.0

# tiempos para graficar los resultados

tiempos = [0.01, 1, 5, 15.0]

# coordenadas

x = np.linspace(0, L, M + 1)
y = np.linspace(0, L, M + 1)

X, Y = np.meshgrid(x, y)

# gráfica para condición inicial del punto caliente central

T_punto = heat_ftcs_2D(Th, Tc, Tm, kappa, L, M, h, t_end,
    initial='punto')

fig1, graf1 = plt.subplots(2, 2)

for i, ax in enumerate(graf1.flat):

    mapa = ax.contourf(X, Y, T_punto[:, :, i],
        levels=20, cmap='hot')

    fig1.colorbar(mapa, ax=ax, label='Temperatura')

    ax.set_title(f'Punto caliente: t = {tiempos[i]}')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

fig1.suptitle('Punto caliente central')
plt.tight_layout()
plt.show()

# gráfica para condición inicial del gradiente

T_gradiente = heat_ftcs_2D(Th, Tc, Tm, kappa, L, M, h, t_end,
    initial='gradiente')

fig2, graf2 = plt.subplots(2, 2)

for i, ax in enumerate(graf2.flat):

    mapa = ax.contourf(X, Y, T_gradiente[:, :, i],
        levels=20, cmap='hot')

    fig2.colorbar(mapa, ax=ax, label='Temperatura')

    ax.set_title(f'Gradiente: t = {tiempos[i]}')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

fig2.suptitle('Un borde caliente y el otro frío')
plt.tight_layout()
plt.show()
