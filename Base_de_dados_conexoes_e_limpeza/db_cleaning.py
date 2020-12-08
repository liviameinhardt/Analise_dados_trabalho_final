import pandas as pd

class Limpador_airport:
    @classmethod
    def drop_cols(cls, df:pd.DataFrame) -> pd.DataFrame:
        """Remove as colunas consideradas pouco úteis

        Parameters
        ----------
        df : pd.DataFrame
            DataFrame com as colunas 'AggregationMethod', 'Unnamed: 0', 'Version', 'Centroid', 'Geography'

        Returns
        -------
        pd.DataFrame
            DataFrame sem as colunas 'AggregationMethod', 'Unnamed: 0', 'Version', 'Centroid', 'Geography'
        """
        columns={'AggregationMethod', 'Unnamed: 0', 'Version', 'Centroid', 'Geography'}
        if type(df) != pd.DataFrame:
            raise TypeError

        if not (set(df.columns).issuperset(columns)):
            raise indexes_not_found_in_dataframe
        df.drop(columns=columns, inplace=True)
        return df

    @classmethod
    def create_datetime_cols(cls, df:pd.DataFrame) -> pd.DataFrame:
        """Convert a coluna Date nas colunas Year, Month e Day

        Parameters
        ----------
        df : pd.DataFrame
            DataFrame com a coluna Date

        Returns
        -------
        pd.DataFrame
            DataFrame com a coluna Date, Year, Month, Day no formato datetime
            
        """
        if type(df) != pd.DataFrame:
            raise TypeError
    
        columns = {'Date'}
        if not (set(df.columns).issuperset(columns)):
            raise indexes_not_found_in_dataframe

        df.loc[:, 'Date'] = pd.to_datetime(df['Date'])
        df.loc[:, 'Year'] = df['Date'].dt.year
        df.loc[:, 'Month'] = df['Date'].dt.month
        df.loc[:, 'Day'] = df['Date'].dt.day
        return df

    @classmethod
    def standardize_country_names(cls, df:pd.DataFrame) -> pd.DataFrame:
        """Padroniza a denomição United States para o Estados Unidos

        Parameters
        ----------
        df : pd.DataFrame
            Dataframe com a coluna Country com 'United States of America (the)', 'United States' em refencia ao país

        Returns
        -------
        pd.DataFrame
            Dataframe com a coluna Country com 'United States' em referência ao país

        """
        columns = {'Country'}

        if type(df) != pd.DataFrame:
            raise TypeError

        if not (set(df.columns).issuperset(columns)):
            raise indexes_not_found_in_dataframe

        df = df.copy()
        df.loc[:, 'Country'].replace('United States of America (the)', 'United States', inplace=True)
        return df

    @classmethod
    def clean_dataframe(cls, df:pd.DataFrame) -> pd.DataFrame:
        """Limpa os dados para permitir a análise.

        Parameters
        ----------
        df : pd.DataFrame
            DataFrame com o dataset covid_airport original.

        Returns
        -------
        pd.DataFrame
            DataFrame com os dados do covid_airport limpos.

        """
        df = cls.drop_cols(df.copy())
        df = cls.create_datetime_cols(df.copy())
        df = cls.standardize_country_names(df.copy())
        return df

class Limpador_fifa:

    @classmethod
    def drop_cols(cls, df:pd.DataFrame) -> pd.DataFrame:
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

    @classmethod
    def drop_na_pos(cls, df:pd.DataFrame) -> pd.DataFrame:
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

    @classmethod
    def drop_na_ReleaseClause(cls, df:pd.DataFrame) -> pd.DataFrame:
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

    @classmethod
    def set_index(cls, df:pd.DataFrame) -> pd.DataFrame:
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

    @classmethod
    def remove_plus_sign(cls, string:str) -> int:
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

    @classmethod
    def clean_position_cols(cls, df:pd.DataFrame) -> pd.DataFrame:
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
            df.loc[:, column] = df.loc[:, column].apply(cls.remove_plus_sign)
        return df

    @classmethod
    def money_to_int(cls, value:str) -> float:
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

    @classmethod
    def clean_money_cols(cls, df:pd.DataFrame) -> pd.DataFrame:
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
            df.loc[:, col] = df[col].apply(cls.money_to_int)
        return df

    @classmethod
    def lbs_to_kg(cls, value:str)->float:
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

    @classmethod
    def clean_weight_col(cls, df:pd.DataFrame) -> pd.DataFrame:
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

        df.loc[:, 'Weight'] = df['Weight'].apply(cls.lbs_to_kg)
        return df

    @classmethod
    def ft_to_meters(cls, value:str) -> float:
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

    @classmethod
    def clean_height_col(cls, df:pd.DataFrame) -> pd.DataFrame:
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
        df.loc[:, 'Height'] = df['Height'].apply(cls.ft_to_meters)
        return df

    @classmethod
    def adjust_dtypes(cls, df:pd.DataFrame) -> pd.DataFrame:
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

    @classmethod
    def foot_to_dummie(cls, df:pd.DataFrame) -> pd.DataFrame:
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

        df.loc[:, 'Preferred_Foot'] = pd.get_dummies(df['Preferred_Foot'])
        return df

    @classmethod
    def clean_dataframe(cls, df:pd.DataFrame) -> pd.DataFrame:
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
        df = cls.drop_cols(df.copy())
        df = cls.drop_na_pos(df.copy())
        df = cls.drop_na_ReleaseClause(df.copy())
        df = cls.set_index(df.copy())
        df = cls.clean_position_cols(df.copy())
        df = cls.clean_money_cols(df.copy())
        df = cls.clean_weight_col(df.copy())
        df = cls.clean_height_col(df.copy())
        df = cls.adjust_dtypes(df.copy())
        df = cls.foot_to_dummie(df.copy())
        return df

class indexes_not_found_in_dataframe(pd.errors.InvalidIndexError):
    """ Exceção levantada quando não existem no DataFrame as colunas que seriam tratadas"""
    pass



if __name__ == '__main__':
    df = pd.read_csv('../Dados/fifa_players.csv')
    df = Limpador_fifa.clean_dataframe(df)
    # print(df.shape)
    #df = clean_dataframe(df)

# if __name__ == '__main__':
#     df = pd.read_csv('../Dados/covid_airport.csv')
#     df = Limpador.clean_dataframe(df)

