import numpy as np
import matplotlib.pyplot as plt


archivo = 'tiempos.txt'
datos = np.loadtxt(archivo)

hilos = datos[:, 0]
tiempo = datos[:, 1]

# Calcular Speedup (asumiendo que la primera fila corresponde a 1 hilo)
speedup = tiempo[0] / tiempo

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))

# Tiempo de ejecución vs Número de hilos
ax1.plot(hilos, tiempo, marker='o', linestyle='-', linewidth=2, label='Tiempo medido')
ax1.set_xlabel('Número de hilos ($N$)')
ax1.set_ylabel('Tiempo de ejecución (s)')
ax1.set_title('Tiempo de Ejecución vs. Hilos')
ax1.set_xticks(hilos)
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.legend()

# Speedup vs Número de hilos
ax2.plot(hilos, speedup, marker='s', linestyle='-', linewidth=2, label='Speedup medido')
ax2.plot(hilos, hilos / hilos[0], linestyle='--', color='gray', label='Escalamiento ideal')
ax2.set_xlabel('Número de hilos ($N$)')
ax2.set_ylabel('Speedup ($T_1 / T_N$)')
ax2.set_title('Speedup vs. Hilos')
ax2.set_xticks(hilos)
ax2.grid(True, linestyle='--', alpha=0.6)
ax2.legend()

plt.tight_layout()
plt.savefig('tiempo_vs_hilos.png', dpi=300)
plt.show()
