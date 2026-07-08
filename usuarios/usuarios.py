def generar_id_usuario(usuarios):
    if not usuarios:
        return 1
    
    mayor = usuarios[0]['id']
    for usuario in usuarios:
        if usuario['id'] >mayor:
            mayor = usuario['id']
    
    return mayor +1


