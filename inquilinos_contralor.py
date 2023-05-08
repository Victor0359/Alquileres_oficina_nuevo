import conec_sql 


def select_inquilino_por_dni(dni):
     conec_sql.connection().cursor()
     with conec_sql.connection().cursor() as cursor:
         cursor.execute("select id_Inquilinos from Inquilinos where DNI=(?);",(dni),)
         dni= cursor.fetchone()
         return dni



def insertar_inquilino(nombre, apellido, dni, cuit,direccion,telefono,celular,correo_electronico,fecha):
     
     conec_sql.connection().cursor()
   
     with conec_sql.connection().cursor() as cursor:
        cursor.execute ("INSERT INTO Inquilinos (Nombre, Apellido, DNI, CUIT, Direccion, Telefono, Celular, Correo_electronico,fecha) VALUES ( (?),(?),(?),(?),(?),(?),(?),(?),(?));",
                        (nombre, apellido, dni, cuit,direccion,telefono,celular,correo_electronico,fecha),)
        cursor.commit()
        
         
            

def obtener_inquilino(apellido):
    conec_sql.connection().cursor()
        
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT * FROM Inquilinos WHERE Apellido LIKE (?) ORDER by Apellido ASC;",
            ("%" + str(apellido) + "%"),
        )
        
        propietarios = cursor.fetchall()
       
        return propietarios


def eliminar_inquilino(id):
     conec_sql.connection().cursor()
    
     with conec_sql.connection().cursor() as cursor:
        cursor.execute("DELETE FROM Inquilinos WHERE id_Inquilinos= (?);", (id,))
        cursor.commit()
        
        


def obtener_inquilino_por_id(id):

    conec_sql.connection().cursor()
    inquilino = None
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT id_Inquilinos,Nombre,Apellido,DNI,CUIT,Direccion,Telefono,Celular,Correo_electronico,fecha FROM Inquilinos WHERE id_Inquilinos=(?)",
            (id,),
        )
        
        inquilino = cursor.fetchone()
        
        
           
        return inquilino


def actualizar_inquilino (nombre, apellido, dni, cuit,direccion,telefono,celular,correo_eletronico,id):

      conec_sql.connection().cursor()
      with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "UPDATE Inquilinos SET Nombre=(?),Apellido=(?),DNI=(?),CUIT=(?),Direccion=(?), Telefono=(?),Celular=(?),Correo_electronico=(?) WHERE id_Inquilinos = (?); ",
            (
                nombre, apellido, dni, cuit,direccion,telefono,celular,correo_eletronico,id
            ),
        )
        cursor.commit()
       