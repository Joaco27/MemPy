from src.handlers import usuarioAct
from src.handlers import getUsuario
import PySimpleGUI as sg

def tema():
    """Setea el tema de un usuario"""
    
    nom=usuarioAct.getUsu()
    dicc=getUsuario.get(nom)
    sg.ChangeLookAndFeel(dicc["configuracion"]["Tema"])


