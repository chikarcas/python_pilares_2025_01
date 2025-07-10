'''dic = {"Fernando":35, 'Esteban':17, 'Marco':66, 'Francisco':65, 'Laura':57}
print(dic["Fernando"])
a=10
for i in dic:
    dic[i] += a

print(dic)
dic["Alma"] = 27
print(dic)'''
print('Este programa crea una base de datos donde registra tu nomre y edad: ')
x=1
dic={}
while x == 1: 
    nombre= input('Escribe tu nombre: ')
    #print(nombre)
    edad= int(input('Escribe tu edad: '))
    dic[nombre] = edad
    print(dic)
    x= int(input('Si deseas agregar otro dato escriba 1, si no desea agregar otro dato escriba 0: '))
else:
    print(dic)