#dic={'Esteban': 17, 'Marco':66 }
#print(dic['Marco'])
dic={}
x=1
list = []
while x==1:
    nombre= input('Escribe tu nombre: ')
    #print(nombre)
    edad= int(input('Escribe tu edad: '))
    num=int(input('Escribe tu número de celular: '))
    dir=input('Escribe tu dirección: ')
    #dic = {edad, num, dir}
    dic = {'Nombre':nombre, 'Edad':edad, 'Número de celular':num, 'Dirección':dir}
    list.append(dic)
    #print(dic)
    x= int(input('Si deseas agregar otro dato escriba 1, si no desea agregar otro dato escriba 0: '))
else:
    print(list)