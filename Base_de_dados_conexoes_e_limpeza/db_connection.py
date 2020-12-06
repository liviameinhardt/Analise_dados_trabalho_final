import pandas  as pd
import pyodbc
'''
INSTRUÇÕES PARA TRANSFORMAR EM CSV

importar módulo

cnxn = db_connect.create_connection()
cursor = cnxn.cursor()
df = db_connect.create_df(tablename, cursor) -> tabelas disponíveis abaixo, retorna pd.DataFrame
'''
server = 'tcp:fgv-db-server.database.windows.net,1433'
database = 'fgv-db'
username = 'student'
password = '@dsInf123'

### AVAILABLE TABLES:
    
    # covid.covid_impact_on_airport_traffic
    # fifa.fifa_players
    # real_state.real_state_values
    # ufc.ufc_master
    # ufc.ufc_most_recent_event
    # ufc.ufc_upcoming_event

### USEFUL COMMANDS:
    
    # cur = cnxn.cursor()
    
    # INFO ABOUT ROW:
        # pyodbc.Row.cursor_description
        
        # IN ORDER:
        
            # column name (or alias, if specified in the SQL)
            # type code
            # display size (pyodbc does not set this value)
            # internal size (in bytes)
            # precision
            # scale
            # nullable (True/False)

    
    # INFO ABOUT TABLES
    # cur.tables -> tables -> pyodbc.Row objects
        # cur.tables.table_name
        # result = [table for table in cur.tables]
        # result[0].cursor_description
        
    # INFO ABOUT COLUMNS
    # result = cursor.columns(table='fifa_players') -> pyodbc.Row object
    # result = iter(result)
    # col = next(result)

    
### TAKING VALUES INTO PANDAS

    # cursor.execute(query)
    # rows = cursor.fetchmany(10)
    # cols = [t[0] for t in rows.cursor_description]
    # values = [list(rows[i]) for i in range(len(rows))] -> list of lists
    # df = pd.DataFrame(values, columns=cols)

def create_connection(server, database, username, password):
    cnxn_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password};'
    cnxn = pyodbc.connect(cnxn_string)
    return cnxn

def create_df(tablename, cursor):
    query = f'SELECT * FROM {tablename};'
    cursor.execute(query)
    rows = cursor.fetchall()
    cols = [t[0] for t in rows[0].cursor_description]
    values = [list(rows[i]) for i in range(len(rows))]
    df = pd.DataFrame(values, columns=cols)
    return df

def save_df_csv(df:pd.DataFrame, name:str):
    df.to_csv(name + '.csv')


