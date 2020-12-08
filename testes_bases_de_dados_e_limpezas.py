#%%
import unittest
import pandas as pd
from Base_de_dados_conexoes_e_limpeza.db_cleaning import *
from numpy import nan
print('-------------------------------------------')
#%%

class testes_Limpador_fifa(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupClass\n')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.df = pd.read_csv('F:/Documentos/Estudos/Disciplinas FGV/Trabalho_Final_LP/Dados/fifa_players.csv')
        self.df_to_test_index=pd.DataFrame([['Ari', 20], ['João', 19], ['Livia', 18],['Luiz',19]],
                                            columns = ['Name1', 'Age']) 
        
    def tearDown(self):
        print('tearDown\n')

    def testando_instancia_e_valores_retornados_pela_drop_cols(self):
        print('testando_instancia_e_valores_retornados_pela_drop_cols')
        self.assertIsInstance(Limpador_fifa.drop_cols(self.df), pd.DataFrame)
        df1=pd.DataFrame([[9,10,1,2,3,4,5,6,7,8]], columns=['Name','Age','Unnamed: 0', 'Counter', 'Photo', 'Flag', 'Club_Logo', 'Loaned_From', 'Real_Face', 'Work_Rate'])
        pd.testing.assert_frame_equal(Limpador_fifa.drop_cols(df1),pd.DataFrame([[9,10]], columns=['Name','Age']))
        
    def testando_excecoes_levantadas_pela_drop_cols(self):
        print('testando_excecoes_levantadas_pela_drop_cols')
        with self.assertRaises(TypeError):
            Limpador_fifa.drop_cols([[1,2,3,4],[4,5,6,7]])
            Limpador_fifa.drop_cols(dict(oi= 1,tudo=2,bem=3))
            Limpador_fifa.drop_cols(tuple(1,2,3,4))
            Limpador_fifa.drop_cols('String')
            Limpador_fifa.drop_cols(50.5)
        
        with self.assertRaises(indexes_not_found_in_dataframe):
            Limpador_fifa.drop_cols(self.df_to_test_index)

    def testando_instancia_retornada_pela_drop_na_pos(self):
        print('testando_instancia_retornada_pela_drop_na_pos')
        self.assertIsInstance(Limpador_fifa.drop_na_pos(self.df),pd.DataFrame)
    
    def testando_excecoes_levantadas_pela_drop_na_pos(self):
        print('testando_excecoes_levantadas_pela_drop_na_pos')
        with self.assertRaises(TypeError):
            Limpador_fifa.drop_na_pos([[1,2,3,4],[4,5,6,7]])
            Limpador_fifa.drop_na_pos(dict(oi= 1,tudo=2,bem=3))
            Limpador_fifa.drop_na_pos(tuple(1,2,3,4))
            Limpador_fifa.drop_na_pos('String')
            Limpador_fifa.drop_na_pos(50.5)
        
    def testando_instancia_e_valores_retornados_pela_drop_na_ReleaseClause(self):
        print('testando_instancia_e_valores_retornados_pela_drop_na_ReleaseClause')
        #Caminho feliz
        self.assertIsInstance(Limpador_fifa.drop_na_ReleaseClause(self.df), pd.DataFrame)
        df1=pd.DataFrame([[9.0],[10.0], [math_nan], [float('nan')]], columns=['Release_Clause'])
        pd.testing.assert_frame_equal(Limpador_fifa.drop_na_ReleaseClause(df1),pd.DataFrame([[9.0],[10.0]], columns=['Release_Clause']))
    
    def testando_excecoes_levantadas_pela_drop_na_ReleaseClause(self):
        print('testando_excecoes_levantadas_pela_drop_na_ReleaseClause')
        with self.assertRaises(TypeError):
            Limpador_fifa.drop_na_ReleaseClause([[1,2,3,4],[4,5,6,7]])
            Limpador_fifa.drop_na_ReleaseClause(dict(oi= 1,tudo=2,bem=3))
            Limpador_fifa.drop_na_ReleaseClause(tuple(1,2,3,4))
            Limpador_fifa.drop_na_ReleaseClause('String')
            Limpador_fifa.drop_na_ReleaseClause(50.5)

        with self.assertRaises(indexes_not_found_in_dataframe):
            Limpador_fifa.drop_na_ReleaseClause(self.df_to_test_index)
    
    def testando_instancia_retornada_pela_set_index(self):
        print('testando_instancia_retornada_pela_set_index')
        #Caminho feliz
        self.assertIsInstance(Limpador_fifa.set_index(self.df),pd.DataFrame)
    
    def testando_excecoes_levantadas_pela_set_index(self):
        print('testando_excecoes_levantadas_pela_set_index')
        with self.assertRaises(TypeError):
            Limpador_fifa.set_index([[1,2,3,4],[4,5,6,7]])
            Limpador_fifa.set_index(dict(oi= 1,tudo=2,bem=3))
            Limpador_fifa.set_index(tuple(1,2,3,4))
            Limpador_fifa.set_index('String')
            Limpador_fifa.set_index(50.5)

        with self.assertRaises(indexes_not_found_in_dataframe):
            Limpador_fifa.set_index(self.df_to_test_index)
        
    def testando_valores_retornados_pela_remove_plus_sign(self):
        print('testando_valores_retornados_pela_remove_plus_sign')
        #Caminho feliz
        self.assertEqual(Limpador_fifa.remove_plus_sign('88+2'), 88)
        self.assertEqual(Limpador_fifa.remove_plus_sign('91+3'), 91)
        self.assertEqual(Limpador_fifa.remove_plus_sign('9+3'), 9)
        self.assertEqual(Limpador_fifa.remove_plus_sign('90000+8'), 90000)
    
    def testando_excecoes_levantadas_pela_remove_plus_sign(self):
        print('testando_excecoes_levantadas_pela_remove_plus_sign')
        with self.assertRaises(TypeError):
            Limpador_fifa.remove_plus_sign([[1,2,3,4],[4,5,6,7]])
            Limpador_fifa.remove_plus_sign(dict(oi= 1,tudo=2,bem=3))
            Limpador_fifa.remove_plus_sign(tuple(1,2,3,4))
            Limpador_fifa.remove_plus_sign(50.5)
        with self.assertRaises(pd.errors.NullFrequencyError):
            Limpador_fifa.remove_plus_sign(float('nan'))
            Limpador_fifa.remove_plus_sign(pd.NA)
            Limpador_fifa.remove_plus_sign(nan)

    def testando_instancia_e_valores_retornados_pela_clean_position_cols(self):
        print('testando_instancia_e_valores_retornados_pela_clean_position_cols')
        #Caminho feliz
        df = Limpador_fifa.drop_na_pos(self.df)
        self.assertIsInstance(Limpador_fifa.clean_position_cols(df),pd.DataFrame)

    def testando_excecoes_levantadas_pela_clean_position_cols(self):
        print('testando_excecoes_levantadas_pela_clean_position_cols')
        with self.assertRaises(TypeError):
            Limpador_fifa.clean_position_cols([[1,2,3,4],[4,5,6,7]])
            Limpador_fifa.clean_position_cols(dict(oi= 1,tudo=2,bem=3))
            Limpador_fifa.clean_position_cols(tuple(1,2,3,4))
            Limpador_fifa.clean_position_cols('String')
            Limpador_fifa.clean_position_cols(50.5)
        
    def testando_valores_retornados_pela_money_to_int(self):
        print('testando_valores_retornados_pela_money_to_int')
        #Caminho feliz
        self.assertEqual(Limpador_fifa.money_to_int('€88K'), 88_000)
        self.assertEqual(Limpador_fifa.money_to_int('€88M'), 88_000_000)
        self.assertEqual(Limpador_fifa.money_to_int('€ 88 M'), 88_000_000)
        self.assertEqual(Limpador_fifa.money_to_int('€ 88 K'), 88_000)
    
    def testando_excecoes_levantadas_pela_money_to_int(self):
        print('testando_excecoes_levantadas_pela_money_to_int')
        with self.assertRaises(TypeError):
            Limpador_fifa.money_to_int([[1,2,3,4],[4,5,6,7]])
            Limpador_fifa.money_to_int(dict(oi= 1,tudo=2,bem=3))
            Limpador_fifa.money_to_int(tuple(1,2,3,4))
            Limpador_fifa.money_to_int(50.5)
            Limpador_fifa.money_to_int('35')
            Limpador_fifa.money_to_int('85G')
        
        with self.assertRaises(pd.errors.NullFrequencyError):
            Limpador_fifa.remove_plus_sign(float('nan'))
            Limpador_fifa.remove_plus_sign(pd.NA)
            Limpador_fifa.remove_plus_sign(nan)
        
    def testando_instancia_e_valores_retornados_pela_clean_money_cols(self):
        print('testando_instancia_e_valores_retornados_pela_clean_money_cols')
        #Caminho feliz
        df = Limpador_fifa.drop_na_ReleaseClause(self.df)
        self.assertIsInstance(Limpador_fifa.clean_money_cols(df), pd.DataFrame)

        df1=pd.DataFrame([['€1K','€2K','€3K']], columns=['Value', 'Wage', 'Release_Clause'])
        pd.testing.assert_frame_equal(Limpador_fifa.clean_money_cols(df1),pd.DataFrame([[1000.0, 2000.0, 3000.0]], columns=['Value', 'Wage', 'Release_Clause']))

    def testando_excecoes_levantadas_pela_clean_money_cols(self):
        print("testando_excecoes_levantadas_pela_clean_money_cols")
        with self.assertRaises(TypeError):
            Limpador_fifa.clean_money_cols([[1,2,3,4],[4,5,6,7]])
            Limpador_fifa.clean_money_cols(dict(oi= 1,tudo=2,bem=3))
            Limpador_fifa.clean_money_cols(tuple(1,2,3,4))
            Limpador_fifa.clean_money_cols('String')
            Limpador_fifa.clean_money_cols(50.5)
        
        with self.assertRaises(indexes_not_found_in_dataframe):
            Limpador_fifa.clean_money_cols(self.df_to_test_index)

    def testando_valores_retornados_pela_lbs_to_kg(self):
        print('testando_valores_retornados_pela_lbs_to_kg')
        #Caminho feliz
        self.assertAlmostEqual(Limpador_fifa.lbs_to_kg('20 lbs'), 9)
        self.assertAlmostEqual(Limpador_fifa.lbs_to_kg('100lbs'), 45)
        self.assertAlmostEqual(Limpador_fifa.lbs_to_kg('150 lbs'), 68)


    def testando_excecoes_levantadas_pela_lbs_to_kg(self):
        print("testando_excecoes_levantadas_pela_lbs_to_kg")
        with self.assertRaises(TypeError):
            Limpador_fifa.lbs_to_kg([[1,2,3,4],[4,5,6,7]])
            Limpador_fifa.lbs_to_kg(dict(oi= 1,tudo=2,bem=3))
            Limpador_fifa.lbs_to_kg(tuple(1,2,3,4))
            Limpador_fifa.lbs_to_kg('30 mg')
            Limpador_fifa.lbs_to_kg('30T')
            Limpador_fifa.lbs_to_kg(50.5)

        with self.assertRaises(pd.errors.NullFrequencyError):
            Limpador_fifa.lbs_to_kg(float('nan'))
            Limpador_fifa.lbs_to_kg(pd.NA)
            Limpador_fifa.lbs_to_kg(nan)


    def testando_instancia_e_valores_retornados_pela_clean_weight_col(self):
        print("testando_instancia_e_valores_retornados_pela_clean_weight_col")
        #Caminho feliz
        df = Limpador_fifa.drop_na_pos(self.df)
        self.assertIsInstance(Limpador_fifa.clean_weight_col(df),pd.DataFrame)

        df1=pd.DataFrame([["6'0",'50lbs']], columns=['Height', 'Weight'])
        pd.testing.assert_frame_equal(Limpador_fifa.clean_weight_col(df1),pd.DataFrame([["6'0", 23.0]], columns=['Height', 'Weight']))

    def testando_excecoes_levantadas_pela_clean_weight_col(self):
        print('testando_excecoes_levantadas_pela_clean_weight_col')
        with self.assertRaises(TypeError):
            Limpador_fifa.clean_weight_col([[1,2,3,4],[4,5,6,7]])
            Limpador_fifa.clean_weight_col(dict(oi= 1,tudo=2,bem=3))
            Limpador_fifa.clean_weight_col(tuple(1,2,3,4))
            Limpador_fifa.clean_weight_col('String')
            Limpador_fifa.clean_weight_col(50.5)
        with self.assertRaises(indexes_not_found_in_dataframe):
            Limpador_fifa.clean_weight_col(self.df_to_test_index)


    def testando_valores_retornados_pela_ft_to_meters(self):
        print('testando_valores_retornados_pela_ft_to_meters')
        #Caminho feliz
        self.assertAlmostEqual(Limpador_fifa.ft_to_meters("2'00"), 0.6096, 2)
        self.assertAlmostEqual(Limpador_fifa.ft_to_meters("5'00"), 1.524, 2)
        self.assertAlmostEqual(Limpador_fifa.ft_to_meters("7'00"), 2.1336, 2)
        
    def testando_excecoes_levantadas_pela_ft_to_meters(self):
        print("testando_excecoes_levantadas_pela_ft_to_meters")
        with self.assertRaises(TypeError):
            Limpador_fifa.ft_to_meters([[1,2,3,4],[4,5,6,7]])
            Limpador_fifa.ft_to_meters(dict(oi= 1,tudo=2,bem=3))
            Limpador_fifa.ft_to_meters(tuple(1,2,3,4))
            Limpador_fifa.ft_to_meters('String')
            Limpador_fifa.ft_to_meters(50.5)
        
        with self.assertRaises(pd.errors.NullFrequencyError):
            Limpador_fifa.ft_to_meters(float('nan'))
            Limpador_fifa.ft_to_meters(pd.NA)
            Limpador_fifa.ft_to_meters(nan)


    def testando_instancia_e_valores_retornados_pela_clean_height_col(self):
        print('testando_instancia_e_valores_retornados_pela_clean_height_col')
        #Caminho feliz
        df = Limpador_fifa.drop_na_pos(self.df)
        self.assertIsInstance(Limpador_fifa.clean_height_col(df),pd.DataFrame)

        df1=pd.DataFrame([["6'0",'50lbs']], columns=['Height', 'Weight'])
        pd.testing.assert_frame_equal(Limpador_fifa.clean_height_col(df1),pd.DataFrame([[1.83, '50lbs']], columns=['Height', 'Weight']))

    def testando_excecoes_levantadas_pela_clean_height_col(self):
        print("testando_excecoes_levantadas_pela_clean_height_col")
        with self.assertRaises(TypeError):
            Limpador_fifa.clean_height_col([[1,2,3,4],[4,5,6,7]])
            Limpador_fifa.clean_height_col(dict(oi= 1,tudo=2,bem=3))
            Limpador_fifa.clean_height_col(tuple(1,2,3,4))
            Limpador_fifa.clean_height_col('String')
            Limpador_fifa.clean_height_col(50.5)
        
        with self.assertRaises(indexes_not_found_in_dataframe):
            Limpador_fifa.clean_height_col(self.df_to_test_index)
    
    def testando_instancia_e_valores_retornados_pela_adjust_dtypes(self):
        print('testando_instancia_e_valores_retornados_pela_adjust_dtypes')
        #Caminho feliz
        df = Limpador_fifa.drop_na_ReleaseClause(self.df)
        self.assertIsInstance(Limpador_fifa.adjust_dtypes(df), pd.DataFrame)
        
    def testando_excecoes_levantadas_pela_adjust_dtypes(self):
        print("testando_excecoes_levantadas_pela_adjust_dtypes")
        with self.assertRaises(TypeError):
            Limpador_fifa.adjust_dtypes([[1,2,3,4],[4,5,6,7]])
            Limpador_fifa.adjust_dtypes(dict(oi= 1,tudo=2,bem=3))
            Limpador_fifa.adjust_dtypes(tuple(1,2,3,4))
            Limpador_fifa.adjust_dtypes('String')
            Limpador_fifa.adjust_dtypes(50.5)

        with self.assertRaises(indexes_not_found_in_dataframe):
            Limpador_fifa.adjust_dtypes(self.df_to_test_index)
 

    def testando_instancia_retornada_pela_foot_to_dummie(self):
        print('testando_instancia_retornada_pela_foot_to_dummie')
        #Caminho feliz
        self.assertIsInstance(Limpador_fifa.foot_to_dummie(self.df), pd.DataFrame)

    def testando_excecoes_levantadas_pela_foot_to_dummie(self):
        print('testando_excecoes_levantadas_pela_foot_to_dummie')
        with self.assertRaises(TypeError):
            Limpador_fifa.foot_to_dummie([[1,2,3,4],[4,5,6,7]])
            Limpador_fifa.foot_to_dummie(dict(oi= 1,tudo=2,bem=3))
            Limpador_fifa.foot_to_dummie(tuple(1,2,3,4))
            Limpador_fifa.foot_to_dummie('String')
            Limpador_fifa.foot_to_dummie(50.5)
        
        with self.assertRaises(indexes_not_found_in_dataframe):
            Limpador_fifa.foot_to_dummie(self.df_to_test_index)


    def testando_instancia_retornada_pela_clean_dataframe(self):
        print('testando_instancia_retornada_pela_clean_dataframe')
        #Caminho feliz
        self.assertIsInstance(Limpador_fifa.clean_dataframe(self.df), pd.DataFrame)
        
    def testando_excecoes_levantadas_pela_clean_dataframe(self):
        print('testando_excecoes_levantadas_pela_clean_dataframe')
        with self.assertRaises(TypeError):
            Limpador_fifa.clean_dataframe([[1,2,3,4],[4,5,6,7]])
            Limpador_fifa.clean_dataframe(dict(oi= 1,tudo=2,bem=3))
            Limpador_fifa.clean_dataframe(tuple(1,2,3,4))
            Limpador_fifa.clean_dataframe('String')
            Limpador_fifa.clean_dataframe(50.5)



class testes_Limpador_ariport(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\n\n testes_db_cleaning_ariport \n\n')
        print('setupClass\n')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.df = pd.read_csv('F:/Documentos/Estudos/Disciplinas FGV/Linguagens de Programação/Trabalho_Final_LP/Dados/covid_airport_dirty.csv')
        self.df_to_test_index=pd.DataFrame([['Ari', 20], ['João', 19], ['Livia', 18],['Luiz',19]],
                                            columns = ['Name1', 'Age'])

    def tearDown(self):
        print('tearDown\n')

    def testando_instancia_e_valores_retornados_pela_drop_cols(self):
        print('testando_instancia_e_valores_retornados_pela_drop_cols')
        self.assertIsInstance(Limpador_airport.drop_cols(self.df), pd.DataFrame)

        df1=pd.DataFrame([[9,10,1,2,3,4,5]], columns=['Name','Age','AggregationMethod', 'Unnamed: 0', 'Version', 'Centroid', 'Geography'])
        pd.testing.assert_frame_equal(Limpador_airport.drop_cols(df1),pd.DataFrame([[9,10]], columns=['Name','Age']))

    def testando_excecoes_levantadas_pela_drop_cols(self):
        print("testando_excecoes_levantadas_pela_drop_cols")
        with self.assertRaises(TypeError):
            Limpador_airport.drop_cols([[1,2,3,4],[4,5,6,7]])
            Limpador_airport.drop_cols(dict(oi= 1,tudo=2,bem=3))
            Limpador_airport.drop_cols(tuple(1,2,3,4))
            Limpador_airport.drop_cols('String')
            Limpador_airport.drop_cols(50.5)
        with self.assertRaises(indexes_not_found_in_dataframe):
            Limpador_airport.drop_cols(self.df_to_test_index)
    
    def testando_instancia_retornada_pela_create_datetime_cols(self):
        print('testando_instancia_retornada_pela_create_datetime_cols')
        self.assertIsInstance(Limpador_airport.create_datetime_cols(self.df), pd.DataFrame)
    
    def testando_excecoes_levantadas_pela_create_datetime_cols(self):
        print('testando_excecoes_levantadas_pela_create_datetime_cols')
        with self.assertRaises(TypeError):
            Limpador_airport.create_datetime_cols([[1,2,3,4],[4,5,6,7]])
            Limpador_airport.create_datetime_cols(dict(oi= 1,tudo=2,bem=3))
            Limpador_airport.create_datetime_cols(tuple(1,2,3,4))
            Limpador_airport.create_datetime_cols('String')
            Limpador_airport.create_datetime_cols(50.5)
        with self.assertRaises(indexes_not_found_in_dataframe):
            Limpador_airport.create_datetime_cols(self.df_to_test_index)

    
    def testando_instancia_e_valores_retornados_pela_country_names(self):
        print('testando_instancia_e_valores_retornados_pela_country_names')
        self.assertIsInstance(Limpador_airport.standardize_country_names(self.df), pd.DataFrame)

        df1=pd.DataFrame([['United States of America (the)'],['United States']], columns=['Country'])
        pd.testing.assert_frame_equal(Limpador_airport.standardize_country_names(df1),pd.DataFrame([['United States'],['United States']], columns=['Country']))

    def testando_excecoes_levantadas_pela_country_names(self):
        print("testando_excecoes_levantadas_pela_country_names")
        with self.assertRaises(TypeError):
            Limpador_airport.standardize_country_names([[1,2,3,4],[4,5,6,7]])
            Limpador_airport.standardize_country_names(dict(oi= 1,tudo=2,bem=3))
            Limpador_airport.standardize_country_names(tuple(1,2,3,4))
            Limpador_airport.standardize_country_names('String')
            Limpador_airport.standardize_country_names(50.5)
        with self.assertRaises(indexes_not_found_in_dataframe):
            Limpador_airport.standardize_country_names(self.df_to_test_index)

    
    def testando_instancia_retornada_pela_clean_dataframe(self):
        print('testando_parametros_clean_dataframe')
        self.assertIsInstance(Limpador_airport.clean_dataframe(self.df), pd.DataFrame)
    
    def testando_excecoes_levantadas_pela_clean_dataframe(self):
        print("testando_excecoes_levantadas_pela_clean_dataframe(self)")
        with self.assertRaises(TypeError):
            Limpador_airport.clean_dataframe([[1,2,3,4],[4,5,6,7]])
            Limpador_airport.clean_dataframe(dict(oi= 1,tudo=2,bem=3))
            Limpador_airport.clean_dataframe(tuple(1,2,3,4))
            Limpador_airport.clean_dataframe('String')
            Limpador_airport.clean_dataframe(50.5)


if __name__ == '__main__':
    unittest.main()