"""Module for various tax calcs"""

from pathlib import Path
import pandas as pd
import math



def net_income(gross_rate: float, allowance: int, counc_tax: int) -> int:
    """Returns the net annual income after income tax, national insurance, and typical council tax payments,
    assuming that all income tax is paid at the lowest rate (20%). Valid for years 2012 and beyond.
    
    
    Parameters
    -------
    gross_rate: float
        Hourly rate (£/hr) from employment prior to tax deductions.

    allowance: int
        Personal allowance (£) for that year.
        
    counc_tax: int
        Annual council tax for that year.

    Returns
    -------
    Estimated net annual income after deductions.

    """

    if math.isnan(gross_rate):
        return math.nan

    # Assume ~37.5 hrs/wk * 52 weeks = 1950 work hours per year
    gross_annual = gross_rate*1950

    # Income tax calculated as:
    income_tax = (gross_annual - allowance)*0.2

    # National insurance is always about £600 /yr
    nat_ins = 600

    net_income = gross_annual - income_tax - nat_ins - counc_tax

    return int(net_income)


def real_value(income: int, income_year: int, base_year: int) -> int:
    """Inflation adjust income obtained in year to find its real value in base year.
    
    
    Parameters
    -------
    income: int
        An amount of money earned in a given income year

    income_year: int
        The income year (2012 -> present)
        
    base_year: int
        The year to adjust real value to (usually the present year)

    Returns
    -------
    Real value of income relative to base year.

    """

    if math.isnan(income):
        return math.nan # is a float, can be int?


    
    # Read in the CPIH values from csv and convert to dictionary
    input_dir = Path.cwd() / "input"
    cpih_csv = input_dir / "cpih.csv"

    cpih_dict = pd.read_csv(cpih_csv, skiprows=1,index_col=0).squeeze("columns").to_dict()

    # CPIH for base / income year = real value multiplier
    real_mult = cpih_dict.get(base_year) / cpih_dict.get(income_year)

    # Return real value of income
    return int(income*real_mult)
