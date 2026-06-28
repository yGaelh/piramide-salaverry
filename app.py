import streamlit as st
import pandas as pd

from grafico import crear_piramide


# -------------------------------------------------------
# CONFIGURACIÓN
# -------------------------------------------------------

st.set_page_config(
    page_title="Pirámide Poblacional",
    page_icon="📊",
    layout="wide"
)

# -------------------------------------------------------
# TÍTULO
# -------------------------------------------------------

st.title("📊 Pirámide Poblacional de Salaverry")

st.write(
    "Aplicación interactiva de la población por sexo y grupo de edad."
)

# -------------------------------------------------------
# LEER EXCEL
# -------------------------------------------------------

df = pd.read_excel("poblacion.xlsx")

df.columns = df.columns.str.strip()

df["Sexo"] = df["Sexo"].astype(str).str.strip()

edades = list(df.columns[2:])

# -------------------------------------------------------
# SLIDER
# -------------------------------------------------------

anio = st.slider(
    "Seleccione el año",
    1971,
    2050,
    1971
)

# -------------------------------------------------------
# FILTRAR
# -------------------------------------------------------

datos = df[df["Año"] == anio]

hombres = datos[
    datos["Sexo"].str.lower() == "masculino"
]

mujeres = datos[
    datos["Sexo"].str.lower() == "femenino"
]

if hombres.empty or mujeres.empty:

    st.error("No existen datos para ese año.")

    st.stop()

valores_hombres = hombres[edades].iloc[0].astype(float)

valores_mujeres = mujeres[edades].iloc[0].astype(float)

# -------------------------------------------------------
# GRÁFICA
# -------------------------------------------------------

fig = crear_piramide(
    edades,
    valores_hombres,
    valores_mujeres,
    anio
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -------------------------------------------------------
# TABLA
# -------------------------------------------------------

st.subheader("Datos del año seleccionado")

st.dataframe(
    datos,
    use_container_width=True,
    hide_index=True
)