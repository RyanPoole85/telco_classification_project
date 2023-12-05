import pandas as pd
import numpy as np

import env
import os

def get_connection_url(db, user=env.user, host=env.host, password=env.password):
    """
    This function takes in 1 positional arguement and checks for username, host, and password credentials from imported env module. 
    Returns a formatted connection url to access mySQL database.
    """
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
    

def check_file_exists(filename, query, url):
    '''
    checks if file already exists.
    '''
    if os.path.exists(filename):
        print('this file exists, reading csv')
        df = pd.read_csv(filename, index_col=0)
    else:
        print('this file doesnt exist, read from sql, and export to csv')
        df = pd.read_sql(query, url)
        df.to_csv(filename)
        
    return df


def get_telco_data():
    '''
    function pulls telco data from the MySQL Codeup db into a dataframe.
    '''
    url = env.get_db_url('telco_churn')
    query = '''
    select *
    from customers
        join contract_types
            using (contract_type_id)
        join internet_service_types
            using (internet_service_type_id)
        join payment_types
            using (payment_type_id)
    '''
    
    filename = 'telco_churn.csv'

    #call the check_file_exists fuction 
    df = check_file_exists(filename, query, url)
    return df