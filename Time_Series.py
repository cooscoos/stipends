#%%
import streamlit as st

from pages.lib import myplots
from pages.lib import sthelper
from pages.lib import constants

# General webpage set up
sthelper.preamble()

# Content of page
st.title("UK PhD stipends over time")
st.info("Click on the left sidebar menu to navigate to other charts.")

sthelper.write_md(constants.MD_DIR / "ts_abstract.md")

# Create and plot time-series chart on the page
c = myplots.time_series(constants.INPUT_DIR / "UK_wage_tax.csv")
st.altair_chart(c,use_container_width=True)

sthelper.write_md(constants.MD_DIR / "ts_method.md")

