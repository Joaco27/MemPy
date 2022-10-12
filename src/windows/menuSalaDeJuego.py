import PySimpleGUI as sg
from src.handlers import getTematiK



def Sala():

    criterio=getTematiK.tema()
    """
    Creacion de la ventana de la sala del juego
    """
    layout = [
        [sg.Text(f'El criterio de hoy es: {criterio}',size=(50,2))],
        [sg.Button('Comenzar', size=(50, 2), key="-play-", bind_return_key=True)],
        [sg.Button('Volver', size=(50, 2), key="-volver-")],
    ]

    window = sg.Window('Sala de Juego',return_keyboard_events=True).Layout(layout)
    return window

