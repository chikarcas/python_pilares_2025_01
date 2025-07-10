print("Inversión de nombre")
nombre=input("escribe tu nombre: ")
print(nombre)
x=nombre
cadena=[]
for i in x:
    cadena.append(i)
#print(cadena)
cadena.reverse()
#print(cadena)
reversa=""
for i in cadena:
    reversa +=i
print(reversa)