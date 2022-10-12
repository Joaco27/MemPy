import PySimpleGUI as sg

def ayuda():
    """
    Creacion de la ventana del menu de ayuda con las instrucciones
    """

    layout = [
        [sg.Text("""
        El juego de la memoria consiste en encontrar pares coincidentes de elementos en un tablero.
            Los elementos que serán parte del juego se seleccionarán en función de criterios que
            detallaremos más adelante. Podrán ser textos o imágenes.

        El tablero contará con con una cierta cantidad de casillas (configurable desde una sección de
            MemPy), las cuales contendrán los elementos a encontrar en forma “oculta”. En cada turno el
            jugador hace clic sobre una casilla, ésta “se da vuelta” mostrando el elemento correspondiente,
            y luego puede hacer clic en otra para encontrar su par. Si es correcta, quedarán ambas dadas
            vueltas y generará los puntos correspondientes. En cambio si no es la correcta, se deberán
            dar vuelta automáticamente ambas casillas ocultando ambos elementos.

        El juego contará con un tiempo máximo de juego de cierta cantidad de minutos (también
            configurable desde MemPy).""")]    ]


    window = sg.Window("Instrucciones",element_justification='center').Layout(layout)

    return window
