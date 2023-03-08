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

sthelper.write_md(constants.MD_DIR / "map_abstract.md")

file = constants.INPUT_DIR / "europe.csv"

df = curr_conv.get_euro(file)

# todo, this earlier
df["country_name"] = df.index
df.set_index("country_code",inplace=True)

map1 = myplots.maps(df,"corrected_gbp","Equivalent income £/yr")
map2 = myplots.maps(df,"net_euro","Absolute income €/yr")

tab1, tab2, tab3, tab4 = st.tabs(["Chart equivalent income (£/yr)", "Map equivalent income (£/yr)", "Map absolute income (€/yr)", "Data"])

import altair as alt
with tab1:
    st.markdown("#### Equivalent annual income in £ (with purchasing power correction)")
    st.write("Bar chart of annual income in £ (factoring in a correction for the relative cost of living)")

    c = alt.Chart(df,width=800,height=450).mark_bar().encode(
        x=alt.X('country_name:O',
                axis = alt.Axis(title=None)
        ),
        y=alt.Y('corrected_gbp:Q',
            axis=alt.Axis(title="Equivalent income (£/yr)"),
            #scale=alt.Scale(domain=(0,25000))
        ),
        color=alt.Color('corrected_gbp:Q',legend=alt.Legend(title="£/yr"))
    ).interactive()


    st.altair_chart(c)

with tab2:
    st.markdown("#### Equivalent annual income in £ (with purchasing power correction)")
    st.write("Heat map of annual income in £ (factoring in a correction for the relative cost of living)")
    folium_static(map1,width=800,height=800)
    

with tab3:
    st.markdown("#### Actual annual income in € (no purchasing power correction)")
    st.write("Heat map of annual income in € (absolute values with no cost of living correction)")
    folium_static(map2,width=800,height=800)

tab4.write(df)



sthelper.write_md(constants.MD_DIR / "map_method.md")


