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
        
        while len(self.x_values) < self.pocet_krokov + 1:
            
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
                self.vysledok=f'ÚSPEŠNE STE SA DOSTALI LESA (minuli ste { len(self.x_values)-1} z { self.pocet_krokov} krokov).'
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
                 tak sa program preruší a vypíše sa výsledok , zároveň sa objaví
                 animovaní graf , ktorý ukazuje postupnosť krokov.Ak nie ,
                 tak dostanete odpoveď , že ste sa stratili v lese a objaví sa video.""")

col1, col2, col3 = st.columns(3)
with col1:
   strana_lesa=st.number_input('Strana lesa:' , min_value=20,max_value=100,step=5 , value=20)

with col2:
   krok=st.slider('Velkost kroka od-do:' , min_value=1,max_value=10,step=1 , value=[1,5])

with col3:
   pocet_krokov=st.number_input('Pocet krokov:' , min_value=5,max_value=100,step=5 , value=20)

od,do = krok
kroky=range(od,do+1)

rw=Randomwalk(pocet_krokov=pocet_krokov, krok=kroky , strana_lesa=strana_lesa)
rw.fill_walk()

point_numbers=range(len(rw.x_values))

x1, y1 = [-strana_lesa,strana_lesa], [strana_lesa,strana_lesa]
x2,y2 = [-strana_lesa,strana_lesa], [-strana_lesa,-strana_lesa]
x3,y3 = [-strana_lesa,-strana_lesa], [-strana_lesa,strana_lesa]
x4,y4 = [strana_lesa,strana_lesa], [-strana_lesa,strana_lesa]

st.text(f'{rw.vysledok}')

if rw.vysledok=='STRATILI STE SA V LESE!!':
    video_file = open('videos/gif.mp4', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes , start_time=0 )
    
    
else:
    import time

    fig, ax1 = plt.subplots()



    ax1.plot(x1, y1, marker = 'o')
    ax1.plot(x2, y2, marker = 'o')
    ax1.plot(x3, y3, marker = 'o')
    ax1.plot(x4, y4, marker = 'o')
    ax1.set(xlim=(-(strana_lesa+15), (strana_lesa+15)), ylim=(-(strana_lesa+15), (strana_lesa+15)))

    time.sleep(0.6)
    #line, = ax1.plot(rw.x_values,rw.y_values , marker='o', markerfacecolor="green" )
    the_plot = st.pyplot(fig)

    #def init():  # give a clean slate to start
    #    line.set_ydata([np.nan] * len(x))

    def animate(i):  # update the y values (every 1000ms)
        try:
            line=ax1.plot(rw.x_values[i:i+2],rw.y_values[i:i+2] , marker='o', markerfacecolor="green"  )
            
            ax1.text(rw.x_values[i]+0.5, rw.y_values[i]+0.05, str(i), fontsize=8, color='black')
            
            the_plot.pyplot(fig)
        except:
            pass


    for i in range(len(point_numbers)):
        animate(i)
        time.sleep(0.6)








plt.style.use('classic')



fig, (ax1,ax2) = plt.subplots(1,2 , sharey=True, sharex=True , figsize=(16,9), dpi=100)




ax1.plot(rw.x_values,rw.y_values , marker='o', markerfacecolor="green" )


ax1.plot(x1, y1, marker = 'o')
ax1.plot(x2, y2, marker = 'o')
ax1.plot(x3, y3, marker = 'o')
ax1.plot(x4, y4, marker = 'o')
ax1.set(xlim=(-(strana_lesa+15), (strana_lesa+15)), ylim=(-(strana_lesa+15), (strana_lesa+15)))

ax2.scatter(rw.x_values,rw.y_values,s=50 , c=point_numbers ,cmap=plt.cm.Blues)
ax2.scatter(rw.x_values[0],rw.y_values[0],s=100 , c='yellow')
ax2.scatter(rw.x_values[-1],rw.y_values[-1],s=100 , c='yellow')

st.pyplot(fig)

#pridat tu spravu o tom ci sa dostali z lesa alebo nie


    





