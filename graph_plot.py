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
df["NLW"] = taxinflate.net_income_df(input_df, Wage.NLW)
df["RLW"] = taxinflate.net_income_df(input_df, Wage.RLW)
df["Stipend"] = taxinflate.net_income_df(input_df,Wage.STP)

# Convert wide-form to long-form df preferred by altair
df["year"] = df.index
df = df.melt(id_vars='year',var_name="income_type",value_name="income")

# Types here: https://altair-viz.github.io/altair-tutorial/notebooks/02-Simple-Charts.html
c = alt.Chart(df).mark_line(
    point=alt.OverlayMarkDef(filled=False, fill="white")
).encode(
    x='year:O',
    y=alt.Y('income:Q',
        axis=alt.Axis(title="Real annual net income (£)"),
        scale=alt.Scale(domain=(12000,19000))
    ),
    color=alt.Color('income_type:N',legend=alt.Legend(title="Income type"))
)


st.set_page_config(layout="wide")


st.sidebar.title("Info")
st.sidebar.info(
    """
    [WebApp](https://streamlit.todo) | [GitHub](https://github.com/cooscoos/todo) | [Twitter](https://twitter.com/CivilPerry)
    """
)


st.title("Real annual net income in the UK")

st.info("Click on the left sidebar menu to navigate to other charts.")

abstract = f"""
The graph below shows a time series, over the last decade, of the net annual income from:

- National Living Wage (NLW) work;
- Real Living Wage (RLW) work, and;
- UKRI's minimum stipend;

after typical income tax, national insurance and council tax deductions.

All incomes are inflation-adjusted to reflect their real value relative to the current year.

"""

st.markdown(abstract)

st.altair_chart(c,use_container_width=True)

f = open("method1.md", "r")
lines = f.readlines()
for line in lines:
    st.markdown(line)


# %%


