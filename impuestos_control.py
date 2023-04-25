import conec_sql


def insertar_impuestos(id_propiedades,abl,aysa,exp_comunes,exp_extraordinarias,seguros,fecha):

    cursor= conec_sql.connection().cursor()
    with conec_sql.connection().cursor() as cursor:
        cursor.execute ("INSERT INTO Impuestos( Id_Propiedades, abl, aysa, exp_comunes, exp_extraordinarias, seguros, fecha) VALUES\
            ((?),(?),(?),(?),(?),(?),(?))",
                        (id_propiedades,abl,aysa,exp_comunes,exp_extraordinarias,seguros,fecha))
        cursor.commit()
          
        
def obtener_impuesto(propiedad):

    cursor = conec_sql.connection().cursor()
    impuesto = None
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT id_Impuestos, pro.DirecciÓn, im.abl, im.aysa, im.exp_comunes, im.exp_extraordinarias, im.seguros, im.fecha\
                FROM Impuestos as im INNER join Propiedades as pro on im.Id_Propiedades=pro.Id_Propiedades WHERE\
                    im.Id_propiedades LIKE (?)",
            ("%" + str(propiedad) + "%"),
        )
        
        impuesto = cursor.fetchall()
       
        return impuesto