import matplotlib.pyplot as plt
import copy
import random
from datetime import datetime



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
