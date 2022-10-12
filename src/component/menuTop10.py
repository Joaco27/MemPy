import PySimpleGUI as sg 
from src.windows import menuTop10
import pandas as pd
import collections
import os


def start():
    """
    Ejecucion del menu Top 10 Palabras primeramente encontradas
    """
    window = loop_menuTop10()
    window.close()


def loop_menuTop10():
    """
    Loop del menu Top 10 Palabras primeramente encontradas
    """

    df_juego = pd.read_csv(os.path.join(os.getcwd(),'datos_de_partidas.csv'))
    top_palabras=[]
    nro=-99999
    for i in range(len(df_juego)):
        if ((df_juego.loc[i,' estado']=='ok')and(df_juego.loc[i,' nro_de_partida']!=nro)and(df_juego.loc[i,' evento']=='intento')):
            nro=df_juego.loc[i,' nro_de_partida']
            top_palabras.append(str(df_juego.loc[i,' palabra']))    #Filtra la primer coincidencia de cada partida
    
    top10_palabras = collections.Counter(top_palabras)   # devuelve un dicc con las palabras y la cantidad que se repite cada una
    lista_de_tupla = list(top10_palabras.items())
    lista_de_tupla.sort(key = lambda x: x[1], reverse=True)   # ordeno en base a su cantidad
    print(lista_de_tupla)
    window = menuTop10.devolverTop(lista_de_tupla)

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "Volver", "-volver-"):
            break

    return window