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
