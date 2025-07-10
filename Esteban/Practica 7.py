dic={}
list=[]
x=1
while x==1:
    key=input('Escribe que dato deseas agregar: ')
    entr=input("Agrega los dato solicitado: ")
    dic[key]=entr
    print(dic)
    x=int(input('Si deseas agregar otro dato escriba 1, por el contrario escriba 0:'))
else:
    print(dic)
'''dic={}
keys=[]
val=[]
x=1
y=0
if x==1:
    key=input('Escibe el dato que deseas agregar: ')
    keys.append(key)
    x=int(input('Si deseas agregar otro dato escriba 1, por el contrario escriba 0:'))
    print(keys)
while x==1:
    valor=input(keys[0])        
    val.append(valor)
    x=int(input('Si deseas agregar otro dato escriba 1, por el contrario escriba 0:'))
    print(val)'''