import PySimpleGUI as sg

def Punt(top_3):
    """
    Creacion de la ventana de puntajes del juego en cada nivel
    """
    
    
    layout = [
        [sg.Text((f'{top_3}'),size=(15,4),font=("Helvetica", 12))],
        [sg.Button('Volver', size=(50, 2), key="-volver-")],

    ]

    window = sg.Window('Puntajes').Layout(layout)
    return window

