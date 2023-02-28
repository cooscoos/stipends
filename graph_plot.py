#%%
import pandas as pd
from pathlib import Path

from lib import taxinflate



# %%

input_dir = Path.cwd() / "input"

wagetax = input_dir / "UK_wage_tax.csv"


df = pd.read_csv(wagetax, header=1)

df["nmw_net"] = df.apply(
    lambda row: taxinflate.net_income(row.nmw_rate, row.allowance, row.counctax),
    axis=1
)

df["rlw_net"] = df.apply(
    lambda row: taxinflate.net_income(row.rlw_rate, row.allowance, row.counctax),
    axis=1
)


df["nmw_netreal"] = df.apply(
    lambda row: taxinflate.real_value(row.nmw_net, row.year, 2023),
    axis=1
)

df["rlw_netreal"] = df.apply(
    lambda row: taxinflate.real_value(row.rlw_net, row.year, 2023),
    axis=1
)

df["stipend_netreal"] = df.apply(
    lambda row: taxinflate.real_value(row.stipend, row.year, 2023),
    axis=1
)

# %%


