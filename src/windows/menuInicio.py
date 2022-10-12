import PySimpleGUI as sg

def Inicio():
    """
    Creacion de la ventana del menu de de inicio
    """

    layout = [
        [sg.Button('Sala de Juego', size=(50, 2), key="-play-")],
        [sg.Button('Registrarse', size=(50, 2), key="-login-")],
        [sg.Button('Configuración', size=(50, 2), key="-settings-")],
        [sg.Button('Puntajes', size=(50, 2), key="-score-")],
        [sg.Button('Estadisticas', size=(50, 2), key="-stadistics-")],
        [sg.Button('Salir', size=(50, 2), key="-exit-")]
    ]

    window = sg.Window("Menu Principal").Layout(layout)

    return window