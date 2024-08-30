from calendar import *
import conec_sql
import datetime
import numpy as np
from itertools import chain



def Num_recibo():
    try:
        cursor= conec_sql.connection().cursor()
        with conec_sql.connection().cursor() as cursor:
            cursor.execute("SELECT max(num_Recibo)+1 FROM Recibo_Inquilino")
            numero = cursor.fetchone()
            
            if numero[0] is None:
                numero = 1
            else:
                numero=numero[0]
           
            
            return numero
        
    except TypeError:
        print("Hay un error")
    except IndexError:
        print("error en la indexacion")   
 
def Num_recibo_propietario():
    try:
        cursor = conec_sql.connection().cursor()
        with conec_sql.connection().cursor() as cursor:
            cursor.execute("SELECT max(num_recibo)+1 FROM Recibo_propietario")
            numero = cursor.fetchone()
           
            if numero[0] is None:
                numero = 1
            else:
                numero=numero[0]
            
    except TypeError:
        print("Hay un error")
    except IndexError:
        print("error en la indexacion")      


def Cuotas(id):
    
        cursor = conec_sql.connection().cursor()
        with conec_sql.connection().cursor() as cursor:
            cursor.execute(
                "select datediff(m,Fecha_inicio,GETDATE()) from contratos where id_inquilinos=(?)",
                (id,),
            )
            cuota = cursor.fetchone()
            
        return cuota
    
def Cuota_propietario(id):
    
        cursor = conec_sql.connection().cursor()
        with conec_sql.connection().cursor() as cursor:
            cursor.execute(
                "select datediff(m,fecha_inicio,GETDATE()) from contratos where id_propiedades=%s",
                (id,),
            )
            
            cuota = cursor.fetchone()
            
        return cuota
    

def Servicios(id):
    try:
        cursor1 = conec_sql.connection().cursor()
        with conec_sql.connection().cursor() as cursor:
            cursor.execute(
                "SELECT Top(1) impuestos.abl,impuestos.aysa, impuestos.exp_comunes,\
                impuestos.exp_extraordinarias,impuestos.seguros FROM Impuestos as\
                impuestos INNER JOIN contratos as contratos on contratos.id_propiedades\
                =impuestos.id_propiedades where contratos.id_inquilinos=(?) group by\
                impuestos.abl,impuestos.aysa, impuestos.exp_comunes,impuestos.exp_extraordinarias\
                ,impuestos.seguros,impuestos.fecha Order By impuestos.fecha desc",(id,),)
           
            servicios = cursor.fetchall()
            cursor1.close()
            cursor2 = conec_sql.connection().cursor()
        
        with conec_sql.connection().cursor() as cursor2:
            cursor2.execute(
                "select mes_contrat FROM Recibo_Inquilino where id_inquilino= (%s) and fecha=(select Max(fecha) from recibo_inquilino where id_inquilino= (%s))",
                (
                    id,
                    id,
                ),
            )
            cuota=Cuotas(id)
            
            mes_contrato = cursor2.fetchone()
            
            if mes_contrato is None:
                mes_contrato=[1]
            
           
           
            cuota1=list(cuota) 
            
                    
            
            cuot=[]
           
            diferencia_cuotapaga1=[]
            
            resultado=[]
            dif=0
            
            
            if mes_contrato is None:
                cuot.append(1) 
                diferencia_cuotapaga1=[b-a for a,b in zip (cuota1,cuot)]
                
            else:
                diferencia_cuotapaga1=[b-a for a,b in zip (mes_contrato,cuota1)]
            
            for i in range(len(diferencia_cuotapaga1)):
                  dif= int(diferencia_cuotapaga1[i])  
                
            
            resultado=[a*dif for a in (servicios[0])] 
            
                                
        
            return resultado  
           

    except ValueError as val:
        print(val)

def direccion(id):
    try:
        cursor = conec_sql.connection().cursor()
        with conec_sql.connection().cursor() as cursor: 
            cursor.execute(
                "SELECT propiedades.id_propiedades, concat(propiedades.dirección,' ',propiedades.localidad) as direccion FROM Contratos as contratos inner join propiedades as propiedades on contratos.id_propiedades=propiedades.id_propiedades where contratos.id_inquilinos=(%s)",
                (id,),
            )
            direccion1=[]
            direccion = cursor.fetchall()
            direccion1=[i for i in direccion]
            
            return direccion1
   
    except ValueError as val:
        print(val)

