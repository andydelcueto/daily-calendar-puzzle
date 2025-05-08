import streamlit as st
from daily_calendar_solver import resolver_fecha, generar_hint

st.set_page_config(page_title="Daily Calendar Puzzle Solver", layout="centered")

# Normalización de entrada
meses_validos = {
    "ene": "Ene", "feb": "Feb", "mar": "Mar", "abr": "Abr", "may": "May", "jun": "Jun",
    "jul": "Jul", "ago": "Ago", "sep": "Sep", "oct": "Oct", "nov": "Nov", "dic": "Dic"
}

dias_semana_validos = {
    "lun": "Lun", "mar": "Mar", "mie": "Mié", "mié": "Mié", "jue": "Jue",
    "vie": "Vie", "sab": "Sáb", "sáb": "Sáb", "dom": "Dom"
}

st.title("🧩 Daily Calendar Puzzle Solver")
st.markdown("""
Selecciona una fecha, elige qué lado de las piezas usar y si quieres resolver el rompecabezas o recibir un *hint* (pista).  
Puedes también guardar la imagen como PNG.
""")

# Entradas del usuario
dia = st.selectbox("📅 Día del mes", list(range(1, 32)))

mes_input = st.text_input("🗓️ Mes", value="May")
semana_input = st.text_input("📆 Día de la semana", value="Mié")

# Normalizar entradas
mes = meses_validos.get(mes_input.lower().strip(), mes_input)
semana = dias_semana_validos.get(semana_input.lower().strip(), semana_input)

lado = st.radio("🔄 ¿Qué lado de las piezas usar?", ["A", "B", "MIXTO"])
modo = st.radio("🎯 ¿Qué deseas hacer?", ["Resolver", "Hint"])

if modo == "Hint":
    nivel = st.slider("🧠 Nivel de ayuda (hint)", min_value=1, max_value=3, value=1)

guardar = st.checkbox("💾 Guardar imagen como PNG")

if st.button("Ejecutar"):
    if modo == "Resolver":
        st.write("🔄 Buscando solución...")
        resolver_fecha(dia, mes, semana, lado, guardar)
        st.success("✅ Solución mostrada.")
    else:
        st.write(f"🔍 Generando hint nivel {nivel}...")
        generar_hint(dia, mes, semana, lado, nivel, guardar)
        st.success("✅ Hint generado.")

st.caption("Hecho con 🧠 + ❤️ por andydelcueto")
