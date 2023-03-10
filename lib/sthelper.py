"""A set of helper functions for repetative tasks in streamlit."""

import streamlit as st
from pathlib import Path

def write_md(md_file: Path):
    """Writes a markdown file located at md_file to a streamlit webpage.
    
    Parameters
    -------
    md_file: Path
        Location of a .md file.

    """
    f = open(md_file, "r")
    lines = f.readlines()
    for line in lines:
        st.markdown(line)
    f.close()

def preamble():
    """Preamble and set up for every streamlit page incl set up sidebar."""

    #st.set_page_config(layout="wide")
    st.sidebar.info(
    """
    [WebApp](https://cooscoos-stipends-time-series-e8m8oo.streamlit.app/) | [GitHub](https://github.com/cooscoos/stipends) | [Twitter](https://twitter.com/CivilPerry)
    """
    )
