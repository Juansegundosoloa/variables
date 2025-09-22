def calcular_factura(cantidad, iva=21):
    
    total = cantidad * (1 + iva / 100)
    return total

print(calcular_factura(60))      
   
