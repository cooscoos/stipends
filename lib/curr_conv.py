"""Module for handling currency and value conversions between European countries."""

import pandas as pd

import pandas as pd
import requests
from pathlib import Path
from lib import curr_conv




def get_euro(file: Path) -> pd.DataFrame:

    # Read in Europe data wages and tax data and calculate inflation-adjusted net annual incomes
    input_df = pd.read_csv(file, header=1, index_col=0)

    # Get exchange rates, todo cache and get once per day
    response = requests.get('https://api.exchangerate-api.com/v4/latest/euro').json()
    rates = response.get('rates')

    # Find net annual stipend for all countries in euros
    df = net_income_euros(input_df,rates)


    # We could use API to get PPP values, but the connection to oecd doesn't support up-to-date encryption, and isn't updated very often.
    #oecd_base =  "https://stats.oecd.org/SDMX-JSON/data/"
    #requester = "SNA_TABLE4/AUT+BEL+DNK+FIN+FRA+DEU+IRL+ITA+NLD+NOR+POL+PRT+ESP+SWE+CHE+GBR+USA.PPPGDP.CD/all?startTime=2021&endTime=2022&dimensionAtObservation=allDimensions"
    #response = requests.get(oecd_base + requester)

    # Just use a csv snapshot of this data instead.
    # Read in Europe data wages and tax data and calculate inflation-adjusted net annual incomes
    #filename = "SNA_TABLE4_06032023125841319.csv"
    filename = "SNA_TABLE4_08032023100526351.csv"
    INPUT_DIR = Path.cwd() / ".." / "input"
    ppp_df = pd.read_csv(INPUT_DIR / filename, header=0, index_col=1)

    df["country_code"] = ppp_df["LOCATION"]
    #df.dropna(inplace=True)

    # now convert to gbp
    df = gbp_worth(df, ppp_df, rates)
    #final["country_code"] = ppp_df["LOCATION"]

   
    return df


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

    # Return net income in euros
    df['net_euro'] = net_local/conversion

    return df




def gbp_worth(df: pd.DataFrame, ppp_df: pd.DataFrame, rates: dict) -> pd.DataFrame:
    """Returns the annual income (in £) for a PhD student after purchasing power parity (PPP) correction for the cost of living
     
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
    
    # PPP values are given in local currency per USD. Convert to euros per USD.
    ppp_df["Unit mult"] = ppp_df['Unit Code'].apply(lambda row: rates.get(row))
    df["ppp"] = ppp_df["Value"] / ppp_df["Unit mult"]

    # The only thing we now care about is this ppp value


    # Divide ppp values by the UK's to find a multiplier
    base_ppp = df["ppp"][df.index=="United Kingdom"].values[0]
    df["col_correction"] = base_ppp/df["ppp"]

    df["corrected_euros"] = df["net_euro"] * df["col_correction"]

    df["corrected_gbp"] =  df["corrected_euros"] * rates.get("GBP")


    return df
