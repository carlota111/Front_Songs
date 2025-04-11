import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt

# Título de la app
st.title("Procesar y Visualizar Datos en Streamlit")

# Datos en formato JSON (tu ejemplo)
json_data = pd.read_json("/home/cgarcipo/Front_Songs/Data/short_cleaned_songs.json")
# Convertir los datos JSON a un DataFrame
data_dict = json.loads(json_data)
st.title(type(json_data))
data = pd.DataFrame([data_dict])

# Mostrar los datos cargados
st.write("Datos cargados:")
st.write(data)

# Visualizar un gráfico de ejemplo
st.write("Gráfico de popularidad y valencia:")
fig, ax = plt.subplots()
data.plot(x="track_name", y=["track_popularity", "valence"], kind="bar", ax=ax)
st.pyplot(fig)
