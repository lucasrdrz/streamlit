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

image = Image.open('./images/salud.png')
st.image(image, caption=None, width=750, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.markdown("-----------")

st.write(":violet[En este apartado podrá consultar las variables más importantes sobre esta categoría de indicadores.]")

df = pd.read_csv("Merged_Dataset_v03.csv")
#------------------------------------------------
# ACA ARRANCA Indicadores de Salud

#Grafico 22


df_gup = df.groupby(['Year'])[ 'Crude Birth Rate (births per 1,000 population)'].sum().reset_index()

fig_tn = px.line(df_gup, x=df_gup["Year"], y=df_gup[ 'Crude Birth Rate (births per 1,000 population)'], title='Tasa de natalidad (nacimientos por cada 1.000 habitantes)')
fig_tn.update_traces(line_color='#728C9F', line_width=3)


#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Crude Birth Rate (births per 1,000 population)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()
selected_pais = st.sidebar.selectbox("Selecciona un país:", paises, key='country_selector7')
# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_tn_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Crude Birth Rate (births per 1,000 population)'],  title=f'Tasa de natalidad (nacimientos por cada 1.000 habitantes) (porcentaje): {selected_pais}')
fig_tn_fil.update_traces(line_color='#ED80DD', line_width=3)



col45,col46 = st.columns(2)

with col45:
    st.plotly_chart(fig_tn,heigth=600)

with col46:
    st.plotly_chart(fig_tn_fil,heigth=600)

st.markdown("-----------")
#------------------------------------------------

#Grafico 23

df_gup = df.groupby(['Year'])[ 'Median Age, as of 1 July (years)' ].sum().reset_index()

fig_em = px.line(df_gup, x=df_gup["Year"], y=df_gup[ 'Median Age, as of 1 July (years)'], title='Edad media, al 1 de julio (años)')
fig_em.update_traces(line_color='#728C9F', line_width=3)


#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])[ 'Median Age, as of 1 July (years)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_em_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered[ 'Median Age, as of 1 July (years)'],  title=f'Edad media, al 1 de julio (años): {selected_pais}')
fig_em_fil.update_traces(line_color='#ED80DD', line_width=3)



col45,col46 = st.columns(2)

with col45:
    st.plotly_chart(fig_em,heigth=600)

with col46:
    st.plotly_chart(fig_em_fil,heigth=600)
st.markdown("-----------")
#------------------------------------------------

#Grafico 24

df_gup = df.groupby(['Year'])[ 'Life Expectancy at Birth, both sexes (years)'].sum().reset_index()

fig_es = px.line(df_gup, x=df_gup["Year"], y=df_gup[ 'Life Expectancy at Birth, both sexes (years)'], title='Esperanza de vida al nacer, ambos sexos (años)')
fig_es.update_traces(line_color='#728C9F', line_width=3)


#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Life Expectancy at Birth, both sexes (years)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_es_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered[ 'Life Expectancy at Birth, both sexes (years)'],  title=f'Esperanza de vida al nacer, ambos sexos (años): {selected_pais}')
fig_es_fil.update_traces(line_color='#ED80DD', line_width=3)



col47,col48 = st.columns(2)

with col47:
    st.plotly_chart(fig_es,heigth=600)

with col48:
    st.plotly_chart(fig_es_fil,heigth=600)
    
st.markdown("-----------")    
#------------------------------------------------

#Grafico 25

df_gup = df.groupby(['Year'])['Infant Mortality Rate (infant deaths per 1,000 live births)'].sum().reset_index()

fig_im = px.line(df_gup, x=df_gup["Year"], y=df_gup['Infant Mortality Rate (infant deaths per 1,000 live births)'], title='Tasa de Mortalidad Infantil (muertes infantiles por cada 1.000 nacidos vivos)')
fig_im.update_traces(line_color='#728C9F', line_width=3)


#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Infant Mortality Rate (infant deaths per 1,000 live births)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_im_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Infant Mortality Rate (infant deaths per 1,000 live births)'],  title=f'Tasa de Mortalidad Infantil (muertes infantiles por cada 1.000 nacidos vivos): {selected_pais}')
fig_im_fil.update_traces(line_color='#ED80DD', line_width=3)



col49,col50 = st.columns(2)

with col49:
    st.plotly_chart(fig_im,heigth=600)

with col50:
    st.plotly_chart(fig_im_fil,heigth=600)
    
st.markdown("-----------")    

#------------------------------------------------

#Grafico 26

df_gup = df.groupby(['Year'])['Infant Deaths, under age 1 (thousands)'].sum().reset_index()

fig_id = px.line(df_gup, x=df_gup["Year"], y=df_gup['Infant Deaths, under age 1 (thousands)'], title='Muertes infantiles, menores de 1 año (miles)')
fig_id.update_traces(line_color='#728C9F', line_width=3)


#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Infant Deaths, under age 1 (thousands)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_id_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Infant Deaths, under age 1 (thousands)'],  title=f'Muertes infantiles, menores de 1 año (miles): {selected_pais}')
fig_id_fil.update_traces(line_color='#ED80DD', line_width=3)



col51,col52 = st.columns(2)

with col51:
    st.plotly_chart(fig_id,heigth=600)

with col52:
    st.plotly_chart(fig_id_fil,heigth=600)
    
st.markdown("-----------")    
#------------------------------------------------
#Grafico 27

df_gup = df.groupby(['Year'])['Maternal Mortality'].sum().reset_index()

fig_mm = px.line(df_gup, x=df_gup["Year"], y=df_gup['Maternal Mortality'], title='Mortalidad maternal')
fig_mm.update_traces(line_color='#728C9F', line_width=3)

#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Maternal Mortality'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_mm_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Maternal Mortality'],  title=f'Mortalidad maternal: {selected_pais}')
fig_mm_fil.update_traces(line_color='#ED80DD', line_width=3)



col53,col54 = st.columns(2)

with col53:
    st.plotly_chart(fig_mm,heigth=600)

with col54:
    st.plotly_chart(fig_mm_fil,heigth=600)