# Parte 1: Preguntar al usuario qué tipos de datos quiere ingresar

print("¡Hola! Primero, dime qué tipos de datos quieres que te pida.")
print("Escribe un tipo de dato (ej. 'nombre', 'edad'). Cuando termines, escribe 'listo'.")

tipos_de_datos_a_pedir = [] # Esta lista guardará los nombres de los datos que quieres

while True:
    tipo_actual = input("Tipo de dato (o 'listo' para terminar): ").strip().lower()

    if tipo_actual == 'listo':
        break # Si el usuario escribe 'listo', salimos de este bucle
    elif tipo_actual: # Asegurarse de que no esté vacío
        tipos_de_datos_a_pedir.append(tipo_actual)
    else:
        print("Por favor, ingresa un tipo de dato válido o 'listo'.")

if not tipos_de_datos_a_pedir:
    print("No seleccionaste ningún tipo de dato. ¡Adiós!")
else:
    # Parte 2: Una vez que tenemos todos los tipos, pedir los valores

    print("\n---")
    print("¡Perfecto! Ahora vamos a pedirte los valores para esos datos.")
    print("---")

    datos_ingresados = {} # Este diccionario guardará el nombre del dato y su valor

    for tipo in tipos_de_datos_a_pedir:
        valor = input(f"Por favor, ingresa tu {tipo}: ")
        datos_ingresados[tipo] = valor # Guardamos el tipo de dato y su valor en el diccionario

    # Parte 3: Mostrar todos los datos recopilados

    print("\n---")
    print("¡Hemos recopilado la siguiente información:")
    for tipo, valor in datos_ingresados.items():
        print(f"- {tipo.capitalize()}: {valor}") # .capitalize() pone la primera letra en mayúscula

    print("\n¡Gracias por usar el programa!")