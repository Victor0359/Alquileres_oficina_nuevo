import conec_sql 
import mariadb 
import sys


def insertar_contrato(id_propietarios, id_inquilinos,id_propiedades, fecha_inicio,duracion_cont,precio_inicial, precio_actual,honorarios):
     
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
    
     cur.execute ("INSERT INTO Contratos ( id_propietarios,id_inquilinos,id_propiedades, fecha_Inicio,duracion_cont, precio_inicial, precio_actual, honorarios) VALUES  (%s,%s,%s,%s,%s,%s,%s,%s);",
               (id_propietarios,id_inquilinos,id_propiedades, fecha_inicio, duracion_cont, precio_inicial,precio_actual, honorarios),)
    
     cur.connection.commit()
     cur.close()
     conn.close()          
            

def obtener_contrato(contratos):

    cursor=conec_sql.connection().cursor()
    propiedad = None
    with conec_sql.connection().cursor() as cursor:
        cursor.execute( "SELECT id_contratos, p.direccion, concat(propietarios.apellido,' ',propietarios.nombre) as propietario, concat(inquilinos.apellido,' ',inquilinos.nombre) as inquilino,fecha_inicio, duracion_cont, fecha_fin, precio_inicial, precio_actual, honorarios FROM contratos_v as con INNER JOIN propiedades_1 as p on p.id_propiedades= con.id_propiedades INNER JOIN propietarios on  propietarios.id_propietarios= con.id_propietarios INNER JOIN inquilinos on inquilinos.id_inqiilinos= con.id_inquilinos WHERE con.id_contratos=%s", (contratos,))
        
        propiedad = cursor.fetchall()
        
       
        return propiedad


def eliminar_contrato(id):
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
    cur.execute("DELETE FROM Contratos WHERE id_contratos=%s", (id,))
    cur.connection.commit()
    cur.close()
    conn.close()
        


def obtener_contrato_por_id(id):

    cursor=conec_sql.connection().cursor()
    contrato = None
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT id_contratos, id_propietarios, id_inquilinos,id_propiedades, fecha_inicio,       duracion_cont, fecha_fin, precio_inicial, precio_actual, honorarios FROM contratos_v \
                    where id_contratos=%s",
            (id,),
        )
       
        contrato = cursor.fetchone()
        print(contrato)
        return contrato


def actualizar_contrato (id_propietarios, id_inquilinos,id_propiedades, fecha_inicio,duracion_contrato,precio_inicial, precio_final, honorarios, id_contratos):

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
            "UPDATE contratos SET id_propietarios=%s, id_inquilinos=%s, id_propiedades=%s,fecha_inicio=%s,duracion_cont=%s, precio_inicial=%s, precio_actual=%s, honorarios=%s WHERE id_contratos = %s ",
            (
               id_propietarios, id_inquilinos,id_propiedades, fecha_inicio,duracion_contrato,precio_inicial, precio_final, honorarios, id_contratos)),
            
    
    cur._connection.commit()
    cur.close()
    conn.close()
        