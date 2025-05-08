import streamlit as st
import os
st.write(\"Archivos en el directorio actual:\", os.listdir())

from daily_calendar_solver import resolver_fecha, generar_hint

st.title("🧩 Daily Calendar Puzzle Solver")

# Entradas del usuario
dia = st.selectbox("Día del mes", list(range(1, 32)))
mes = st.selectbox("Mes", ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"])
semana = st.selectbox("Día de la semana", ["LUN", "MAR", "MIE", "JUE", "VIE", "SAB", "DOM"])
lado = st.radio("¿Qué lado de las piezas usar?", ["A", "B", "MIXTO"])
modo = st.radio("¿Qué deseas hacer?", ["Resolver", "Hint"])

# Si se pide hint, elegir el nivel
if modo == "Hint":
    nivel = st.slider("Nivel de ayuda (hint)", min_value=1, max_value=3, value=1)

guardar = st.checkbox("Guardar como imagen PNG")

if st.button("Ejecutar"):
    if modo == "Resolver":
        resolver_fecha(dia, mes, semana, lado, guardar)
    else:
        generar_hint(dia, mes, semana, lado, nivel, guardar)

st.caption("Creado con ❤️ para fans del Daily Calendar Puzzle")
