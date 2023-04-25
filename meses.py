from calendar import *
import conec_sql
import datetime
import functools
import numpy as np
from itertools import chain
import itertools

def meses(id):
    
   
    salida=None
    mes2=None
    impagos=[]
    impagos1=[]
    impagos2=[]
    impagos3=[]
    entrada=None
    cuota_inicio=None
    
    
    cursor = conec_sql.connection().cursor()
    with conec_sql.connection().cursor() as cursor:
            cursor.execute(
                "select MAX(month (fecha))from Recibo_Inquilino Where id_Inquilino=(?)",
                (id,),
            )
            
            entrada = cursor.fetchone()
            entrada=entrada[0] 
        
    cursor1 = conec_sql.connection().cursor()
    with conec_sql.connection().cursor() as cursor1:   
            cursor1.execute(
                "SELECT month(Fecha_Inicio) FROM Contratos1 WHERE id_inquilinos=(?)",
                (id,)
            )
            if cuota_inicio is None:
               cuota_inicio=cursor1.fetchone()
               cuota_inicio1=cuota_inicio[0]
               
            
               
            if entrada is None:
                  entrada=cuota_inicio1+1
               
            else:
                entrada = entrada +1
                
               
               
    salida= datetime.datetime.now().strftime("%m")
    salida=int(salida)
    print(entrada,salida,cuota_inicio1) 
    
    mes1=["enero", "febrero","marzo","abril","mayo","junio",
          "julio","agosto","septiembre","octubre","noviembre",
          "diciembre",]
    mes2=list(range(1,13))
    
    mes= dict(zip(mes2,mes1))
    mes=dict(mes)
    
    if entrada is None:
        entrada=cuota_inicio1
        print(entrada)
    
    if entrada == salida:
        impagos=entrada
        impagos3.append(impagos)
    elif entrada < salida and salida <=12:
        impagos1=[i for i in range(1,salida+1)]
        impagos3.append(impagos1)
    elif entrada > salida:
        impagos2.extend([i for i in range(entrada,13)])
        impagos2.extend([i for i in range(1,salida+1)])
        impagos3.extend(impagos2)
    print(impagos,"-",impagos1,"-",impagos2,"-",impagos3)   
    
   
    dic_impago= list(map(mes.get,impagos3))
    
       
    j=functools.reduce(lambda sub, ele: sub * 1 + " - " + ele, dic_impago)
         
    return j
   