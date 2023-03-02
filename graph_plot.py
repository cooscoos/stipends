#%%
import pandas as pd
from pathlib import Path

from lib import taxinflate
from lib.taxinflate import Wage


import streamlit as st
import altair as alt


# %%

input_dir = Path.cwd() / "input"

wagetax = input_dir / "UK_wage_tax.csv"


input_df = pd.read_csv(wagetax, header=1, index_col=0)

df = pd.DataFrame()
df["NMW"] = taxinflate.net_income_df(input_df, Wage.NLW)
df["RLW"] = taxinflate.net_income_df(input_df, Wage.RLW)
df["Stipend"] = taxinflate.net_income_df(input_df,Wage.STP)


# Make the index the year


st.title("Real income from NMW, RLW and UKRI Stipend")
st.line_chart(df)

# %%


