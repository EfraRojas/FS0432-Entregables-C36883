import numpy as np
import matplotlib.pyplot as plt
import time
import gauss

from construir_matriz_poisson3d import poisson_3d

valores_n = [4, 6, 8, 10, 12]

valores_N = []
tiempos = []

for n in valores_n:

    A, b = poisson_3d(n)

    N = n**3
    
    A_lista = A.flatten().tolist()
    b_lista = b.tolist()

#fatten() hace que la matriz bidimensional se conveirta en una lista unidimensional, una funcion muy conveniente
#y tolist hace que el arreglo de numpy sea la lista para que asi pueda trabajar en c++

    inicio = time.perf_counter()

    u = gauss.eliminacionGaussiana(A_lista, b_lista)

    fin = time.perf_counter()

    tiempo = fin - inicio

    residuo = np.linalg.norm(A @ np.array(u) - b)
#aqui usamos la funcion de numpy linalg.norm que hace la norma del residuo y en su argumetno esta la multiplicacion de la matriz con el vector

    valores_N.append(N)
    tiempos.append(tiempo)

    print(f"n = {n}, N = {N}, tiempo = {tiempo:.6f} s, residuo = {residuo:.3e}")
    
plt.plot(valores_N, tiempos, 'o-')
plt.xlabel('N incognitas')
plt.ylabel('Tiempo de ejecucion (s)')
plt.title('Tiempo de la eliminacion gaussiana')
plt.grid(True)
plt.show()