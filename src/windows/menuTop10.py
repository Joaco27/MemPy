import PySimpleGUI as sg 


def devolverTop(lista_de_tupla):
    """
    Devuelve en pantalla las 10 palabras que se encuentran primero en todas las palabras
    """
    
    layout = [
                [sg.Button('Volver', size=(30, 2), key="-volver-")],
        ]

    for i in range(len(lista_de_tupla)):
        if(i<10):
            layout += [
                [sg.Text(f"{lista_de_tupla[i][0]}", key=f"{i}", text_color="darkblue",size=(20, 2))]
            ]
    
    window = sg.Window('Top 10').Layout(layout)
    return window