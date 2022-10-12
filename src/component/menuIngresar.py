import PySimpleGUI as sg
from src.windows import menuIngresar
from src.windows import menuAyuda
from src.handlers import cargarUsuario
from src.handlers import existe
from src.handlers import usuarioAct


def start():
    """
    Ejecucion del menu ingresar
    """
    window = loop_menuIngresar()
    window.close()



def loop_menuIngresar():
    """
    Loop del menu ingresar
    """
    window = menuIngresar.LogIn()
    configu = {"Medidas": "4X2", "Coincidencias": "2", "Ayuda": "No",'Tiempo Total':'3', "Tipo de Elemento": "Palabra","Texto Victoria":"Ganaste!!!!!!!!!!",
            "Texto Derrota":"Perdiste, intetalo de nuevo","Texto Poco Tiempo":"Te queda poco tiempo!", "Tema": "BrownBlue" }
            #configuracion default
    dicc={}
    est = {"Partidas Jugadas": 0, "Victorias": 0, "Derrotas": 0, "Puntaje Total": 0}
    default = {"info": {"genero":"","edad":""}, "configuracion": configu, "estadisticas": est}  #estructura de un usuario
    while True:
        event, value = window.read()
        
        if event in (sg.WINDOW_CLOSED, "Volver", "-volver-"):
            break

        
        if event == "-save-":                       
            oki=existe.existe(value['-nick-'])  
            if (oki):           #Si existe el usuario no guarda la info
                break
            else:               #Si no existe guarda la info ingresada
                if not("" in (value['-nick-'], value["-age-"], value["-gender-"])):
                    dicc[value['-nick-']] = default
                    dicc[value['-nick-']]["info"]["edad"] = value["-age-"]
                    dicc[value['-nick-']]["info"]["genero"] = value["-gender-"]
                    break
                elif "" in (value['-nick-'], value["-age-"], value["-gender-"]):
                    sg.Popup("Ingrese TODOS los Datos")



        if event == "-help-":         #Muestra las instrucciones si se presiona el boton ayuda
            window.hide
            ayudaa=menuAyuda.ayuda()
            while True:
                e,_values=ayudaa.read()
                if e in (sg.WINDOW_CLOSED,"-Volver-","Volver"):           
                    break
            window.un_hide
    
    #fin del while

    if not(event in (sg.WINDOW_CLOSED, "Volver", "-volver-")):  #Instruccion para que no falle si no se ingresa nada y se presiona volver    
        usuarioAct.setUsu(value['-nick-'])      #setea el nombre del usuario actual
        if not(oki) and not("" in (value["-age-"], value["-gender-"])):    #Si no existe el usuario se carga la info
            nom=value['-nick-']
            cargarUsuario.cargar(dicc,nom)
    return window
    