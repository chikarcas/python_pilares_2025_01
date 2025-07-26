'''dic = {key: val, key2: val2}
pers = {"nombre": "Fer", "Edad": 35}
pers["nombre"] Va imprimir "Fer"
Añadir una llave nueva:
pers ["Tel"] = 556668855
Actividad agregar una llave a un diccionario nuevo
'''
print("Crear un directiorio vacio dondel usuario debera agregar las llaves con su respectivo valor")

diccionario = {}
sn = int(input("Que desea Realizar: \n0 = Añadir llave y valor\n1 = mostrar lista\n3 = salir\n"))
while sn  <= 1:
    if sn == 0:
        key = (input("Ingrese el nombre de la llave: \n"))
        val = (input("Ingrese el valor de la llave:\n"))
        diccionario[key] = val
        sn = int(input("Que desea Realizar: \n0 = Añadir llave y valor\n1 = mostrar lista\n3 = salir\n"))
    elif sn == 1:
        print(diccionario)
        sn = int(input("Que desea Realizar: \n0 = Añadir llave y valor\n1 = mostrar lista\n 3 = salir\n"))
print ("Saliendo...")