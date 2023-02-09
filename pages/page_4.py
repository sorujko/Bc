import requests
import pandas as pd
import datetime
from matplotlib import pyplot as plt
import streamlit as st
st.set_page_config(layout="wide")
import plotly.graph_objects as go

plt.style.use("fivethirtyeight")
#Mozem dat ze proste kolko ktori den pribudlo nakazenyhc v akom kraji  , kolko pribudlo ockovanych
tab1, tab2 = st.tabs(["Vakcíny + Pozitivita", "PCR okresy"])
with tab1:
    datum=datetime.datetime(2023, 1, 1)
    d_set = st.date_input(
        "Zvolte datum , od ktoreho chcete dane statistiky sledovat",
        datum)

    #VACKCINACIE
    #dnes=datetime.now()
    #today=dnes.strftime("%Y-%m-%d")
    

    try:
        pribudli_vakcinacie_request = requests.get(f"https://data.korona.gov.sk/api/vaccinations?updated_since={d_set}%2008%3A34%3A56")

        pribudli_vakcinacie_json=pribudli_vakcinacie_request.json()

        vacinations=pribudli_vakcinacie_json['page']

        df= pd.DataFrame(vacinations)
        spolu_vakciny=df['dose2_count'].sum() + df['dose1_count'].sum()

        Kosicky=df[df['region_id']==1]['dose1_count'].sum() + df[df['region_id']==1]['dose2_count'].sum()
        Nitriansky=df[df['region_id']==2]['dose1_count'].sum() + df[df['region_id']==2]['dose2_count'].sum()
        Bratislavsky=df[df['region_id']==3]['dose1_count'].sum() + df[df['region_id']==3]['dose2_count'].sum()
        Trenciansky=df[df['region_id']==4]['dose1_count'].sum() + df[df['region_id']==4]['dose2_count'].sum()
        Zilinsky=df[df['region_id']==5]['dose1_count'].sum() + df[df['region_id']==5]['dose2_count'].sum()
        Banskobystricky=df[df['region_id']==6]['dose1_count'].sum() + df[df['region_id']==6]['dose2_count'].sum()
        Trnavsky=df[df['region_id']==7]['dose1_count'].sum() + df[df['region_id']==7]['dose2_count'].sum()
        Presovsky=df[df['region_id']==8]['dose1_count'].sum() + df[df['region_id']==8]['dose2_count'].sum()
        kraje_nazvy=['spolu_vakciny','Kosicky','Nitriansky','Bratislavsky','Trenciansky','Zilinsky','Banskobystricky','Trnavsky','Presovsky']
        kraje=[spolu_vakciny,Kosicky,Nitriansky,Bratislavsky,Trenciansky,Zilinsky,Banskobystricky,Trnavsky,Presovsky]

        d=pd.DataFrame()
        d['kraje']=kraje_nazvy
        d['pocty_novo_zaockovanych']=kraje

        import plotly.express as px
        fig = px.bar(d,x='pocty_novo_zaockovanych',  y="kraje", orientation='h')

        st.write(fig)
    except:
        st.write("""##### Pre dnesnok este nenahodili udaje  , skuste skorsi datum""")



    #AG testy


    pribudli_vakcinacie_request = requests.get(f"https://data.korona.gov.sk/api/ag-tests/by-region?updated_since={d_set}%2012%3A34%3A56")

    #df = pd.DataFrame(r.json())
    pribudli_vakcinacie_json=pribudli_vakcinacie_request.json()
    vacinations=pribudli_vakcinacie_json['page']
    df= pd.DataFrame(vacinations)


    try:
        
        d_set=d_set.strftime("%Y-%m-%d")
        df=df.loc[df['published_on']>=d_set,:]


        spolu_vakciny=df['positives_count'].sum()

        Kosicky=df[df['region_id']==1]['positives_count'].sum()
        Nitriansky=df[df['region_id']==2]['positives_count'].sum() 
        Bratislavsky=df[df['region_id']==3]['positives_count'].sum() 
        Trenciansky=df[df['region_id']==4]['positives_count'].sum() 
        Zilinsky=df[df['region_id']==5]['positives_count'].sum() 
        Banskobystricky=df[df['region_id']==6]['positives_count'].sum() 
        Trnavsky=df[df['region_id']==7]['positives_count'].sum() 
        Presovsky=df[df['region_id']==8]['positives_count'].sum()
        kraje_nazvy=['testy_spolu','Kosicky','Nitriansky','Bratislavsky','Trenciansky','Zilinsky','Banskobystricky','Trnavsky','Presovsky']
        kraje=[spolu_vakciny,Kosicky,Nitriansky,Bratislavsky,Trenciansky,Zilinsky,Banskobystricky,Trnavsky,Presovsky]

        spolu_vakcinyn=df['negatives_count'].sum()
        Kosickyn=df[df['region_id']==1]['negatives_count'].sum()
        Nitrianskyn=df[df['region_id']==2]['negatives_count'].sum() 
        Bratislavskyn=df[df['region_id']==3]['negatives_count'].sum() 
        Trencianskyn=df[df['region_id']==4]['negatives_count'].sum() 
        Zilinskyn=df[df['region_id']==5]['negatives_count'].sum() 
        Banskobystrickyn=df[df['region_id']==6]['negatives_count'].sum() 
        Trnavskyn=df[df['region_id']==7]['negatives_count'].sum() 
        Presovskyn=df[df['region_id']==8]['negatives_count'].sum()

        krajen=[spolu_vakcinyn,Kosickyn,Nitrianskyn,Bratislavskyn,Trencianskyn,Zilinskyn,Banskobystrickyn,Trnavskyn,Presovskyn]

        import plotly.express as px
        d=pd.DataFrame()
        d['kraje']=kraje_nazvy
        d['pocty_poz']=kraje
        col1, col2 = st.columns([1,2],gap="large")
        with col1:
            d['kraje']=kraje_nazvy
            d['pocty_poz']=kraje
            fig = px.bar(d,x='pocty_poz',  y="kraje", orientation='h')
            fig.update_layout(
            height=400,
            width=400,)
            st.write(fig)
        with col2:
            d['kraje']=kraje_nazvy
            d['pocty_neg']=krajen
            fig = px.bar(d,x='pocty_neg',  y="kraje", orientation='h')
            st.write(fig )
        

        #tu su pie charty matplotlib prve 4
        try:
            col1, col2,col3,col4 = st.columns(4)
            Kosice= [kraje[1],krajen[1]]
            Nitra= [kraje[2],krajen[2]]
            Bratislava= [kraje[3],krajen[3]]
            Trencin= [kraje[4],krajen[4]]
            with col1:
                figure, axes = plt.subplots()
                plt.pie(Kosice, labels=['Pozitívne','Negatívne'],  shadow=True,
                        startangle=90, autopct='%1.1f%%',
                        wedgeprops={'edgecolor': 'black'})
                plt.title("Miera pozitivity Ag testov v KE kraji")
                plt.tight_layout()
                st.write(figure)
        except:
            st.write("Graf pre Kosice sa nepodarilo zobrazit , neboli dodane udaje cez api, skuste skorsi datum")

        try:
            with col2:
                figure, axes = plt.subplots()
                plt.pie(Nitra, labels=['Pozitívne','Negatívne'],  shadow=True,
                        startangle=90, autopct='%1.1f%%',
                        wedgeprops={'edgecolor': 'black'})
                plt.title("Miera pozitivity Ag testov v NI kraji")
                plt.tight_layout()
                st.write(figure)
        except:
            st.write("Graf pre Nitru sa nepodarilo zobrazit , neboli dodane udaje cez api, skuste skorsi datum")
        try:
            with col3:
                figure, axes = plt.subplots()
                plt.pie(Bratislava, labels=['Pozitívne','Negatívne'],  shadow=True,
                        startangle=90, autopct='%1.1f%%',
                        wedgeprops={'edgecolor': 'black'})
                plt.title("Miera pozitivity Ag testov v BA kraji")
                plt.tight_layout()
                st.write(figure)
        except:
            st.write("Graf pre Bratislavu sa nepodarilo zobrazit , neboli dodane udaje cez api, skuste skorsi datum")
        
        try:
            with col4:
                figure, axes = plt.subplots()
                plt.pie(Trencin, labels=['Pozitívne','Negatívne'],  shadow=True,
                        startangle=90, autopct='%1.1f%%',
                        wedgeprops={'edgecolor': 'black'})
                plt.title("Miera pozitivity Ag testov v TN kraji")
                plt.tight_layout()
                st.write(figure)
        except:
            st.write("Graf pre Trenin sa nepodarilo zobrazit , neboli dodane udaje cez api, skuste skorsi datum")

        try:
            col1, col2,col3,col4 = st.columns(4)
            Zilina= [kraje[5],krajen[5]]
            BanskaBystrica= [kraje[6],krajen[6]]
            Trnava= [kraje[7],krajen[7]]
            Presov= [kraje[8],krajen[8]]

            with col1:
                figure, axes = plt.subplots()
                plt.pie(Zilina, labels=['Pozitívne','Negatívne'],  shadow=True,
                        startangle=90, autopct='%1.1f%%',
                        wedgeprops={'edgecolor': 'black'})
                plt.title("Miera pozitivity Ag testov v ZA kraji")
                plt.tight_layout()
                st.write(figure)
        except:
            st.write("Graf pre Zilinu sa nepodarilo zobrazit , neboli dodane udaje cez api, skuste skorsi datum")

        try:
            with col2:
                figure, axes = plt.subplots()
                plt.pie(BanskaBystrica, labels=['Pozitívne','Negatívne'],  shadow=True,
                        startangle=90, autopct='%1.1f%%',
                        wedgeprops={'edgecolor': 'black'})
                plt.title("Miera pozitivity Ag testov v BB kraji")
                plt.tight_layout()
                st.write(figure)
        except:
            st.write("Graf pre Bansku Bystricu sa nepodarilo zobrazit , neboli dodane udaje cez api, skuste skorsi datum")

        try:
            with col3:
                figure, axes = plt.subplots()
                plt.pie(Trnava, labels=['Pozitívne','Negatívne'],  shadow=True,
                        startangle=90, autopct='%1.1f%%',
                        wedgeprops={'edgecolor': 'black'})
                plt.title("Miera pozitivity Ag testov v TA kraji")
                plt.tight_layout()
                st.write(figure)
        except:
                st.write("Graf pre Trnavu sa nepodarilo zobrazit , neboli dodane udaje cez api, skuste skorsi datum")
        try:
            with col4:
                figure, axes = plt.subplots()
                plt.pie(Presov, labels=['Pozitívne','Negatívne'],  shadow=True,
                        startangle=90, autopct='%1.1f%%',
                        wedgeprops={'edgecolor': 'black'})
                plt.title("Miera pozitivity Ag testov v PO kraji")
                plt.tight_layout()
                st.write(figure)
        except:
            st.write("Graf pre Kosice sa nepodarilo zobrazit , neboli dodane udaje cez api, skuste skorsi datum")
    


        
        
            

    except:
        st.write("""##### Pre dnesnok este nenahodili udaje pre Ag testy , skuste skorsi datum""")

