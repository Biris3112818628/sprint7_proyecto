import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

st.header("📊 Visualizaciones interactivas con Plotly Express")

st.write("Haz clic en uno de los botones para generar un gráfico:")

# Botón 1: Histograma
if st.button("Mostrar histograma"):
    # Datos de ejemplo para el histograma
    data_hist = pd.DataFrame({
        "valores": np.random.normal(loc=50, scale=15, size=300)
    })
    fig_hist = px.histogram(
        data_hist,
        x="valores",
        nbins=20,
        title="Histograma - distribución de valores (aleatorio)"
    )
    st.write("Histograma generado usando datos aleatorios:")
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón 2: Gráfico de dispersión
if st.button("Mostrar dispersión"):
    # Datos de ejemplo para scatter (puedes sustituir por tu dataset)
    # Ejemplo con 3 columnas: x, y y categoría
    np.random.seed(42)
    data_scatter = pd.DataFrame({
        "x": np.random.normal(loc=0, scale=1, size=200),
        "y": np.random.normal(loc=0, scale=1, size=200),
        "grupo": np.random.choice(["A", "B", "C"], size=200)
    })
    fig_scatter = px.scatter(
        data_scatter,
        x="x",
        y="y",
        color="grupo",
        size_max=12,
        title="Gráfico de dispersión - datos aleatorios por grupo",
        hover_data={"x": True, "y": True, "grupo": True}
    )
    st.write("Gráfico de dispersión generado usando datos aleatorios:")
    st.plotly_chart(fig_scatter, use_container_width=True)

# Mensaje por defecto si no se ha pulsado ningún botón
if not st.session_state.get("_clicked", False):
    st.write("Ningún gráfico seleccionado todavía. Pulsa un botón para generar uno.")


# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')