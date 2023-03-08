### Method and assumptions

#### Cost of living correction

Purchasing Power Parity (PPP) is a number that reflects the price of a basket of goods in one country relative to another country. This measure can, with limitations, be used to compare the cost of living between countries [C1](https://www.oecd.org/sdd/prices-ppp/purchasingpowerparities-frequentlyaskedquestionsfaqs.htm).

Here, we use OECD's "PPP for actual individual consumption" [C2](https://stats.oecd.org/Index.aspx?datasetcode=SNA_TABLE4). With this measure of PPP, the "basket of goods" covers the goods and services actually consumed by households [C3](https://www.oecd.org/sdd/statistical-insights-purchasing-power-paritiesnot-only-about-big-macs.htm).

The units of PPP are USD$ per local currency.


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