import PySimpleGUI as sg 

from src.handlers import usuarioAct
from src.handlers import getUsuario


def tablero():
    """
    Construye la ventana del tablero del juego
    """

    usu = usuarioAct.getUsu()
    dicc = getUsuario.get(usu)
    hora = dicc["configuracion"]["Tiempo Total"] 

    if dicc["configuracion"]["Medidas"] == '4x2':
        alto = 2
        nivel = "Facil"
    elif dicc["configuracion"]["Medidas"] == '4x3':
        alto = 3
        nivel = "Medio"
    else:
        alto = 4
        nivel = "Dificil"

    layout = [
        [sg.Text(f"Jugador: {usu}", key="-P1-", text_color="darkblue",size=(10, 2),font=("Helvetica", 11),justification="center"),
        sg.Text("-Tiempo de Partida = ",font=("Helvetica", 10),key="--",size=(20,2)),
        sg.Text("",font=("Helvetica", 12),justification="center",key="-TIMER-",size=(4,2)),
        sg.Text(f"/  {hora}:00",font=("Helvetica", 12),justification="center",key="-------",size=(6,2)),
        sg .Text(f"La Cantidad de elementos encontrados:", key="-P3-", text_color="darkblue",size=(20, 2),font=("Helvetica", 10),justification="center"),sg.Text("",font=("Helvetica", 10),key="-i-",size=(6,2))
        ],
        [sg.Text(f"Nivel: {nivel}", key="-P4-", text_color="darkblue",size=(10, 2),font=("Helvetica", 10),justification="center"),
         ]
       
    ]
    
    
    ancho = 4
    board_data = [[" "] * ancho for _i in range(alto)]

         
    for y in range(ancho):
        layout += [
            [
                sg.Button(board_data[x][y], size=(15, 4), key=f"cell-{x}-{y}")
                for x in range(alto)
            ]
        ]
    [sg.Button('Volver', size=(50, 2), key="-volver-")],
    board = sg.Window("Tablero").Layout(layout)

    return board



