#%%
import pandas as pd

def drop_cols(df:pd.DataFrame) -> pd.DataFrame:
    """Remove do DataFrame algumas colunas consideradas pouco úteis para analise

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame com os dados originais do dataset fifa_players

    Returns
    -------
    pd.DataFrame
        DataFrame sem as colunas 'Unnamed: 0', 'Counter', 'Photo', 'Flag', 'Club_Logo', 'Loaned_From', 'Real_Face' e 'Work_Rate'

    """

    columns={'Unnamed: 0', 'Counter', 'Photo', 'Flag', 'Club_Logo', 'Loaned_From', 'Real_Face', 'Work_Rate'}
    df.drop(columns=columns, inplace=True)
    return df

def drop_na_pos(df:pd.DataFrame) -> pd.DataFrame:
    """Remove linhas com excesso de NaN

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame de entrada

    Returns
    -------
    pd.DataFrame
        Dataframe com linhas com no minimo 5 campos sem NaN

    """

    non_na = df.shape[1] - 5 #Valor arbitrário para permitir alguns NA
    df.dropna(thresh=non_na, inplace=True)
    return df

def drop_na_ReleaseClause(df:pd.DataFrame) -> pd.DataFrame:
    """Remove linhas com NaN na coluna Release_Clause

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame de entrada

    Returns
    -------
    pd.DataFrame
        DataFrame com todas a linhas possuindo dados de Release_Clause

    """

    flt = df['Release_Clause'].notna()
    df = df[flt]
    return df

def set_index(df:pd.DataFrame) -> pd.DataFrame:
    """Define a coluna ID como index do DataFrame

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame de entrada

    Returns
    -------
    pd.DataFrame
        DataFrame com a coluna ID definida como index

    """

    df.set_index('ID', inplace=True)
    return df

def remove_plus_sign(string:str) -> int:
    """Remove o sinal + do penúltimo caractere

    Parameters
    ----------
    string : str
        String com valores numéricos e um "mais" no penultimo caractere

    Returns
    -------
    int
        

    Raises
    ------
    ValueError
        Se houver uma string sem o sinal + no penultimo caratere, é levantada esta exceção

    """

    if string[-2] != '+':
        raise ValueError('Penúltimo dígito de {} não é um "+" - Ajustar função'.format(string))
    num = string[:-2]
    return int(num)

def clean_position_cols(df:pd.DataFrame) -> pd.DataFrame:
    """Remove as features referente as habilidades de um jogador em cada posicionamento

    Parameters
    ----------
    df : pd.DataFrame
        Dataframe com dados dos fifa_players.

    Returns
    -------
    pd.DataFrame
        Datframe sem informações de habilidade em cada posicionamento

    """

    cols = list(df.columns)
    start = cols.index('LS')
    end = start + 26

    position_columns = df.columns[start:end]
    for column in position_columns:
        df.loc[:, column] = df.loc[:, column].apply(remove_plus_sign)
    return df

def money_to_int(value:str) -> float:
    """

    Parameters
    ----------
    value : str
        String com caracteres monetarios.

    Returns
    -------
    float
        Valor numerico 

    Raises
    ------
    ValueError
        Erro na alteracao dos valores

    """

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
    raise ValueError('Erro no multiplicador do valor {}'.format(value))

def clean_money_cols(df:pd.DataFrame) -> pd.DataFrame:
    """Limpa as features relacionadas dinheiro.

    Parameters
    ----------
    df : pd.DataFrame
        Dataframe com dados dos fifa_players.

    Returns
    -------
    pd.DataFrame
        Dataframe sem simbolos referentes a moeda

    """

    cols = ['Value', 'Wage', 'Release_Clause']
    for col in cols:
        df.loc[:, col] = df[col].apply(money_to_int)
    return df

def lbs_to_kg(value:str)->float:
    """Converte libras para kilos nas colunas relativas a peso

    Parameters
    ----------
    value : str
        Valor numérico em Libras

    Returns
    -------
    float
        Valor convertido para kilos

    Raises
    ------
    ValueError
        Se a String não possuir a terminação lbs, é levantada a exceção.

    """

    if value[-3:] != 'lbs':
        raise ValueError('Erro de unidade: três últimos dígitos de {} não são "lbs"'.format(value))
    value = float(value[:-3])
    return round(value * 0.4535923, 0)

def clean_weight_col(df:pd.DataFrame) -> pd.DataFrame:
    """Converte todos os medidas em Libras para Kilos

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame com a feature Weight em Libras.

    Returns
    -------
    pd.DataFrame
        DataFrame com a feature Weight em Kilos.

    """
    
    df.loc[:, 'Weight'] = df['Weight'].apply(lbs_to_kg)
    return df

def ft_to_meters(value:str) -> float:
    """Converte a unidade pés para metros

    Parameters
    ----------
    value : str
        Valor em unidade de pés.

    Returns
    -------
    float
        Valor convertido para unidade metro.

    Raises
    ------
    ValueError
        Se a String não estiver em formato de pés, é levando a exceção.

    """

    if value[1] != '\'':
        raise ValueError('Segundo dígito de {} precisa ser uma aspas simples'.format(value))
    inches = int(value[0]) * 12
    inches += int(value[2:])
    return round(float(inches * 0.0254), 2)

def clean_height_col(df:pd.DataFrame) -> pd.DataFrame:
    """Converte todos os medidas em Pés para Metros

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame com a feature Height em Pés.

    Returns
    -------
    pd.DataFrame
        DataFrame com a feature Height em Metros.

    """
    df.loc[:, 'Height'] = df['Height'].apply(ft_to_meters)
    return df

def adjust_dtypes(df:pd.DataFrame) -> pd.DataFrame:
    """Converte as fetures Joined e Contract_Valid_Until para o tipo datetime.

    Parameters
    ----------
    df : pd.DataFrame
        

    Returns
    -------
    pd.DataFrame
        Dataframe fifa_players com as variáveis de data como datetime.
    """
    df.loc[:, 'Joined'] = pd.to_datetime(df['Joined'])
    df.loc[:, 'Contract_Valid_Until'] = pd.to_numeric(df['Contract_Valid_Until'])
    return df

def foot_to_dummie(df:pd.DataFrame) -> pd.DataFrame:
    """Converte a classificação categórica da 'Preferred_Foot' para classificação binária.

    Parameters
    ----------
    df:pd.DataFrame
        DataFrame com coluna 'Preferred_Foot'  com valores 'Right' ou 'Left'
        
    Returns
    -------
    df:pd.DataFrame
    DataFrame com coluna 'Preferred_Foot' com valor 1 para Right e 0 para Left.
        
    """

    array = (df['Preferred_Foot'] == 'Right')
    df.loc[:, 'Preferred_Foot'] = array
    return df

def clean_dataframe(df:pd.DataFrame) -> pd.DataFrame:
    """Faz o tratamento necessário para a implementação de modelos e visualizações do dataset fifa_players.

    Parameters
    ----------
    df : pd.DataFrame
        Dados originais do dataset fifa_players

    Returns
    -------
    pd.DataFrame
        Dataframe com todos os dados necessários limpos
    """
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
#%%
if __name__ == '__main__':
    df = pd.read_csv('../Dados/fifa_players.csv')
    print(df.shape)
    #df = clean_dataframe(df)

