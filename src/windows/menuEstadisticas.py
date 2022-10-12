import PySimpleGUI as sg

def Stadistic():
    """
    Creacion de la ventana de las opciones de estadisticas
    """
  
    layout = [
        [sg.Button('Estadisticas de tus Partidas', size=(50, 2), key="-partidas-")],
        [sg.Button('Top 10 de palabras que se encuentran primero de todas las partidas', size=(50, 2), key="-top10-")],
        [sg.Button('Gráfico que muestre el porcentaje de partidas por estado', size=(50, 2), key="-estados-")],
        [sg.Button('Gráfico que muestre el porcentaje de partidas finalizadas según género', size=(50, 2), key="-generos-")],
        [sg.Button('Volver', size=(50, 2), key="-volver-")]
    ]


    window = sg.Window('Estadisticas').Layout(layout)
    return window