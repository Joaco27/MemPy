
from src.handlers import csvActual

import random

def generarTablero(ancho,alto):

    """Funcion que genera un tablero paralelo el cual contiene los valores de  las casillas"""

    board_data = [[""] * ancho for _i in range(alto)]
    lista = csvActual.getCsv()
    listaAux = []

    tamaño = ancho * alto
    
    for i in range(int(tamaño/2)):
        posR = random.randrange(len(lista))
        listaAux.append(lista[posR])
        lista.pop(posR)

    listaAux.extend(listaAux)

    for y in range(ancho):
        for x in range(alto):
            posR = random.randrange(len(listaAux))
            board_data[x][y] = listaAux[posR]
            
            listaAux.pop(posR)

    return board_data


