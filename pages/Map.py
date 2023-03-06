#%%
from pathlib import Path
import streamlit as st

import pandas as pd

import sys
sys.path.insert(0, '..')



from lib import sthelper
from lib import myplots


import requests



# Constants
INPUT_DIR = Path.cwd() / ".."/ "input"    # location of input data
MD_DIR = Path.cwd() / ".."/ "markdown"    # location of markdown

# General webpage set up
sthelper.preamble()

# Content of page
st.title("To do, a map")
st.info("Click on the left sidebar menu to navigate to other charts.")

file = INPUT_DIR / "europe.csv"

# Read in Europe data wages and tax data and calculate inflation-adjusted net annual incomes
input_df = pd.read_csv(file, header=1, index_col=0)


# Get exchange rates, todo cache and get once per day
response = requests.get('https://api.exchangerate-api.com/v4/latest/euro').json()
rates = response.get('rates')


# Add in the column for the euro -> currency conversion

# deduct taxes and fees to find net income in local currency
# convert to euros
def net_income_euros(df: pd.DataFrame, rates: dict) -> pd.DataFrame:
    
    # Net income in local currency
    net_local = df['stip'] - df['tax'] - df['fee']

    # Convert to euros
    conversion = df['curr'].apply(lambda row: rates.get(row))

    new_df = pd.DataFrame()
    new_df.index = df.index

    new_df['net_euro'] = net_local/conversion

    return new_df



df = net_income_euros(input_df,rates)






def gbp_worth(df: pd.DataFrame, rates: dict) -> pd.DataFrame:
    # another fn should
    # apply a PPP multiplier
    # convert to GBP
    # for a separate map in a tab

    # Could use API like so, but the connection to oecd doesn't support up-to-date encryption, and isn't updated very often. Just use a csv snapshot of this data instead.
    #oecd_base =  "https://stats.oecd.org/SDMX-JSON/data/"
    #requester = "SNA_TABLE4/AUT+BEL+DNK+FIN+FRA+DEU+IRL+ITA+NLD+NOR+POL+PRT+ESP+SWE+CHE+GBR+USA.PPPGDP.CD/all?startTime=2021&endTime=2022&dimensionAtObservation=allDimensions"
    #response = requests.get(oecd_base + requester)

    # Read in Europe data wages and tax data and calculate inflation-adjusted net annual incomes
    ppp_df = pd.read_csv(INPUT_DIR / "SNA_TABLE4_06032023125841319.csv", header=0, index_col=1)

    # have to convert to usd per euro
    ppp_df["Unit mult"] = ppp_df['Unit Code'].apply(lambda row: rates.get(row))
    ppp_df["ppp"] = ppp_df["Value"] / ppp_df["Unit mult"]

    ppp = ppp_df['ppp']

    base_ppp = ppp[ppp.index=="United Kingdom"].values[0]

    correction = ppp/base_ppp

    pig = df.merge(correction,left_index=True, right_index=True)

    final = pd.DataFrame()
    final["gbp"] = (pig["net_euro"] / pig["ppp"]) * rates.get("GBP")

    
    return final


# now convert to gbp

final = gbp_worth(df,rates)


# a function to convert 

# sthelper.write_md(MD_DIR / "ts_abstract.md")

# # Create and plot time-series chart on the page
# c = myplots.time_series(INPUT_DIR / "UK_wage_tax.csv")
# st.altair_chart(c,use_container_width=True)

# sthelper.write_md(MD_DIR / "ts_method.md")
# %%
