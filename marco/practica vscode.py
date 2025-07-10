
print("este programa nos mostrara el nombre al reves." )
nombre = input("escribe un nombre:")
print(nombre)
listanombre = []
for i in nombre:
    listanombre.append(i)
print(listanombre)
listanombre.reverse()
print(listanombre)
nombreversa = ""
for i in listanombre:
    nombreversa += i
print("el nombre en reversaa es:", nombreversa)       

