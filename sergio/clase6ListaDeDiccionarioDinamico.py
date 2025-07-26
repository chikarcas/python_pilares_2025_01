print("Actividad:\nConvinar el diccionario dinamico con la lista de diccionario")
agenda=[]
persona={}
sn = int(input("Que desea Realizar: \n0 = Añadir contacto y valores\n1 = mostrar contacto\n2 mostrar toda la agenda\n. = salir\n"))
while sn<=2:
    if sn == 0:
        key = (input("Ingrese el nombre de la llave: \n"))
        val = (input("Ingrese el valor de la llave:\n"))
        persona[key] = val
        sn = int(input("0 = Añadir llave y valor\n1 = mostrar contacto\n2 mostrar toda la agenda\n. = salir\n"))
        if sn == 2:
            agenda.append(persona)
    elif sn==2:
        pos = int(input("ingrese la posicion del contacto:\n"))
        print(agenda[pos])
        sn = int(input("0 = Añadir llave y valor\n1 = mostrar contacto\n2 mostrar toda la agenda\n. = salir\n"))        
    elif sn ==3:
        print(agenda)
print("Saliendo...") 