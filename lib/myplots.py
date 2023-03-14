"""Module to create plots for streamlit pages."""


import pandas as pd
import altair as alt
from lib import taxinflate
from pathlib import Path
from lib.taxinflate import Wage

import folium
from folium.features import GeoJsonTooltip
import geopandas as gpd

import streamlit as st


@st.cache_data(ttl=3600) # Cache data and graphs for 1 hour
def time_series(input_path: Path) -> alt.Chart:
    """Returns an altair chart: a time-series of real income from PhD stipends and salaried work.
    Caches data for one hour after reading in once from the input directory.
     
    Parameters
    -------
    input_path: Path
        Path to input data directory

    Returns
    -------
    alt.Chart time-series.

    """

    # Read in UK wages and tax data
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
    """Returns chloropleths of countries in Europe with stipend values. Chloropleths can't be cached, so if caching is
    required, this function should be passed a cached dataframe instead.
     
    Parameters
    -------
    df: pd.DataFrame
        Dataframe of European stipends and taxes with index set to ISO 3-letter European country code

    column_name: str
        The column name of df to plot on the chloropleth map

    legend_name: str
        A human-readable name for what the column data are
    
    input_path: Path
        Path to input data directory

    Returns
    -------
    folium.Map: the chloropleth map.

    """

    # Read in geojson data: this contains polygons that describe European country borders
    geojson_file = input_path / "custom.geojson"
    geojson_df = gpd.read_file(geojson_file)

    # Pick out geometry info and then merge geojson and financial df into a single dataframe.
    # This is optional, but it makes it easier to debug and sanity check the mapping.
    geojson_df = geojson_df[['adm0_iso','geometry']]
    geojson_df.set_index("adm0_iso",inplace=True)
    df_final = geojson_df.merge(df, left_index=True,right_index=True)
    df_final = df_final[~df_final['geometry'].isna()]

    # Create blank map of Europe
    map = folium.Map(location=[55,18], tiles="CartoDB positron", zoom_control=False,
                zoom_start=4, min_zoom=4,max_zoom=4)
    
    # Overlay financial data as a "heat map" (yellow orange red chloropleth)
    folium.Choropleth(
        geo_data=geojson_file.as_posix(),
        name="chloropleth",
        data=df_final,
        columns=[df_final.index,column_name],
        key_on="feature.properties.adm0_iso",
        fill_color="YlOrRd",
        nan_fill_color="White",
        highlight=True,
        fill_opacity=0.7,
        line_opacity=1,
        overlay=False,
        legend_name=legend_name
    ).add_to(map)

    # Add map pop up for info on mouse hover
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
            ).add_to(map)

    return map