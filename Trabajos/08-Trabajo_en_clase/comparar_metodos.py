import numpy as np
import matplotlib.pyplot as plt

def jacobi(A, b, x0, tolerancia, iter_maxima):
    n = len(b)
    x = x0.copy()

    residuo = np.linalg.norm(b - A @ x)
    residuos = [residuo]
     
     
    for k in range(iter_maxima):
        if residuos[-1] < tolerancia:
            break
            
        x_nuevo = x.copy()

        for i in range(n):

            suma = 0.0

            for j in range(n):
                if j != i:
                    suma += A[i, j] * x[j]

            x_nuevo[i] = (b[i] - suma) / A[i, i]

        x = x_nuevo

        residuo = np.linalg.norm(b - A @ x)
        residuos.append(residuo)
        
    return x, residuos


def gauss_seidel(A, b, x0, tolerancia, iter_maxima):

    x = x0.copy()
    n = len(b)

    residuo = np.linalg.norm(b - A @ x)
    residuos = [residuo]

    for k in range(iter_maxima):

        if residuos[-1] < tolerancia:
            break

        for i in range(n):
            suma = 0.0
            
            for j in range(n):

                if j != i:
                    suma += A[i, j] * x[j]

            x[i] = (b[i] - suma) / A[i, i]

        residuo = np.linalg.norm(b - A @ x)

        residuos.append(residuo)

    return x, residuos



A = np.array([
    [ 3, -1,  0,  0,  0,  0],
    [-1,  3, -1,  0,  0,  0],
    [ 0, -1,  3, -1,  0,  0],
    [ 0,  0, -1,  3, -1,  0],
    [ 0,  0,  0, -1,  3, -1],
    [ 0,  0,  0,  0, -1,  3]
], dtype=float)

b = np.array([1, 2, 3, 4, 5, 6], dtype=float)

x0 = np.zeros(6)
tolerancia = 1e-8
iter_maxima = 1000


x_jacobi, residuos_jacobi = jacobi(A, b, x0.copy(), tolerancia, iter_maxima)
x_gauss, residuos_gauss = gauss_seidel(A, b, x0.copy(), tolerancia, iter_maxima)


#restamos uno ya que la lista incluye el residuo inicial
iter_jacobi = len(residuos_jacobi) - 1
iter_gauss = len(residuos_gauss) - 1

residuo_final_jacobi = residuos_jacobi[-1]
residuo_final_gauss = residuos_gauss[-1]
convergencia_jacobi = residuo_final_jacobi < tolerancia
convergencia_gauss = residuo_final_gauss < tolerancia


# Resultados
print("Metodo de Jacobi")
print("Solución aproximada:")
print(x_jacobi)
print("Número de iteraciones:", iter_jacobi)
print(f"Norma final del residuo: {residuo_final_jacobi:.6e}")
print("¿Alcanzó la tolerancia?:", convergencia_jacobi)


print("Metodo de Gauss Seidel")
print("Solución aproximada:")
print(x_gauss)
print("Número de iteraciones:", iter_gauss)
print(f"Norma final del residuo: {residuo_final_gauss:.6e}")
print("¿Alcanzó la tolerancia?:", convergencia_gauss)


# Grafica
k_jacobi = np.arange(len(residuos_jacobi))
k_gauss = np.arange(len(residuos_gauss))

plt.figure(figsize=(15, 10))
plt.semilogy(k_jacobi,residuos_jacobi,"o-", label="Jacobi")
plt.semilogy( k_gauss,residuos_gauss,"o-",label="Gauss-Seidel")

plt.axhline(y=tolerancia,color="red",linestyle="--",label="Tolerancia = 1e-8")

plt.title("Convergencia de Jacobi y Gauss-Seidel")
plt.xlabel("Número de iteraciones k")
plt.ylabel("Norma del residuo")

plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("residuos.png", dpi=300)
plt.show()