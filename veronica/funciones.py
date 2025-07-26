import math as m
import cmath as cm

def area_circulo (radio):
    m.pi
    area = m.pi * (radio ** 2)
    return area 

resultado = area_circulo 
print ("el ara del circualo es", resultado)

def volumen_cilindro (radio, altura):
    pi = 3.1416
    volumen = area_circulo(radio) * altura 
    return volumen 

resultado = volumen_cilindro(1, 1)
print("el volumen es", resultado)

print (area_circulo(1))

def formula_general(a,b,c):
    x1 = - b + cm.sqrt(b ** 2 - 4 * a * c) / (2 * a)
    x2 = - b - cm.sqrt(b ** 2 - 4 * a * c) / (2 * a)
    x = [x1, x2]
    return x

resultado = formula_general (1, -1, 1)
print (resultado)