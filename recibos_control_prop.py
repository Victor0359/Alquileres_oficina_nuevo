import conec_sql
import json
import datetime
import recibos_control
import os
import itertools

def recibo_del_mes(id):

    with conec_sql.connection().cursor() as cursor3:
        cursor3.execute ("select id_recibo_propietario from Recibo_propietario where id_propiedad=(?) and\
                          fecha between fecha and Getdate()", (id,))
        
        recibo_del_mes= cursor3.fetchone()   
        
        
    return recibo_del_mes

def get_recibo_propietario(id):
   
    with conec_sql.connection().cursor() as cursor:
        cursor.execute ("select re.id_propiedad, max(re.num_recibo)+1, concat(prop.Apellido,' ', prop.Nombre) as propietario, pro.Dirección,mes_contrato,meses_adeudados, Mensualidad='0', abl='0',aysa='0',exp_extraor='0', seguros='0', varios,honorarios='0',monto_mensualidad from Recibo_propietario as re inner join Propiedades as Pro on pro.id_propiedades=re.id_propiedad inner join Propietarios as prop on prop.id_propietario = re.id_propietario where id_propiedad= (?) and re.fecha between (select top(1) max(fecha) from Recibo_propietario where id_propiedad=(?)  group by id_recibo_propietario,  fecha order by fecha desc) and  getdate() group by re.id_propiedad, re.num_recibo, prop.Apellido,prop.Nombre,pro.Dirección,mes_contrato, meses_adeudados,varios,monto_mensualidad", (id,id,))
        
        ultimo_recibo= cursor.fetchall()
        

    suma4=['id_propiedad', 'numRecibo','apellido', 'direccion', 'cuotameses','mes_de_ontrato', 'meses', 'abl', 'aysa','exp_ext','seguros','varios','honorarios','monto_mensualidad']  

    suma3=dict(zip(suma4,ultimo_recibo[0]))
    
    return suma3

def exp_extraordinarias_rec_prop(id):
    exp_ext=None
    cursor= conec_sql.connection().cursor()
    with conec_sql.connection().cursor() as cursor:
        cursor.execute ("select sum (isnull(imp.exp_extraordinarias,0)) as exp from Impuestos as imp inner\
                       join Recibo_Inquilino as rec on rec.id_propiedad = imp.Id_Propiedades where\
                imp.fecha <= (select max(fecha) from Recibo_Inquilino Where id_propiedad=(?)) and imp.Id_Propiedades=(?)",
                        (id,id,),)
        exp_ext=cursor.fetchone()
        exp_ext=[int(i) for i in exp_ext]
        if exp_ext[0] is None:
            exp_ext[0]=0
       
    return exp_ext[0]

def suma_pagos_rec_inq(id):
    num_recibo=None
    exp_ext=None
    suma2= []
    suma=None
    cursor= conec_sql.connection().cursor()
    with conec_sql.connection().cursor() as cursor:
        cursor.execute ("select concat(Inq.Nombre,' ', Inq.Apellido) as nombre, pr.Dirección as\
            dirección, re.mes_contrat,sum(re.Meses_Adeudados) as meses, sum(re.abl)as abl,sum(re.aysa) as aysa,\
            sum(re.seguros)as seguros, con.honorarios as honorarios from Recibo_Inquilino as re inner join\
            inquilinos as Inq on Inq.id_Inquilinos=re.id_Inquilino inner join\
            Propiedades as pr on pr.Id_Propiedades = re.id_propiedad  inner join\
            contratos1 as con on con.id_Propiedades=re.id_propiedad where re.id_propiedad=(?)\
            and re.fecha between (select max(fecha) from Recibo_Inquilino Where  id_propiedad= (?)) and\
            (select isnull(max(fecha),getdate()) from Recibo_propietario Where  id_propiedad=(?)) group by\
             Inq.Apellido , Inq.Nombre, pr.Dirección, con.honorarios, re.mes_contrat"
,(id,id,id,),)
        suma=cursor.fetchall()
       
        
    cursor1= conec_sql.connection().cursor()
    with conec_sql.connection().cursor() as cursor1:
            cursor1.execute ("select concat(Inq.Nombre,' ', Inq.Apellido) as nombre, pr.Dirección as\
            dirección, re.mes_contrat,re.str_mes,sum(re.Meses_Adeudados) as meses, sum(re.abl)as abl,sum(re.aysa) as aysa,\
            sum(re.seguros)as seguros, con.honorarios as honorarios,sum(re.pago) from Recibo_Inquilino as re inner join\
            inquilinos as Inq on Inq.id_Inquilinos=re.id_Inquilino inner join\
            Propiedades as pr on pr.Id_Propiedades = re.id_propiedad  inner join\
            contratos1 as con on con.id_Propiedades=re.id_propiedad where re.id_propiedad=(?) \
            and re.fecha between (select max(fecha) from Recibo_Inquilino Where  id_propiedad= (?)) and \
            getdate() group by\
             Inq.Apellido , Inq.Nombre, pr.Dirección, re.str_mes,con.honorarios, re.mes_contrat",(id,id,),)
            suma1=cursor1.fetchall()
            suma2=[i for i in suma1[0]]
         
    cursor2= conec_sql.connection().cursor()
    
    with conec_sql.connection().cursor() as cursor2:
            cursor2.execute ("select max(num_recibo)+1 from Recibo_propietario")   
            num_recibo= cursor2.fetchone()     

    
    suma3=['apellido', 'direccion', 'cuotameses','mes_de_ontrato', 'meses', 'abl', 'aysa','seguros', 'honorarios','pago']   
    
    suma_de_valores1= dict(zip(suma3,suma2))
  
    
    fecha = datetime.datetime.now()
    fecha1=recibos_control.formato_fecha(fecha)
   
     
    suma_de_valores1['numRecibo']= num_recibo[0]
    suma_de_valores1['exp_ext']= exp_extraordinarias_rec_prop(id)
    suma_de_valores1['fecha1']= fecha1
    
    
    
    return suma_de_valores1


