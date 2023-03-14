"""Module for handling PhD income calculations for European countries."""

from pathlib import Path
import pandas as pd
import requests
import streamlit as st


@st.cache_data(ttl=3600) # cache data for 1 hour
def get_europe_incomes(input_path: Path) -> pd.DataFrame:
    """Returns the net annual income for PhD students around Europe after taxes and cost of living corrections.
     
    Parameters
    -------
    input_path: Path
        Path to input data directory

    Returns
    -------
    pd.DataFrame The net income of PhD students in euros and gbp before and after cost of living corrections.
    """

    # Read in Europe data wages and tax data
    input_df = pd.read_csv(input_path / "europe.csv", header=1, index_col=0)

    # Get exchange rates from api (or cache)
    rates = get_api_exrates()

    # Use income and tax data with exchange rates to calculate net annual stipend for PhD students around Europe in euros
    df = net_income_euros(input_df,rates)

    # We now want to make the cost of living correction. We could use API to get PPP values as follows...
    #oecd_base =  "https://stats.oecd.org/SDMX-JSON/data/"
    #requester = "SNA_TABLE4/AUT+BEL+DNK+FIN+FRA+DEU+IRL+ITA+NLD+NOR+POL+PRT+ESP+SWE+CHE+GBR+USA.PPPGDP.CD/all?startTime=2021&endTime=2022&dimensionAtObservation=allDimensions"
    #response = requests.get(oecd_base + requester)

    # ...but connection to OECD doesn't support up-to-date encryption.
    # PPP values are only updated once every 3 years anyway, so just grab data from a local csv.
    ppp_csv = input_path / "SNA_TABLE4_08032023100526351.csv"
    ppp_df = pd.read_csv(ppp_csv, header=0, index_col=1)
       
    # Use PPP values and exchange rates to convert net euro values to an equivalent gbp after cost of living correction
    df = gbp_worth(df, ppp_df, rates)

    return df


@st.cache_data(ttl=86400) # cache data for 1 day (86400 seconds)
def get_api_exrates() -> dict:
    """Returns exchange rates for Euros.

    Returns
    -------
    dict: Today's exchange rates to Euros.
    """
    response = requests.get('https://api.exchangerate-api.com/v4/latest/euro').json()
    rates = response.get('rates')
    return rates


@st.cache_data(ttl=3600) # cache data for 1 hour
def net_income_euros(df: pd.DataFrame, rates: dict) -> pd.DataFrame:
    """Returns the net annual income (in Euros) for a PhD student after taxes
     
    Parameters
    -------
    df: pd.DataFrame
        European countries annual stipend/wages, taxes, and currency data

    rates: dict
        Exchange rates to EUR (use e.g. exchangerate-api.com)

    Returns
    -------
    pd.DataFrame The net income of a PhD student in euros
    """
    
    # Find the net income in local currency
    net_local = df['stip'] - df['tax'] - df['fee']

    # Get conversions from local currency to EUR
    conversion = df['curr'].apply(lambda row: rates.get(row))

    # Return net income in euros (rounded to nearest euro)
    df['net_euro'] = net_local/conversion
    df['net_euro'] = df['net_euro'].round()

    return df



@st.cache_data(ttl=3600) # cache data for 1 hour
def gbp_worth(df: pd.DataFrame, ppp_df: pd.DataFrame, rates: dict) -> pd.DataFrame:
    """Updates the input df with a column that shows the annual income (in £) for a PhD
    student after purchasing power parity (PPP) correction for the cost of living.
     
    Parameters
    -------
    df: pd.DataFrame
        Net annual income in Euros for each country

    ppp_df: pd.DataFrame
        PPP values for each country

    rates: dict
        Exchange rates to EUR (use e.g. exchangerate-api.com)

    Returns
    -------
    pd.DataFrame The annual income of PhD student in £ after PPP correction
    """
    
    # Update income df to have a an ISO 3-letter country code
    df["country_code"] = ppp_df["LOCATION"]

    # PPP values are given in local currency per USD. Convert to euros per USD.
    ppp_df["Unit mult"] = ppp_df['Unit Code'].apply(lambda row: rates.get(row))
    df["ppp"] = ppp_df["Value"] / ppp_df["Unit mult"]

    # Divide ppp values by the UK's to find a multiplier
    base_ppp = df["ppp"][df.index=="United Kingdom"].values[0]
    df["col_correction"] = base_ppp/df["ppp"]

    # Find euros and gbp after a cost of living correction
    df["corrected_euros"] = df["net_euro"] * df["col_correction"]
    df["corrected_gbp"] =  df["corrected_euros"] * rates.get("GBP")

    # Round to nearest integer
    df['corrected_euros'] = df['corrected_euros'].round()
    df['corrected_gbp'] = df['corrected_gbp'].round()

    # Make the ISO country code the index of df
    df["country_name"] = df.index
    df.set_index("country_code",inplace=True)


    return df
