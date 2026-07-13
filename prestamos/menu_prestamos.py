from utils.persistencia import cargar_datos,guardar_datos
from prestamos.prestamos import mostrar_prestamos,realizar_prestamos
from utils.entradas import pedir_numero,pedir_texto,pedir_booleano
from utils.helpers import buscar_por_id
from datetime import date

RUTA_DE_PRESTAMOS = 'data/prestamos.json'
prestamos = cargar_datos(RUTA_DE_PRESTAMOS)

RUTA_DE_USUARIOS = 'data/usuarios.json'
usuarios = cargar_datos(RUTA_DE_USUARIOS)

RUTA_DE_LIBROS = 'data/libros.json'
libros = cargar_datos(RUTA_DE_LIBROS)


def menu_prestamos():
    while True:
        print("""
              1, Mostrar Prestamos
              2. Registrar prestamos
              3. Registrar devolucion
              4. Salir
              """)
        
        opcion = pedir_numero('Elige una opcion: ')
        if opcion == 1:
            mostrar_prestamos(prestamos)
        elif opcion == 2:
            id_usuario = pedir_numero('Id_del usuario: ')
            usuario = buscar_por_id(usuarios, id_usuario)
            id_libro = pedir_numero('Id del libro: ')
            libro = buscar_por_id(libros, id_libro)
            if not usuario:
                print('usuario no encontrado')
            elif not libro:
                print('libro no encontrado')
            else: 
                realizar_prestamos(prestamos,usuarios, usuario,libros, libro)
                guardar_datos(RUTA_DE_PRESTAMOS, prestamos)
        elif opcion == 3:
            id_prestamo = pedir_numero('Id del prestamo: ')
            item_prestamo = buscar_por_id(prestamos, id_prestamo)
    
            if not item_prestamo:
                print('prestamo no encontrado')
            elif item_prestamo['devuelto']:
                print('este prestamo ya fue devuelto')
            else:
              devolucion = pedir_booleano('Quieres hacer la devolucion del libro: ')
              if devolucion:
                  item_prestamo['devuelto'] = True
                  item_prestamo['fecha_devolucion'] = str(date.today())
                  guardar_datos(RUTA_DE_PRESTAMOS, prestamos)
            
                  libro = buscar_por_id(libros, item_prestamo['id_libro'])
                  if libro:
                     libro['disponible'] = True
                     guardar_datos(RUTA_DE_LIBROS, libros)
                  print('Devolucion exitosa')
              else:
               print('devolucion cancelada')
        elif opcion == 4:
            break