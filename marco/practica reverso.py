#Primero usamos la función print() la cual nos mostrará que es lo que hará nuestro
# programa.
print("Este programa nos pide escribir un nombre y nos devuelte el nombre en reversa.")

#Luego almacenaremos un nombre que introduciremos mediante el teclado usando
# la función input().
nombre = input("Escribe un nombre: ")

#Este es una función print() de prueba para ver si se almaceno correctamente
# el nombre.
print("EL nombre escrito fue:", nombre)

#Posteriormente creamos una lista vacia donde almacenaremos todas las letras de
# nuestro nombre.
listanombre = []

#En este paso usamos un ciclo for para ir recorriendo y extrayendo todas las letras
# de nuestra cadena #y almacenarlas en la lista vacia antes creada con el método
# para listas append().
for i in nombre:
    listanombre.append(i)

#Este es un print de prueba para ver como quedo la lista.
print("La lista creada es:", listanombre)

#Invierto la lista con el metodo reverse().
listanombre.reverse()

#Creo una cadena vacia para almacenar las letras de mi lista ya invertida.
nombreversa = ""

#Creo  un ciclo for para poder ir extrayendo los elementos de mi lista ya
# invertida y sumarlos a la cadena vacia para que me genere la cadena
# final ya con el nombre en reversa.
for i in listanombre:
    nombreversa += i

#Este ees el print final que muestra el resultado.
print("El nombre en reversa es:", nombreversa)