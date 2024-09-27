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
- National insurance contributions of £600/yr are deducted (this is a typical value for 40&nbsp;hr/wk work over the last decade).
- Average historical council tax values are deducted to make the net incomes from salaried work and PhD stipends comparable. Historical rates can be found in [[5]](https://www.gov.uk/government/statistical-data-sets/live-tables-on-council-tax), and we have subtracted the average value for England each year.

The final net income for salaried NLW / RLW jobs is therefore:

Net income = gross annual salary - income tax - national insurance - council tax.

#### Real value calculation

The real value of income from previous years can be calculated using the consumer price index with housing costs (CPIH), taken from the ONS [[6]](https://www.ons.gov.uk/economy/inflationandpriceindices/timeseries/l522/mm23). For incomplete years, annual CPIH is estimated as the mean of the CPIH values for available months.

If you had an income, $I$, in 2013 and wanted to calculate what its equivalent value, $R$, would be in 2023, you would use:

$$R = I \times {C(2023) \over C(2013)},$$

where $C(2023)$ and $C(2013)$ are the CPIH values in 2023 and 2013 respectively. In the time series graph, the net incomes from stipends and salaried work are inflation adjusted using equations of this form.

Inflation adjustment is not required to show that PhD stipends and the NLW have converged, but it does show that the real value of PhD stipends have remained constant.


#### Time offsets

NMW, RLW and Stipends are all announced and come into effect at different times. This is accounted for by offsetting the time points for each income type by $F$ months:

$$F = m + i,$$

where $m$ is the month that the income type is announced, $i$ is the implementation delay.

For example:
- NLW increases come into effect each April (this is $m=+3$ months after January). They are implemented immediately ($i=0$), and so $F=3$.
- RLW is announced at the end of October (or $m=10$ months after January). Employers have $i=6$ months to implement them, so they come into effect at the start of May in the following year.
- UKRI stipends come into effect immediately in August of the year they are announced ($m=7$, $i=0$, so $F=7$ months).
