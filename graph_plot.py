#%%
import pandas as pd
from pathlib import Path

from enum import Enum
from lib import taxes



# %%

input_dir = Path.cwd() / "input"

wagetax = input_dir / "UK_wage_tax.csv"


df = pd.read_csv(wagetax, header=1)

# %%


