def decimal_a_binario(n):
     return bin(n)[2:]  


def binario_a_decimal(b):
    return int(b, 2)

print("Decimal 25 a binario:", decimal_a_binario(25))   
print("Binario 11001 a decimal:", binario_a_decimal("11001"))  
