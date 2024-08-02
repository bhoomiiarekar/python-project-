"""DATA CLEANING"""
import pandas as pd
def dataset_loading(country_wise_latest.csv):
    return pd.read_csv("\country_wise_latest.csv")

def handling_missing_values(df):
    df.fillna(method='fill', inplace=True)
    return df

def correct_datatypes(df):
    df['Date'] = pd.to_datetime(df['Date'])
    return df

def consistency(df):
    df['Country/Region'] = df['Country/Region'].str.strip()
    return df

def clean_data(country_wise_latest.csv):
    df = dataset_loading(country_wise_latest.csv)
    df = handling_missing_values(df)
    df = correct_datatypes(df)
    df = consistency(df)
    return df

def cleaned_datset(df, output_path):
    df.to_csv(output_path, index=False)
