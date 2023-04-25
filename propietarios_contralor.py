import conec_sql


def insertar_propietario(nombre, apellido, dni, cuit,direccion,telefono,celular,correo_electronico,fecha):

    conec_sql.connection().cursor()
   
    with conec_sql.connection().cursor() as cursor:
        cursor.execute ("INSERT INTO Propietarios (Nombre, Apellido, DNI, CUIT, Direccion, Telefono, Celular, Correo_electronico,fecha) VALUES ( (?),(?),(?),(?),(?),(?),(?),(?),(?));",
                        (nombre, apellido, dni, cuit,direccion,telefono,celular,correo_electronico,fecha),)
        cursor.commit()
            

def obtener_propietario(apellido):

    conec_sql.connection().cursor()
    
    propietario = None
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT * FROM Propietarios WHERE Apellido LIKE (?) ORDER by Apellido ASC;",
            ("%" + str(apellido) + "%"),
        )
        
        propietario = cursor.fetchall()
    return propietario


def eliminar_propietario(id):

    conec_sql.connection().cursor()
    with conec_sql.connection().cursor() as cursor:
        cursor.execute("DELETE FROM Propietarios WHERE id_Propietario= (?);", (id,))
        cursor.commit()
        


def obtener_propietario_por_id(id):

    conec_sql.connection().cursor()
    propietario = None
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT id_Propietario,Nombre,Apellido,DNI,CUIT,Direccion,Telefono,Celular,Correo_electronico,fecha FROM Propietarios WHERE id_Propietario=(?)",
            (id,),
        )
        
        propietario = cursor.fetchone()
        
        
           
        return propietario


def actualizar_propietario (nombre, apellido, dni, cuit,direccion,telefono,celular,correo_eletronico,id):

    conec_sql.connection().cursor()
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "UPDATE Propietarios SET Nombre=(?),Apellido=(?),DNI=(?),CUIT=(?),Direccion=(?), Telefono=(?),Celular=(?),Correo_electronico=(?) WHERE id_Propietario = (?); ",
            (
                nombre, apellido, dni, cuit,direccion,telefono,celular,correo_eletronico,id
            ),
        )
        cursor.commit()

    
       

            


