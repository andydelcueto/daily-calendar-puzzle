import streamlit as st
from daily_calendar_solver import resolver_fecha, generar_hint

st.set_page_config(page_title="Daily Calendar Puzzle Solver", layout="centered")
st.title("🧩 Daily Calendar Puzzle Solver")

st.markdown("""
Selecciona una fecha, elige qué lado de las piezas usar y si quieres resolver el rompecabezas o recibir un *hint* (pista).  
""")

# Entradas del usuario
dia = st.selectbox("📅 Día del mes", list(range(1, 32)))
mes = st.selectbox("🗓️ Mes", ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"])
semana = st.selectbox("📆 Día de la semana", ["LUN", "MAR", "MIE", "JUE", "VIE", "SAB", "DOM"])
lado = st.radio("🔄 ¿Qué lado de las piezas usar?", ["A", "B", "MIXTO"])
modo = st.radio("🎯 ¿Qué deseas hacer?", ["Resolver", "Hint"])

# Nivel del hint
if modo == "Hint":
    nivel = st.slider("🧠 Nivel de ayuda (hint)", min_value=1, max_value=3, value=1)

guardar = st.checkbox("💾 Guardar como imagen PNG")

# Botón de ejecución
if st.button("Ejecutar"):
    if modo == "Resolver":
        st.write("🔄 Buscando solución...")
        resolver_fecha(dia, mes, semana, lado, guardar)
        st.success("✅ Solución mostrada.")
    else:
        st.write(f"🔍 Generando hint nivel {nivel}...")
        generar_hint(dia, mes, semana, lado, nivel, guardar)
        st.success("✅ Hint generado.")

st.caption("Creado con ❤️ por andydelcueto")
