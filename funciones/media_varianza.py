import math

def estadisticas(lista):
    n = len(lista)
    if n == 0:
        return None  
    
    media = sum(lista) / n
    varianza = sum((x - media) ** 2 for x in lista) / n
    desviacion = math.sqrt(varianza)
    
    return {
        "media": media,
        "varianza": varianza,
        "desviacion_tipica": desviacion
    }

datos = [1, 2, 3, 4, 5]
print(estadisticas(datos))
