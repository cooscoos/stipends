"""Module for various tax and inflation calcs in the UK."""

from pathlib import Path
import pandas as pd
import streamlit as st


from enum import Enum
class Wage(str,Enum):
    """Enum:

    - NLW: UKGov's National Living / Minimum Wage rate
    - RLW: Real living wage foundation's Real Living Wage rate
    - STI: UKRI's minumum annual PhD stipend"""

    NLW = "nmw"
    RLW = "rlw"
    STP = "stipend"


def net_income_df(df: pd.DataFrame, wage: Wage, input_path: Path) -> pd.DataFrame:
    """Returns the net annual income after income tax, national insurance, and typical council tax payments,
    assuming that all income tax is paid at the lowest rate (20%). Valid for years 2012 and beyond.
    
    
    Parameters
    -------
    df: pd.DataFrame
        Income data. Must contain a rate, counctax, and allowance fields.

    wage: WageType
        Either national minimum / real living 
    
    base_year: int
        The year to adjust real value to (usually the present year)

    input_path: Path
        Path to input data


    Returns
    -------
    df with of net real annual income for each year after any deductions.

    """

    
    match wage:
        case Wage.NLW | Wage.RLW:
            # Assume 1950 work hours per year
            gross_annual = df[f'{wage}_rate'] *1950

            # Income tax calculated as:
            income_tax = (gross_annual - df["allowance"])*0.2

            # National insurance has been about £600/yr for low wages for decades
            nat_ins = 600

            net_income = gross_annual - income_tax - nat_ins - df["counctax"]

        case Wage.STP:
            net_income = df["stipend"]

    # Inflation adjust the income to find its real value today (in base year)
    real_income = net_income * real_mult(2023, input_path)

    return real_income



@st.cache_data(ttl=3600) # cache data for 1 hour
def real_mult(base_year: int, input_path: Path) -> pd.DataFrame:
    """Use inflation to calculate real value multipliers for each year relative to a base year.
    
    Parameters
    -------
    base_year: int
        The year to adjust real value to (usually the present year)

    input_path: Path
        Path to data

    Returns
    -------
    pd.DataFrame: real value multiplier of income vs year.

    """

    file = input_path / "cpih.csv"
    df = pd.read_csv(file,skiprows=1,index_col=0)

    # Get CPIH from base year
    base_cpih = df["cpih"][df.index==base_year].values[0]

    # Calculate and return the real value multiplier
    mult = base_cpih / df["cpih"]

    return mult


