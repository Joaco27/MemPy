import json
import os

from PySimpleGUI.PySimpleGUI import Print


def existe(name):
    """"Devuelve si existe un usuario en el archivo json"""
    
    try:
        oki=True
        with open(f"{os.getcwd()}/Usuarios.json","r", encoding='utf-8-sig') as archivo:
            JsonPython = dict(json.load(archivo))
            try:
                print(f'{name} = {JsonPython[name]}')
            except KeyError:
                oki=False
    except FileNotFoundError:
        oki=False
    return oki