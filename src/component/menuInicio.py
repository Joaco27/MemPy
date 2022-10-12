import PySimpleGUI as sg
from src.windows import menuInicio
from src.component import menuConfiguracion
from src.component import menuEstadisticas
from src.component import menuIngresar
from src.component import menuPuntajes
from src.component import menuSalaDeJuego
from src.handlers import usuarioAct
from src.handlers import setTema

def start():
    """
    Ejecucion del menu principal
    """
    window = loop_menuInicio()
    window.close()


def loop_menuInicio():
    """
    Loop del menu principal
    """

    window = menuInicio.Inicio()
    while True:
        event, _values = window.read()


        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-"):
            break

        #En caso de no estar logueado no se puede acceder a ninguna otra ventana que no sea Inicio de Aplicacion

        if event == "-play-":
            if(usuarioAct.getUsu() != " "):
                window.hide()
                menuSalaDeJuego.start()
                window.un_hide()
            else:
                sg.Popup("Dirijase a Inicio de Aplicacion e Ingrese su Usuario o Registrese")


        if event == "-settings-":
            if(usuarioAct.getUsu() != " "):
                window.hide()
                menuConfiguracion.start()
                window.un_hide()
            else:
                sg.Popup("Dirijase a Inicio de Aplicacion e Ingrese su Usuario o Registrese")

        if event == "-score-":
            if(usuarioAct.getUsu() != " "):
                window.hide()
                #try:
                menuPuntajes.start()
                #except:
                    #sg.popup("Debes jugar al menos una vez")
                window.un_hide()
            else:
                sg.Popup("Dirijase a Inicio de Aplicacion e Ingrese su Usuario o Registrese")

        if event == "-stadistics-":
            if(usuarioAct.getUsu() != " "):
                window.hide()
                menuEstadisticas.start()
                window.un_hide()
            else:
                sg.Popup("Dirijase a Inicio de Aplicacion e Ingrese su Usuario o Registrese")
        
        if event == "-login-":
            window.hide()            
            menuIngresar.start()
            try:        #excepcion necesaria en caso de no ingresar usuario
                setTema.tema()   #setea el tema luego del login del usuario
            except:
                pass
            window.un_hide()

    sg.PopupYesNo('Disfrutaste el juego???')
    return window