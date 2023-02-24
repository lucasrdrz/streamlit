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

image = Image.open('./images/demograficos.png')
st.image(image, caption=None, width=750, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.markdown("-----------")

st.write(":violet[En este apartado podrá consultar las variables más importantes sobre esta categoría de indicadores.]")

#df = pd.read_csv("Merged_Dataset_v03.csv")
# Crear figura de Matplotlib
#fig, ax = plt.subplots()
#ax.hist(df["Time required to start a business (days)"], bins=30)
# Mostrar gráfico en Streamlit
#st.pyplot(fig)




#with st.sidebar:
    #Campaign_filter = st.multiselect(label= 'Select The Campaign',
                                #options=df['Net Number of Migrants (thousands)'].sum(),
                                #default=df['Net Number of Migrants (thousands)'].sum())

    #Age_filter = st.multiselect(label='Select Age Group',
                            #options=df['age'].unique(),
                            #default=df['age'].unique())

    #Gender_filter = st.multiselect(label='Select Gender Group',
                            #options=df['gender'].unique(),
                            #default=df['gender'].unique())




df = pd.read_csv("Merged_Dataset_v03.csv")

# ARRANCAN Indicadores Demográficos

#Grafico 18


df_gup = df.groupby(['Year'])['Population Total'].sum().reset_index()

fig_pb = px.line(df_gup, x=df_gup["Year"], y=df_gup['Population Total'], title="Total de Poblacion")
fig_pb.update_traces(line_color='#728C9F', line_width=3)
#-----------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Population Total'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()
selected_pais = st.sidebar.selectbox("Selecciona un país:", paises, key='country_selector7')

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_pb_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Population Total'],  title=f'Total de poblacion: {selected_pais}')
fig_pb_fil.update_traces(line_color='#ED80DD', line_width=3)

col35,col36 = st.columns(2)

with col35:
    st.plotly_chart(fig_pb,heigth=600)

with col36:
    st.plotly_chart(fig_pb_fil,heigth=600)
st.markdown("-----------")
#------------------------------------------------


#Grafico 19

df_gup = df.groupby(['Year'])['Population Density'].sum().reset_index()

fig_dp = px.line(df_gup, x=df_gup["Year"], y=df_gup['Population Density'], title="Densidad de la poblacion")
fig_dp.update_traces(line_color='#728C9F', line_width=3)
#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Population Density'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_dp_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Population Density'],  title=f'Densidad de la poblacion: {selected_pais}')
fig_dp_fil.update_traces(line_color='#ED80DD', line_width=3)

col37,col38 = st.columns(2)

with col37:
    st.plotly_chart(fig_dp,heigth=600)

with col38:
    st.plotly_chart(fig_dp_fil,heigth=600)
    
st.markdown("-----------")
#------------------------------------------------
#Grafico 20

df_gup = df.groupby(['Year'])['Natural Change, Births minus Deaths (thousands)'].sum().reset_index()

fig_nm= px.line(df_gup, x=df_gup["Year"], y=df_gup['Natural Change, Births minus Deaths (thousands)'], title='Cambio natural, nacimientos menos muertes (miles)')
fig_nm.update_traces(line_color='#728C9F', line_width=3)
#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Natural Change, Births minus Deaths (thousands)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_nm_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Natural Change, Births minus Deaths (thousands)'],  title=f'Cambio natural, nacimientos menos muertes (miles): {selected_pais}')
fig_nm_fil.update_traces(line_color='#ED80DD', line_width=3)

col39,col40 = st.columns(2)

with col39:
    st.plotly_chart(fig_nm,heigth=600)

with col40:
    st.plotly_chart(fig_nm_fil,heigth=600)
st.markdown("-----------")
#------------------------------------------------
#Grafico 21

df_gup = df.groupby(['Year'])['Rate of Natural Change (per 1,000 population)'].sum().reset_index()

fig_nm= px.line(df_gup, x=df_gup["Year"], y=df_gup['Rate of Natural Change (per 1,000 population)'], title='Cambio natural, nacimientos menos muertes (miles)')
fig_nm.update_traces(line_color='#728C9F', line_width=3)
#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Rate of Natural Change (per 1,000 population)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_nm_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Rate of Natural Change (per 1,000 population)'],  title=f'Cambio natural, nacimientos menos muertes (miles): {selected_pais}')
fig_nm_fil.update_traces(line_color='#ED80DD', line_width=3)


col41,col42 = st.columns(2)

with col41:
    st.plotly_chart(fig_nm,heigth=600)

with col42:
    st.plotly_chart(fig_nm_fil,heigth=600)
st.markdown("-----------")
#------------------------------------------------
#Grafico 22

df_gup = df.groupby(['Year'])['Population Growth Rate (percentage)'].sum().reset_index()

fig_tp= px.line(df_gup, x=df_gup["Year"], y=df_gup['Population Growth Rate (percentage)'], title='Tasa de crecimiento de la población (porcentaje)')
fig_tp.update_traces(line_color='#728C9F', line_width=3)
#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Population Growth Rate (percentage)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_tp_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Population Growth Rate (percentage)'],  title=f'Tasa de crecimiento de la población (porcentaje): {selected_pais}')
fig_tp_fil.update_traces(line_color='#ED80DD', line_width=3)


col43,col44 = st.columns(2)

with col43:
    st.plotly_chart(fig_tp,heigth=600)

with col44:
    st.plotly_chart(fig_tp_fil,heigth=600)

#

