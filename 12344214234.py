import pandas as pd
def create_companyDF(income, expenses, years):
    df =pd.DataFrame({'Income': income , 'Expenses': expenses} , index = years)
    return df
def get_profit(df, year):
    if year in df.index:       
        result = df.loc[year, ['Income']] - df.loc[year , ['Expenses']]
    else:
        result = None    
    return result

import pandas as pd
def create_companyDF(income, expenses, years):
    df = pd.DataFrame({
        'Income': income,
        'Expenses': expenses
        },
        index = years
    )
    return df
def get_profit(df, year):
    if year in df.index:
        profit = df.loc[year, 'Income'] - df.loc[year, 'Expenses']
    else:
        profit=None
    return profit