import streamlit as st
import pandas as pd
from PIL import Image


st.markdown ('...**_Analytic Hound data load complete_**')

#COSTADO

st.sidebar.caption("GITHUB REPOSITORY | [LINK](https://github.com/Analytic-Hound-Consulting)")
st.sidebar.caption("MAILING | analytichound@gmail.com")



st.sidebar.header(":violet[ **Developed by Analytic Hound group®**]")

#LOGO
image = Image.open('./images/banner.png')
st.image(image, caption=None, width=750, use_column_width=None, clamp=False, channels="RGB", output_format="auto")


st.markdown("-----------")


#1st paragraph
st.header(":violet[ A MIGRATION PROJECT ]")
st.markdown("""Throughout history, migratory flows have undergone multiple changes. These changes are the translation of the different sociopolitical, demographic, environmental and economic aspects among others. "
_**The Analytic Hound ®**_ consulting team, with the contribution of data provided by **Data hub, World bank group and United nations**, has developed an interactive platform for the dynamic analysis of human movement around the world starting from the year 2000.""")
st.markdown ("""On the left side of your screen, you will find a side toolbar which allows you to navigate through this website.""")
    


st.markdown("---")

#2nd paragraph

st.header(":violet[ABOUT US:]")
st.markdown("""_**Analytic Hound ®**_ is a traditional highly specialized consulting firm based in Buenos Aires, Argentina. 
Our mission is to improve the society in which we live through consultancy and, to achieve this, we study, design, execute and evaluate projects and actions that can improve society as we know it. 
This goal is achieved whether they are promoted by the public sector (NGO, governments, etc.) or arise from the private sector.""")

st.markdown("---")


#3rd paragraph

st.header(":violet[DATA SOURCE:]")

image = Image.open('./images/Fuentes.png')
st.image(image, caption=None, width=750, use_column_width=None, clamp=False, channels="RGB", output_format="auto")


col1, col2, col3= st.columns(3)

with col1:      
    with st.expander("UNITED NATIONS"):
        st.markdown("[LINK](https://www.un.org/development/desa/pd/data-landing-page)")
       

        
with col2: 
    with st.expander("DATAHUB"):
        st.markdown("[LINK](https://datahub.io/)")
        
with col3: 
    with st.expander("WORLD BANK GLOBAL"):
        st.markdown("[LINK](https://data.worldbank.org/)")
       
       


st.markdown("---")

#4th paragraph:

st.header(":violet[DISCLAIMER:]")

st.markdown("""**_Analytic Hound_ ®** has no socio-political or economic conflict of interest regarding the subject of study. 

The following documentation  is published in good faith and for general information purposes only. We do not make any warranties about the completeness, reliability, and accuracy of this information. 
Any action you may take upon the information here present is strictly at your own risk. We are not liable for any losses and damages in connection with the use of this document.""")

st.write("_**The Analytic Hound team ®**_")

st.markdown("---")



#TEAM

st.header( " :violet[PROJECT TEAM MEMBERS:]"  )




image1 = Image.open('./images/team.png')
st.image(image1, caption=None, width=750, use_column_width=None, clamp=False, channels="RGB", output_format="auto")


st.markdown("---")


col1, col2, col3, col4, col5 = st.columns(5)

    
        
with col1:          
    if st.button('ALAN MYSLER'):
       st.write("[DATA SCIENTIST](https://www.linkedin.com/in/amysler/)")
    else:
        st.write("[DATA SCIENTIST](https://www.linkedin.com/in/amysler/)")
     #st.markdown("DATA SCIENSTIST")
     #st.markdown("[ALAN MYSLER](https://www.linkedin.com/in/amysler/)") 
         
        
with col2:
    if st.button("BELEN ZAPATA"):
       st.write("[DATA ANALYST](https://www.linkedin.com/in/bel%C3%A9n-zapata/)")
    else:
        st.write("[DATA ANALYST](https://www.linkedin.com/in/bel%C3%A9n-zapata/)")        
    # st.markdown("DATA ANALYST")
     #st.markdown(" [BELEN ZAPATA](https://www.linkedin.com/in/bel%C3%A9n-zapata/)")
        
with col3:      
    if st.button("LUCAS RODRIGUEZ "):
       st.write("[DATA ENGINEER ](https://www.linkedin.com/in/lucasrdrz/)")
    else:
        st.write("[DATA ENGINEER ](https://www.linkedin.com/in/lucasrdrz/)")    
     #st.markdown("DATA ENGINEER")
     #st.markdown("[RODRIGUEZ LUCAS](https://www.linkedin.com/in/lucasrdrz/)")
       


with col4:       
    if st.button("EUGENIA BALL"):
       st.write("[DATA ENGINEER](https://www.linkedin.com/in/eugenia-ball/)")
    else:
        st.write("[DATA ENGINEER](https://www.linkedin.com/in/eugenia-ball/)")
    #st.markdown("DATA ENGINEER")
    #st.markdown("[EUGENIA BALL](https://www.linkedin.com/in/eugenia-ball/)")
       
              
        
with col5:
    if st.button("MAURO G. PINI"):
       st.write("[FUNCTIONAL ANALYST](https://www.linkedin.com/in/maurogpini/)")
    else:
        st.write("[FUNCTIONAL ANALYST](https://www.linkedin.com/in/maurogpini/)")
     #st.markdown("FUNCTIONAL ANALYST")
     #st.markdown("[MAURO PINI](https://www.linkedin.com/in/maurogpini/)")
       

st.markdown("---")

