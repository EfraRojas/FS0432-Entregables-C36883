#include <iostream>

//funcion que muiestre arreglo usando bucle e imprima

void muestra_notas( double* notas, int cantidad)
{
	std::cout << " Cantidad de notas validas ingresadas:  " << std::endl;
	for (int i = 0; i < cantidad; i++)
	{
	std::cout <<  i + 1 << " : " << notas[i] << std::endl;
	}	

}


// funcion void recibe puntero el array y las clasifique usando if etc, usar referencias para retornar cantidad
// de reprobados etc, e imprimir resultados en main.

void clasifica_notas( double *notas, int cantidad, int &reprobados, int &aprobados, int &sobresaliente)
{
	reprobados = 0;
	aprobados = 0;
	sobresaliente = 0;
	
	for (int i = 0; i < cantidad; i++)
	{
		if (notas[i] < 70.0) { reprobados++; }

		else if (notas[i] < 90.0) { aprobados++; }  

		else { sobresaliente++; }  
	}

}


// funcion double reciba puntero al array y num de notas, calcule y retorne el promedio e imprimirse en main

double calculo_prom( double *notas, int cantidad)
{
	double sumatoria = 0.0;

	for ( int i = 0; i < cantidad; i++ )
	{
		sumatoria += notas[i];
	}
	return sumatoria / cantidad;

}


//funcion void recibe puntero al array y num de notas, nota max y min, retornando por referencia e imprimise en main 

void MaxMin (double *notas, int cantidad, double &maxima, double &minima)
{
	maxima = notas[0];
	minima = notas[0];
	
	for ( int i = 1; i < cantidad; i++)
	{
		if (notas[i] > maxima) { maxima = notas[i]; }
		
		if (notas[i] < minima) { minima = notas[i]; }	


	}
	//aqui esto de notas tuve que buscarlo pq la verdad no se me ocurria y era mas sencillo de lo que crei
	// iterar comparando hasta que se llegue al maximo o minimo

}
//main 

int main()
{

	double notas[100];
	int cantidad = 0;
	int intentos = 0;
	double nota;

	do
	{
        std::cout << "Ingrese una nota de 0 a 100 o -1 para terminar: ";
        std::cin >> nota;

       
        if (nota == -1)
        {
            break;
        }

        intentos++;

       
        if (nota < 0.0 || nota > 100.0)
        {
            std::cout << "Nota invalida";

            continue;
        }

       
        notas[cantidad] = nota;
        cantidad++;

	} while (intentos < 100);

	if (cantidad == 0)
	{
        std::cout << " No se ingresaron notas validas";
        return 0;	
	}

	muestra_notas(notas, cantidad);
  
	int reprobados;
	int aprobados;
	int sobresalientes;

	clasifica_notas(notas, cantidad, reprobados, aprobados, sobresalientes);

	std::cout << "Clasificacion:";
	std::cout << "Reprobados: " << reprobados << std::endl;	
	std::cout << "Aprobados: " << aprobados << std::endl;	
	std::cout << "Sobresalientes: " << sobresalientes << std::endl;
	

	double promedio = calculo_prom(notas, cantidad);
		std::cout << "Promedio : " << promedio << std::endl;

	double maxima;	
	double minima;

	MaxMin(notas, cantidad, maxima, minima);

		std::cout << "Nota maxima: " << maxima << std::endl;	
		std::cout << "Nota minima: " << minima << std::endl;

		return 0;	
	


}


