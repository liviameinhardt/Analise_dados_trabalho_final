import unittest
import os
import sys
import pyodbc
import pandas as pd
#sys.path.insert(0, os.path.abspath('..'))
print('-------------------------------------------')

from Base_de_dados_conexoes_e_limpeza import db_connection

class testes_db_connection(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupClass\n')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        self.server = 'tcp:fgv-db-server.database.windows.net,1433'
        self.database = 'fgv-db'
        self.username = 'student'
        self.password = '@dsInf123'
        self.connection_class = db_connection.create_connection(self.server, self.database, self.username, self.password)
        print('setUp')

    def tearDown(self):
        print('tearDown\n')

    def testando_parametros_da_create_conection(self):
        print('test_create_connection')
        connection_class = db_connection.create_connection(self.server, self.database, self.username, self.password)
        self.assertIsInstance(connection_class, pyodbc.Connection)
        
        with self.assertRaises(db_connection.invalid_server_string_format):
            db_connection.create_connection('fgv-db-server.database.windows.net', self.database, self.username, self.password)
            db_connection.create_connection('tcp:fgv-db-server.database.windows.net', self.database, self.username, self.password)
            db_connection.create_connection('tcp:fgv-db-server.database.windows.net1433', self.database, self.username, self.password)
        
        with self.assertRaises(db_connection.invalid_server_port_value):
            db_connection.create_connection('tcp:fgv-db-server.database.windows.net,A123', self.database, self.username, self.password)
            
        with self.assertRaises(TypeError):
            db_connection.create_connection(121234, 546, 515, 9873)
            db_connection.create_connection(self.server, 0.5, self.username, self.password)
            db_connection.create_connection(self.server, self.database, self.username, 805)
            db_connection.create_connection(5, self.database, -12, self.password)
            db_connection.create_connection(5.8, self.database, -18, self.password)
            db_connection.create_connection(self.server, 5.9, -12, 27)
            db_connection.create_connection([1,2,4], self.database, self.username, self.password)
            db_connection.create_connection(self.server, dict(1,2,4), self.username, self.password)
            db_connection.create_connection(('1','2','3','4'), ('1','2','3','4'), ('1','2','3','4'), ('1','2','3','4'))
            db_connection.create_connection(dict('1','3','4'), dict('1','3','4'), dict('1','3','4'), dict('1','3','4'))
            db_connection.create_connection(['1','3','4'],['1','2', '3'], ['1','2', '3'], ['1','2', '3'])
            db_connection.create_connection(self.server, self.database, True, self.password)
            db_connection.create_connection(False, self.database, self.username, self.password)
            db_connection.create_connection(False, False, False, False)
            db_connection.create_connection(True, True, True, True)

        
    
    def testando_parametros_da_create_df(self):
        print('testando_parametros_do_create_df')
        connection_class = db_connection.create_connection(self.server, self.database, self.username, self.password)
        cursor = connection_class.cursor()
        self.assertIsInstance(db_connection.create_df('fifa.fifa_players',cursor),pd.DataFrame)
        self.assertIsInstance(db_connection.create_df('covid.covid_impact_on_airport_traffic',cursor),pd.DataFrame)
        self.assertIsInstance(db_connection.create_df('real_state.real_state_values',cursor),pd.DataFrame)
        self.assertIsInstance(db_connection.create_df('ufc.ufc_master',cursor),pd.DataFrame)
        self.assertIsInstance(db_connection.create_df('ufc.ufc_most_recent_event',cursor),pd.DataFrame)
        self.assertIsInstance(db_connection.create_df('ufc.ufc_upcoming_event',cursor),pd.DataFrame)

        with self.assertRaises(TypeError):
            db_connection.create_df(1234,cursor)
            db_connection.create_df(['fifa.fifa_player'],cursor)
            db_connection.create_df(dict('fifa_player'), cursor)
            db_connection.create_df(tuple('fifa_player'), cursor)
            db_connection.create_df(1234,1234)
            db_connection.create_df(['fifa.fifa_player'],'pyodbc.Cursor')

        with self.assertRaises(db_connection.invalid_table_name):
            db_connection.create_df('PES.PES_player',cursor)
            db_connection.create_df('Bomba_Patch2021.Bomba_Patch_player',cursor)
            db_connection.create_df('wwe.ufc_upcoming_event',cursor)
            db_connection.create_df('ufc.xfactor_most_recent_event',cursor)
            db_connection.create_df('covid.covid_impact_on_aeroporto_traffic',cursor)

    def testando_parametros_da_save_df_csv(self):
        with self.assertRaises(TypeError):
            db_connection.save_df_csv(123,'test')
            db_connection.save_df_csv(123,dict(1,2))
            db_connection.save_df_csv('nome_do_arquivo',(1,2))
            db_connection.save_df_csv(pd.DataFrame([[1,2,3,4],[5,6,7,8]]), [1,2,3])



if __name__ == '__main__':
    unittest.main()
