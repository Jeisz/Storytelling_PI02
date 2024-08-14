import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import geopandas as gpd
from streamlit_folium import folium_static
import folium

# Configuración de la página
st.set_page_config(page_title="Análisis de Acceso a Internet en Argentina", layout="wide")

# Título del Dashboard
st.title("Análisis de Acceso a Internet en Argentina")

# Función 1: Análisis de Accesos por Tecnología
# Cargar el DataFrame de accesos por tecnología
df_accesos_tecnologia = pd.read_csv('accesos_tecnologia.csv')

# Mostrar las columnas del DataFrame para verificar los nombres
st.write("Columnas disponibles en el DataFrame:", df_accesos_tecnologia.columns)

# Reestructuramos el DataFrame usando las columnas correctas
id_vars = ['Año', 'Trimestre', 'Provincia']
value_vars = ['ADSL', 'Cablemodem', 'Fibra óptica', 'Wireless', 'Otros']

df_melted = df_accesos_tecnologia.melt(
    id_vars=id_vars,  
    value_vars=value_vars,  
    var_name='Tecnología',
    value_name='Accesos'
)

# Filtros de selección
selected_year = st.selectbox('Selecciona el Año', df_melted['Año'].unique())
selected_province = st.selectbox('Selecciona la Provincia', df_melted['Provincia'].unique())

# Filtrar los datos por año y provincia seleccionados
filtered_data = df_melted[(df_melted['Año'] == selected_year) & (df_melted['Provincia'] == selected_province)]

# Crear el gráfico de barras
st.write("Gráfico de Accesos por Tecnología:")
fig, ax = plt.subplots()
sns.barplot(data=filtered_data, x='Tecnología', y='Accesos', ax=ax)
plt.title(f"Accesos por Tecnología en {selected_province} - Año {selected_year}")
plt.xlabel("Tecnología")
plt.ylabel("Accesos")
st.pyplot(fig)

# Función 4: Mapa de Calor de Conectividad por Provincia con gráfico de barras adicional

# Cargar el archivo Excel
file_path = 'mapa_conectividad.xlsx'
df_conectividad = pd.read_excel(file_path)

# Mostrar las columnas del DataFrame para verificar los nombres
st.write("Columnas disponibles en el DataFrame:", df_conectividad.columns)

# Relacionar ambos DataFrames por 'Provincia'
df_combined = pd.merge(df_conectividad, df_accesos_tecnologia, on=['Provincia'], how='inner')

# Mostrar las columnas disponibles después del merge
st.write("Columnas disponibles en df_combined:", df_combined.columns)

# Inspeccionar el DataFrame combinado
st.write("Datos combinados para la provincia seleccionada:", df_combined.head())

# Verificación: Calcular los totales de accesos por tecnología en el DataFrame combinado
tech_columns = ['ADSL', 'Cablemodem', 'Fibra óptica', 'Wireless', 'Otros']

# Revisar si las columnas están presentes antes de la suma
if all(col in df_combined.columns for col in tech_columns):
    df_combined['Total Accesos'] = df_combined[tech_columns].sum(axis=1)
else:
    st.write("Las columnas esperadas no están disponibles en df_combined.")

# Filtrar los datos por la provincia seleccionada
filtered_combined_data = df_combined[df_combined['Provincia'] == selected_province]

# Mostrar el contenido del DataFrame filtrado
st.write("Datos filtrados para la provincia seleccionada:", filtered_combined_data[tech_columns].head())

# Crear el mapa centrado en Argentina
col1, col2 = st.columns([2, 1])
with col1:
    m = folium.Map(location=[-38.4161, -63.6167], zoom_start=5)

    # Añadir los puntos de cada localidad al mapa para la provincia seleccionada
    for _, row in filtered_combined_data.iterrows():
        folium.Marker(
            location=[row['Latitud'], row['Longitud']],
            popup=(
                f"<b>Provincia:</b> {row['Provincia']}<br>"
                f"<b>Localidad:</b> {row['Localidad']}<br>"
                f"<b>Población:</b> {row['Población']}<br>"
                f"<b>ADSL:</b> {row['ADSL']}<br>"
                f"<b>Cablemódem:</b> {row['Cablemódem']}<br>"
                f"<b>Fibra óptica:</b> {row['Fibra óptica']}<br>"
                f"<b>Wireless:</b> {row['Wireless']}<br>"
                f"<b>3G:</b> {row['3G']}<br>"
                f"<b>4G:</b> {row['4G']}<br>"
            ),
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(m)

    # Mostrar el mapa en Streamlit
    st.write(f"Mapa de Conectividad en {selected_province}:")
    folium_static(m)

# Crear el gráfico de barras utilizando los datos combinados
with col2:
    st.write(f"Distribución de Tecnologías en {selected_province}")
    if not filtered_combined_data.empty:
        # Verificación de totales
        tech_totals = filtered_combined_data[tech_columns].sum()
        tech_df = pd.DataFrame({'Tecnología': tech_columns, 'Total Accesos': tech_totals})
        st.write("Totales de accesos por tecnología:", tech_df)

        # Crear el gráfico
        fig4 = px.bar(tech_df, x='Tecnología', y='Total Accesos', title=f"Accesos por Tecnología en {selected_province}")
        st.plotly_chart(fig4)
    else:
        st.write("No hay datos disponibles para la provincia seleccionada.")
