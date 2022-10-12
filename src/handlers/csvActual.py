import os
import csv
name=" "


def setCsv(nom):
    """Setea el nombre del csv actual"""

    global name
    name=nom


def getCsv():
    """Devuelve el archivo .csv"""
    global name
    with open(f"{os.getcwd()}/{name}","r") as arch:
        reader = csv.reader(arch, delimiter=',')
        csvlist=list(reader)
        #encabezado = next(csvreader)
    return csvlist

