import conec_sql

def Num_recibo():
    try:
        cursor=conec_sql.connection().cursor()
        with conec_sql.connection().cursor() as cursor:
            cursor.execute("SELECT * FROM propietarios")
                     
            numero = cursor.fetchone()
            print(numero)
        while numero != None:
                numero[0]
                recibo = int(numero[0]) + 1
                return recibo
    except TypeError:
        print("Hay un error")
    except IndexError:
        print("error en la indexacion")   
    
def Cuotas(id):
    try:
        cursor=conec_sql.connection().cursor()
        with conec_sql.connection().cursor() as cursor:
          cursor.execute ("SELECT datediff(m,Fecha_Inicio,getdate())+1 as cuota from contratos WHERE id_propiedades=(?)",
                (id,),  )
          cuota = cursor.fetchone()
          return cuota        
       
    except TypeError:
        print("Hay un error")
    except IndexError:
        print("error en la indexacion")   
        
