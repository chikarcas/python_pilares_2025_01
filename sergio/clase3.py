# Funcion range
# Imprime los números del 1 al 10
# This code snippet uses a for loop to print numbers from 1 to 10
for i in range(1, 11):
    print(i)
## Imprime los números del 1 al 10, pero con un paso de 2
print("\nCon paso de 2:")
for i in range(1, 11, 2):
    print(i)
#range(1, 11, 2) inicia en 1, termina en 11 (sin incluirlo) y avanza de 2 en 2.
import numpy as np
#se importa apartir de este momento la libreria numpy
print("\nCon numpy:")
#for i in np.arange(1, 10.5, 0.5):
 #   print(i)


print("\nCon paso de 0.5:")
for i in range(1, 11):
    print(i/2)


#se comento el import numpy para ver como funciona cn un llamado directo
print("\nlibreria numpy:")
from numpy import arange
for i in arange(1, 10.5, 0.5):
    print(i)
#se comento el import numpy para ver como funciona cn un llamado directo

#APLICANDO A LISTAS 
print("\nAplicacion a Listas:")
list = [3, 4.0, True, "hola"]
# Imprime el tercer elemento de la lista
print(list [2])

#Se Crea una lista de números del 1 al 10
print("\nLista del 1 al 10 usando linspace importarndo nummpy:\n")
import numpy as np
#divide en 20 espacios los elementos del rango de 0.5 a 10
lista = np.linspace(0.5, 10, 20)
for i in lista:
    print(i)

print("\nLista del 1 al 10 usando range:\n")
for i in range(1, 20):
    print(lista[i])

print("uso de la funcion len() para saber el largo de la lista:")
len(lista)
print(len(lista))

print("Forma facil de imprimir el largo de la lista")
for i in lista:
    print(i)

print("***************************************************************************************")
#USO DE CADENAS 
print("\nUso de Cadenas:")
nombre = "Sergio"
for i in nombre:
    print(i)    
print("****************************************************************************************")
print(lista[-1])
print(nombre[-1])
print("****************************************************************************************")
# Escribir el nombre al revés usando append