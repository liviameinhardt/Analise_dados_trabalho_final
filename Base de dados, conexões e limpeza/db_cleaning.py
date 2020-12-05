import pandas as pd

def drop_cols(df):
    columns={'Unnamed: 0', 'Counter', 'Photo', 'Flag', 'Club_Logo', 'Loaned_From', 'Real_Face', 'Work_Rate'}
    df.drop(columns=columns, inplace=True)
    return df

def drop_na_pos(df):
    non_na = df.shape[1] - 5 #Valor arbitrário para permitir alguns NA
    df.dropna(thresh=non_na, inplace=True)
    return df

def drop_na_ReleaseClause(df):
    flt = df['Release_Clause'].notna()
    df = df[flt]
    return df

def set_index(df):
    df.set_index('ID', inplace=True)
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

    position_columns = df.columns[start:end]
    for column in position_columns:
        df.loc[:, column] = df.loc[:, column].apply(remove_plus_sign)
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
        df.loc[:, col] = df[col].apply(money_to_int)
    return df

def lbs_to_kg(value):
    if value[-3:] != 'lbs':
        raise TypeError('Erro de unidade: três úl timos dígitos de {} não são "lbs"'.format(value))
    value = float(value[:-3])
    return round(value * 0.4535923, 0)

def clean_weight_col(df):
    df.loc[:, 'Weight'] = df['Weight'].apply(lbs_to_kg)
    return df

def ft_to_meters(value):
    if value[1] != '\'':
        raise ValueError('Segundo dígito de {} precisa ser uma aspas simples'.format(value))
    inches = int(value[0]) * 12
    inches += int(value[2:])
    return round(float(inches * 0.0254), 2)

def clean_height_col(df):
    df.loc[:, 'Height'] = df['Height'].apply(ft_to_meters)
    return df

def adjust_dtypes(df):
    df.loc[:, 'Joined'] = pd.to_datetime(df['Joined'])
    df.loc[:, 'Contract_Valid_Until'] = pd.to_numeric(df['Contract_Valid_Until'])
    return df

def foot_to_dummie(df):
    array = (df['Preferred_Foot'] == 'Right')
    df.loc[:, 'Preferred_Foot'] = array
    return df

def clean_dataframe(df):
    df = drop_cols(df.copy())
    df = drop_na_pos(df.copy())
    df = drop_na_ReleaseClause(df.copy())
    df = set_index(df.copy())
    df = clean_position_cols(df.copy())
    df = clean_money_cols(df.copy())
    df = clean_weight_col(df.copy())
    df = clean_height_col(df.copy())
    df = adjust_dtypes(df.copy())
    df = foot_to_dummie(df.copy())
    return df

if __name__ == '__main__':
    df = pd.read_csv('../Dados/fifa_players.csv')
    df = clean_dataframe(df)









