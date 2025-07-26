# Ejercicio clase 3
# Recibir un nombre y mostrarlo letra a letra, luego mostrar el nombre al revés.
nombre = input("inserte nombre:")
for i in nombre:
    print(i)
print("nombre al reves:")
reversa = []
longitud = len(nombre)
while longitud > 0:
    longitud -= 1
    reversa.append(nombre[longitud])
nombre_reverso = ""
for i in reversa:
    nombre_reverso += i
print(nombre_reverso)