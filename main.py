from menu import menu
from libros import mostar_libros,agregar_libro,buscar_por_id
from entradas import pedir_datos_libro,pedir_numero
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
      break