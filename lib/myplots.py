"""Module to create plots for streamlit pages."""


import pandas as pd
import altair as alt
from lib import taxinflate
from pathlib import Path
from lib.taxinflate import Wage

import folium
from folium.features import GeoJsonTooltip
import geopandas as gpd



def time_series(input_path: Path) -> alt.Chart:
    """Returns an altair chart: a time-series of real income from PhD stipends and salaried work.
     
    Parameters
    -------
    input_path: Path
        Path to data input directory

    Returns
    -------
    alt.Chart time-series.

    """

    # Read in UK wages and tax data and calculate inflation-adjusted net annual incomes

    wage_file = input_path / "UK_wage_tax.csv"
    

    input_df = pd.read_csv(wage_file, header=1, index_col=0)

    df = pd.DataFrame()
    df["NLW"] = taxinflate.net_income_df(input_df, Wage.NLW, input_path)
    df["RLW"] = taxinflate.net_income_df(input_df, Wage.RLW, input_path)
    df["Stipend"] = taxinflate.net_income_df(input_df,Wage.STP, input_path)

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




def maps(df: pd.DataFrame, column_name: str, legend_name: str, input_path: Path) -> folium.Map:
    """Returns chloropleths of Europe with stipend values.
     
    Parameters
    -------
    input_path: Path
        UK wage and tax data.

    Returns
    -------
    alt.Chart time-series.

    """



    json1 = input_path / "custom.geojson"

    geojson = gpd.read_file(json1)

    # These steps are optional but it makes it easier to view geojson data alongside df
    geojson = geojson[['adm0_iso','geometry']]
    geojson.set_index("adm0_iso",inplace=True)
    df_final = geojson.merge(df, left_index=True,right_index=True)
    df_final = df_final[~df_final['geometry'].isna()]

 
    map1 = folium.Map(location=[55,18], tiles="CartoDB positron", zoom_control=False,
                zoom_start=4, min_zoom=4,max_zoom=4)
    
    map1
    #custom_scale = (df[column_name].quantile((0,0.2,0.4,0.6,0.8,0.9,1))).tolist()

    folium.Choropleth(
        geo_data=json1.as_posix(),
        name="chloropleth",
        data=df_final,
        columns=[df_final.index,column_name],
        key_on="feature.properties.adm0_iso",
        fill_color="YlOrRd",
        #threshold_scale=custom_scale,
        nan_fill_color="White",
        highlight=True,
        fill_opacity=0.7,
        line_opacity=1,
        overlay=False,
        legend_name=legend_name
    ).add_to(map1)

    folium.features.GeoJson(
        data=df_final,
        name=legend_name,
        smooth_factor=2,
        style_function=lambda x: {'color':'black','fillColor':'transparent','weight':0.5},
        tooltip=GeoJsonTooltip(
            fields=["country_name", column_name],
            aliases=["Country", legend_name], 
            localize=True,
            sticky=False,
            labels=True,
            style="""
                background-color: #F0EFEF;
                border: 2px solid black;
                border-radius: 3px;
                box-shadow: 3px;
            """,
            max_width=800,),
                highlight_function=lambda x: {'weight':3,'fillColor':'grey'},
            ).add_to(map1)

    return map1