def saldo_anterior_mensualiadad(id):
       
        cursor= conec_sql.connection().cursor()
        with conec_sql.connection().cursor() as cursor:
            cursor.execute("select top(1) monto_mensualidad from Saldo_propietario where id_propiedad=(?)\
                           group by monto_mensualidad, id_saldo_prop order by id_saldo_Prop",(id),)
            saldo_anterior = cursor.fetchone()
            
            if saldo_anterior == None:
                saldo_anterior = 0

            #saldo_anterior1= itertools.chain(*saldo_anterior)
           
           
          
            return saldo_anterior

          
def Num_recibo_prop():
    try:
        cursor= conec_sql.connection().cursor()
        with conec_sql.connection().cursor() as cursor:
            cursor.execute("SELECT max(num_Recibo)+1 FROM Recibo_Propietario")
            numero = cursor.fetchone()
            while numero != None:
                numero[0]
                recibo = int(numero[0]) + 1
                return recibo
    except TypeError:
        print("Hay un error")
    except IndexError:
        print("error en la indexacion")  
        


def honorarios(id):
    
    cursor= conec_sql.connection().cursor()
    with conec_sql.connection().cursor() as cursor:
        cursor.execute ("select top(1) honorarios from Contratos1\
            where id_Propiedades=(?) order by Fecha_Inicio desc",
                        (id,),)
        honorarios=cursor.fetchone()
        
    return honorarios

def id_propietario(id):
    cursor= conec_sql.connection().cursor()
    with conec_sql.connection().cursor() as cursor:
        cursor.execute ("select propietario from Propiedades where id_Propiedades=(?)",
                        (id),)
        id_prop= list(cursor.fetchone())
    return id_prop

def guardar_rec_prop(guardar):
    cursor= conec_sql.connection().cursor()
    with conec_sql.connection().cursor() as cursor:
        cursor.execute ("insert into  Recibo_propietario (num_recibo,id_propietario,\
                        id_propiedad,fecha,mes_contrato,meses_adeudados,Mensualidad,abl,aysa, exp_extraor,seguros,\
                        varios, monto_mensualidad,honorarios,total,pago) values ((?),(?),(?),(?),\
                        (?),(?),(?),(?),(?),(?),(?),(?),(?),(?),(?),(?))",(guardar),)
       
        cursor.commit()

def ver_recibo_propietario(id):
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT * FROM Recibo_propietario WHERE id_Propietario=(?)",
            (id,),
        )
       
        propiedad = cursor.fetchall()
        return propiedad
    
def escrito_prop(ids):
    
    with conec_sql.connection().cursor() as cursor:
        cursor.execute (
            "SELECT top(5)rec.id_recibo_propietario, rec.num_recibo, concat(propin.Apellido,' ',propin.Nombre)\
                ,prop.Dirección,prop.localidad,rec.fecha,rec.mes_contrato,rec.meses_adeudados,rec.Mensualidad,\
                rec.abl,rec.aysa,rec.exp_extraor, rec.seguros,rec.varios,rec.monto_mensualidad,rec.honorarios,\
                 rec.total, rec.pago from Recibo_Propietario as rec Inner join Propiedades as prop on prop.id_propiedades =rec.id_propiedad inner Join Propietarios as propin on propin.id_Propietario=rec.id_propietario where rec.id_recibo_propietario=(?) order by rec.id_Recibo_propietario",
                 (ids,), )
         
        recibo= cursor.fetchall()
       
        
        return recibo
    
