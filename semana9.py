import pandas as pd
import streamlit as st

# Carga el archivo CSV en un DataFrame
df = pd.read_csv("./static/proyecto9.csv")

# Muestra información del DataFrame
st.write("Información del DataFrame:")
st.write(df.info())

# Muestra estadísticas descriptivas
st.write("Estadísticas descriptivas:")
st.write(df.describe())

# Muestra el conteo de valores por 'Nivel_Educativo'
st.write("Conteo de valores por Nivel Educativo:")
st.write(df['Nivel_Educativo'].value_counts())

# Muestra la carrera más común
st.write("Carrera más común:")
st.write(df['Carrera'].value_counts().idxmax())

# Muestra la institución más común
st.write("Institución más común:")
st.write(df['Institución'].value_counts().idxmax())

# Filtra y muestra los datos de posgrado
st.write("Datos de Posgrado:")
df_posgrado = df[df['Nivel_Educativo'] == 'Posgrado']
st.write(df_posgrado)

# Filtra y muestra los datos de Ingeniería Informática en la Universidad Complutense de Madrid
st.write("Datos de Ingeniería Informática en la Universidad Complutense de Madrid:")
df_ingenieria_madrid = df[(df['Carrera'] == 'Ingeniería Informática') & (df['Institución'] == 'Universidad Complutense de Madrid')]
st.write(df_ingenieria_madrid)

# Filtra y muestra los datos de Honduras con nivel educativo universitario
st.write("Datos de Honduras con nivel educativo universitario:")
df_honduras_universitario = df[(df['País'] == 'Honduras') & (df['Nivel_Educativo'] == 'Universitario')]
st.write(df_honduras_universitario)

# Muestra una tabla cruzada de País y Nivel Educativo
st.write("Tabla cruzada de País y Nivel Educativo:")
st.write(pd.crosstab(df['País'], df['Nivel_Educativo']))

# Muestra la edad promedio por nivel educativo
st.write("Edad promedio por Nivel Educativo:")
st.write(df.groupby('Nivel_Educativo')['Edad'].mean())


df_posgrado.to_csv('posgrado.csv', index=False) 