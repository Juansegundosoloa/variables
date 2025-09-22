def factorial(numero):
    if numero < 0:
        return "El número debe ser entero positivo"
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

print(factorial(5))
