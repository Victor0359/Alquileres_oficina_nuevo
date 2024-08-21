import conec_sql

def loguin(nombre,usuario):
  
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT id_Login FROM login where nombre=(?) and clave=(?);", (nombre,usuario),
            )
        loguin = cursor.fetchone()
        cursor.close()
        return loguin