### Method and assumptions:

#### Income data

- NLW values are obtained from [[1]](https://www.gov.uk/government/publications/20-years-of-the-national-minimum-wage) and related government publications.
- The Real Living Wage Foundation's Real Living Wage (RLW) is obtained from [[2]](https://www.livingwage.org.uk/what-real-living-wage).
- UKRI minimum annual stipends are publicly available in lots of places, including [[3]](https://www.uea.ac.uk/research/research-with-us/postgraduate-research/latest-phds-and-research-studentships/postgraduate-research-fees-and-funding/stipends-and-fee-levels).

NLW and RLW salaries (£/hr) are converted to net annual income (£) by assuming a person works an average of 37.5&nbsp;hr/wk for 52&nbsp;weeks per year, i.e.:

Gross annual salary = hourly rate (£/hr) $\times$ 1950 hr/year.

#### Tax deductions

UKRI stipends are not subject to income taxes, and PhD students do not pay concil tax. Their net income is therefore equal to their annual stipend.

For salaried jobs at NLW / RLW rates:

- Income tax of 20% is applied to income above the personal allowance for that year.
- National insurance contributions on 37.5&nbsp;hr/wk minimum / real living wage jobs have hovered between £550-£650/yr over the last decade, so we subtract a flat quantity of £600.
- PhD students do not pay council tax, so we should also subtract council tax from the take-home pay of NLW / RLW salaries to make the incomes equivalent. Average historical council tax figures can be found in [[4]](https://www.gov.uk/government/statistical-data-sets/live-tables-on-council-tax), and we have used the average for England in each year.

The final net income for salaried NLW / RLW jobs is therefore:

Net income = gross annual salary - income tax - national insurance - council tax.

#### Real value calculation 

The real value of income from previous years can be calculated using the consumer price index with housing costs (CPIH), taken from the ONS [[5]](https://www.ons.gov.uk/economy/inflationandpriceindices/timeseries/l522/mm23).

If you had income, $I$, in 2013 and wanted to calculate what its equivalent value, $R$, would be in 2023, you would use: 

$$ R = I \times {C(2023) \over C(2013)} $$,

where $C(2023)$ and $C(2013)$ are the CPIH values in 2023 and 2013 respectively. In the time series graph, the net incomes from UKRI stipends, NLW / RLW are inflation adjusted using this equation.

Inflation adjustment is not required to show that PhD stipends and the national living wage (NLW) have converged, but it does show that PhD stipends have failed to keep pace with inflation &mdash; even more so than salaried jobs.