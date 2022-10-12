import time
import os
import csv
nro_partida=0
name="datos_de_partidas.csv"
datos = "tiempo_partida, nro_de_partida, cant_palabras, evento, nick, genero, edad, estado, palabra, nivel, puntaje\n"

def nroac():
    """Funcion que devuelve el nro de partida actual"""
    with open(f"{os.getcwd()}/{name}","r") as archivo:
        reader = csv.reader(archivo)
        lista = list(reader)
    global nro
    nro=int(lista[len(lista)-1][1])
    return nro
    
def ultP():
    """Funcion que devuelve el nro de la ultima partida +1"""
    with open(f"{os.getcwd()}/{name}","r") as archivo:
        reader = csv.reader(archivo)
        lista = list(reader)
    nro_partida = int(lista[len(lista)-1][1]) + 1
    return nro_partida




def guardar(cant_palabras, evento, nick, genero, edad, estado, nivel,puntaje, palabra=""):
    """
    Guarda los datos de las acciones que se producen durante la partida
    """
    if not(os.path.isfile(name)):
        archivo = open(f"{os.getcwd()}/{name}","x")
        archivo.write(datos)
        archivo.write(f"{round(time.time())},{1},{cant_palabras},{evento},{nick},{genero},{edad},{estado},{palabra},{nivel},{puntaje}\n")
        archivo.close() 
    else:  
        if evento == "inicio_partida":
            nro_partida=ultP()
        else:
            nro_partida=nroac()
        with open(f"{os.getcwd()}/{name}", "a") as archivo:
            archivo.write(f"{round(time.time())},{nro_partida},{cant_palabras},{evento},{nick},{genero},{edad},{estado},{palabra},{nivel},{puntaje}\n")
    print("Se guardaron los datos correctamente")

