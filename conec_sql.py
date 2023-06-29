import pyodbc

def connection():

    try:   
       connSqlServer = pyodbc.connect(driver='{ODBC Driver 17 for SQL server}',
                               server='alquileres.mssql.somee.com',
                               database='alquileres',
                               uid='mrnct_SQLLogin_1',
                               pwd='81x55n8d5y')
       
    except:
        print ('coneccion cerrada')
   
    return connSqlServer  