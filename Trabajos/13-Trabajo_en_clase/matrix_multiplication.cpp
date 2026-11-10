
#include <iostream>
#include <vector>
#include <omp.h>

int main() 
{
	int N = 12800;

   std::vector<double> A(N * N, 1.5);
   std::vector<double> B(N * N, 2.0);
   std::vector<double> C(N * N, 0.0);

   int num_threads = omp_get_max_threads();

   double tinicial = omp_get_wtime();

	#pragma omp parallel for
   for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			
			double suma = 0.0;

            for (int k = 0; k < N; k++) {suma += A[i * N + k] * B[k * N + j];}
					C[i * N + j] = suma;}
				}

    double tfinal = omp_get_wtime();
    double tiempo = tfinal - tinicial;

    std::cout << num_threads << " " << tiempo << std::endl;

    return 0;
}
