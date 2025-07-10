def saludo(n):
    """Esta funcion imprime un saludo a la persona que se escrba como argumento"""
    print("Hola "+ n)
    return
def suma(a, b):
    '''Este programa nos devuelve el resultado de la suma impresa de dos numeros dados '''
    print(a+b)
    return
def descuento(pr, des):
    "Este programa  te da el precio con descuento de un producto"
    print("Total con descuento: "+ str(pr-pr*des/100))
    print('Total descontado: '+ str(pr*des/100))
    return
descuento(100, 20)