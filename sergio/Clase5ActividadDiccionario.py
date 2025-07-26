'''Crear un programa que le pregunte al usuario 
nombre, edad, telefono, y direccion de una persona 
y se almacene en un diccionario y al final imprimir 
el diccionario
ej.

Nombre:"Fer", edad: 35, Tel: 55 555 5555, direc: "Av. principal" 

nombre = input("Escribe el nombre: ")
'''

print("La finalidad de este programa es realizar un agenda de contactos asi como su Nombre, Apellido, Edad, numero  de Telefono y Direccion")
contactos = {}
contactos["Nombre"] = input("Nombre: ")
contactos["Apellido"] = input("Apellido: ")
contactos["Tel"] = input("Numero telefonico: ")
contactos["dir"] = input("Direccion: ")
print("\nLa direccion agregada es :\n")
for i in contactos:
    print(contactos[i])
