def contar_palabras(cadena):
    palabras = cadena.lower().split()
    frecuencia = {}
    for palabra in palabras:
        palabra = palabra.strip(".,;:!?()[]{}\"'")
        if palabra:
            frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia


def palabra_mas_frecuente(diccionario):
   
    if not diccionario:
        return None
    palabra = max(diccionario, key=diccionario.get)
    return (palabra, diccionario[palabra])

texto = "Hola hola mundo! Este es un ejemplo. Mundo, mundo, mundo."
frecuencias = contar_palabras(texto)

print("Frecuencias:", frecuencias)
print("Palabra más frecuente:", palabra_mas_frecuente(frecuencias))