def direccion_propietario(id):
    try:
        cursor = conec_sql.connection().cursor()
        with conec_sql.connection().cursor()  as cursor:
            cursor.execute(
                "SELECT propiedades.id_propiedades, concat(propiedades.dirección,' ',propiedades.localidad) FROM contratos as contratos inner join propiedades as propiedades on contratos.id_propiedades=propiedades.id_propiedades where contratos.id_propietarios=(%s)",
                (id,),
            )
            direccion = cursor.fetchall()
            
            return direccion
   
    except ValueError as val:
        print(val)



def formato_fecha(date):
    fecha = f"{date}".split()[0] #obtenemos solo la fehca YYYY-MM-DD
    year,month,day = fecha.split("-") #separamos cada parte
    #creamos un diccionario con todos los mese
    months = {
                1: "Enero",
                2: "Febrero",
                3: "Marzo",
                4: "Abril",
                5: "Mayo",
                6: "Junio",
                7: "Julio",
                8: "Agosto",
                9: "Septiembre",
                10: "Octubre",
                11: "Noviembre",
                12: "Diciembre",
            }
    #retornamos el resultado
    return f"{day} días del mes de {months[int(month)]} del {year}"

def formato_fecha_vencimiento(date):
    fecha = f"{date}".split()[0] #obtenemos solo la fehca YYYY-MM-DD
    year,month,day = fecha.split("-") #separamos cada parte
    #creamos un diccionario con todos los mese
    months = {
                1: "Enero",
                2: "Febrero",
                3: "Marzo",
                4: "Abril",
                5: "Mayo",
                6: "Junio",
                7: "Julio",
                8: "Agosto",
                9: "Septiembre",
                10: "Octubre",
                11: "Noviembre",
                12: "Diciembre",
            }
   
    #retornamos el resultado
    return f"del mes de {months[int(month)]} del {year}"


def formato_fecha_mes(date):
    
    months = {
                1: "Enero",
                2: "Febrero",
                3: "Marzo",
                4: "Abril",
                5: "Mayo",
                6: "Junio",
                7: "Julio",
                8: "Agosto",
                9: "Septiembre",
                10: "Octubre",
                11: "Noviembre",
                12: "Diciembre",
            }
    #retornamos el resultado
    return months[int(date)]


def valores(x):
    if x < 24:
        return x


def locura(id):
    #try:
        cursor = conec_sql.connection().cursor()
        with conec_sql.connection().cursor() as cursor:
            cursor.execute(
                "SELECT Precio_Inicial,Precio_actual FROM Contratos where id_inquilinos=(%s)",
                (id,)
            )
            valores = cursor.fetchall()
            
        cursor1 = conec_sql.connection().cursor()
        with conec_sql.connection().cursor() as cursor1:   
            cursor1.execute(
                "SELECT mes_contrato FROM recibo_inquilino WHERE id_inquilino=(%s) and fecha_rec=(select max(fecha_rec) from recibo_inquilino where id_inquilino=%s);",
                (id, id,),
             )
            cuota_recibo = cursor1.fetchone()
            
            cuot=[1]
            valores1=list(valores) # valores contrato
            
            cuota= Cuotas(id) #cuota contrato
            if cuota is None:
            
              cuota=tuple(cuot)
            if cuota_recibo is None:
                cuota_recibo=[1]
            
            valores2=np.array(valores1)
            valores3=valores2.flatten().tolist()
            diferencia_cuotapaga= [e1 - e2 for e1, e2 in zip (cuota,cuota_recibo)]
            diferencia_cuotapaga=[int(i)for i in diferencia_cuotapaga]
            diferencia_cuotapaga1=diferencia_cuotapaga[0]
            
              
            
            cuot = [1]
            resultado=[]
            
            if cuota is None:
              cuota=tuple(cuot)
            diferencia_cuotapaga2=[]
               
            if diferencia_cuotapaga1== []:
                    diferencia_cuotapaga2 = list(range(cuota_recibo[0], cuota[0] + 1))
            else:
                  diferencia_cuotapaga2 = list(range(cuota_recibo[0]+1, cuota[0]+1)) 
           
          
            lista_6 = []
            lista_12 = []
            lista_18 = []
            lista_24 = []
            lista_30 = []
            lista_36 = []

            for i in diferencia_cuotapaga2:
                    if i <= 6:
                        lista_6.append(i)
                    elif i <= 12:
                        lista_12.append(i)
                    elif i <= 18:
                        lista_18.append(i)
                    elif i <= 24:
                        lista_24.append(i)
                    elif i <= 30:
                        lista_30.append(i)
                    else:
                        lista_36.append(i)
            
            
            x_lista6  = len(lista_6)
            x_lista12 = len(lista_12)
            x_lista18 = len(lista_18)
            x_lista24 = len(lista_24)
            x_lista30 = len(lista_30)
            x_lista36 = len(lista_36)
            
            
            if valores3==[]:
                    
              lista_precios_6 = 0 * x_lista6
              lista_precios_12 = 0 * x_lista12
              lista_precios_18 = 0 * x_lista18
              lista_precios_24 = 0 * x_lista24
              lista_precios_30 = 0 * x_lista30
              lista_precios_36 = 0 * x_lista36
            else:
              lista_precios_6 = valores3[0] * x_lista6
              lista_precios_12 =valores3[1] * x_lista12
              lista_precios_18 = valores3[2] * x_lista18
              lista_precios_24 = valores3[3] * x_lista24
              lista_precios_30 = valores3[4] * x_lista30
              lista_precios_36 = valores3[5] * x_lista36
                
            resultado = (
                    lista_precios_6
                    + lista_precios_12
                    + lista_precios_18
                    + lista_precios_24
                    + lista_precios_30
                    + lista_precios_36
                )
           
          
            return resultado
   
    #except TypeError as error :
       # print( error )


