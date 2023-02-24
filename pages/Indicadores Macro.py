import pandas as pd
import streamlit as st
import plotly.express as px
import base64
import numpy as np
import matplotlib.pyplot as plt
import folium
from streamlit_folium import folium_static
import plotly.graph_objs as go
from PIL import Image

st.set_page_config(
    page_title='TEST',
    layout='wide'
)


#GRAFICO 4 ---------------------------

image = Image.open('./images/macro.png')
st.image(image, caption=None, width=750, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.markdown("-----------")

st.write(":violet[En este apartado podrá consultar las variables más importantes sobre esta categoría de indicadores.]")


# Gráfico de barras FIJO


df = pd.read_csv("Merged_Dataset_v03.csv")

df_gup = df.groupby(['Year'])["Gross Domestic Product"].sum().reset_index()

fig_15123 = px.line(df_gup, x=df_gup["Year"], y=df_gup["Gross Domestic Product"], title="Gross Domestic Product por año")
fig_15123.update_traces(line_color='#728C9F', line_width=3)
# Mostrar gráfico en Streamlit
#st.plotly_chart(fig_15123)

#------------------------------------------------

# Gráfico de barras FILTRADO TEST

df = pd.read_csv("Merged_Dataset_v03.csv")

# Agrupar por año y país
df_gup = df.groupby(['Year', 'Country Name'])["Gross Domestic Product"].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Añadir selectbox para filtrar por país
selected_pais = st.sidebar.selectbox("Selecciona un país:", paises, key='country_selector')

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_gross = px.line(df_filtered, x='Year', y='Gross Domestic Product',  title=f'Gross Domestic Product por año: {selected_pais}')
fig_gross.update_traces(line_color='#ED80DD', line_width=3)
# Mostrar gráfico en Streamlit
#st.plotly_chart(fig)

col7,col8 = st.columns(2)

with col7:
    st.plotly_chart(fig_15123,heigth=600)

with col8:
    st.plotly_chart(fig_gross,heigth=600)
st.markdown("-----------")
#------------------------------------------

#Grafico 5

#SI DEJO ESTE FUNCIONA BIEN VOY A SACAR LOS DE ARRIBA

df = pd.read_csv("Merged_Dataset_v03.csv")

df_gup = df.groupby(['Year'])['GDP Growth'].sum().reset_index()

fig_gdp = px.line(df_gup, x=df_gup["Year"], y=df_gup["GDP Growth"], title="Tasa de crecimienteo interanual del GDP")
fig_gdp.update_traces(line_color='#728C9F', line_width=3)
# Mostrar gráfico en Streamlit
#st.plotly_chart(fig_gdp)

#------------------------------------------------

# Gráfico de barras FILTRADO

df_gup = df.groupby(['Year','Country Name'])['GDP Growth'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Añadir selectbox para filtrar por país
#selected_pais = st.sidebar.selectbox("Selecciona un país:", paises, key='country_selector')

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_gdp_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['GDP Growth'],  title=f'Tasa de crecimienteo interanual del GDP del pais: {selected_pais}')
fig_gdp_fil.update_traces(line_color='#ED80DD', line_width=3)

# Mostrar gráfico en Streamlit
#st.plotly_chart(fig_gdp_fil)


col9,col10 = st.columns(2)

with col9:
    st.plotly_chart(fig_gdp,heigth=600)

with col10:
    st.plotly_chart(fig_gdp_fil,heigth=600)

st.markdown("-----------")
#------------------------------------------
#Grafico 6

df = pd.read_csv("Merged_Dataset_v03.csv")

df_gup = df.groupby(['Year'])['Total reserves (gold + US$)'].sum().reset_index()

fig_total = px.line(df_gup, x=df_gup["Year"], y=df_gup['Total reserves (gold + US$)'], title="Total reserves (gold + US$)")
fig_total.update_traces(line_color='#728C9F', line_width=3)
#st.plotly_chart(fig_total)

#------------------------------------------------

# Gráfico de barras FILTRADO

df_gup = df.groupby(['Year','Country Name'])['Total reserves (gold + US$)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Añadir selectbox para filtrar por país
#selected_pais = st.sidebar.selectbox("Selecciona un país:", paises, key='country_selector1')

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_total_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Total reserves (gold + US$)'],  title=f'Total reserves (gold + US$) del pais: {selected_pais}')
fig_total_fil.update_traces(line_color='#ED80DD', line_width=3)
# Mostrar gráfico en Streamlit
#st.plotly_chart(fig_total_fil)


col11,col12 = st.columns(2)

with col11:
    st.plotly_chart(fig_total,heigth=600)

with col12:
    st.plotly_chart(fig_total_fil,heigth=600)
st.markdown("-----------")
#------------------------------------------

#Grafico 7


df_gup = df.groupby(['Year'])['Unemployment'].sum().reset_index()

fig_desempleo = px.line(df_gup, x=df_gup["Year"], y=df_gup['Unemployment'], title="Desempleo Total")
fig_desempleo.update_traces(line_color='#728C9F', line_width=3)
#------------------------------------------------

# Gráfico de barras FILTRADO

df_gup = df.groupby(['Year','Country Name'])['Unemployment'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Añadir selectbox para filtrar por país
#selected_pais = st.sidebar.selectbox("Selecciona un país:", paises, key='country_selector2')

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_desempleo_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Unemployment'],  title=f'Desempleo Total: {selected_pais}')
fig_desempleo_fil.update_traces(line_color='#ED80DD', line_width=3)

# Mostrar gráfico en Streamlit
#st.plotly_chart(fig_desempleo_fil)


col13,col14 = st.columns(2)

with col13:
    st.plotly_chart(fig_desempleo,heigth=600)

with col14:
    st.plotly_chart(fig_desempleo_fil,heigth=600)
st.markdown("-----------")
#------------------------------------------
#Grafico 8

df_gup = df.groupby(['Year'])['Exports of goods and services (PCT of GDP)'].sum().reset_index()

fig_expor = px.line(df_gup, x=df_gup["Year"], y=df_gup['Exports of goods and services (PCT of GDP)'], title="Exportaciones de bienes y servicios (PCT del PIB)")
fig_expor.update_traces(line_color='#728C9F', line_width=3)
#st.plotly_chart(fig_expor)

#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Exports of goods and services (PCT of GDP)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Añadir selectbox para filtrar por país
#selected_pais = st.sidebar.selectbox("Selecciona un país:", paises, key='country_selector3')

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_expor_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Exports of goods and services (PCT of GDP)'],  title=f'Exportaciones de bienes y servicios (PCT del PIB) del pais: {selected_pais}')
fig_expor_fil.update_traces(line_color='#ED80DD', line_width=3)

# Mostrar gráfico en Streamlit
#st.plotly_chart(fig_expor_fil)


col15,col16 = st.columns(2)

with col15:
    st.plotly_chart(fig_expor,heigth=600)

with col16:
    st.plotly_chart(fig_expor_fil,heigth=600)


st.markdown("-----------")
#------------------------------------------
#Grafico 9

df_gup = df.groupby(['Year'])['Imports of goods and services (PCT of GDP)'].sum().reset_index()

fig_impor = px.line(df_gup, x=df_gup["Year"], y=df_gup['Imports of goods and services (PCT of GDP)'], title="Importaciones de bienes y servicios (PCT del PIB)")
fig_impor.update_traces(line_color='#728C9F', line_width=3)

#st.plotly_chart(fig_expor)

#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Imports of goods and services (PCT of GDP)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Añadir selectbox para filtrar por país
#selected_pais = st.sidebar.selectbox("Selecciona un país:", paises, key='country_selector4')

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_impor_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Imports of goods and services (PCT of GDP)'],  title=f'Importaciones de bienes y servicios (PCT del PIB) del pais: {selected_pais}')
fig_impor_fil.update_traces(line_color='#ED80DD', line_width=3)

# Mostrar gráfico en Streamlit
#st.plotly_chart(fig_expor_fil)


col17,col18 = st.columns(2)

with col17:
    st.plotly_chart(fig_impor,heigth=600)

with col18:
    st.plotly_chart(fig_impor_fil,heigth=600)