import conec_sql
import mariadb
import sys


def insertar_impuestos(id_propiedades,abl,aysa,exp_comunes,exp_extraordinarias,seguros,fecha):
        
     
        conn = mariadb.connect(
        user="root",
        password="victor9530",
        host="localhost",
        port=3306,
        database="alquileres"
         )
    
        cur = conn.cursor()
        cur.execute ("INSERT INTO impuestos( id_propiedades, abl, aysa, exp_comunes, exp_extraordinarias, seguro, fecha) VALUES\
            ((%s),(%s),(%s),(%s),(%s),(%s),(%s))",
                        (id_propiedades,abl,aysa,exp_comunes,exp_extraordinarias,seguros,fecha))
   
        conn.commit()
        
        conn.close()
   
   
          
        
def obtener_impuesto(propiedad):

    cursor = conec_sql.connection().cursor()
    impuesto = None
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT im.int_impuestos, pro.direccion, im.abl, im.aysa, im.exp_comunes, im.exp_extraordinarias, im.seguro, im.fecha FROM impuestos as im INNER join propiedades_1 as pro on im.id_propiedades=pro.id_propiedades WHERE pro.direccion LIKE %s;", ('%' + str(propiedad) + '%',)
           
        )
        
        impuesto = cursor.fetchall()
        
        return impuesto