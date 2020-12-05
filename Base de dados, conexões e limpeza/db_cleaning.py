import pandas as pd
import numpy as np

columns={'Unnamed: 0', 'Counter', 'Photo', 'Flag', 'Club_Logo', 'Loaned_From', 'Real_Face', 'Work_Rate'}

# def def_df(path):
#     if path is pd.DataFrame:
#         df = path
#     else:
#         df = pd.read_csv(path)
#     return df

def drop_cols(df, columns=columns):
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

def clean_position_col(df):
    cols = list(df.columns)
    start = cols.index('LS')
    end = start + 26

    position_columns = df[start:end]
    for column in position_columns:
        df[column] = df[column].apply(remove_plus_sign)

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










