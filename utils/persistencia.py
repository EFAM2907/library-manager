import json

def cargar_datos(ruta):
    try:
        with open(ruta, encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("No se encontró el archivo.")
        return []
    except json.JSONDecodeError:
        return []


def guardar_datos(ruta, lista):
   with open(ruta, 'w', encoding="utf-8") as archivo:
       json.dump(lista, archivo, indent=4, ensure_ascii=False)

