import streamlit as st
st.set_page_config(layout='centered')
st.title('Custom_filter')
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
df=pd.read_csv('data/new_population.csv')
df2 = df.copy()
st.write("### Filtrujte dataset ")

roky = st.slider("Vyberte si rozmedzie od roku 1900 az po 2021", min_value=1900 , max_value=2021 , step=1 ,
value=[1900,2021])
od,do=roky
populacia = st.slider("Vyberte si rozmedzie od 0 do 2,5 miliard", min_value=0 , max_value=250_000_000 , step=50_000 ,
value=[0,250_000_000])
odp , dop = populacia

country_options = df['Entity'].unique().tolist()
krajiny =st.multiselect('Ktoré krajiny by ste radi videli?' , country_options)

podmienka1 = df2.loc[df2.Year >=od,: ]
podmienka1 = podmienka1.loc[df2.Year <=do,: ]
podmienka1 = podmienka1.loc[df2.Population <=dop,: ]
podmienka1 = podmienka1.loc[df2.Population >=odp,: ]

if krajiny:
    podmienka1 = podmienka1[df['Entity'].isin(krajiny)]

st.write(podmienka1)





country_options2 = df['Entity'].unique().tolist()
#years =df['Year'].unique().tolist()

country= st.multiselect('Ktoré krajiny by ste radi videli?' , country_options2,['Slovakia'])

rozmedzie = st.slider('Vyberte si rozmedzieod roku 1900 az po 2021', min_value=1900 , max_value=2021 , step=1 ,
value=[1900,2021])
od, do =rozmedzie

df= df[df['Entity'].isin(country)]
maximum=df['Population'].max()
maximum=int(maximum)
step=maximum//100
step=int(step)
start=0

podmienka = df.loc[df.Year >=od,: ]
podmienka = podmienka.loc[df.Year <=do,: ]
fig=px.line(podmienka,x='Year',y='Population' , color='Entity')
fig.update_layout(width=800)

st.write(fig)
st.write(f"Animované priebeh rastu zvolených krajín")

horna_hranica=st.slider('Zvolte hornu hranicu' , min_value=start , max_value=maximum ,step=step, value=[start,maximum])
od,do = horna_hranica
fig2=px.bar(df,x='Entity',y='Population' , color='Entity' , animation_frame='Year',animation_group='Entity',range_y=[0,do])
fig2.update_layout(width=800)
st.write(fig2)


