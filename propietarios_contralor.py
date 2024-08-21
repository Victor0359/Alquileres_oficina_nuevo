import conec_sql
import mariadb
import sys

def propietario_por_dni (dni):
     conec_sql.connection().cursor()
     with conec_sql.connection().cursor() as cursor:
          cursor.execute("select id_propietarios from propietarios where dni = %s;",(dni,))
          dni=cursor.fetchone()
          cursor.close()
        
          return dni


def insertar_propietario(nombre, apellido, dni, cuit,direccion,telefono,celular,correo_elect):
    
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
  cur.execute ("INSERT INTO propietarios (nombre, apellido, dni, cuil,      direccion, telefono, celular, correo_elec ) VALUES ( %s,%s,%s,%s,%s,%s,%s,%s);",
  (nombre, apellido, dni, cuit,direccion,telefono[:12],celular,correo_elect),)
   
  conn.commit()
        
  conn.close()
    
        
            

def obtener_propietario(apellido):

    conec_sql.connection().cursor()
    
    propietario = None

    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT * FROM propietarios WHERE apellido LIKE %s ORDER by apellido ASC;",
            ("%" + str(apellido)+ "%",),
        )
        
        propietario = cursor.fetchall()
        
        cursor.close()
        
        return propietario


def eliminar_propietario(id):

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
              "DELETE FROM propietarios WHERE id_propietarios= %s;", (id,))
  conn.commit()
  conn.close()
        


def obtener_propietario_por_id(id):

    conec_sql.connection().cursor()
    propietario = None
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT id_propietarios,nombre,apellido,dni,cuil,direccion,telefono,celular,correo_elec FROM propietarios WHERE id_propietarios=%s;",
            (id,)
        )
        
        propietario = cursor.fetchone()
              
           
        return propietario


def actualizar_propietario (nombre, apellido, dni, cuit,direccion,telefono,       celular, correo_elect,id):
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
                "UPDATE propietarios SET nombre=%s,apellido=%s,dni=%s,cuil=%s,direccion=%s,telefono=%s,celular=%s,correo_elec=%s WHERE id_propietarios=%s;",
            (
                nombre, apellido, dni, cuit,direccion,telefono,celular,correo_elect,id,
        
            ),
             )
    conn.commit()
    conn.close()

    
       

            


