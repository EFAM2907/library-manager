from utils.helpers import generador_id
from utils.entradas import pedir_texto,pedir_email


def mostar_usuarios(usuarios):
    if not usuarios:
     return[]
 
    for usuario in usuarios:
       print(f"""
          ID : {usuario['id']}
          Nombre: {usuario['nombre']}
          Email: {usuario['email']}
          Activo: {usuario['activo']}
              """)
       
       
def agregar_usuario(usuarios,nombre,email):
    usuarios.append({'id': generador_id(usuarios), 'nombre': nombre, 'email': email, 'activo':True})
    

def pedir_datos_usuario():
    nombre = pedir_texto('Nombre de usuario: ')
    email = pedir_email()
     
    return nombre, email


def actualizar_usuario(usuario, nombre, email, activo):
    usuario['nombre'] = nombre
    usuario['email'] = email
    usuario['activo'] = activo
    
    
def eliminar_usuario(usuarios, usuario):
    usuarios.remove(usuario)