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

Tax on salaries are calculated using online tools like [[TAX1]](https://www.icalculator.info) or [[TAX2]](https://investomatica.com/income-tax-calculator).

Assumptions are always onerous: we'll choose salaries at the lower end of the spectrum, and will assume scholarships don't cover international fee rates (even if they usually do).

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

Searches at the time of writing revealed PhDs with gross taxable annual stipends of around €32,000/yr [[BEL2]](https://www.findaphd.com/phds/belgium/). Belgium's tax rates are higher than Austria's, so this results in a lower net income.

Fees can be up to €980/yr [[BEL1]](https://www.findaphd.com/guides/phd-study-in-belgium) depending on the institution.


##### Denmark

Salaries for PhD students from the DTU are gross 51600&nbsp;krone/yr[[DNK1]](https://www.dtu.dk/english/education/phd/intro/salary).

Fees for international students vary but are typically around 6700&nbsp;krone/yr.

##### Finland

Info on full scholarships for PhD students could not be found. Finland do not charge fees [[FIN1]](https://www.findaphd.com/guides/phd-study-in-finland).

##### France

CIFRE suggest an annual minimum salary of €23,484/yr [[FRA1]](https://www.enseignementsup-recherche.gouv.fr/fr/le-financement-doctoral-46472). Fees for UK students are €380/yr [[FRA2]](https://www.findaphd.com/guides/phd-study-in-france).


##### Germany

Germany Universities and institutions typically offer salaries at 65% of TVöD 13, which is around €32,000/yr at the time of writing (Spring 2023) [[DEU1]](https://www.chemistryworld.com/news/wage-rise-for-max-planck-phd-candidates-approved/4013241.article). There are sometimes fees of up to €700/yr [[DEU2]](https://www.findaphd.com/blog/8810/is-postgraduate-study-in-germany-really-free).

Germany's tax system is quite complicated, but here we assume the €32,000/yr salary is taxed at category I in Berlin. This results in taxes and social securities of around €9,600/yr.

##### Italy (None)

##### Ireland

Searches on findPhD revealed Irish stipends are typically €18,000/yr&mdash;19,500/yr. It is unclear, but we believe that fees on scholarships are usually covered for UK students.

##### Netherlands

Searches on findPhD revealed gross annual salaries of €29,000/yr &mdash; €41,000/yr, and here we will take the lower end as a value.

There are typically no fees for students in the Netherlands [[NLD1]](https://www.findaphd.com/guides/phd-study-in-netherlands)

##### Norway (None)

##### Portugal (None)

##### Spain (None)

##### Sweden

Salaries of around 348,000 kr/yr are typical [[SWE1]](https://staff.ki.se/employment-as-a-doctoral-student-at-ki), and there are no fees [[SWE2]](https://www.findaphd.com/guides/phd-study-in-sweden).

##### Switzerland

Searches on findPhD revealed salaries of 50,000&mdash; 55,000 CHF/yr and there are no fees if a UK student finds a paid PhD position [[CHE1]](https://www.findaphd.com/guides/phd-funding-switzerland).

##### United Kingdom

Minimum stipends are available on UKRI's website [[GB1]](https://www.ukri.org/what-we-offer/developing-people-and-skills/find-studentships-and-doctoral-training/get-a-studentship-to-fund-your-doctorate/) and most of the time, academic insitutions will match this value. PhD students do not pay income taxes on their stipends, nor do they pay council tax.