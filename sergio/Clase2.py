estudiantes = [] 
print ("Legaron estudiantes?")
opcion = int(input("1 = Si  2 = No "))
if opcion == 1:
    while opcion == 1:
        nombre = input("inserte un nombre: ")
        estudiantes.append(nombre)
        print ("Añadir otro estudiante?")
        opcion = int(input("1 = Si  2 = No "))
else:
    print ("No llegaron")
print ("Los alumnos que llegaron fueron: ")
for alumno in estudiantes:
    print (alumno)
print ("Con la cantidad de :", len(estudiantes), "integrantes")