agenda=[]
print("La finalidad de este programa es realizar un agenda de contactos asi como su Nombre, Apellido, Edad, numero  de Telefono y Direccion")
opcion = True
sn = 0
#while opcion == True:
#    sn=input("Desea agregar un contacto?(1=Si/0=No) ")
#    if sn == 1:    
contactos = {}
contactos["Nombre"] = input("Nombre: ")
contactos["Apellido"] = input("Apellido: ")
contactos["Tel"] = input("Numero telefonico: ")
contactos["dir"] = input("Direccion: ")
agenda.append(contactos)
contactos["Nombre"] = input("Nombre: ")
contactos["Apellido"] = input("Apellido: ")
contactos["Tel"] = input("Numero telefonico: ")
contactos["dir"] = input("Direccion: ")
agenda.append(contactos)

#    elif sn == 0:
#opcion = False
print("\nLos contactos de la agenda son :\n")
print(agenda)