import pandas as pd

class Limpador:

    @classmethod
    def drop_cols(cls, df):
        columns={'AggregationMethod', 'Unnamed: 0', 'Version', 'Centroid', 'Geography'}
        df.drop(columns=columns, inplace=True)
        return df

    @classmethod
    def create_datetime_cols(cls, df):
        df.loc[:, 'Date'] = pd.to_datetime(df['Date'])
        df.loc[:, 'Year'] = df['Date'].dt.year
        df.loc[:, 'Month'] = df['Date'].dt.month
        df.loc[:, 'Day'] = df['Date'].dt.day
        return df

    @classmethod
    def standardize_country_names(cls, df):
        df = df.copy()
        df.loc[:, 'Country'].replace('United States of America (the)', 'United States', inplace=True)
        return df

    @classmethod
    def clean_dataframe(cls, df):
        df = cls.drop_cols(df.copy())
        df = cls.create_datetime_cols(df.copy())
        df = cls.standardize_country_names(df.copy())
        return df

if __name__ == '__main__':
    df = pd.read_csv('../Dados/covid_airport.csv')
    df = Limpador.clean_dataframe(df)