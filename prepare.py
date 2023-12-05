import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split


def prep_telco(df):
    '''
    function will do necessary cleaning specifically for the database 'telco_churn'.
    It will:
    - drop unnecessary columns
    - fill in null values where needed. 
    - encode and rename most categorical columns.
    return: concatenated and cleaned dataframe 'telco_churn' as 'df'
    '''
    #change total charges to dtype float
    df['total_charges'] = df.total_charges.str.replace(' ', '0').astype(float)
    #drop duplicate or unnecessary columns
    df = df.drop(columns=['contract_type_id', 'payment_type_id', 'internet_service_type_id'])

    #fill in null values
    df['internet_service_type'] = df['internet_service_type'].fillna(value='No Internet Service')
    
    #change payment type to payment types which will have automatic or manual payment types as options.
    df['payment_types'] = df['payment_type'].apply(lambda x: 'Manual' if x in ['Electronic check', 'Mailed check'] else 'Automatic')
    df = df.drop(columns=['payment_type'])

    #encode columns for modeling
    df['gender_encoded'] = df.gender.map({'Female': 1, 'Male':0})
    df['partner_encoded'] = df.partner.map({'Yes':1, 'No':0})
    df['dependents_encoded'] = df.dependents.map({'Yes':1, 'No':0})
    df['phone_service_encoded'] = df.phone_service.map({'Yes':1, 'No':0})
    df['paperless_billing_encoded'] = df.paperless_billing.map({'Yes':1, 'No':0})
    df['churn_encoded'] = df.churn.map({'Yes':1, 'No':0})

    #encode nonbinary variables for modeling
    dummy_df = pd.get_dummies(df[['multiple_lines',
                                     'online_security',
                                     'online_backup',
                                     'device_protection', 
                                     'tech_support',
                                     'streaming_tv',
                                     'streaming_movies', 
                                     'contract_type', 
                                     'internet_service_type',
                                     'payment_types']],
                                  drop_first=True,
                                  dtype=int)
    df = pd.concat([df, dummy_df], axis=1)

    return df



def splitting_data(df, col):
    '''
    Takes in a df and a column (target variable) and splits into df, validate and test. 
    Ex: df, validate, test = prepare_telco.splitting_data(df, 'churn')
    '''

    #first split
    train, validate_test = train_test_split(df,
                     train_size=0.6,
                     random_state=123,
                     stratify=df[col]
                    )
    
    #second split
    validate, test = train_test_split(validate_test,
                                     train_size=0.5,
                                      random_state=123,
                                      stratify=validate_test[col]
                        
                                     )
    return train, validate, test

