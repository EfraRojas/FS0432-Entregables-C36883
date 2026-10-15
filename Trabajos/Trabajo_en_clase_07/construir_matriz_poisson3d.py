import numpy as np


def poisson_3d(n):

    if not isinstance(n, (int, np.integer)) or n < 1:
        raise ValueError("n debe ser un entero positivo")

    N = n**3
    h = 1.0 / (n + 1)
    A = np.zeros((N, N), dtype=float)
    b = np.ones(N, dtype=float)

    for k in range(n):
        for j in range(n):
            for i in range(n):
                p = i + n*j + n*n*k
                A[p, p] = 6.0
                if i > 0:
                    A[p, p-1] = -1.0
                if i < n-1:
                    A[p, p+1] = -1.0
                if j > 0:
                    A[p, p-n] = -1.0
                if j < n-1:
                    A[p, p+n] = -1.0
                if k > 0:
                    A[p, p-n*n] = -1.0
                if k < n-1:
                    A[p, p+n*n] = -1.0

    return A / h**2, b
