import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from random import randint
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px


class Die:
    def __init__(self,num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1,self.num_sides)


pocet_kociek = st.number_input('Počet kociek:' , min_value=1,max_value=10,step=1 , value=2)
pocet_hodov =st.number_input('Počet hodov:' , min_value=1,max_value=1000,step=20 , value = 100)



kocky=[]
for i in range(pocet_kociek):
    kocky.append(Die())

hody=[]
sucty=[]
parne=0
neparne=0
for i in range(pocet_hodov):
    sucet=0
    for kocka in kocky:
        hod=kocka.roll()
        if hod in [2,4,6]:
            parne+=1
        if hod in [1,3,5]:
            neparne+=1
        sucet+=hod
        hody.append(hod)
    sucty.append(sucet)

frequencies = []
max_sucet = pocet_kociek*6
for i in range(pocet_kociek,max_sucet+1):
    frequency= sucty.count(i)
    frequencies.append(frequency)




# print(kocky,end=" ")
# print(len(kocky))
# print(hody , end=" ")
# print(len(hody))
# print(sucty , end= " ")
# print(len(sucty))
# print(frequencies, end=" ")
# print(len(frequencies))

os_x1=list(range(pocet_kociek,max_sucet+1))
a=sorted(sucty)
os_y =a[-1]



frequencies2 = []
for i in range(1,7):
    frequency=hody.count(i)
    frequencies2.append(frequency)
    


os_x2=list(range(1,7))

st.write("Súčet jednotlivých hodov",text_align="center")
fig = make_subplots(rows=1, cols=2 ,specs=[[{'type': 'xy'},{'type': 'domain'}]] )

fig.add_trace(
    go.Bar(x=os_x1, y=frequencies) ,
    row=1, col=1
)

fig.add_trace(
    go.Pie(labels=os_x1, values=frequencies),
    row=1, col=2
)


fig.update_xaxes(nticks=max_sucet)

st.plotly_chart(fig)

st.write("Súčet 1-6")
fig2 = make_subplots(rows=1, cols=2 ,specs=[[{'type': 'xy'},{'type': 'domain'}]] )

fig2.add_trace(
    go.Bar(x=os_x2, y=frequencies2),
    row=1, col=1
)

fig2.add_trace(
    go.Pie(labels=os_x2, values=frequencies2),
    row=1, col=2
)
fig2.update_xaxes(nticks=7)
st.plotly_chart(fig2)

st.write("Súčet párne-nepárne")
fig3 = make_subplots(rows=1, cols=2 ,specs=[[{'type': 'xy'},{'type': 'domain'}]] )

fig3.add_trace(
    go.Bar(x=['parne','neparne'], y=[parne,neparne]),
    row=1, col=1
)

fig3.add_trace(
    go.Pie(labels=['parne','neparne'], values=[parne,neparne]),
    row=1, col=2
)
st.plotly_chart(fig3)

