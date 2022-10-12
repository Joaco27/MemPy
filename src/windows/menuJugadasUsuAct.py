import PySimpleGUI as sg
from src.handlers import getUsuario
from src.handlers import usuarioAct

def partidas():
    """
    Creacion de la ventana de estadisticas de partidas del Usuario Actual
    """
    actual = usuarioAct.getUsu()
    usu = {}
    usu[actual] = getUsuario.get(actual)
    totales = usu[actual]['estadisticas']['Partidas Jugadas']
    ganadas = usu[actual]['estadisticas']['Victorias']
    perdidas = usu[actual]['estadisticas']['Derrotas']
    puntaje_total = usu[actual]['estadisticas']['Puntaje Total']
    layout = [
        [sg.Text(f'Partidas Totales: {totales}')],
        [sg.Text(f'Partidas Ganadas: {ganadas}')],
        [sg.Text(f'Partidas Perdidas: {perdidas}')],
        [sg.Text(f'Puntaje Total: {puntaje_total}')],
        [sg.Button('Volver', size=(50, 2), key="-volver-")],
    ]

    window = sg.Window('Estadisticas de tus Partidas!!!').Layout(layout)
    return window