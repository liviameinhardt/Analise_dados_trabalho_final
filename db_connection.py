import pandas  as pd
import pyodbc

server = 'tcp:fgv-db-server.database.windows.net,1433'
database = 'fgv-db'
username = 'student'
password = '@dsInf123'

cnxn_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password};'
cnxn = pyodbc.connect(cnxn_string)
cursor = cnxn.cursor()

while True:
    query = input('>>> ')
    if query == '-1':
        cnxn.close()
        break
    cursor.execute(query)
    r = cursor.fetchall()
    for t in r:
        print(t)
