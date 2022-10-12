import json
import os

def get(name):
    """Devuelve los datos de un usuario"""
    
    with open(f"{os.getcwd()}/Usuarios.json","r", encoding='utf-8-sig') as archivo:
        JsonPython = dict(json.load(archivo))
    return JsonPython[name]