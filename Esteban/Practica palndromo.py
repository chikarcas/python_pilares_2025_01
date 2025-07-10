print("Detector de palindromos: ")
palabra=input("Escribe una palabra:").lower()
print("palabra escrita: ", palabra)
x=palabra
cadena=[]
for i in x:
    cadena.append(i)
#print(cadena)
cadena.reverse()
#print(cadena)
reversa=""
for i in cadena:
    reversa +=i
print("palabra en reversa:",reversa)
if palabra==reversa:
    print("Es un palindromo")
else:
    print("No es un palindromo")