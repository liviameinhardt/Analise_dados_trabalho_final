import pandas as pd


def drop_cols(df):
    columns={'AggregationMethod', 'Unnamed: 0', 'Version', 'Centroid', 'Geography'}
    df.drop(columns=columns, inplace=True)
    return df

def create_datetime_cols(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df.loc[:, 'Year'] = df['Date'].dt.year
    df.loc[:, 'Month'] = df['Date'].dt.month
    df.loc[:, 'Day'] = df['Date'].dt.day
    return df

def standardize_country_names(df):
    df.loc[:, 'Country'].replace('United States of America (the)', 'United States', inplace=True)
    return df

def clean_dataframe(df):
    df = drop_cols(df.copy())
    df = create_datetime_cols(df.copy())
    df = standardize_country_names(df.copy())
    return df

if __name__ == '__main__':
    df = pd.read_csv('../Dados/covid_airport.csv')
    df = clean_dataframe(df)