import os
import json

def cargar(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        return []
    try:
        with open(nombre_archivo, "r") as archivo:
            return json.load(archivo)
    except json.JSONDecodeError:
        return []
    
def guardar(nombre_archivo, datos):
    with open(nombre_archivo, "w") as archivo:
        json.dump(datos, archivo, indent=4)

def generar_id(lista):
    if not lista:
        return 1
    return lista[-1]["id"] + 1