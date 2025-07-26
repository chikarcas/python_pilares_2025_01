'''Crear un programa que le pregunte al usuario 
nombre, edad, telefono, y direccion de una persona 
y se almacene en un diccionario y pregunte si se desea agregar un contactoy al final imprimir 
el diccionario
ej.

Nombre:"Fer", edad: 35, Tel: 55 555 5555, direc: "Av. principal" 

nombre = input("Escribe el nombre: ")
'''

print("La finalidad de este programa es realizar un agenda de contactos asi como su Nombre, Apellido, Edad, numero  de Telefono y Direccion")
opcion = True
sn = 0
agenda=[]#lista 
contactos = {} #diccionario
while opcion == True:
    sn=int(input("Desea agregar un contacto?(1=Si/0=No) "))
    if sn == 1:    
        contactos["Nombre"] = input("Nombre: ")
        contactos["Apellido"] = input("Apellido: ")
        contactos["Tel"] = input("Numero telefonico: ")
        contactos["dir"] = input("Direccion: ")
        agenda.append(contactos)
    elif sn == 0:
        opcion = False
        print("\nLos contactos de la agenda son :\n")    
        print(agenda)
