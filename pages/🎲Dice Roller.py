import streamlit as st
st.set_page_config(
    page_title="Dice Roller"
)



from random import randint
import random
from plotly.subplots import make_subplots
import plotly.graph_objects as go

st.markdown("# Dice Roller")
st.sidebar.header("Dice Roller")
st.sidebar.write("##### Popis:")
st.sidebar.write("""Táto stránka obsahuje 2 inputy - počet hodov
                 a počet kociek , ktoré budú hodené v backende programu
                 a vám sa už len zobrazí výsledok v podobe 3 dvojíc grafov.
                 Prvá reprezentuje súčty hodov, druhá koľkokrát padlo ktoré číslo
                 a tretia koľko padlo párnych(2-4-6) a koľko nepárnych(1-3-5) cifier.
                 Farby reprezentujú danú X hodnotu v oboch stĺpcovh , sú generovane
                 náhodne , niekedy celkom crazy xD.
                 Keď ich náhodou od seba neviete rozoznať , tak re-roll i guess.""")
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

#st.write("Súčet jednotlivých hodov",text_align="center")
farby=[]
for item in frequencies:
    farby.append(f'#{random.randrange(256**3):06x}')

fig = make_subplots(rows=1, cols=2 ,specs=[[{'type': 'xy'},{'type': 'domain'}]] )

fig.add_trace(
    go.Bar(x=os_x1, y=frequencies,marker=dict(color=farby)) ,
    row=1, col=1
)

fig.add_trace(
    go.Pie(labels=os_x1, values=frequencies,marker=dict(colors=farby)),
    row=1, col=2
)


fig.update_xaxes(nticks=max_sucet)

fig.update_layout(
    title="Súčet jednotlivých hodov",
    title_x=0.5,
    title_y=0.9
)
st.plotly_chart(fig)

farby=[]
for item in frequencies2:
    farby.append(f'#{random.randrange(256**3):06x}')


#st.write("Súčet 1-6")
fig2 = make_subplots(rows=1, cols=2 ,specs=[[{'type': 'xy'},{'type': 'domain'}]] )

fig2.add_trace(
    go.Bar(x=os_x2, y=frequencies2,marker=dict(color=farby)),
    row=1, col=1
)

fig2.add_trace(
    go.Pie(labels=os_x2, values=frequencies2,marker=dict(colors=farby)),
    row=1, col=2
)
fig2.update_xaxes(nticks=7)

fig2.update_layout(
    title="Súčet 1-6",
    title_x=0.5,
    title_y=0.9
)

st.plotly_chart(fig2)


farby=[]
for i in range(2):
    farby.append(f'#{random.randrange(256**3):06x}')

#st.write("Súčet párne-nepárne")
fig3 = make_subplots(rows=1, cols=2 ,specs=[[{'type': 'xy'},{'type': 'domain'}]] )

fig3.add_trace(
    go.Bar(x=['parne','neparne'], y=[parne,neparne],marker=dict(color=farby)),
    row=1, col=1
)

fig3.add_trace(
    go.Pie(labels=['parne','neparne'], values=[parne,neparne],marker=dict(colors=farby)),
    row=1, col=2
)

fig3.update_layout(
    title="Párne-nepárne",
    title_x=0.5,
    title_y=0.9
)
st.plotly_chart(fig3)

