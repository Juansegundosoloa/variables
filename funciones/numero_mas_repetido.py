lista = [1,3,3,2,5]
def mas_repetida(lista):
    conteo ={}
    for num in lista:
        if num in conteo:
            conteo [num] +=1
        else:
            conteo [num] =1 
    print (conteo)
    max_count = 0
    frecuente = None
    for num, count in conteo.items():
        if count > max_count:
            max_count = count
            frecuente = num
    return frecuente
numero_mas_frecuente =mas_repetida(lista) 
print (numero_mas_frecuente)      