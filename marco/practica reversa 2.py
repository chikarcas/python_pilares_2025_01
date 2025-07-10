
print("Este texto sera invertido.")
texto = input("escribe un nombre: ")
#print(texto)
listatexto=[]
for i in texto:
    listatexto.append(i)
#print(listatexto)
listatexto.reverse()
textoversa = ""
for i in listatexto:
    textoversa += i
print(textoversa)
