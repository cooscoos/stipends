"""Home page"""

from pathlib import Path
import streamlit as st

import pandas as pd

from lib import calculations
from lib import myplots
from lib import sthelper


# Filepath constants for input data and markdown
INPUT_DIR = Path.cwd() / "input"
MD_DIR = Path.cwd() / "markdown"

# Base year for real value calculations
BASE_YEAR = 2024

# Webpage set up
st.set_page_config(page_title="UKRI Stipends", page_icon=":eyeglasses:")
sthelper.do_sidebar()

# Page content
st.title("UK PhD stipends: the last decade")
st.info("Click on the left sidebar menu to navigate to other charts.")

# Introduce the graphs
sthelper.write_md(MD_DIR / "ts_abstract.md")

# Create and plot time-series chart on the page
df = calculations.do_calcs(input_path=INPUT_DIR, base_year=BASE_YEAR)

c = myplots.time_series_plot(
    df,
    min_y=12000,
    max_y=32000,
    chart_title=f"Inflation adjusted to {BASE_YEAR}")

st.altair_chart(c, use_container_width=True)

# Describe the method
sthelper.write_md(MD_DIR / "ts_method.md")
