print("en este programa se estcibira un nombre y sera debuelto al reves")
nombre = input()
print(nombre)
listanombre = []
for i in nombre:
    listanombre.append(i)
print(listanombre)
listanombre.reverse()
nombreversa ="" 
for i in listanombre:
    nombreversa += i
print(nombreversa)       
