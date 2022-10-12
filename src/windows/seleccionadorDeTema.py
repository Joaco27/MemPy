import PySimpleGUI as sg

def themeL():
    """Creacion de la ventana de seleccion de tema, seteando el elegido o el default"""
    
    sg.theme('Dark Grey')
    tema=""

    layout = [[sg.Text('Buscador de temas')],
            [sg.Text('Clickea un tema y se vera una ventana de demostracion .Tu tema default es DarkBlue3')],
            [sg.Listbox(values=sg.theme_list(), size=(20, 12), key='-LIST-', enable_events=True)],
            [sg.Button('Guardar y Volver',key='Exit')]]

    window = sg.Window('Theme Browser', layout,no_titlebar=True)

    while True:  # Event Loop
        event, values = window.read()
        if event in ('Exit'):
            break
        sg.theme(values['-LIST-'][0])
        sg.popup_get_text('This is {}'.format(values['-LIST-'][0]))
    window.close()
    return tema.join(values['-LIST-'])

