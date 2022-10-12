import PySimpleGUI as sg

def LogIn():
    """
    Creacion de la ventana del menu de inicio de sesion 
    """

    layout = [
        [sg.Text('Igresar SOLO Nick Para Iniciar Sesion o Complete TODOS los Datos Para Registrarse')],
        [sg.Text('Igresar  Nick'),sg.InputText(key="-nick-")],
        [sg.Text('Igresar  Edad'),sg.InputText(key="-age-")],
        [sg.Text('Igresar  Genero'),sg.InputText(key="-gender-")],
        [sg.Button('Guardar', size=(50, 2), key="-save-", bind_return_key=True)],
        [sg.Button('Ayuda', size=(50, 2), key="-help-")],
        [sg.Button('Volver', size=(50, 2), key="-volver-")],
    ]


    window = sg.Window("Log In",return_keyboard_events=True).Layout(layout)
    
    return window
