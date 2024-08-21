import mariadb
import sys

def connection():

    
    try:   
       conn = mariadb.connect(
            user="root",
            password="victor9530",
            host="localhost",
            database="alquileres"
            )
       
    except mariadb.Error as e:
        print(f"Error al conectar a MariaDB: {e}")
        sys.exist(1)
    
    return conn