def saldo_anterior(id):
    try:
        cursor = conec_sql.connection().cursor()
        with conec_sql.connection().cursor() as cursor:
            saldo_inq=None
            cursor.execute(
                "SELECT Top (1) ISNULL(saldo.monto_serv_anterior,0) as serv, ISNULL\
                    ( saldo.monto_an_mensualidad,0) as mensu FROM Saldo_inquilino as\
                    saldo inner join Recibo_Inquilino as recibo on recibo.id_Inquilino=\
                    saldo.id_Inquilino where recibo.id_Inquilino=(?) order by saldo.id_saldo desc",
                (id,),)
           
            saldo_inq = cursor.fetchall()
            saldo_inq1=None
            
            if len(saldo_inq) ==0: 
               saldo_inq1=[(0,0)]
                 
               return saldo_inq1
            elif saldo_inq is not None:
                saldo_inq=[i for i in saldo_inq]
               
                return saldo_inq    
               
        
    except ValueError as valores:
       print(valores)
       

def guardar_recibo (num_Recibo,id_Inquilino,id_propiedad,fecha,mes_contrat,str_mes,Meses_Adeudados,abl,\
                aysa,expensas_comunes,seguros,varios,total, pago, saldo_pen_servicios, saldo_mes_adeudado):
   
    try:
        conec_sql.connection().cursor()
        with conec_sql.connection().cursor() as cursor:
            cursor.execute(
                "INSERT INTO recibo_inquilino (num_recibo,id_inquilino,id_propiedad,fecha,mes_contrato,str_mes,meses_adeudados,abl,\
                aysa,ex_comunes,seguros,varios,total, pago, saldo_pen_serv, saldo_mes_adeudado) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (num_Recibo,id_Inquilino,id_propiedad,fecha,mes_contrat,str_mes,Meses_Adeudados,abl,\
                aysa,expensas_comunes,seguros,varios,total, pago, saldo_pen_servicios, saldo_mes_adeudado),
                )
            
            cursor.commit()
           
    
    except ValueError as valores:
        print('Se ha producido un error' + valores)
        
def guardar_recibo_prop (num_Recibo,id_propietario,id_propiedad,fecha,mes_contrat,Meses_Adeu,abl,\
                aysa,exp_extraor,seguros,varios, monto_mensualidad, monto_servicios,total, pago):
   
    try:
        conec_sql.connection().cursor()
        with conec_sql.connection().cursor() as cursor:
            cursor.execute(
                "INSERT INTO Recibo_Inquilino (num_Recibo,id_propietario,id_propiedad,fecha,mes_contrato,Mensualidad,abl,\
                aysa,exp_extraor,seguros,varios,monto_mensualidad, monto_servicios,total, pago) values\
                    ((?),(?),(?),(?),(?),(?),(?),(?),(?),\
                        (?),(?),(?),(?),(?),(?))",
                (num_Recibo,id_propietario,id_propiedad,fecha,mes_contrat,Meses_Adeu,
                 abl,aysa,exp_extraor,seguros,varios, monto_mensualidad, monto_servicios,\
                     total, pago),
                )
            
            cursor.commit()
            
    
    except ValueError as valores:
        print('Se ha producido un error' + valores)



def dif_mes(id):
     try:
        cursor = conec_sql.connection().cursor()
        with conec_sql.connection().cursor() as cursor:
            cursor.execute("SELECT month(max(fecha))as mes FROM recibo_inquilino where id_inquilino=%s )", (id,))
            
        rango = cursor.fetchone()
        
        return rango
    
     except ValueError:
       print("Error")

def mensaje_contrat_vacio(id):
    conec_sql.connection().cursor()
    with conec_sql.connection().cursor() as cursor:
            cursor.execute("")

    return 
    