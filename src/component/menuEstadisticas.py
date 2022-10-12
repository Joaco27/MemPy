import PySimpleGUI as sg 
from src.windows import menuEstadisticas
from src.component import menuJugadasUsuActual
from src.handlers import datosEstadisticas
from src.component import menuTop10

def start():
    """
    Ejecucion del menu estadisticas
    """
    window = loop_menuEstadisticas()
    window.close()


def loop_menuEstadisticas():
    """
    Loop del menu Estadisticas
    """
    window = menuEstadisticas.Stadistic()

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "Volver", "-volver-"):
            break

        if event == "-partidas-":
            window.hide()
            menuJugadasUsuActual.start()
            window.un_hide()

        if event == "-top10-":
            window.hide()
            try:
                menuTop10.start()
            except:
                sg.popup("Debes jugar al menos una vez")
            window.un_hide()

        if event == "-estados-":
            window.hide()
            try:
                datosEstadisticas.porcenEstado()
            except:
                sg.popup("Debes jugar al menos una vez")
            window.un_hide()

        if event == "-generos-":
            window.hide()
            try:
                datosEstadisticas.porcenGenero()
            except:
                sg.popup("Debes jugar al menos una vez")
            window.un_hide()

    return window