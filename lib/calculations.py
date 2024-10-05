"""High level calculations of income."""
from enum import Enum
from pathlib import Path

import pandas as pd
import streamlit as st


class Wage(str, Enum):
    """Enum:
    - NLW: UKGov's National Living / Minimum Wage rate
    - RLW: Real living wage foundation's Real Living Wage rate
    - STI: UKRI's minumum annual PhD stipend
    - GRAD: UKGov's average annual graduate salary (age 21-30)
    - NONGRAD: UKGov's average annual non-graduate salary (age 21-30)
    - POSTGRAD: UKGov's average annual Postgraduate salary (age 21-30)
    """
    NLW = "nmw"
    RLW = "rlw"
    STP = "stipend"
    GRAD = "Graduate"
    NONGRAD = "Non-Graduate"
    POSTGRAD = "Postgraduate"


# Time offsets that apply to each income type. See the ts_method.md for justification.
TIME_OFFSETS = {
    'NLW': 3+0,    # Start of April(m=+3 months after January) + immediate implementation (i=+0)
    'RLW': 10+6,   # End of October(m=+10) + 6 month implementation
    'Stipend': 7+0,  # Start of August(m=+7) + immediate implementation
    'Graduate': +6,  # median salary data is for the middle of the year
    'Non-Graduate': +6,
    'Postgraduate': +6
}


def add_time_offset(row):
    """Adjusts the year of a given row to the correct date based on the income type."""
    offset = TIME_OFFSETS.get(row['income_type'], 0)
    return row['year'] + pd.DateOffset(months=offset)


def parse_uk_gov_tables(input_path: Path) -> pd.DataFrame:
    """Returns trimmed down df of graduate, non-graduate and
    post-graduate salaries from
    `input_path`/yearly_salaries_by_gender2_200723.csv."""
    # Read in and handle the graduate data
    grad_df = pd.read_csv(input_path /
                          "yearly_salaries_by_gender2_200723.csv")

    # Remove gender=Male and gender=Female rows
    grad_df = grad_df[grad_df['gender'].apply(
        lambda x: x not in ['Male', 'Female'])]

    # Only keep age group 21-30
    grad_df = grad_df[grad_df['age_group'] == '21-30']

    # Only keep time_period, graduate_type and median columns
    grad_df = grad_df[['time_period', 'graduate_type', 'median']]

    grad_df = grad_df.pivot(index='time_period',
                            columns='graduate_type',
                            values='median').reset_index()

    # Rename time period to time
    grad_df.rename(columns={'time_period': 'year'}, inplace=True)
    grad_df = grad_df.set_index('year')
    return grad_df


def do_calcs(input_path: Path, base_year: int) -> pd.DataFrame:
    wage_file = input_path / "UK_wage_tax.csv"
    input_df = pd.read_csv(wage_file, header=1, index_col=0)

    grad_df = parse_uk_gov_tables(input_path)

    #merge input_df and graddf on year
    input_df = input_df.merge(grad_df, left_index=True, right_index=True)

    df = pd.DataFrame()
    df["NLW"] = net_income_df(input_df, Wage.NLW, input_path, base_year)
    df["RLW"] = net_income_df(input_df, Wage.RLW, input_path, base_year)
    df["Stipend"] = net_income_df(input_df, Wage.STP, input_path, base_year)
    df["Graduate"] = net_income_df(input_df, Wage.GRAD, input_path, base_year)
    df["Non-Graduate"] = net_income_df(input_df, Wage.NONGRAD, input_path, base_year)
    df["Postgraduate"] = net_income_df(input_df, Wage.POSTGRAD, input_path, base_year)

    # Convert wide-form dataframe to the long-form preferred by altair
    df["year"] = df.index
    df = df.melt(id_vars='year', var_name="income_type", value_name="income")

    # Adjust the year to the correct date using an offset based on the income type
    df['year'] = pd.to_datetime(df['year'], format='%Y')
    df['midpoint_datetime'] = df.apply(add_time_offset, axis=1)

    return df



def net_income_df(df: pd.DataFrame, wage: Wage, input_path: Path,
                  base_year: int) -> pd.DataFrame:
    """Returns the net annual income after income tax, national insurance,
    and typical council tax payments, assuming that all income tax is paid
    at the lowest rate (20%). Valid for years 2012 and beyond.

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
            gross_annual = df[f'{wage}_rate'] * 1950

            # Income tax calculated as:
            income_tax = (gross_annual - df["allowance"]) * 0.2

            # National insurance has been £600/yr for decades
            nat_ins = 600

            net_income = gross_annual - income_tax - nat_ins - df["counctax"]
        case Wage.STP:
            net_income = df["stipend"]
        case Wage.GRAD | Wage.NONGRAD | Wage.POSTGRAD:
            # Yearly incomes
            gross_annual = df[f'{wage}']
            income_tax = (gross_annual - df["allowance"]) * 0.2
            nat_ins = 600
            net_income = gross_annual - income_tax - nat_ins - df["counctax"]

    # Inflation adjust the income to find its real value today (in base year)
    real_income = net_income * real_mult(base_year, input_path)

    return real_income


@st.cache_data(ttl=3600)  # cache data for 1 hour
def real_mult(base_year: int, input_path: Path) -> pd.DataFrame:
    """Return a `df` of real value multipliers vs year. Uses
    inflation info at `input_path`/cpih.csv to calculate real
    value multipliers for each year relative to a `base year`.
    """

    file = input_path / "cpih.csv"
    df = pd.read_csv(file, skiprows=1, index_col=0)

    # Get CPIH from base year
    base_cpih = df["cpih"][df.index == base_year].values[0]

    # Calculate and return the real value multiplier
    mult = base_cpih / df["cpih"]

    return mult
