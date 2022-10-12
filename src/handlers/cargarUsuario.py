import json
import os

def cargar(dicc,name):
    """Se carga un usuario o se realiza la modificacion de usuario al archivo json"""
    
    if not(os.path.isfile("Usuarios.json")):
        archivo = open(f"{os.getcwd()}/Usuarios.json","w")
        carga={}
        carga[name]=dicc[name]
        archivo.write(json.dumps(carga, indent=4))
        archivo.close() 
    else:  
        archivo=open(f"{os.getcwd()}/Usuarios.json","r")
        carga=dict(json.load(archivo))
        archivo.close()
        carga[name]=dicc[name]
        a=open(f"{os.getcwd()}/Usuarios.json","w")
        a.write(json.dumps(carga, indent=4))
        a.close()