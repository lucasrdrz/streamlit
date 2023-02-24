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

image = Image.open('./images/micro.png')
st.image(image, caption=None, width=750, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.markdown("-----------")

st.write(":violet[En este apartado podrá consultar las variables más importantes sobre esta categoría de indicadores.]")

#Grafico 10 INICIO indicadores MICRO

df = pd.read_csv("Merged_Dataset_v03.csv")

df_gup = df.groupby(['Year'])['Foreign direct investment, net inflows (BoP, current US$)'].sum().reset_index()

fig_inver = px.line(df_gup, x=df_gup["Year"], y=df_gup['Foreign direct investment, net inflows (BoP, current US$)'], title="Inversión extranjera directa, entradas netas (balanza de pagos, US$ a precios actuales)")
fig_inver.update_traces(line_color='#728C9F', line_width=3)


#st.plotly_chart(fig_expor)

#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Foreign direct investment, net inflows (BoP, current US$)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Añadir selectbox para filtrar por país
selected_pais = st.sidebar.selectbox("Selecciona un país:", paises, key='country_selector5')

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_inver_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Foreign direct investment, net inflows (BoP, current US$)'],  title=f'Inversión extranjera directa, entradas netas (balanza de pagos, US$ a precios actuales) del pais: {selected_pais}')
fig_inver_fil.update_traces(line_color='#ED80DD', line_width=3)

# Mostrar gráfico en Streamlit
#st.plotly_chart(fig_expor_fil)


col19,col20 = st.columns(2)

with col19:
    st.plotly_chart(fig_inver,heigth=600)

with col20:
    st.plotly_chart(fig_inver_fil,heigth=600)
st.markdown("-----------")

#------------------------------------------



#Grafico 11 


df_gup = df.groupby(['Year'])['Total tax and contribution rate (PCT of profit)'].sum().reset_index()

fig_tax = px.line(df_gup, x=df_gup["Year"], y=df_gup['Total tax and contribution rate (PCT of profit)'], title="Impuesto total y tasa de contribución (PCT de ganancias)")
fig_tax.update_traces(line_color='#728C9F', line_width=3)


#st.plotly_chart(fig_expor)

#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Total tax and contribution rate (PCT of profit)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Añadir selectbox para filtrar por país
#selected_pais = st.sidebar.selectbox("Selecciona un país:", paises, key='country_selector6')

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_tax_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Total tax and contribution rate (PCT of profit)'],  title=f'Impuesto total y tasa de contribución (PCT de ganancias) del pais: {selected_pais}')
fig_tax_fil.update_traces(line_color='#ED80DD', line_width=3)

# Mostrar gráfico en Streamlit
#st.plotly_chart(fig_expor_fil)


col21,col22 = st.columns(2)

with col21:
    st.plotly_chart(fig_tax,heigth=600)

with col22:
    st.plotly_chart(fig_tax_fil,heigth=600)
st.markdown("-----------")
#------------------------------------------



#Grafico 12


df_gup = df.groupby(['Year'])[ 'Time required to start a business (days)'].sum().reset_index()

fig_tax = px.line(df_gup, x=df_gup["Year"], y=df_gup[ 'Time required to start a business (days)'], title="Tiempo requerido para iniciar un negocio (días)")
fig_tax.update_traces(line_color='#728C9F', line_width=3)

#st.plotly_chart(fig_expor)

#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])[ 'Time required to start a business (days)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Añadir selectbox para filtrar por país
#selected_pais = st.sidebar.selectbox("Selecciona un país:", paises, key='country_selector7')

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_tax_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered[ 'Time required to start a business (days)'],  title=f'Tiempo requerido para iniciar un negocio (días) del pais: {selected_pais}')
fig_tax_fil.update_traces(line_color='#ED80DD', line_width=3)

# Mostrar gráfico en Streamlit
#st.plotly_chart(fig_expor_fil)


col23,col24 = st.columns(2)

with col23:
    st.plotly_chart(fig_tax,heigth=600)

with col24:
    st.plotly_chart(fig_tax_fil,heigth=600)

st.markdown("-----------")
#------------------------------------------



#Grafico 12


df_gup = df.groupby(['Year'])['Research and development expenditure (PCT of GDP)'].sum().reset_index()

fig_desa = px.line(df_gup, x=df_gup["Year"], y=df_gup['Research and development expenditure (PCT of GDP)'], title="Gastos en investigación y desarrollo (PCT del PIB)")
fig_desa.update_traces(line_color='#728C9F', line_width=3)


#st.plotly_chart(fig_expor)

#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])[ 'Research and development expenditure (PCT of GDP)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Añadir selectbox para filtrar por país
#selected_pais = st.sidebar.selectbox("Selecciona un país:", paises, key='country_selector7')

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_desa_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered[ 'Research and development expenditure (PCT of GDP)'],  title=f'Gastos en investigación y desarrollo (PCT del PIB) del pais: {selected_pais}')
fig_desa_fil.update_traces(line_color='#ED80DD', line_width=3)

# Mostrar gráfico en Streamlit
#st.plotly_chart(fig_expor_fil)


col25,col26 = st.columns(2)

with col25:
    st.plotly_chart(fig_desa,heigth=600)

with col26:
    st.plotly_chart(fig_desa_fil,heigth=600)

#------------------------------------------



