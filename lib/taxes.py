"""Module for various tax calcs"""

def net_income(gross_rate: float, allowance: int, counc_tax: int) -> int:
    """Returns the net annual income after income tax, national insurance, and typical council tax payments,
    assuming that all income tax is paid at the lowest rate (20%). Valid for years 2012 and beyond.
    
    
    Parameters
    -------
    gross_rate: float
        Hourly rate (£/hr) from employment prior to tax deductions.

    allowance: int
        Personal allowance (£) for that year.
        
    counc_tax: int
        Annual council tax for that year.

    Returns
    -------
    Estimated net annual income after deductions.

    """

    # Assume ~37.5 hrs/wk * 52 weeks = 1950 work hours per year
    gross_annual = gross_rate*1950

    # Income tax calculated as:
    income_tax = (gross_annual - allowance)*0.2

    # National insurance is always about £600 /yr
    nat_ins = 600

    net_income = gross_annual - income_tax - nat_ins - counc_tax

    return net_income


