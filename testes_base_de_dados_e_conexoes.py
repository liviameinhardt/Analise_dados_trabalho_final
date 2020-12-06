import unittest
import os
import sys
import pyodbc
import pandas as pd
#sys.path.insert(0, os.path.abspath('..'))
print('-------------------------------------------')

from Base_de_dados_conexoes_e_limpeza import db_connection
from Base_de_dados_conexoes_e_limpeza import exceptions

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
        print('setUp')

    def tearDown(self):
        print('tearDown\n')

    def testando_parametros_do_create_conection(self):
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
            connection_class = db_connection.create_connection(121234, 546, 515, 9873)
            connection_class = db_connection.create_connection(self.server, 0.5, self.username, self.password)
            connection_class = db_connection.create_connection(self.server, self.database, self.username, 805)
            connection_class = db_connection.create_connection(5, self.database, -12, self.password)
            connection_class = db_connection.create_connection(5.8, self.database, -18, self.password)
            connection_class = db_connection.create_connection(self.server, 5.9, -12, 27)
            connection_class = db_connection.create_connection([1,2,4], self.database, self.username, self.password)
            connection_class = db_connection.create_connection(self.server, dict(1,2,4), self.username, self.password)
            connection_class = db_connection.create_connection(('1','2','3','4'), ('1','2','3','4'), ('1','2','3','4'), ('1','2','3','4'))
            connection_class = db_connection.create_connection(dict('1','3','4'), dict('1','3','4'), dict('1','3','4'), dict('1','3','4'))
            connection_class = db_connection.create_connection(['1','3','4'],['1','2', '3'], ['1','2', '3'], ['1','2', '3'])
            connection_class = db_connection.create_connection(self.server, self.database, True, self.password)
            connection_class = db_connection.create_connection(False, self.database, self.username, self.password)
            connection_class = db_connection.create_connection(False, False, False, False)
            connection_class = db_connection.create_connection(True, True, True, True)

        
    
    def testando_parametros_do_create_df(self):
        print('testando_parametros_do_create_df')
        connection_class = db_connection.create_connection(self.server, self.database, self.username, self.password)
        cursor = connection_class.cursor()
        self.assertIsInstance(db_connection.create_df('fifa.fifa_players',cursor),pd.DataFrame)
        self.assertIsInstance(db_connection.create_df('covid.covid_impact_on_airport_traffic',cursor),pd.DataFrame)
        self.assertIsInstance(db_connection.create_df('real_state.real_state_values',cursor),pd.DataFrame)
        self.assertIsInstance(db_connection.create_df('ufc.ufc_master',cursor),pd.DataFrame)
        self.assertIsInstance(db_connection.create_df('ufc.ufc_most_recent_event',cursor),pd.DataFrame)
        self.assertIsInstance(db_connection.create_df('ufc.ufc_upcoming_event',cursor),pd.DataFrame)
    
        
    

if __name__ == '__main__':
    unittest.main()
