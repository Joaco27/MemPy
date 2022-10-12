import PySimpleGUI as sg 
from src.windows import tablero
from src.handlers import cargarUsuario
from src.handlers import tableroDeValores
from src.handlers import usuarioAct
from src.handlers import getUsuario
from src.handlers import guardar_datos

import time as t


def start():
    """
    Lanza la ejecución de la ventana del tablero
    """
    window = loop()
    window.close()


def loop():
    """
    Loop de la ventana del tablero que capta sus eventos
    """
    usu = usuarioAct.getUsu()
    dicc={}
    dicc[usu] = getUsuario.get(usu)
    horaTotal = int(dicc[usu]["configuracion"]["Tiempo Total"]) * 60
    if dicc[usu]["configuracion"]["Medidas"] == '4x2':
        alto = 2
        nivel = "facil"
    elif dicc[usu]["configuracion"]["Medidas"] == '4x3':
        alto = 3
        nivel = "medio"
    else:
        alto = 4
        nivel = "dificil"

    ancho = 4
    coincidenciaTotal = int((ancho * alto) / 2)
    evento_inicio = "inicio_partida"
    evento_fin = "fin"
    evento = "intento"
    genero = dicc[usu]["info"]["genero"]
    edad = dicc[usu]["info"]["edad"]

    board_data = tableroDeValores.generarTablero(ancho,alto)
    
    window =tablero.tablero()
    
    intentos = ["",""]

    start_time = t.time()
    coincidencias = 0

    dicc[usu]["estadisticas"]["Partidas Jugadas"] = int(dicc[usu]["estadisticas"]["Partidas Jugadas"]) + 1

    guardar_datos.guardar(coincidenciaTotal, evento_inicio, usu, genero, edad,"" , nivel, "", "")
                
    while True:
        event, _values = window.read(timeout=100)

        if event in (sg.WINDOW_CLOSED, "Volver", "-volver-"):
            guardar_datos.guardar(coincidenciaTotal, evento_fin, usu, genero, edad,"abandonada" , nivel, coincidencias, "")
            dicc[usu]["estadisticas"]["Derrotas"] = dicc[usu]["estadisticas"]["Derrotas"] + 1
            dicc[usu]["estadisticas"]["Puntaje Total"] = dicc[usu]["estadisticas"]["Puntaje Total"] + coincidencias
            cargarUsuario.cargar(dicc,usu)
                
            break

        if event.startswith("cell"):
            _prefix, x, y = event.split("-")
            
            palabra = board_data[int(x)][int(y)][0]
            if intentos[0] == "":  
                ubi1=event
                window[event].update(palabra)
                intentos[0]  = palabra
                window[event].update(disabled=True)    
                
                            
            elif intentos[1] == "":
                window[event].update(palabra)
                intentos[1] = palabra
                window[event].update(disabled=True)
                ubi2=event
                window.refresh()
                t.sleep(2)
            
                if intentos[1] == intentos[0]:
                    coincidencias += 1
                    guardar_datos.guardar(coincidenciaTotal, evento, usu, genero, edad,"ok" , nivel,coincidencias, palabra)
    
                else:
                    window[ubi1].update(disabled=False)
                    window[ubi2].update(disabled=False)
                    window[ubi1].update("")
                    window[ubi2].update("")
                    guardar_datos.guardar( coincidenciaTotal, evento, usu, genero, edad,"error" , nivel,coincidencias, palabra)
    
                intentos = ["",""]

                if coincidencias == coincidenciaTotal:
                    guardar_datos.guardar(coincidenciaTotal, evento_fin, usu, genero, edad,"finalizada" , nivel, coincidencias*10, "")
                    sg.popup(f"{dicc[usu]['configuracion']['Texto Victoria']}")
                    dicc[usu]["estadisticas"]["Victorias"] = dicc[usu]["estadisticas"]["Victorias"] + 1
                    dicc[usu]['estadisticas']['Puntaje Total']=dicc[usu]['estadisticas']['Puntaje Total'] + coincidencias*10
                    cargarUsuario.cargar(dicc,usu)
                    break
                   
        current_time = t.time() - start_time
        window["-TIMER-"].update(
            f"{round(current_time // 60):02d}:{round(current_time % 60):02d}")
        window["-i-"].update(f"{coincidencias}")
        window.refresh()
        
        
        if (int(current_time)==(horaTotal-60)):
            Poco=dicc[usu]["configuracion"]['Texto Poco Tiempo']
            sg.popup(f"{Poco}")

        if (horaTotal == int(current_time)):
            sg.popup(dicc[usu]["configuracion"]['Texto Derrota'])
            guardar_datos.guardar( coincidenciaTotal, evento_fin, usu, genero, edad,"timeout" , nivel, coincidencias*2, "")
            dicc[usu]["estadisticas"]["Derrotas"] = dicc[usu]["estadisticas"]["Derrotas"] + 1
            dicc[usu]['estadisticas']['Puntaje Total']=dicc[usu]['estadisticas']['Puntaje Total'] + coincidencias*2
            cargarUsuario.cargar(dicc,usu)

    
            break
    

    return window