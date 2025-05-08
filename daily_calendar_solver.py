import matplotlib.pyplot as plt
import copy
import random
from datetime import datetime

# Tablero real basado en la imagen: 7 columnas x 8 filas
tablero = [
    "Ene", "Feb", "Mar", "Abr", "May", "Jun", "X",        # Fila 0
    "Jul", "Ago", "Sep", "Oct", "Nov", "Dic", "X",        # Fila 1
    "1", "2", "3", "4", "5", "6", "7",                     # Fila 2
    "8", "9", "10", "11", "12", "13", "14",                # Fila 3
    "15", "16", "17", "18", "19", "20", "21",              # Fila 4
    "22", "23", "24", "25", "26", "27", "28",              # Fila 5
    "29", "30", "31", "Lun", "Mar", "Mié", "Jue",          # Fila 6
    "X", "X", "X", "X", "Vie", "Sáb", "Dom"                # Fila 7
]

COLUMNAS = 7
FILAS = 8

tablero_2d = [tablero[i * COLUMNAS:(i + 1) * COLUMNAS] for i in range(FILAS)]

def generar_mapa_tablero(tablero_2d):
    mapa = {}
    for y, fila in enumerate(tablero_2d):
        for x, valor in enumerate(fila):
            if valor != "X":
                mapa[valor] = (x, y)
    return mapa

mapa_tablero = generar_mapa_tablero(tablero_2d)

# Piezas lado A
piezas_A = {
    "Pieza_1_A": [(-1,0),(0,0),(1,0),(0,1),(0,2),(0,3)],
    "Pieza_2_A": [(0,0),(0,1),(0,2),(-1]()
