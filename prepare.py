import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from datetime import timedelta, datetime

import acquire as a

import warnings
warnings.filterwarnings('ignore')


def store_prepared():
    
    df = a.acquire_store()
    
    df['sale_date'] = pd.to_datetime(df['sale_date'])
    
    df = df.set_index('sale_date')
    
    df['sale_amount'].plot(kind = 'hist')
    plt.show()
    
    df['item_price'].plot(kind = 'hist')
    plt.show()
    
    df['month'] = df.index.month_name()
    
    df['sales_total'] = df['sale_amount'] * df['item_price']
    
    return df


def clean_germany_df():
    
    germany_df = a.get_renewable_energy_data()
    
    germany_df.columns = germany_df.columns.str.lower()
    germany_df['date'] = pd.to_datetime(germany_df['date'])    
    
    germany_df = germany_df.set_index('date')
        
    germany_df['month'] = germany_df.index.month_name()
    germany_df['year'] = germany_df.index.year

    germany_df.fillna(0, inplace = True)
    
    return germany_df


def dist_of_col():

    germany_df = a.get_renewable_energy_data()
    
    germany_df.columns = germany_df.columns.str.lower()
    germany_df['date'] = pd.to_datetime(germany_df['date'])

    columns = germany_df.columns

    for col in columns:

        if col != 'date':
            germany_df[col].plot(kind = 'hist')
            plt.xlabel(col)
            plt.show()