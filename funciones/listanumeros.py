def media(lista):
   
    if len(lista) == 0:
        return None  
    return sum(lista) / len(lista)

print(media([1,2,3,4,5,6,7,8]))  
    
