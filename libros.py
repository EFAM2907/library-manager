
def generar_id(libros):
    if not libros:
        return 1
    mayor = libros[0]['id']
    for libro in libros:
      if libro['id'] > mayor:
        mayor = libro['id']
    return mayor +1

def agregar_libro (libros, titulo, autor,categoria,anio ):
    libros.append({'id': generar_id(libros), 'titulo': titulo, 'autor': autor, 'categoria':categoria,
                   'anio':anio, 'prestado': False})


def mostar_libros(libros):
    if not libros:
        print('no hay libros regristrados')
    for libro in libros:
        print(f"""
            ID:        {libro['id']}
            Título:    {libro['titulo']}
            Autor:     {libro['autor']}
            Categoría: {libro['categoria']}
            Año:       {libro['anio']}
            Prestado:  {libro['prestado']}
            
            ==========================================              
              """)
        
        
def buscar_por_id(libros, id):
   for libro in libros:
       if libro['id'] == id:
        return libro
   return None
