import pandas as pd
from matplotlib import pyplot as plt
import collections
import os


def porcenEstado():

    """Funcion que realiza un grafico de barras de las partidas por estado"""

    df_juego = pd.read_csv(os.path.join(os.getcwd(),'datos_de_partidas.csv')) #Apertura del csv de datos de partida
    estados=[]
    for i in range(len(df_juego)):
        
        if ((df_juego.loc[i,' evento']=='fin')):
            estados.append(str(df_juego.loc[i,' estado']))  #Se filtran solo los elementos cuyo evento sea fin
        
    counter = collections.Counter(estados) #Cuenta la cantidad de apariciones por estado
    claves = list(counter.keys())   #Lista con estados
    valores = list(counter.values())    #Lista con cantidad de apariciones por estado
    plt.bar(claves,valores) #Grafico
    plt.show()  

def porcenGenero():

    """Funcion que realiza un grafico de barras de las partidas finalizadas por genero"""

    df_juego = pd.read_csv(os.path.join(os.getcwd(),'datos_de_partidas.csv'))   #Apertura del csv de datos de partida
    generos=[]
    for i in range(len(df_juego)):

        if ((df_juego.loc[i,' estado']=='finalizada')):
            generos.append(str(df_juego.loc[i,' genero']))  #Se filtran solo los elementos cuyo evento sea finalizada (ganadas)

    counter = collections.Counter(generos)  #Cuenta la cantidad de apariciones por genero
    claves = list(counter.keys())   #Lista con generos
    valores = list(counter.values())    #Lista con cantidad de apariciones por genero
    plt.bar(claves,valores) #Grafico
    plt.show()  


