import cmath
def saludo(n):
    """Esta funcion imprime un saludo a la persona que se escrba como argumento."""
    print("Hola "+ n)
    return
def suma(a, b):
    '''Este programa nos devuelve el resultado de la suma impresa de dos numeros dados. '''
    print(a+b)
    return
def descuento(pr, des):
    """Este programa  te da el precio con descuento de un producto."""
    print("Total con descuento: "+ str(pr-pr*des/100))
    print('Total descontado: '+ str(pr*des/100))
    return
def tipo(x):
    '''Este programa te devuelve el tipo de variable que es.'''
    print('El tipo de variable es: '+ str(type(x)))
    return
def numprim(y):
    '''Este programa detacta si un numero es primo o no.'''
    for i in range(2, y):
        mod=y%i
        if mod !=0:
            continue
        else:
            return print('No es un numero primo.')
    return print('Es un numero primo.')
def fg(a, b, c):
    '''Este programa saca la respuesta con una formula general'''
    list=[]
    x1=-b + cmath.sqrt(b**2 - 4*a*c)/2*a
    x2=-b - cmath.sqrt(b**2 - 4*a*c)/2*a
    list.append(x1)
    list.append(x2)
    print(list)
    return list
fg(1, 0, 4)
print(fg(1, 0, 4)[0])