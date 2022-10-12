import PySimpleGUI as sg 
from src.windows import menuPuntajes
import os
import pandas as pd


def start():
    """
    Ejecucion del menu puntajes
    """
    window = loop_menuPuntajes()
    window.close()


def loop_menuPuntajes():
    """
    Loop del menu Puntajes
    """
    df_juego = pd.read_csv(os.path.join(os.getcwd(),'datos_de_partidas.csv'))
    df_juego = df_juego[[' nro_de_partida',' evento',' nick',' nivel',' puntaje', ' estado']]

    lista = []
    nro=9999
    dicc = {'facil':0,'medio':0,'dificil':0}

    for i in range(len(df_juego)):
        if ((df_juego.loc[i,' nro_de_partida']!=nro)and(df_juego.loc[i,' evento']== "fin")and(df_juego.loc[i,' estado']!= "abandonada")):
            nro=df_juego.loc[i,' nro_de_partida']
            lista.append([str(df_juego.loc[i,' nick']),str(df_juego.loc[i,' nivel']),int(df_juego.loc[i,' puntaje'])])
            #Se filtran solo los datos necesarios para los puntajes 
            
    for i in range(len(lista)):
        dicc[lista[i][1]] += int(lista[i][2])   #Se actualizan los puntajes de los niveles

       #Se ordenan los niveles dependiendo de la puntuacion
    claves = list(dicc.keys())
    valores = list(dicc.values())

    df = pd.DataFrame(zip(claves,valores), columns = ['Nivel','Puntaje'])  #Crea la tablas de los niveles y sus puntajes
    dfa = df.sort_values('Puntaje',ascending=False)
    dfa.reset_index(drop=True, inplace=True)
    window = menuPuntajes.Punt(dfa)

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "Volver", "-volver-"):
            break

    return window