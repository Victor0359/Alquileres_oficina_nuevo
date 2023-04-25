import conec_sql

def loguin(nombre,usuario):
    cursor= conec_sql.connection().cursor()
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT id_Login FROM Login where Nombre=(?) and clave=(?);", (nombre,usuario),
        )
        loguin = cursor.fetchone()

        return loguin