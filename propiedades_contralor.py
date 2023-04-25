import conec_sql


def insertar_propiedad(direccion, localidad, propietario,fecha):

    conec_sql.connection().cursor()
    with conec_sql.connection().cursor() as cursor:

        cursor.execute(
            "INSERT INTO Propiedades (Dirección,Localidad,propietario,fecha) values((?),(?),(?),(?))",
            (direccion, localidad, propietario,fecha),
        )
    cursor.commit()
       


def obtener_propiedad(propietario):

    cursor=conec_sql.connection().cursor()
    propiedad = None
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT id_Propiedades, Dirección, Localidad, propietario, fecha FROM Propiedades WHERE propietario = (?)",
            (propietario,)
        )

        propiedad = cursor.fetchall()
      

        return propiedad


def eliminar_propiedad(id):

    cursor=conec_sql.connection().cursor()
    with conec_sql.connection().cursor() as cursor:
        cursor.execute("DELETE FROM Propiedades WHERE id_Propiedades=(?)", (id,))
       
        cursor.commit()
        


def obtener_propiedad_por_id(id):

    cursor=conec_sql.connection().cursor()
    propiedad = None
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT id_Propiedades,Dirección,Localidad,propietario,fecha FROM Propiedades WHERE id_Propiedades=(?)",
            (id,),
        )
       
        propiedad = cursor.fetchone()
        
        return propiedad


def actualizar_propiedad(direccion, localidad, propietario, id):

    cursor=conec_sql.connection().cursor()
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "UPDATE Propiedades SET Dirección = (?), Localidad = (?), propietario = (?) WHERE id_Propiedades = (?) ",
            (
                direccion,
                localidad,
                propietario,
                id,
            ),
        )
        cursor.commit()
       