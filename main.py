from Classes.DataLoader import DataJSONLoader, DataLoader, DataAPILoader
import streamlit as st
import pandas as pd 

data_loader = DataLoader(DataJSONLoader("Data/short_cleaned_songs.json"))
datos=data_loader.load()

df = pd.DataFrame(datos['datos_limpios'])

st.title("Análisis de canciones de Spotify:")

st.subheader("Visualización de datos")
st.dataframe(df, use_container_width=True) 