#%%
import streamlit as st
import altair as alt
from pathlib import Path
from streamlit_folium import folium_static
import sys  

# add lib to path
sys.path.append('../..')

from lib import myplots
from lib import sthelper
from lib import phdincome


# Filepath constants for input data and markdown
INPUT_DIR = Path.cwd()  / "input"
MD_DIR = Path.cwd() / "markdown" 


# Webpage set up
sthelper.sidebar()

# Page content
st.title("PhD incomes across Europe")
st.info("Click on the left sidebar menu to navigate to other charts.")

# Introduce the graphs
st.warning("These maps are a work in progress and may be inaccurate. If you'd like to help fill in some blanks, or if you've spotted a mistake in income or taxes for a country, then please contact me using one of the links in the sidebar to the left.")
sthelper.write_md(MD_DIR / "map_abstract.md")

# Grab PhD stipend/salary income data from around Europe
df = phdincome.get_europe_incomes(INPUT_DIR)

# Use data to plot chloropleths of student income
map1 = myplots.maps(df,"corrected_gbp","Equivalent income £/yr", INPUT_DIR)
map2 = myplots.maps(df,"net_euro","Absolute income €/yr", INPUT_DIR)

tab1, tab2, tab3, tab4 = st.tabs(["Chart equivalent income (£/yr)", "Map equivalent income (£/yr)", "Map absolute income (€/yr)", "Data"])

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

# Describe the method
sthelper.write_md(MD_DIR / "map_method.md")
