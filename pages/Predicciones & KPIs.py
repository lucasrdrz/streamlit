import streamlit as st
import pandas as pd
from PIL import Image


image = Image.open('./images/predicciones.png')
st.image(image, caption=None, width=750, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.write(":violet[En este apartado podrá consultar las variables más importantes sobre esta categoría de indicadores.]")