import pandas as pd
import requests
from pathlib import Path
from pages.lib import curr_conv

from pages.lib import constants


def get_euro(file: Path) -> pd.DataFrame:

    # Read in Europe data wages and tax data and calculate inflation-adjusted net annual incomes
    input_df = pd.read_csv(file, header=1, index_col=0)

    # Get exchange rates, todo cache and get once per day
    response = requests.get('https://api.exchangerate-api.com/v4/latest/euro').json()
    rates = response.get('rates')

    # Find net annual stipend for all countries in euros
    df = curr_conv.net_income_euros(input_df,rates)


    # We could use API to get PPP values, but the connection to oecd doesn't support up-to-date encryption, and isn't updated very often.
    #oecd_base =  "https://stats.oecd.org/SDMX-JSON/data/"
    #requester = "SNA_TABLE4/AUT+BEL+DNK+FIN+FRA+DEU+IRL+ITA+NLD+NOR+POL+PRT+ESP+SWE+CHE+GBR+USA.PPPGDP.CD/all?startTime=2021&endTime=2022&dimensionAtObservation=allDimensions"
    #response = requests.get(oecd_base + requester)

    # Just use a csv snapshot of this data instead.
    # Read in Europe data wages and tax data and calculate inflation-adjusted net annual incomes
    ppp_df = pd.read_csv(constants.INPUT_DIR / "SNA_TABLE4_06032023125841319.csv", header=0, index_col=1)

    df["country_code"] = ppp_df["LOCATION"]
    df.dropna(inplace=True)

    # now convert to gbp
    final = curr_conv.gbp_worth(df, ppp_df, rates)
    #final["country_code"] = ppp_df["LOCATION"]

    df = df.merge(final,left_index=True,right_index=True)


    return df
