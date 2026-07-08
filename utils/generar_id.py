def generador_id(lista):
    if not lista:
        return 1
    
    return max(lista, key= lambda elemento : elemento['id'])['id']+1