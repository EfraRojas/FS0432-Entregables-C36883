#include <iostream>
#include <vector>
#include <iomanip>
#include <cmath>

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>



std::vector<double> eliminacionGaussiana(
    std::vector<double>& A,
    std::vector<double>& b
) {
    int N = b.size();
    std::vector<double> x(N);

    // 1. Eliminación hacia adelante
    for (int k = 0; k < N; k++) 
    {
        for (int i = k + 1; i < N; i++) 
        {
            double factor = A[i * N + k] / A[k * N + k];

            for (int j = k; j < N; j++) 
            {
                A[i * N + j] -= factor * A[k * N + j];
            }

            b[i] -= factor * b[k];
        }
    }

    // 2. Sustitución hacia atrás
    for (int k = N - 1; k >= 0; k--)
    {
        double suma = 0.0;

        for (int j = k + 1; j < N; j++) 
        {
            suma += A[k * N + j] * x[j];
        }

        x[k] = (b[k] - suma) / A[k * N + k];
    }

    return x;
}

//PONEMOS LA FUNCION QUE LOS AYUDA A PODER USAR EL METODO DESDE PYTHON

PYBIND11_MODULE(gauss, m)
{
	m.def("eliminacionGaussiana", &eliminacionGaussiana);
}



/*
double calcularNormaResiduo(
    std::vector<double>& A,
    std::vector<double>& b,
    std::vector<double>& x
) {
    
    int N = x.size();
    double norma_cuadrada = 0.0;
    
    for (int i = 0; i < N; i++)
    {
        double r_i = 0.0;
        double suma = 0.0;
        for (int j = 0; j < N; j++) 
        {
            suma += A[i * N + j] * x[j];
        }
        r_i = suma - b[i];
        norma_cuadrada += r_i * r_i;
    }

    return std::sqrt(norma_cuadrada);
}


int main() {

    int N = 6;

    // Matriz A almacenada como un único vector 1D.
    std::vector<double> A = {
        10,  2, -1,  0,  1,  0,
         2, 11,  1, -1,  0,  2,
        -1,  1, 10,  2, -1,  0,
         0, -1,  2, 12,  1, -2,
         1,  0, -1,  1,  9,  1,
         0,  2,  0, -2,  1, 10
    };

    // Vector b (lado derecho del sistema de ecuaciones)
    std::vector<double> b = {15, 24, -3, 28, 7, 18};
    

    std::cout << "Resolviendo el sistema A x = b"
              << std::endl;

    // Vector solución x
    std::vector<double> x = eliminacionGaussiana(A, b);

    std::cout << std::endl;
    std::cout << "Solucion:" << std::endl;

    for (int i = 0; i < N; i++) {
        std::cout
            << "x[" << i << "] = "
            << std::fixed
            << std::setprecision(6)
            << x[i]
            << std::endl;
    }

    std::cout << std::endl;

    std::cout
        << "Norma L2 del residuo = "
        << std::scientific
        << std::setprecision(3)
        << calcularNormaResiduo(A, b, x)
        << std::endl;


    return 0;
}
*/
