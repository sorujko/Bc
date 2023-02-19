import streamlit as st

st.set_page_config(
    page_title="Welcome",
    page_icon="👋",
)


st.write("# Vitajte! 👋")
st.write("""   \tToto je webová aplikácia , ktorú som vytvoril v rámci praktictej časti
            bakalárskej práce. Obsahom sú momentálne 4 interatktívne podstránky.""")

st.write("#### 1.Podstránka je hod kockami")
st.write("#### 2.Podstránka je cesta z lesa")
st.write("#### 3.Podstránka je práca z dataframom")
st.write("#### 4.Podstránka su realtime covid data dostupne na data.corona.gov API a mapa.covid.chat")

st.sidebar.success("Vyberte si z ponuky hore.")

#streamlit run c:/Users/matdu/Desktop/aplikacia/myapp/stremalit_app.py

#dat k tomu 1 mapu a vyznacit krajiny ktore su v tom boxe

#dat toho jak je ten chodec nejake ohranicenie , ze ci prekona tu lajnu

#dat novu podla videa , ze zadas text o ono ti to vsetky znaky vypise
# a spocita , nejake grafy a tak
