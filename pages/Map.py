#%%
from pathlib import Path
import streamlit as st
import pandas as pd
import requests

import sys
sys.path.insert(0, '..')

from lib import sthelper
from lib import myplots

from lib import curr_conv


# Constants - to do define elsewhere higher up and have pages do rendering only with caches
INPUT_DIR = Path.cwd() / ".."/ "input"    # location of input data
MD_DIR = Path.cwd() / ".."/ "markdown"    # location of markdown

# General webpage set up
sthelper.preamble()

# Content of page
st.title("To do, a map")
st.info("Click on the left sidebar menu to navigate to other charts.")


# Read in Europe data wages and tax data and calculate inflation-adjusted net annual incomes
input_df = pd.read_csv(INPUT_DIR / "europe.csv", header=1, index_col=0)

# Get exchange rates, todo cache and get once per day
response = requests.get('https://api.exchangerate-api.com/v4/latest/euro').json()
rates = response.get('rates')

# Find net annual stipend for all countries in euros
df = curr_conv.net_income_euros(input_df,rates)


# We could use API to get PPP values, but the connection to oecd doesn't support up-to-date encryption, and isn't updated very often.
#oecd_base =  "https://stats.oecd.org/SDMX-JSON/data/"
#requester = "SNA_TABLE4/AUT+BEL+DNK+FIN+FRA+DEU+IRL+ITA+NLD+NOR+POL+PRT+ESP+SWE+CHE+GBR+USA.PPPGDP.CD/all?startTime=2021&endTime=2022&dimensionAtObservation=allDimensions"
#response = requests.get(oecd_base + requester)

# Just use a csv snapshot of this data instead.
# Read in Europe data wages and tax data and calculate inflation-adjusted net annual incomes
ppp_df = pd.read_csv(INPUT_DIR / "SNA_TABLE4_06032023125841319.csv", header=0, index_col=1)


# now convert to gbp
final = curr_conv.gbp_worth(df, ppp_df, rates)


# sthelper.write_md(MD_DIR / "ts_abstract.md")

# # Create and plot time-series chart on the page
# c = myplots.time_series(INPUT_DIR / "UK_wage_tax.csv")
# st.altair_chart(c,use_container_width=True)

# sthelper.write_md(MD_DIR / "ts_method.md")
# %%
