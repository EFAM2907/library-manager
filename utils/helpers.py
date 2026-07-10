def generador_id(lista):
    if not lista:
        return 1
    
    return max(lista, key= lambda elemento : elemento['id'])['id']+1


def buscar_por_id(lista, id):
    for item in lista:
        if item['id'] == id:
            return item
        
    return None



