import math

def area_circulo(radio):
   
    return math.pi * radio**2

def volumen_cilindro(radio, altura):
   
    return area_circulo(radio) * altura

print("Área de un círculo de radio 5:", area_circulo(5))
print("Volumen de un cilindro de radio 5 y altura 10:", volumen_cilindro(5, 10))
