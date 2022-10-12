import PySimpleGUI as sg


def Config():
    """
    Creacion de la ventana del menú de configuracion del juego
    """
    lmed = ['medidas',['4x2', '4x3', '4x4']]
    lcoin = ['coincidencias',['2']]
    ltipo = ['tipo',['Palabra']]
    ltime = ['time',['3', '5', '7']]
    layuda = ['ayuda',['Si', 'No']]
    layout = [
        [sg.Text('Elegir Texto de Partida')],
        [sg.Text('Texto de victoria'),sg.InputText(key='textv')],[sg.Text('Texto de derrota'),sg.InputText(key='textd')],[sg.Text('Conteo final'),sg.InputText(key='textcf')],
        [sg.Text('Cant de Casilleros/Nivel: ')],[sg.ButtonMenu('Seleccionar', lmed,key='medidas')],
        [sg.Text('Cantidad de coincidencias: ')],[sg.ButtonMenu('Seleccionar', lcoin,key='coincidencias')],
        [sg.Text('Tipo de elemento ')],[sg.ButtonMenu('Seleccionar', ltipo,key='tipo')],
        [sg.Text('Ayuda In-Game')],[sg.ButtonMenu('Seleccionar', layuda,key='ayuda')],
        [sg.Text('Tiempo total de partida')],[sg.ButtonMenu('Seleccionar', ltime,key='time')],
        [sg.Text('Tema a usar')], [sg.Button('Seleccionar', key='them')],
        [sg.Button('Guardar', size=(50, 2), key="-Guardar-", bind_return_key=True)],
        [sg.Button('Volver', size=(50, 2), key="-volver-")],
    ]

    window = sg.Window('Configuracion',return_keyboard_events=True).Layout(layout)
    return window

