"""Module to create plots for streamlit pages."""


import pandas as pd
import altair as alt
import pages.lib.taxinflate as taxinflate
from pathlib import Path
from pages.lib.taxinflate import Wage


def time_series(file: Path) -> alt.Chart:
    """Returns an altair chart: a time-series of real income from PhD stipends and salaried work.
     
    Parameters
    -------
    file: Path
        UK wage and tax data.

    Returns
    -------
    alt.Chart time-series.

    """

    # Read in UK wages and tax data and calculate inflation-adjusted net annual incomes
    input_df = pd.read_csv(file, header=1, index_col=0)

    df = pd.DataFrame()
    df["NLW"] = taxinflate.net_income_df(input_df, Wage.NLW)
    df["RLW"] = taxinflate.net_income_df(input_df, Wage.RLW)
    df["Stipend"] = taxinflate.net_income_df(input_df,Wage.STP)

    # Convert wide-form dataframe to the long-form preferred by altair
    df["year"] = df.index
    df = df.melt(id_vars='year',var_name="income_type",value_name="income")

    # Define a time-series chart
    # Info on type notation: https://altair-viz.github.io/altair-tutorial/notebooks/02-Simple-Charts.html
    c = alt.Chart(df,height=450).mark_line(
        point=alt.OverlayMarkDef(filled=False, fill="white")
    ).encode(
        x='year:O',
        y=alt.Y('income:Q',
            axis=alt.Axis(title="Real annual net income (£)"),
            scale=alt.Scale(domain=(12000,19000))
        ),
        color=alt.Color('income_type:N',legend=alt.Legend(title="Income type"))
    )
    return c