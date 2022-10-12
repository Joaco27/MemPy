import PySimpleGUI as sg 
from src.windows import menuSalaDeJuego
from src.component import menuTablero


def start():
    """
    Ejecucion del menu SalaDeJuego
    """
    window = loop_menuSalaDeJuego()
    window.close()


def loop_menuSalaDeJuego():
    """
    Loop del menu SalaDeJuego
    """
    window = menuSalaDeJuego.Sala()

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "Volver", "-volver-"):
            break

        if event == "-play-":
            window.hide()
            menuTablero.start()
            window.un_hide()

    return window