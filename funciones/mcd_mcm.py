def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mcm(a, b):
   return abs(a * b) // mcd(a, b)

print("Maximo comun divisor de 24 y 36:", mcd(24, 36))  
print("Minimo comun multiplo de 24 y 36:", mcm(24, 36))   
