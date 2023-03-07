#%%

import streamlit as st

from streamlit_folium import folium_static
from pages.lib import myplots

#import plotly.express as px

from pages.lib import sthelper
from pages.lib import constants


#%%

# General webpage set up
sthelper.preamble()

# Content of page
st.title("To do, a map")
st.info("Click on the left sidebar menu to navigate to other charts.")

file = constants.INPUT_DIR / "europe.csv"

map1 = myplots.maps(file,"gbp","Equivalent £")
map2 = myplots.maps(file,"net_euro","Absolute Euros")

tab1, tab2 = st.tabs(["Equivalent annual income (£)", "Absolute annual income (euros)"])

with tab1:
    st.subheader("Equivalent annual £ income after cost of living correction")
    folium_static(map1,width=800,height=800)
    

with tab2:
    st.subheader("Annual income in Euros without cost of living correction")
    folium_static(map2,width=800,height=800)


