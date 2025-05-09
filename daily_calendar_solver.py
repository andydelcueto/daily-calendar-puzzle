import matplotlib.pyplot as plt
import copy
import random
from datetime import datetime

# Tablero plano
tablero = [
    "Ene", "Feb", "Mar", "Abr", "May", "Jun", "X",       # Renglón 0
    "Jul", "Ago", "Sep", "Oct", "Nov", "Dic", "X",       # Renglón 1
    "1", "2", "3", "4", "5", "6", "7",                    # Renglón 2
    "8", "9", "10", "11", "12", "13", "14",              # Renglón 3
    "15", "16", "17", "18", "19", "20", "21",            # Renglón 4
    "22", "23", "24", "25", "26", "27", "28",            # Renglón 5
    "29", "30", "31", "Lun", "Mar", "Mié", "Jue",        # Renglón 6
    "X", "X", "X", "X", "Vie", "Sáb", "Dom"              # Renglón 7
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
    "Pieza_2_A": [(0,0),(0,1),(0,2),(-1,2)],
    "Pieza_3_A": [(0,0),(0,1),(-1,1),(-1,2),(-1,3)],
    "Pieza_4_A": [(-1,0),(-1,1),(0,1),(0,2)],
    "Pieza_5_A": [(-1,0),(0,0),(1,0),(1,1),(1,2)],
    "Pieza_6_A": [(-1,0),(0,0),(-1,1),(-1,2),(-1,3)],
    "Pieza_7_A": [(-1,0),(0,0),(0,1),(0,2),(-1,2)],
    "Pieza_8_A": [(-1,0),(0,0),(0,1),(0,2),(1,2)],
    "Pieza_9_A": [(-1,0),(-1,1),(0,1),(-1,2),(0,2)],
    "Pieza_10_A": [(0,0),(0,1),(0,2),(0,3)]
}

# Rotación para lado B
def rotar_pieza(pieza):
    return [(-y, x) for x, y in pieza]

piezas_B = {
    nombre.replace("_A", "_B"): rotar_pieza(forma)
    for nombre, forma in piezas_A.items()
}

todas_las_piezas = {**piezas_A, **piezas_B}

def colocar_pieza(tablero_ocupado, pieza, pos):
    x0, y0 = pos
    coords_absolutas = []
    for dx, dy in pieza:
        x, y = x0 + dx, y0 + dy
        if not (0 <= x < COLUMNAS and 0 <= y < FILAS):
            return None
        if tablero_2d[y][x] == "X" or (x, y) in tablero_ocupado:
            return None
        coords_absolutas.append((x, y))
    return coords_absolutas

def resolver(tablero_ocupado, piezas_restantes, soluciones, espacios_libres):
    if not piezas_restantes:
        if len(tablero_ocupado) == espacios_libres:
            soluciones.append(copy.deepcopy(tablero_ocupado))
        return
    nombre, pieza = piezas_restantes[0]
    for y in range(FILAS):
        for x in range(COLUMNAS):
            nueva = colocar_pieza(tablero_ocupado, pieza, (x, y))
            if nueva:
                tablero_ocupado.update(nueva)
                resolver(tablero_ocupado, piezas_restantes[1:], soluciones, espacios_libres)
                for coord in nueva:
                    tablero_ocupado.remove(coord)

def visualizar_solucion(ocupadas, libres, guardar=False, titulo="solucion"):
    import streamlit as st
    fig, ax = plt.subplots(figsize=(7, 8))
    for y in range(FILAS):
        for x in range(COLUMNAS):
            if tablero_2d[y][x] == "X":
                continue
            color = "white"
            if (x, y) in ocupadas:
                color = "skyblue"
            elif (x, y) in libres:
                color = "lightgreen"
            rect = plt.Rectangle((x, y), 1, 1, facecolor=color, edgecolor="black")
            ax.add_patch(rect)
            ax.text(x + 0.5, y + 0.5, tablero_2d[y][x], ha="center", va="center", fontsize=8)
    ax.set_xlim(0, COLUMNAS)
    ax.set_ylim(0, FILAS)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.gca().invert_yaxis()
    plt.title("Visualización de " + titulo)
    if guardar:
        filename = f"{titulo}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        plt.savefig(filename, bbox_inches='tight')
        st.success(f"Imagen guardada como: {filename}")
    st.pyplot(fig)

def resolver_fecha(dia, mes, semana, lado="A", guardar=False):
    import streamlit as st
    import itertools

    st.header("🧩 Búsqueda exhaustiva de solución")

    # Obtener coordenadas de los espacios a dejar libres
    coord_dia = mapa_tablero.get(str(dia))
    coord_mes = mapa_tablero.get(mes)
    coord_semana = mapa_tablero.get(semana)

    st.write(f"📅 Día ({dia}): {coord_dia}")
    st.write(f"🗓️ Mes ({mes}): {coord_mes}")
    st.write(f"📆 Semana ({semana}): {coord_semana}")

    libres = set(filter(None, [coord_dia, coord_mes, coord_semana]))
    if len(libres) != 3:
        st.error("❌ Alguno de los valores no fue encontrado en el tablero.")
        return []

    # Generar todas las combinaciones posibles de A/B para 10 piezas
    opciones = list(itertools.product(["A", "B"], repeat=10))

    st.write("🔄 Probando combinaciones A/B (hasta 1024)...")

    for idx, combo in enumerate(opciones):
        piezas_combo = []
        for i, lado_ab in enumerate(combo, start=1):
            nombre = f"Pieza_{i}_{lado_ab}"
            piezas_combo.append((nombre, todas_las_piezas[nombre]))

        soluciones = []
        resolver(set(), piezas_combo, soluciones, len(mapa_tablero) - 3)

        if soluciones:
            st.success(f"✅ Solución encontrada con combinación #{idx + 1}: {[p[0] for p in piezas_combo]}")
            visualizar_solucion(soluciones[0], libres, guardar, titulo="solucion")
            return soluciones

    st.warning("⚠️ Se probaron las 1024 combinaciones y no se encontró solución para esta fecha.")
    return []


def generar_hint(dia, mes, semana, lado="A", nivel=1, guardar=False):
    import streamlit as st
    libres = set(filter(None, [
        mapa_tablero.get(str(dia)),
        mapa_tablero.get(mes),
        mapa_tablero.get(semana)
    ]))
    if len(libres) != 3:
        st.error("⚠️ Uno de los campos (día, mes o semana) no fue encontrado correctamente en el tablero.")
        return []
    piezas = [(n, f) for n, f in todas_las_piezas.items()] if lado == "MIXTO" else \
             [(n, f) for n, f in todas_las_piezas.items() if lado in n]
    random.shuffle(piezas)
    piezas_hint = {1: random.randint(2, 3), 2: 4, 3: 5}.get(nivel, 2)
    ocupadas = set()
    usadas = []
    for nombre, forma in piezas:
        for _ in range(100):
            x, y = random.randint(0, COLUMNAS - 1), random.randint(0, FILAS - 1)
            nueva = colocar_pieza(ocupadas.union(libres), forma, (x, y))
            if nueva:
                ocupadas.update(nueva)
                usadas.append((nombre, nueva))
                break
        if len(usadas) >= piezas_hint:
            break
    visualizar_solucion(ocupadas, libres, guardar, titulo=f"hint_nivel{nivel}")
