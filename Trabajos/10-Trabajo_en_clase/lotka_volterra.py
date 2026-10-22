#TRABAJO EN CLASE 10 - METODO DE RK4 EN PYTHO
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt


def f(t, u, alpha, beta, gamma, delta):
    x, y = u
    dxdt = alpha*x - beta*x*y
    dydt = delta*x*y - gamma*y
    
    return np.array([dxdt, dydt], dtype=float)
    
def rk4(t0,tf,alpha, u0, h, beta, gamma, delta ):
    
    N = int(round((tf - t0) / h)) 
    t = np.linspace(t0, tf, N + 1)
    u= np.zeros((N + 1, 2))
    u[0] = u0
    
    for i in range(N):
        k1 = h*f(t[i], u[i], alpha, beta, gamma, delta)
        k2 = h*f(t[i] + 0.5*h, u[i] + 0.5*k1, alpha, beta, gamma, delta )
        k3 = h*f(t[i] + 0.5*h, u[i] + 0.5*k2, alpha, beta, gamma, delta)
        k4 = h*f(t[i] + h, u[i] + k3 , alpha, beta, gamma, delta)
        u[i + 1] = u[i] + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
    
    return t, u
    
def main():
    beta=0.4
    gamma=0.4
    alpha = 1.1
    delta= 0.1
    x0=10
    y0=5
    t0=0
    tf=30
    h=0.1
    
    u0 = np.array([10, 5])
    t, u = rk4(t0,tf,alpha, u0, h, beta, gamma, delta )
    
    x=u[:, 0]
    y= u[:, 1]
# plt.savefig('nombre_del_archivo.png')

#Grafica


    plt.figure()

    # Graficamos ambas poblaciones con diferente color y estilo
    plt.plot(t, x, 'o-', label='Presas')
    plt.plot(t, y, 'o-', label='Predadores')

    # Agregamos titulo, etiquetas y leyenda
    plt.title('Poblaciones de presas y predadores')
    plt.xlabel('Tiempo')
    plt.ylabel('Poblacion')
    plt.legend()
    plt.grid(True)
    plt.savefig('/Users/efrain/Desktop/Computacional/Tema08/poblaciones.png', dpi=300)
    plt.show()

    # GRAFICA 2: PLANO DE FASE

    plt.figure()

    # Graficamos predadores en funcion de presas
    plt.plot(x, y, 'o-', label='Trayectoria')

    # Marcamos el estado inicial
    plt.plot(x[0], y[0], 'o-', label='Estado inicial')

    # Agregamos titulo, etiquetas y leyenda
    plt.title('Plano de fase')
    plt.xlabel('Presas')
    plt.ylabel('Predadores')
    plt.legend()
    plt.grid(True)
    # Guardamos la segunda grafica
    plt.savefig('/Users/efrain/Desktop/Computacional/Tema08/plano_fase.png', dpi=300)
    plt.show()
main()
#RESPUESTAS BREVES 

#1. las presas llegan a su maximo primero que los predadores, las presas lo hacen en t=10 y los predadores un poco despues, esto se debe a que los mientras aumenta el numero de presas, comienza a aumnetar en numero de predadores ya que se alimentas de estos, y si bajan las presas, despues bajan los predadores y asi.

#2. Justamente este diagrama es lo que justifica lo que explique anteriormente, en como representa un comportamiento periodico en ambas poblaciones, y esta se repite, no hay casos de que una poblacion se extinga lo cual seria importante tomar en cuenta ya analisis mas realista

