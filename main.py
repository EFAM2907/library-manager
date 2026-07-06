from menu import menu
from libros import mostar_libros,agregar_libro,buscar_por_id,prestar_libro,devolver_libro,obtener_libros_disponibles,obtener_libros_prestados,buscar_por_categoria
from entradas import pedir_datos_libro,pedir_numero,pedir_texto
from persistencia import guardar_libros,cargar_libros

RUTA_DE_LIBROS = 'libros.json'
libros = cargar_libros(RUTA_DE_LIBROS)


while True:
    menu()
    opcion = input('Elige una opcion: ')
    
    if opcion == '1':
        mostar_libros(libros)
    elif opcion == '2':
        titulo, autor,categoria,anio = pedir_datos_libro()
        agregar_libro(libros, titulo, autor,categoria,anio )
        guardar_libros(RUTA_DE_LIBROS, libros)
    elif opcion == '3':
        numero = pedir_numero('numero de Id: ')
        libro = buscar_por_id(libros, numero)
        if libro is not None:
            print(f"""
            ID:        {libro['id']}
            Título:    {libro['titulo']}
            Autor:     {libro['autor']}
            Categoría: {libro['categoria']}
            Año:       {libro['anio']}
            Prestado:  {libro['prestado']}
                  """)
        else:
            print('no se encontro el libro')
    elif opcion == '4':
        
        numero_id = pedir_numero('numero de Id: ')
        libro = buscar_por_id(libros, numero_id)
        if libro:
          if prestar_libro(libro):
             guardar_libros(RUTA_DE_LIBROS, libros)  
             print('libro prestado con exito')
          else:
              print('libro no disponible')
        else:
            print('libro no encontrado por ID')
    elif opcion == '5':  
      id= pedir_numero('numero de id: ')
      libro= buscar_por_id(libros, id)
      if libro:
          if devolver_libro(libro):
            guardar_libros(RUTA_DE_LIBROS, libros)  
            print('libro devuelto con exito')
          else:
              print('el libro no estaba prestado')
      else:
          print('libro no encontrado')
    elif opcion == '6':
       libros_disponibles = obtener_libros_disponibles(libros)
       if libros_disponibles:
            mostar_libros(libros_disponibles)
       else:
           print('no hay libros disponibles')
    elif opcion == '7':
        libros_prestados =  obtener_libros_prestados(libros)
        if libros_prestados:
            mostar_libros(libros_prestados)
        else:
            print('no hay libros prestados')
    elif opcion == '8':
        categoria = pedir_texto('Que categoria prefieres: ').lower()
        filtrado_categorias = buscar_por_categoria(libros, categoria)
        if filtrado_categorias:
            mostar_libros(filtrado_categorias)
        else:
            print('no tenemos esa categoria')
    elif opcion == '9':
      break