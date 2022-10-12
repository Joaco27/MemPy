import PySimpleGUI as sg 
from src.windows import menuConfiguracion
from src.windows import seleccionadorDeTema
from src.handlers import getUsuario
from src.handlers import usuarioAct 
from src.handlers import cargarUsuario 


def start():
    """
    Ejecucion del menu configuracion
    """
    window = loop_menuConfiguracion()
    window.close()


def loop_menuConfiguracion():
    """
    Loop del menu configuracion
    """
    window = menuConfiguracion.Config()

    usu=usuarioAct.getUsu()     #usu = nombre del usuario actual
    usuarioDicc={}
    
    usuarioDicc[usu]=getUsuario.get(usu)        #usuarioDicc = informacion de tu usuario

    dicc={}
    dicc=usuarioDicc[usu]["configuracion"]      #dicc = configuracion por defecto o modificada del usuario


    while True:
        e, v = window.read()

        if e in (sg.WINDOW_CLOSED, 'Volver', '-volver-'):
            break

        if e == 'medidas':
            dicc['Medidas'] = v['medidas']

        if e == 'time':
            dicc['Tiempo Total'] = v['time']

        if e == 'coincidencias':
            dicc['Coincidencias'] = v['coincidencias']

        if e == 'ayuda':
            dicc['Ayuda'] = v['ayuda']

        if e == 'tipo':
            dicc['Tipo de Elemento'] = v['tipo']

        if (e == '-Guardar-'):
            if(v['textv']!=""):
                dicc['Texto Victoria'] = v['textv']
            if(v['textd']!=""):
                dicc['Texto Derrota'] = v['textd']
            if(v['textcf']!=""):
                dicc['Texto Poco Tiempo'] = v['textcf']
            break

        if e == 'them':
            tema = seleccionadorDeTema.themeL()
            if(tema != "" ):
                dicc['Tema'] = tema
        
    #fin del while

    usuarioDicc[usu]["configuracion"]=dicc  #actualiza la informacion de tu usuario
    cargarUsuario.cargar(usuarioDicc,usu)   #se carga la informacion actualizada
    return window
