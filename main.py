from libros.menu_libros import menu_libros
from usuarios.menu_usuarios import menu_usuarios
from prestamos.menu_prestamos import menu_prestamos
from utils.entradas import pedir_numero


def mostrar_menu():
    while True:
        print("""
              ============== MENU DE OPCIONES =============
              1. Menu de usuarios
              2. Menu de libros
              3. Menu de prestamos
              4. Salir
              """)

        opcion = pedir_numero('Elige una opcion: ')
        
        if opcion == 1:
            menu_usuarios()
        elif opcion == 2:
            menu_libros()
        elif opcion == 3:
            menu_prestamos()
        elif opcion == 4:
            break



mostrar_menu()