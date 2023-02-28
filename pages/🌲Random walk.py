import streamlit as st
import matplotlib.pyplot as plt
from random import choice

class Randomwalk:

    def __init__(self , pocet_krokov=30, krok=list(range(5)) , strana_lesa=20):
        self.pocet_krokov=pocet_krokov
        self.krok=krok
        self.strana_lesa=strana_lesa
        self.vysledok='STRATILI STE SA V LESE!!'

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        
        while len(self.x_values) < self.pocet_krokov:
            
            x_direction = choice([-1,1])
            x_distance = choice(self.krok)
            x_step = x_direction * x_distance

            y_direction = choice([-1,1])
            y_distance = choice(self.krok)
            y_step = y_direction * y_distance

            if x_step==0 and y_step ==0:
                continue

            x=self.x_values[-1] +x_step
            y=self.y_values[-1] + y_step

            

            self.x_values.append(x)
            self.y_values.append(y)

            if self.x_values[-1]<-self.strana_lesa or self.x_values[-1] > self.strana_lesa or self.y_values[-1]>self.strana_lesa or self.y_values[-1]<-self.strana_lesa:
                self.vysledok=f'ÚSPEŠNE STE SA DOSTALI LESA (minuli ste { len(self.x_values)} z { self.pocet_krokov} krokov).'
                break

st.set_page_config(page_title="Random walk")

st.markdown("# Random walk")
st.sidebar.header("Random walk")
st.sidebar.write("##### Popis:")
st.sidebar.write("""Táto stránka obsahuje 3 inputy - veľkosť strany lesa
                 - to je ten farebný štvorec ,veľkosť kroku - od koľko
                 do koľko sa môže vykonať , ďalši krok a celkový počet krokov.
                 Na základe tohto inputu sa budú náhodne generovať guličky ,
                 ktoré reprezentujú napr. strateného turistu v lese ,
                 ak bol počet krokov na nájdenie cesty z lesa dostačujúci ,
                 tak sa program preruší a vypíše sa výsledok , ak nie ,
                 rak dostanete odpoveď , že ste sa stratili v lese.""")


col1, col2, col3 = st.columns(3)

with col1:
   strana_lesa=st.number_input('Strana lesa:' , min_value=20,max_value=100,step=5 , value=20)

with col2:
   krok=st.slider('Velkost kroka od-do:' , min_value=1,max_value=10,step=1 , value=[1,5])

with col3:
   pocet_krokov=st.number_input('Pocet krokov:' , min_value=5,max_value=100,step=5 , value=30)




od,do = krok
kroky=range(od,do+1)

rw=Randomwalk(pocet_krokov=pocet_krokov, krok=kroky , strana_lesa=strana_lesa)
rw.fill_walk()

plt.style.use('classic')

st.text(f'{rw.vysledok}')


fig, (ax1,ax2) = plt.subplots(1,2 , sharey=True, sharex=True , figsize=(16,9), dpi=100)


point_numbers=range(len(rw.x_values))


ax1.plot(rw.x_values,rw.y_values , marker='o', markerfacecolor="green" )
x1, y1 = [-strana_lesa,strana_lesa], [strana_lesa,strana_lesa]
x2,y2 = [-strana_lesa,strana_lesa], [-strana_lesa,-strana_lesa]
x3,y3 = [-strana_lesa,-strana_lesa], [-strana_lesa,strana_lesa]
x4,y4 = [strana_lesa,strana_lesa], [-strana_lesa,strana_lesa]

ax1.plot(x1, y1, marker = 'o')
ax1.plot(x2, y2, marker = 'o')
ax1.plot(x3, y3, marker = 'o')
ax1.plot(x4, y4, marker = 'o')
ax1.set(xlim=(-(strana_lesa+15), (strana_lesa+15)), ylim=(-(strana_lesa+15), (strana_lesa+15)))

ax2.scatter(rw.x_values,rw.y_values,s=50 , c=point_numbers ,cmap=plt.cm.Blues)
ax2.scatter(rw.x_values[0],rw.y_values[0],s=100 , c='yellow')
ax2.scatter(rw.x_values[-1],rw.y_values[-1],s=100 , c='red')

st.pyplot(fig)

import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import time

fig, ax = plt.subplots()

max_x = 5
max_rand = 10

x = np.arange(0, max_x)
ax.set_ylim(0, max_rand)
line, = ax1.plot(rw.x_values,rw.y_values , marker='o', markerfacecolor="green" )
the_plot = st.pyplot(plt)

def init():  # give a clean slate to start
    line.set_ydata([np.nan] * len(x))

def animate(i):  # update the y values (every 1000ms)
    line.set_ydata(np.random.randint(0, max_rand, max_x))
    the_plot.pyplot(plt)

init()
for i in range(100):
    animate(i)
    time.sleep(0.1)

