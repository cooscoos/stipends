#%%

import streamlit as st

from streamlit_folium import folium_static
from pages.lib import myplots

#import plotly.express as px

from pages.lib import sthelper
from pages.lib import constants
from pages.lib import curr_conv


#%%

# General webpage set up
sthelper.preamble()

# Content of page
st.title("PhD stipends around Europe")
st.info("Click on the left sidebar menu to navigate to other charts.")

file = constants.INPUT_DIR / "europe.csv"

df = curr_conv.get_euro(file)

# todo, this earlier
df["country_name"] = df.index
df.set_index("country_code",inplace=True)

map1 = myplots.maps(df,"gbp","Equivalent income £/yr")
map2 = myplots.maps(df,"net_euro","Absolute income €/yr")


tab1, tab2, tab3 = st.tabs(["Data", "Equivalent income (£/yr)", "Absolute income (€/yr)"])

tab1.write(df)

with tab2:
    st.markdown("#### Equivalent annual income in £ (with purchasing power correction)")
    folium_static(map1,width=800,height=800)
    

with tab3:
    st.markdown("#### Actual annual income in € (no purchasing power correction)")
    folium_static(map2,width=800,height=800)




