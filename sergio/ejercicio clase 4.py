# Ejercicio clase 4
# Recibir una palabra y decir si es palindromo o no .
palabra = input("inserte palabra:")
palabra_m = palabra.lower() 
reversa = []
longitud = len(palabra_m)
while longitud > 0:
    longitud -= 1
    reversa.append(palabra_m[longitud])
normal = []
for i in palabra_m:
    normal.append(i)
Espalindromo = True
for i in normal:
    if normal[i] != reversa[i]:
        Espalindromo = False
if Espalindromo == False:
        print ("La palabra: ", palabra_m, "no es un palindromo")
if Espalindromo == True:
    print ("La palabra: ", palabra_m, " su palindromo es: ", reversa)
