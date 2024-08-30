import conec_sql 
import mariadb 
import sys


def select_inquilino_por_dni(dni):
     conec_sql.connection().cursor()
     with conec_sql.connection().cursor() as cursor:
         cursor.execute("select id_inqiilinos from inquilinos where dni=%s;",(dni,),)
         dni= cursor.fetchone()
         cursor.close()
         print(dni)
         return dni



def insertar_inquilino(nombre, apellido, dni, cuit,direccion,telefono,celular,correo_elec):
     
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
 cur.execute ("INSERT INTO inquilinos (nombre, apellido, dni, cuit ,direccion, telefono, celular,correo_elec) VALUES ( %s,%s,%s,%s,%s,%s,%s,%s);",                        (nombre, apellido, dni, cuit,direccion,telefono,celular,correo_elec,))
 conn.commit()
 conn.close() 
         
            

def obtener_inquilino(apellido):
   
    conec_sql.connection().cursor()

    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT * FROM inquilinos WHERE apellido LIKE %s ORDER by apellido ASC;",
            ("%" + str(apellido) + "%",),
        )
        
        obtener = cursor.fetchall()
        cursor.close()
           
       
    return obtener


def eliminar_inquilino(id):
     
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
    
 cur.execute("DELETE FROM inquilinos WHERE id_inqiilinos= %s;", (id,))
       
 conn.commit()
 conn.close()        


def obtener_inquilino_por_id(id):

    conec_sql.connection().cursor()
    inquilino = None
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT id_inqiilinos,nombre,apellido,dni,cuit,direccion,telefono,celular,correo_elec FROM inquilinos WHERE id_inqiilinos=%s;",
            (id,),
        )
        
        inquilino = cursor.fetchone()
        
        
           
        return inquilino


def actualizar_inquilino (nombre, apellido, dni, cuit,direccion,telefono,celular, correo_elec,id):

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
            "UPDATE inquilinos SET nombre=%s,apellido=%s,dni=%s,cuit=%s,direccion=%s, telefono=%s,celular=%s,correo_elec=%s WHERE id_inqiilinos = %s; ",
            (
                nombre, apellido, dni, cuit,direccion,telefono,celular, correo_elec,id
            ),
        )
      
 conn.commit()
 conn.close()
       