with tab2:
    st.write("bohuzial streamlit io nevie tento content nacitat , pre viac info pozrite moj github")
    st.write("https://github.com/sorujko/Bc")
    import os, sys

    @st.experimental_singleton
    def installff():
        os.system('sbase install geckodriver')
        os.system('ln -s /home/appuser/venv/lib/python3.9/site-packages/seleniumbase/drivers/geckodriver /home/appuser/venv/bin/geckodriver')

    _ = installff()
    import pandas as pd
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    #from selenium.webdriver.chrome.options import Options
    import numpy as np
   
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    
    # Start a Microsoft Edge webdriver in headless mode
    driver = webdriver.Chrome(executable_path="chromedriver.exe",options=options)
    # Navigate to the specified webpage
    driver.get("https://mapa.covid.chat/")
    try:
        if len(driver.find_elements(By.ID, "c-p-bn")) > 0:
            # Click on the accept cookies button
            driver.find_element(By.ID, "c-p-bn").click()
    except:
        pass
    # Wait for the tbody element with id "cities-table" to be present

    try:
        wait = WebDriverWait(driver ,timeout=10)
        wait.until(EC.text_to_be_present_in_element((By.XPATH, "//tbody[@id='cities-table']"), "Prievidza"))

    except:
        pass
    tbody = driver.find_element(By.XPATH, "//tbody[@id='cities-table']")
    # Get the rows from the tbody element
    rows = tbody.find_elements(By.XPATH, "tr")

    # Store the data in a list
    data = []
    for row in rows:
        cells = row.find_elements(By.XPATH, "td")
        row_data = [cell.text for cell in cells]
        data.append(row_data)

    # Create a pandas dataframe from the data
    df = pd.DataFrame(data, columns=['okres', 'pocet', 'nove_pripady'])
    df.sort_values(by=['okres'] , inplace=True)
    df.to_csv("covid_data2.csv", index=False, encoding='UTF-8-sig')


    # Close the webdriver
    driver.quit()
    import geopandas as gpd
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    st.write("Ak sa nezobrazí modrá mapa/nie su na nej cisla , dajte prosim Rerun , aj viackrat , ano funguje to xD")
    # Load your GeoDataFrame
    okresy = pd.read_csv('covid_data2.csv')
    okresy.fillna(0, inplace=True)
    okresy['nove_pripady'] = okresy['nove_pripady'].astype(np.int64)

    gdf = gpd.read_file('districts.shp', encoding = 'utf8')
    gdf = gpd.GeoDataFrame(gdf, geometry='geometry')
    gdf.crs = 'epsg:4326'
    # Plot the GeoDataFrame
    ax = gdf.plot()
    annotations = []
    for i,row in gdf.iterrows():
        if okresy.iloc[i,2]>0:
            annotation=plt.annotate(okresy.iloc[i,2], xy=row.geometry.centroid.coords[0], ha='center', fontsize=10)
            annotations.append(annotation)
    # Show the plot
    fig= ax.get_figure()
    st.pyplot(fig)
    st.image('okresy.png')
    


    

    

    


