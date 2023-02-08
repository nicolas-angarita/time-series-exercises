import pandas as pd
import requests
import os
from env import get_connection



def get_people_data():
    '''
    This function is to acquire the people data from the api and check if there is a local csv, if not then it makes one
    '''
    
    if os.path.isfile('people.csv'):
        
        return pd.read_csv('people.csv')
    
    else:
       
        url = 'https://swapi.dev/api/people/'
        response = requests.get(url)
        json = response.json()

        people = pd.DataFrame(json['results'])
        
        people.to_csv('people.csv', index = False)
   
    return people


def get_planets_data():
    '''
    This function is to acquire the planets data from the api and check if there is a local csv, if not then it makes one

    '''
    
    if os.path.isfile('planets.csv'):
        
        return pd.read_csv('planets.csv')
    
    else:
       
        url = 'https://swapi.dev/api/planets/'
        response = requests.get(url)
        json = response.json()

        planets = pd.DataFrame(json['results'])
        
        planets.to_csv('planets.csv', index = False)
   
    return planets


def get_starships_data():
    '''
    This function is to acquire the starships data from the api and check if there is a local csv, if not then it makes one

    '''
    
    if os.path.isfile('starships.csv'):
        
        return pd.read_csv('starships.csv')
    
    else:
       
        url = 'https://swapi.dev/api/starships/'
        response = requests.get(url)
        json = response.json()

        starships = pd.DataFrame(json['results'])
        
        starships.to_csv('people.csv', index = False)
   
    return starships


def combine_df(df_x, df_y, df_z):
    '''
    This function is to combine 3 seperate dfs
    '''    
    pd.options.display.max_columns = None
    
    starwars_df = pd.concat([df_x, df_y, df_z], axis = 1)
    
    return starwars_df


def acquire_store():
    
    filename = 'store.csv'
    
    if os.path.exists(filename):
        
        return pd.read_csv(filename)
    
    else:
        
        query = '''
                SELECT sale_date, sale_amount,
                item_brand, item_name, item_price,
                store_address, store_zipcode
                FROM sales
                LEFT JOIN items USING(item_id)
                LEFT JOIN stores USING(store_id)
                '''
        
        url = get_connection(db='tsa_item_demand')
        
        df = pd.read_sql(query, url)
        
        df.to_csv(filename, index=False)
        
        return df
    
def get_renewable_energy_data():
    
    if os.path.isfile('renewable_energy_production.csv'):
        
        return pd.read_csv('renewable_energy_production.csv')
    
    else:
       
        url = 'https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv'

        df = pd.DataFrame(pd.read_csv(url))
        
        df.to_csv('renewable_energy_production.csv', index = False)
   
    return df    