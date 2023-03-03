### Method and assumptions

#### Income data

- National Living Wage (NLW) values are obtained from [[1]](https://www.gov.uk/government/publications/20-years-of-the-national-minimum-wage) and related government publications.
- The Real Living Wage Foundation's Real Living Wage (RLW) is obtained from [[2]](https://www.livingwage.org.uk/what-real-living-wage).
- UKRI minimum annual stipends are publicly available in lots of places, including [[3]](https://www.uea.ac.uk/research/research-with-us/postgraduate-research/latest-phds-and-research-studentships/postgraduate-research-fees-and-funding/stipends-and-fee-levels).

Table 15 of [[4]](https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/earningsandworkinghours/timeseries/ybuy/lms) shows that, in 2022, the median gross annual earnings for 22-29 year-olds was £27,492, and their median hourly rate was £14.04. This suggests the median 22-29 year-old works ~1950&nbsp;hrs/year (equivalent to working about 40&nbsp;hrs/wk for 48&nbsp;weeks per year).

Gross annual salary for NLW / RLW work is therefore calculated as hourly rate (£/hr) $\times$ 1950 (hr/year).

#### Tax deductions

UKRI stipends are not subject to income taxes, and PhD students do not pay council tax. Their net income is therefore equal to their annual stipend.

For salaried jobs at NLW / RLW rates:

- Income tax of 20% is applied to income above the personal allowance for that year.
- National insurance contributions on 37.5&nbsp;hr/wk minimum / real living wage jobs have hovered between £550-£650/yr over the last decade, so we subtract a flat quantity of £600.
- Average historical council tax figures can be found in [[5]](https://www.gov.uk/government/statistical-data-sets/live-tables-on-council-tax), and we have subtracted the average for England in each year. This is done to make the net incomes from salaried work and PhD stipends comparable.

The final net income for salaried NLW / RLW jobs is therefore:

Net income = gross annual salary - income tax - national insurance - council tax.

#### Real value calculation 

The real value of income from previous years can be calculated using the consumer price index with housing costs (CPIH), taken from the ONS [[6]](https://www.ons.gov.uk/economy/inflationandpriceindices/timeseries/l522/mm23). For incomplete years, annual CPIH is estimated as the mean of the CPIH values for available months.

If you had income, $I$, in 2013 and wanted to calculate what its equivalent value, $R$, would be in 2023, you would use: 

$$ R = I \times {C(2023) \over C(2013)} $$,

where $C(2023)$ and $C(2013)$ are the CPIH values in 2023 and 2013 respectively. In the time series graph, the net incomes from UKRI stipends, NLW / RLW are inflation adjusted using equations of this form.

Inflation adjustment is not required to show that PhD stipends and the NLW have converged, but it does show that PhD stipends have not kept pace with RLW income.