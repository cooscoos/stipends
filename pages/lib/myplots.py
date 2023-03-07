"""Module to create plots for streamlit pages."""


import pandas as pd
import altair as alt
from pages.lib import taxinflate
from pathlib import Path
from pages.lib.taxinflate import Wage
from pages.lib import euro_conv


import folium

from pages.lib import constants


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




def maps(file: Path, column_name: str, legend_name: str) -> folium.Map:
    """Returns chloropleths of Europe with stipend values.
     
    Parameters
    -------
    file: Path
        UK wage and tax data.

    Returns
    -------
    alt.Chart time-series.

    """


    df = euro_conv.get_euro(file)
    
    json1 = constants.INPUT_DIR / "custom.geojson"

    tiletype = 'CartoDB positron'

    map1 = folium.Map(location=[55,18], tiles=tiletype, zoom_control=False,
                zoom_start=4, min_zoom=4,max_zoom=4)

    folium.Choropleth(
        geo_data=json1.as_posix(),
        name="chloropleth",
        data=df,
        columns=["country_code",column_name],
        key_on="feature.properties.adm0_iso",
        fill_color="YlOrRd",
        fill_opacity=0.8,
        line_opacity=0.1,
        legend_name=legend_name
    ).add_to(map1)


    return map1