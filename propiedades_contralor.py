
import conec_sql
import mariadb
import sys

def insertar_propiedad(direccion, localidad, propietario):
    try:
        conn = mariadb.connect(
        user="root",
        password="victor9530",
        host="localhost",
        port=3306,
        database="alquileres"
    )
    except mariadb.Error as e:
        print(f"Error al conectar a MariaDB: {e}")
        sys.exit(1)

    cur = conn.cursor()

        
    cur.execute ("INSERT INTO propiedades_1 (direccion,localidad,propietario) values(%s,%s,%s);",
            (direccion, localidad, propietario)),


    conn.commit()


    conn.close()
    
   
def obtener_propiedad(propietario):

    cursor=conec_sql.connection().cursor()
    propiedad = None
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT id_propiedades, direccion, localidad, propietario FROM propiedades_1 WHERE propietario = %s  order by direccion; ",
            (propietario,)
        )

        propiedad = cursor.fetchall()
      

        return propiedad


def eliminar_propiedad(id):
    
    try:
        conn = mariadb.connect(
        user="root",
        password="victor9530",
        host="localhost",
        port=3306,
        database="alquileres"
    )
    except mariadb.Error as e:
        print(f"Error al conectar a MariaDB: {e}")
        sys.exit(1)
        
    cur = conn.cursor() # Obtén un cursor para ejecutar consultas

        
    cur.execute("DELETE FROM propiedades_1 WHERE id_propiedades=%s;", (id,)) # Ejemplo de consulta de actualización

    conn.commit() # Confirma los cambios

    conn.close() # Cierra la conexión
 
def obtener_propiedad_por_id(id):

    cursor=conec_sql.connection().cursor()
    propiedad = None
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT id_propiedades,direccion,localidad,propietario FROM propiedades_1 WHERE id_propiedades=%s;",
            (id,),
        )
       
        propiedad = cursor.fetchone()
        cursor.close()
        
        
        return propiedad


def actualizar_propiedad(direccion, localidad, propietario, id):

   try:
        conn = mariadb.connect(
        user="root",
        password="victor9530",
        host="localhost",
        port=3306,
        database="alquileres"
         )
    
   except mariadb.Error as e:
        print(f"Error al conectar a MariaDB: {e}")
        sys.exit(1)
   cur = conn.cursor()
   cur.execute(
            "UPDATE propiedades_1 SET direccion = %s, localidad = %s, propietario = %s WHERE id_propiedades = %s; ",
            (
                direccion,
                localidad,
                propietario,
                id,
            ),
        )
   conn.commit()
   conn.close()
 


def obtener_propiedad1(direccion):

    cursor=conec_sql.connection().cursor()
    propiedad = None
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT id_propiedades,direccion,localidad,propietario FROM propiedades_1 where direccion like %s ORDER by direccion ASC;", ("%" + str(direccion) + "%",),
           
        )
       
        propiedad = cursor.fetchall()
        print(propiedad)
        cursor.close()
    
     
        return propiedad

def obtener_propiedad():

    cursor=conec_sql.connection().cursor()
    propiedad = None
    with conec_sql.connection().cursor()as cursor:
        cursor.execute(
            "SELECT id_propiedades,dirección,localidad,propietario FROM propiedades_1 clear order by direccion;")
       
        propiedad = cursor.fetchall()
        cursor.close()
    
        
        return propiedad




       