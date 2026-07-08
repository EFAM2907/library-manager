import json


def guardar_libros(ruta, libros):
   with open(ruta, 'w', encoding="utf-8") as archivo:
       json.dump(libros, archivo, indent=4, ensure_ascii=False)
       
       
def cargar_libros(ruta):
    
    try:
      with open(ruta) as archivo:
       libros =  json.load(archivo)
    except FileNotFoundError:
        print('no se encontro la ruta')
        libros = []
        
    return libros



