import pandas as pd
import numpy as np

# def def_df(path):
#     if path is pd.DataFrame:
#         df = path
#     else:
#         df = pd.read_csv(path)
#     return df

def drop_cols(df):
    columns={'Unnamed: 0', 'Counter', 'Photo', 'Flag', 'Club_Logo', 'Loaned_From', 'Real_Face', 'Work_Rate'}
    df.drop(columns, inplace=True)
    return df

def drop_na_pos(df):
    non_na = df.shape[1] - 26
    df.dropna(thresh=non_na, inplace=True)
    return df

def drop_na_ReleaseClause(df):
    flt = df['Release_Clause'].notna()
    df = df[flt]
    return df

def remove_plus_sign(string):
    if string[-2] != '+':
        raise TypeError('Penúltimo dígito de {} não é um "+" - Ajustar função'.format(string))
    num = string[:-2]
    return int(num)

def clean_position_cols(df):
    cols = list(df.columns)
    start = cols.index('LS')
    end = start + 26

    position_columns = df[start:end]
    for column in position_columns:
        df[column] = df[column].apply(remove_plus_sign)
    return df

def money_to_int(value):
    value = str(value)
    value = value[1:] # Remove €
    if value[-1] == '0': # There is a value of "€0"
        return float(0)
    money = float(value[:-1])
    multiplier = value[-1]
    if multiplier == 'K':
        return money * 1_000
    elif multiplier == 'M':
        return money * 1_000_000
    raise TypeError('Erro no multiplicador do valor {}'.format(value))

def clean_money_cols(df):
    cols = ['Value', 'Wage', 'Release_Clause']
    for col in cols:
        df[col] = df[col].apply(money_to_int)
    return df

def lbs_to_kg(value):
    if value[-3:] != 'lbs':
        raise TypeError('Erro de unidade: três úl timos dígitos de {} não são "lbs"'.format(value))
    value = float(value[:-3])
    return round(value * 0.4535923, 0)

def clean_wight_col(df):
    df['Weight'] = df['Weight'].apply(lbs_to_kg)
    return df

def ft_to_meters(value):
    if value[1] != '\'':
        raise ValueError('Segundo dígito de {} precisa ser uma aspas simples'.format(value))
    inches = int(value[0]) * 12
    inches += int(value[2:])
    return round(float(inches * 0.0254), 2)

def clean_height_col(df):
    df['Height'] = df['Height'].apply(ft_to_meters)
    return df

def adjust_dtypes(df):
    df['Joined'] = pd.to_datetime(df['Joined'])
    df['Contract_Valid_Until'] = pd.to_numeric(df['Contract_Valid_Until'])
    return df

