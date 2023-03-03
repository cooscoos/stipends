#%%
from pathlib import Path
import streamlit as st

from lib import sthelper
from lib import myplots

# Constants
INPUT_DIR = Path.cwd() / "input"    # location of input data
MD_DIR = Path.cwd() / "markdown"    # location of markdown

# General webpage set up
st.set_page_config(layout="wide")
st.sidebar.title("Info")
st.sidebar.info(
    """
    [WebApp](https://streamlit.todo) | [GitHub](https://github.com/cooscoos/todo) | [Twitter](https://twitter.com/CivilPerry)
    """
)

# Content of page
st.title("PhD stipend income in the UK")
st.info("Click on the left sidebar menu to navigate to other charts.")

sthelper.write_md(MD_DIR / "ts_abstract.md")

# Create and plot time-series chart on the page
c = myplots.time_series(INPUT_DIR / "UK_wage_tax.csv")
st.altair_chart(c,use_container_width=True)

sthelper.write_md(MD_DIR / "ts_method.md")

