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




anios = [3, 1, 2]

for i in range(len(anios)):
    for j in range(len(anios) - 1):
        if anios[j] > anios[j + 1]:
           print(anios[j])

