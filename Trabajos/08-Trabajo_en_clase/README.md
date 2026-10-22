Resultados finales;

Metodo de Jacobi
Solución aproximada:[0.98143236 1.94429708 2.85145888 3.61007957 3.97877984 3.32625995]
Número de iteraciones: 41
Norma final del residuo: 6.879926e-09
¿Alcanzó la tolerancia?: SI
Metodo de Gauss Seidel
Solución aproximada:[0.98143236 1.94429708 2.85145888 3.61007957 3.97877984 3.32625995]
Número de iteraciones: 22
Norma final del residuo: 5.611383e-09
¿Alcanzó la tolerancia?: Si


Respuestas del analisis;
 a. En los dos la norma del residuo decrese conforme aumentan las iteraciones, ambas aproximan correctamente, pero Gauss Seidel lo hace con una mejor convergencia que Jacobi.
 
 b. Gauss Seidel alcanza las 22 iteraciones, ya que esta usa los valores actualizados de cada componente y Jacobu usa valores de la interacion anterior, por eesto mismo es que Jacobi alcanza las 41 iteraciones.
 
 c. Si, los dos metodos cumplieron con la tolerancia de 10^-8 y los residuos finales serian, Jacobi = 6.879926e-09, Gauss-Seidel = 5.611383e-09