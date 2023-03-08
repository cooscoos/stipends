### Method and assumptions

#### Currency conversions

Currency conversions to and from € use today's exchange rates, $E$, available at [[E1]](https://www.exchangerate-api.com/).

#### Cost of living correction

Purchasing Power Parity (PPP) is a number that reflects the price of a *basket of goods* in one country relative to another country. This measure can, with limitations, be used to compare the cost of living between countries [[C1]](https://www.oecd.org/sdd/prices-ppp/purchasingpowerparities-frequentlyaskedquestionsfaqs.htm).

Here, we use OECD's "Purchasing Power Parity for actual individual consumption" [[C2]](https://stats.oecd.org/Index.aspx?datasetcode=SNA_TABLE4), which is measured every 3 years (the last update was in 2021). With this value of PPP, the *basket of goods* covers goods and services that tend to be consumed by households [[C3]](https://www.oecd.org/sdd/statistical-insights-purchasing-power-paritiesnot-only-about-big-macs.htm).

The OECD define the PPP for each country as national currency per USD\$, i.e. units are C/\$ where $C$ could be £, €, kr, etc. For example, if the PPP for the UK is 0.75&nbsp;£/\$, it suggests that households in the UK need to spend (1/0.75 =) 1.3 times as much as households in the US to buy the same basket of goods.

To find the cost of living (CoL) correction, we first convert all of the OECD's PPP values from units of C/USD to units of €/USD by using today's exhange rates, $E$:

$$ PPP[€/ \$ ] = PPP[C/\$] \times E[€/C] $$.

We can then find a CoL correction factor for each country relative to the UK:

$$ CoL = {PPP(UK) [€/ \$ ] \over PPP(country) [€/ \$ ]} $$.


#### PhD stipends, salaries and taxes for each country

PhD incomes can vary widely even within countries. In this analysis, we have tried to find typical values for PhD income,for example the stipend or salary levels recommended by each country's national PhD funding bodies.

Countries below which are denoted "None" mean that:

- no information on typical income could be found;
- no grants for UK citizens could be found, and/or;
- the sources of information found were not in English.

If you'd like to help us fill in some blanks, or if you've spotted a mistake in income or taxes for a country, then please contact me on Twitter.

##### Austria

Austria’s Agency for Education and Internationalisation have a grant funding tool [[A1]](https://grants.at/en/) that shows PhD scholarships for UK students have stipends that range from gross €32,000/yr to €42,000/yr [[AUT1]](https://phd.pages.ista.ac.at/funding-and-awards/). Austrian PhDs are paid 14 times per year rather than 12.

Fees for international students are typically €1500/yr [[AUT2]](https://www.findaphd.com/guides/phd-study-in-austria), althought a scholarship would normally waive or pay for these.

Here, we onerously assume a gross income €32,000/yr is taxed, and then subject to €1500/yr fees. Even with these assumptions, Austria's PhD incomes are some of the most generous for UK citizens within Europe at the time of writing (Spring 2023).


##### Belgium

##### Denmark

##### Finland

##### France

##### Germany

##### Italy (None)

##### Ireland

##### Netherlands

##### Norway (None)

##### Portugal (None)

##### Spain (None)

##### Sweden

##### Switzerland

##### United Kingdom

Minimum stipends are available on UKRI's website [[GB1]](https://www.ukri.org/what-we-offer/developing-people-and-skills/find-studentships-and-doctoral-training/get-a-studentship-to-fund-your-doctorate/) and most of the time, academic insitutions will match this value. PhD students do not pay income taxes on their stipends, nor do they pay council tax.