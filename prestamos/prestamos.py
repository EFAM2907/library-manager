from utils.helpers import generador_id
from utils.entradas import pedir_booleano
from utils.persistencia import guardar_datos,cargar_datos
from datetime import date

RUTA_DE_USUARIOS = 'data/usuarios.json'
usuarios = cargar_datos(RUTA_DE_USUARIOS)

RUTA_DE_LIBROS = 'data/libros.json'
libros = cargar_datos(RUTA_DE_LIBROS)

def mostrar_prestamos(prestamos):
    for prestamo in prestamos:
        print(f"""
        "id": {prestamo['id']}
        "id_usuario": {prestamo['id_usuario']},
        "id_libro": {prestamo['id_libro']},
        "fecha_prestamo": {prestamo['fecha_prestamo']},
        "fecha_devolucion": {prestamo['fecha_devolucion']},
        "devuelto": {prestamo['devuelto']}
              """)
        
        
def registrar_prestamos(prestamos, id_usuario,id_libro, fecha_prestamo):
    prestamos.append({
        'id': generador_id(prestamos),
        'id_usuario': id_usuario,
        'id_libro': id_libro,
        'fecha_prestamo': fecha_prestamo,
        'fecha_devolucion': None,
        'devuelto': False
        
    })
    

def realizar_prestamos(prestamos, usuarios, usuario,libros, libro):
    if not usuario['activo']:
        print('el usuario esta inactivo')
        activo = pedir_booleano('Quieres activar este usuario: ')
        if activo:
            usuario['activo'] = True
            guardar_datos(RUTA_DE_USUARIOS,usuarios)
        else:
            print('registro cancelado')
            return
    if libro['prestado']:
        print('El libro ya esta prestado')     
        return
 
    fecha_prestamo = str(date.today())  # '2026-07-10'
    registrar_prestamos(prestamos,usuario['id'],libro['id'],fecha_prestamo)
    libro['prestado'] = True
    guardar_datos(RUTA_DE_USUARIOS, usuarios)
    guardar_datos(RUTA_DE_LIBROS,libros)
    print('Prestamos realizado con exito')
        
         # elif opcion == 2:
          #  id_usuario = pedir_numero('Id_del usuario: ')
           # usuario = buscar_por_id(usuarios, id_usuario)
           # id_libro = pedir_numero('Id del libro: ')
           # libro = buscar_por_id(libros, id_libro)
           # if not usuario:
            #   print('usuario no encontrado')
            #elif not libro:
            #   print('libro no encontrado')
            #elif not usuario['activo']:
            #   print('usuario inactivo')
            #elif not libro['disponible']:
            #   print('libro no disponible')
            #else:
            #   fecha_prestamo = str(date.today())  # '2026-07-10'
            #   registrar_prestamos(prestamos,usuario['id'],libro['id'],fecha_prestamo)