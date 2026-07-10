from utils.entradas import pedir_numero,pedir_texto,pedir_booleano
from usuarios.usuarios import mostar_usuarios,agregar_usuario,pedir_datos_usuario, actualizar_usuario,eliminar_usuario
from utils.persistencia import cargar_datos,guardar_datos
from utils.helpers import buscar_por_id

def menu_usuarios():
    
    RUTA_DE_USUARIOS = 'data/usuarios.json'
    usuarios = cargar_datos(RUTA_DE_USUARIOS)
    
    while True:
      print("""\n ======= SISTEMA DE USUARIOS =======
          1. Mostrar usuarios
          2. Agregar usuarios
          3. Buscar Usuario
          4. Actualizar usuario
          5. Eliminar usuario
          6. salir
          """)
     
      opcion = pedir_numero('Elige una opcion: ')
      if opcion == 1:
          mostar_usuarios(usuarios)
      elif opcion == 2:
          nombre, email = pedir_datos_usuario()  
          agregar_usuario(usuarios, nombre,email)
          guardar_datos(RUTA_DE_USUARIOS, usuarios)
      elif opcion == 3:
          id_usuario = pedir_numero('Id del usuario: ')
          usuario = buscar_por_id(usuarios, id_usuario)
          if usuario:
              print(f"""
            Nombre: {usuario['nombre']}
            Email: {usuario['email']}
            Activo: {usuario['activo']}
                """)
          else:
              print('usuario no encontrado')
      elif opcion == 4:
          id_usuario =pedir_numero('Id del usuario: ')
          usuario = buscar_por_id(usuarios, id_usuario)
          if usuario:
              nombre, email = pedir_datos_usuario()
              activo = pedir_booleano('esta activo? ')
              actualizar_usuario(usuario, nombre, email,activo)
              guardar_datos(RUTA_DE_USUARIOS, usuarios)
          else:
              print('no se encontro el usuario')
      elif opcion == 5:
          id_usuario = pedir_numero(' ID del usuario: ')
          usuario = buscar_por_id(usuarios, id_usuario)
          if usuario:
            eliminar_usuario(usuarios, usuario)
            guardar_datos(RUTA_DE_USUARIOS, usuarios)
            print('usuario eliminado')
          else:
              print('no se encontro el usuario')
      elif opcion == 6:
          break