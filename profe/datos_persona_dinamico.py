# Mostramos un mensaje al usuario para que sepa que realizará el programa.
print("Este programa crea un diccionario con datos personales de un individuo.")

#M Creamos el dccionario vacio al cual poesteriormente añadiremos las entradas.
persona = {}

# Creamos la variable que almacenara el valor para seleccionar si se crea una entrada, o no.
cond = input("¿Quieres agregar un dato sobre la persona? (Sí = 1, No = Cualquier otro valor): ")

while cond != "0":
    if cond == "1":
        key = input("Ingresa el tipo de dato a solicitar: ")
        value = input("Ingresa el valor del dato solicitado: ")
        persona[key] = value
        cond = input("¿Quieres agregar un dato sobre la persona? (Sí = 1, No = 0): ")
    elif cond == "0":
        print(persona)
    else:
        while cond != "1" and cond != "0":
            cond = input("Introduce un valor valido (Sí = 1, No = 0): ")

print("El programa ha fiinalizado, el diccionario generado es:")
print(persona)