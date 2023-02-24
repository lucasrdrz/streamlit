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


image = Image.open('./images/migrantes.png')
st.image(image, caption=None, width=750, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.markdown("-----------")

st.write(":violet[En este apartado podrá consultar las variables más importantes sobre esta categoría de indicadores.]")

df = pd.read_csv("Merged_Dataset_v03.csv")
#------------------------------------------------
#ACA ARRANCA Indicadores sobre Migración
#Grafico 27

df_gup = df.groupby(['Year'])['Net Number of Migrants (thousands)'].sum().reset_index()

fig_ntm = px.line(df_gup, x=df_gup["Year"], y=df_gup['Net Number of Migrants (thousands)'], title='Número neto de migrantes (miles)')
fig_ntm.update_traces(line_color='#728C9F', line_width=3)


#------------------------------------------------


# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Net Number of Migrants (thousands)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

selected_pais = st.sidebar.selectbox("Selecciona un país:", paises, key='country_selector7')

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_ntm_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Net Number of Migrants (thousands)'],  title=f'Número neto de migrantes (miles): {selected_pais}')
fig_ntm_fil.update_traces(line_color='#ED80DD', line_width=3)

col55,col56 = st.columns(2)

with col55:
    st.plotly_chart(fig_ntm,heigth=600)

with col56:
    st.plotly_chart(fig_ntm_fil,heigth=600)
st.markdown("-----------")
#------------------------------------------------

#Grafico 28

df_gup = df.groupby(['Year'])['Net Migration Rate (per 1,000 population)'].sum().reset_index()

fig_ntmh = px.line(df_gup, x=df_gup["Year"], y=df_gup['Net Migration Rate (per 1,000 population)'], title='Tasa neta de migración (por 1.000 habitantes)')
fig_ntmh.update_traces(line_color='#728C9F', line_width=3)


#------------------------------------------------


# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Net Migration Rate (per 1,000 population)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_ntmh_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Net Migration Rate (per 1,000 population)'],  title=f'Tasa neta de migración (por 1.000 habitantes): {selected_pais}')
fig_ntmh_fil.update_traces(line_color='#ED80DD', line_width=3)

col57,col58 = st.columns(2)

with col57:
    st.plotly_chart(fig_ntmh,heigth=600)

with col58:
    st.plotly_chart(fig_ntmh_fil,heigth=600)
    
st.markdown("-----------")    
#------------------------------------------------

#Grafico 29

df_gup = df.groupby(['Year'])['Refugee population by country or territory of origin'].sum().reset_index()

fig_rp = px.line(df_gup, x=df_gup["Year"], y=df_gup['Refugee population by country or territory of origin'], title='Población de refugiados por país o territorio de origen')
fig_rp.update_traces(line_color='#728C9F', line_width=3)


#------------------------------------------------


# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Refugee population by country or territory of origin'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_rp_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Refugee population by country or territory of origin'],  title=f'Población de refugiados por país o territorio de origen: {selected_pais}')
fig_rp_fil.update_traces(line_color='#ED80DD', line_width=3)

col59,col60 = st.columns(2)

with col59:
    st.plotly_chart(fig_rp,heigth=600)

with col60:
    st.plotly_chart(fig_rp_fil,heigth=600)
    
st.markdown("-----------")    
#------------------------------------------------

#Grafico 30

df_gup = df.groupby(['Year'])['Refugee population by country or territory of asylum'].sum().reset_index()

fig_rpp= px.line(df_gup, x=df_gup["Year"], y=df_gup['Refugee population by country or territory of asylum'], title='Población de refugiados por país o territorio de asilo')
fig_rpp.update_traces(line_color='#728C9F', line_width=3)


#------------------------------------------------


# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Refugee population by country or territory of asylum'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_rpp_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Refugee population by country or territory of asylum'],  title=f'Población de refugiados por país o territorio de asilo: {selected_pais}')
fig_rpp_fil.update_traces(line_color='#ED80DD', line_width=3)

col61,col62 = st.columns(2)

with col59:
    st.plotly_chart(fig_rpp,heigth=600)

with col60:
    st.plotly_chart(fig_rpp_fil,heigth=600)
