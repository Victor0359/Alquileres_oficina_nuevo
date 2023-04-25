import conec_sql


def insertar_contrato(id_propietarios, id_inquilinos,id_propiedades, fecha_inicio,duracion_contrato,precio_inicial,precio_6meses,
                     precio_12meses,precio_18meses, precio_24meses, precio_30meses, honorarios):

    cursor = conec_sql.connection().cursor()
    with conec_sql.connection().cursor() as cursor:
        cursor.execute ("INSERT INTO Contratos1 ( id_Propietarios,id_Inquilinos,id_Propiedades, Fecha_Inicio, duracion_contrato, Precio_Inicial, Precio_6Meses, Precio_12Meses,\
            Precio_18Meses, Precio_24Meses, Precio_30Meses, honorarios) VALUES  ((?)\
                ,(?),(?),(?),(?),(?),(?),(?),(?),(?),(?),(?))",
                        (id_propietarios,id_inquilinos,id_propiedades, fecha_inicio, duracion_contrato, precio_inicial, precio_6meses,\
                            precio_12meses, precio_18meses, precio_24meses, precio_30meses, honorarios))
        cursor.commit()
          
            

def obtener_contrato(contratos):

    cursor=conec_sql.connection().cursor()
    propiedad = None
    with conec_sql.connection().cursor() as cursor:
        cursor.execute( "SELECT id_Contratos, p.Dirección, concat(propietarios.Apellido,' ',propietarios.Nombre) as propietario, concat(inquilinos.Apellido,' ',inquilinos.Nombre) as inquilino,Fecha_Inicio\
        , duracion_contrato, Precio_Inicial, Precio_6Meses, Precio_12Meses, Precio_18Meses, Precio_24Meses, Precio_30Meses,honorarios, Fecha_Finalizacion FROM Contratos1 as\
            con INNER JOIN Propiedades as p on p.Id_Propiedades= con.id_Propiedades INNER JOIN Propietarios on propietarios.Id_Propietario= con.id_Propietarios INNER JOIN Inquilinos on\
                inquilinos.Id_Inquilinos= con.id_Inquilinos\
                WHERE con.id_Contratos=(?)", (contratos,))
        
        propiedad = cursor.fetchall()
        
       
        return propiedad


def eliminar_contrato(id):

    cursor=conec_sql.connection().cursor()
    with conec_sql.connection().cursor() as cursor:
        cursor.execute("DELETE FROM Contratos1 WHERE id_Contratos=(?)", (id,))
        cursor.commit()
        


def obtener_contrato_por_id(id):

    cursor=conec_sql.connection().cursor()
    contrato = None
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT id_Contratos, id_Propietarios, id_Inquilinos,id_Propiedades, Fecha_Inicio,\
                    duracion_contrato, Fecha_Finalizacion, Precio_Inicial, Precio_6Meses, Precio_12Meses,\
                    Precio_18Meses, Precio_24Meses, Precio_30Meses, honorarios FROM Contratos1 \
                    where id_Contratos=(?)",
            (id,),
        )
       
        contrato = cursor.fetchone()
       
        return contrato


def actualizar_contrato (id_propietarios, id_inquilinos,id_propiedades, fecha_inicio,duracion_contrato,precio_inicial,
                         precio_6meses, precio_12meses,precio_18meses, precio_24meses, precio_30meses, honorarios,
                         id_contratos):

    conexion = cursor=conec_sql.connection().cursor()
    with conexion.cursor() as cursor:
        cursor.execute(
            "UPDATE Contratos1 SET id_Propietarios=(?), id_Inquilinos=(?), id_Propiedades=(?),Fecha_Inicio=(?),duracion_contrato=(?),Precio_Inicial=(?),\
                Precio_6Meses=(?),Precio_12Meses=(?),Precio_18Meses=(?),Precio_24Meses=(?),Precio_30Meses=(?),honorarios=(?)\
                    WHERE id_Contratos = (?) ",
            (
               id_propietarios, id_inquilinos,id_propiedades, fecha_inicio,duracion_contrato,precio_inicial,precio_6meses,
                     precio_12meses,precio_18meses, precio_24meses, precio_30meses, honorarios, id_contratos),
            )
    
        cursor.commit()
        