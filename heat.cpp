#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>
#include <omp.h>

std::vector<std::vector<std::vector<double>>> heat_ftcs_2D(double Th, double Tc, double Tm, 
    double kappa, double L, int M, double h, double t_end, const std::string&initial, 
    const std::vector<double>& x, std::vector<double>& y, double T_hot = 100.0) {

        int size = M + 1;
        int num_tiempos = 4;

        // matriz de temperaturas
        std::vector<std::vector<double>> T(size, std::vector<double>(size, Tm));
        std::vector<std::vector<double>> Tp = T;

        // condiciones iniciales
        if (initial == "punto") {
            int i_mid = 0;
            int j_mid = 0;
            double min_x_val = std::abs(x[0] - L / 2.0);
            double min_y_val = std::abs(y[0] - L / 2.0);

            for(int i = 0; i <= M; ++i) {

                if (std::abs(x[i] - L / 2.0) < min_x_val) {

                    min_x_val = std::abs(x[i] - L / 2.0);
                    i_mid = i;

                }

                if (std::abs(y[i] - L / 2.0) < min_y_val) {

                    min_y_val = std::abs(y[i] - L / 2.0);
                    j_mid = i;

                } 

            }

            T[j_mid][i_mid] = T_hot;

            // condiciones de frontera

            for (int i = 0; i <= M; ++i) {

                T[i][0] = Tm;
                T[i][M] = Tm;
                T[0][i] = Tm;
                T[M][i] = Tm;

            }

        }

        else if (initial == "gradiente") {

            for (int i = 0; i <= M; ++i) {

                T[i][0] = Th;
                T[i][M] = Tc;
                T[0][i] = Tm;
                T[M][i] = Tm;

            }

        }
        
        Tp = T;

        double dx = L / M;
        double dy = L / M;

        double rx = (kappa * h) / (dx * dx);
        double ry = (kappa * h) / (dy * dy);
        
        std::vector<double> tiempos = {0.01, 1.0, 5.0, 15.0};

        std::vector<std::vector<std::vector<double>>> T_res(size, std::vector<std::vector<double>>(size, std::vector<double>(num_tiempos, 0.0)));

        int its = static_cast<int>(std::round(t_end / h));

        for (int n = 1; n<= its; ++n) {

            double current_t = n * h;

            // paralelizar 

            #pragma omp parallel for collapse(2) shared(T, Tp, rx, ry, M)
            for (int j = 1; j < M; ++j) {

                for (int i = 1; i < M; ++i) {

                    Tp[j][i] = T[j][i] + rx * (T[j][i + 1] - 2.0 * T[j][i] + T[j][i - 1]) + ry * (T[j + 1][i] - 2.0 * T[j][i] + T[j - 1][i]);

                }

            }

            T = Tp;

            for (size_t k = 0; k < tiempos.size(); ++k) {

                if (std::abs(current_t - tiempos[k]) < h / 2.0) {

                    // paralelizar

                    #pragma omp parallel for collapse(2) shared(T_res, T, M, k)
                    for (int j = 0; j <= M; ++j) {

                        for (int i = 0; i <= M; ++i) {

                            T_res[j][i][k] = T[j][i];

                        }

                    }

                }

            }

        }

        return T_res;

    }


    int main() {

        //parámetros

        double Th = 100.0;
        double Tc = 0.0;
        double Tm = 25.0;
        double kappa = 1.0;
        double L = 1.0;
        int M = 20;
        double h = 0.0001;
        double t_end = 15.0;

        // coordenadas

        std::vector<double> x(M + 1);
        std::vector<double> y(M + 1);

        for (int i = 0; i <= M; ++i) {

            x[i] = i * (L / M);
            y[i] = i * (L / M);

        }

        std::cout << "Calculando T con condición inicial de punto caliente..." << std::endl;
        auto T_punto = heat_ftcs_2D(Th, Tc, Tm, kappa, L, M, h, t_end, "punto", x, y);

        std::cout << "Calculando T con condición inicial de gradiente..." << std::endl;
        auto T_gradiente = heat_ftcs_2D(Th, Tc, Tm, kappa, L, M, h, t_end, "gradiente", x, y);

        std::cout << "Simulación finalizada. Mostrando resultados." <<std::endl;

        std::vector<double> tiempos = {0.01, 1.0, 5.0, 15.0};
        int centro = M / 2;

        // punto caliente

        // mostrar resumen

        std::cout << "============================================================" << std::endl;
        std::cout << "Evolución térmica en el centro de la placa (Punto caliente)" << std::endl;
        std::cout << "============================================================" << std::endl;
        for (size_t k = 0; k < tiempos.size(); ++k) {

            std::cout << "A t = " << tiempos[k] << " s: Temperatura central: "
            << T_punto[centro][centro][k] << " °C" << std::endl;

        }

        // guardar csv

        std::ofstream archivo_punto("resultados_punto.csv");
        archivo_punto << "Tiempo, j, i, Temperatura\n";
        for (size_t k = 0; k < tiempos.size(); ++k) {

            for (int j = 0; j <= M; ++j) {

                for (int i = 0; i <= M; ++i) {

                    archivo_punto << tiempos[k] << "," << j << "," << i << "," << T_punto[j][i][k] << "\n";

                }

            } 

        }

        archivo_punto.close();


        // gradiente

        // mostrar resumen

        std::cout << "============================================================" << std::endl;
        std::cout << "Evolución térmica en el centro de la placa (Gradiente)" << std::endl;
        std::cout << "============================================================" << std::endl;
        for (size_t k = 0; k < tiempos.size(); ++k) {

            std::cout << "A t = " << tiempos[k] << " s: Temperatura central: "
            << T_gradiente[centro][centro][k] << " °C" << std::endl;

        }

        // guardar csv

        std::ofstream archivo_gradiente("resultados_gradiente.csv");
        archivo_gradiente << "Tiempo, j, i, Temperatura\n";
        for (size_t k = 0; k < tiempos.size(); ++k) {

            for (int j = 0; j <= M; ++j) {

                for (int i = 0; i <= M; ++i) {

                    archivo_gradiente << tiempos[k] << "," << j << "," << i << "," << T_gradiente[j][i][k] << "\n";

                }

            } 

        }

        archivo_gradiente.close();

        std::cout << "Se han guardado los datos completos en resultados_punto.csv y resultados_gradiente.csv." << std::endl;

        return 0;

    }