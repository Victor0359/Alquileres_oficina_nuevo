import pyodbc

def connection():

    try:   
       connSqlServer = pyodbc.connect(driver='{ODBC Driver 17 for SQL server}',
                               server='tcp:miservidorsql9530.database.windows.net',
                               database='Alquileres',
                               uid='VictHugo',pwd='Victor9530')
       
    except:
        print ('coneccion cerrada')
   
    return connSqlServer  