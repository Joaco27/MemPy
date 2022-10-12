import PySimpleGUI as sg 
from src.windows import menuJugadasUsuAct


def start():
    """
    Ejecucion del menu estadisticas del usuario actual
    """
    window = loop_menuEstadisticasDelUsuario()
    window.close()


def loop_menuEstadisticasDelUsuario():
    """
    Loop del menu Estadisticas del usuario actual
    """
    window = menuJugadasUsuAct.partidas()

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "Volver", "-volver-"):
            break

    return window