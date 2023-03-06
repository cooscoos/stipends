"""Module for handling currency and value conversions between European countries."""

import pandas as pd

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
    new_df = pd.DataFrame()
    new_df.index = df.index
    new_df['net_euro'] = net_local/conversion

    return new_df




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
    ppp_df["ppp"] = ppp_df["Value"] / ppp_df["Unit mult"]

    # The only thing we now care about is this ppp value
    ppp = ppp_df['ppp']

    # Divide ppp values by the UK's to find a multiplier
    base_ppp = ppp[ppp.index=="United Kingdom"].values[0]
    correction = ppp/base_ppp

    merged_df = df.merge(correction,left_index=True, right_index=True)

    # Calculate the corrected £ value
    final = pd.DataFrame()
    final["gbp"] = (merged_df["net_euro"] / merged_df["ppp"]) * rates.get("GBP")

    return final
