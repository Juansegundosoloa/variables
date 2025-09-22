from deep_translator import GoogleTranslator #Tuve que instalar la libreria deep por que la google translator no me funcionaba
palabra = input("Ingresa una palabra: ")
traduccion = GoogleTranslator(source='es', target='en').translate(palabra)
print(traduccion)  
