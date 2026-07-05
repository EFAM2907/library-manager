
def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print('no debe estar vacio')
       

def pedir_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print('deben ser numeros')


def pedir_datos_libro():
    titulo = pedir_texto('nombre del libro: ')
    autor = pedir_texto('nombre del autor: ')
    categoria = pedir_texto('que categoria de libro es: ')
    anio = pedir_numero('anio del libro: ')
    
    return titulo, autor, categoria, anio
    
    
    
