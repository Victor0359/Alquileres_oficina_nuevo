#!usr/bin/env python
# -*- coding: utf-8 -*-
import json
from flask import Flask, request, render_template, redirect, url_for,flash
import datetime
import propiedades_contralor
import propietarios_contralor
import inquilinos_contralor
import impuestos_control
import listas
import contratos_control
import recibos_control 
import calendar
import contralor_escritos
import numeros_a_letras 
from decimal import *
import recibos_control_prop 
from flask_restful import Resource, Api
import meses
import loguin
from formularios import Formularios
import itertools
import mariadb

app = Flask(__name__)
api=Api(app)
app.secret_key= 'Victor9865'


recibo1 = {}

@app.route("/", methods=["POST","GET"])
def log():
  
    form= Formularios()
    if request.method=="POST":
         nombre=request.form [ 'nombre' ]
         usuario=request.form['password']
         login= loguin.loguin(nombre,usuario)
         if login is None:
             succes_message=("El usuario o la contraseña no son correctos")
             flash(succes_message)
             return redirect(url_for('log'))
         else:
            
            return render_template ('principal.html')    
    else:
            return render_template("loguin.html",form=form)


@app.route("/")
def index():
    return render_template("principal.html")

@app.errorhandler(404)
def page_not_found(error):
 return render_template("pagina_no_encontrada.html"), 404

# ----------------------------   Propiedad   ------------------------------------#               

@app.route("/guardar_propiedad", methods=["POST"])
def guardar_propiedad():
    if request.method=="POST":
        direccion = request.form["txtDireccion"].title()
        localidad = request.form["txtLocalidad"].title()
        propietario = int(request.form["prop"])
        fecha = request.form["fecha"]
        #fecha_dt = datetime.datetime.strptime(fecha, "%Y-%m-%d")
        propiedades_contralor.insertar_propiedad(direccion, localidad, propietario,fecha)
        return redirect (url_for('guardar_propiedad'))
    else: 
        propietario=listas.lista_propietarios()
        
        return render_template("guardar_propiedad.html", Propietario=propietario)




@app.route("/propiedades")
def propiedades():
    direccion=request.args.get("prop")
    propiedad = propiedades_contralor.obtener_propiedad1(direccion)
  
    return render_template("propiedades.html", Propiedad=propiedad)    


@app.route("/eliminar_propiedad/<int:id>")
def eliminar_propiedad(id):
    propiedades_contralor.eliminar_propiedad(id)
    
    return redirect("/propiedades")


@app.route("/editar_propiedad/<int:id>")
def editar_propiedad(id):
    propietarios=listas.lista_propietarios()
    propiedad = propiedades_contralor.obtener_propiedad_por_id(id)
    propietarios1=itertools.chain(propietarios)
   
    return render_template("editar_propiedad.html", Propiedad=propiedad, Propietarios=propietarios1)


@app.route("/actualizar_propiedad", methods=["POST"])
def actualizar_propiedad():
    id = int(request.form["id"])
    direccion = request.form["direccion"].title()
    localidad = request.form["localidad"].title()
    propietario = int(request.form["prop"])

    propiedades_contralor.actualizar_propiedad(direccion, localidad, propietario, id)

    return redirect("/propiedades")

    # ------------------------------------------- propietarios-------------------------------------------!


@app.route("/guardar_propietario")
def guardar1():
    return render_template("guardar_propietario.html")


@app.route("/guardar_propietario", methods=["POST"])
def guardar_propietario():
    error=None
    nombre = request.form["nombre"].title()
    apellido = request.form["apellido"].title()
    dni = request.form["dni"]
    cuit = request.form["cuit"].title()
    direccion = request.form["direccion"].title()
    correo_electronico = request.form["correo_electronico"]
    telefono = request.form["telefono"]
    celular = request.form["celular"]
    
    #fecha = request.form["fecha"]
    #fecha_dt = datetime.datetime.strptime(fecha, "%Y-%m-%d")
    
   
    dni1=propietarios_contralor.propietario_por_dni(dni)
     
    if  (dni1 != None):
        flash('hay un Propietario registrado!!')
    else:
        propietarios_contralor.insertar_propietario(
        nombre,
        apellido,
        dni,
        cuit,
        direccion,
        telefono,
        celular,
        correo_electronico
       
        #fecha
        )
    return redirect(url_for('guardar_propietario', error=error))


@app.route("/propietario")
def propietario():
    apellido = request.args.get("apellido")
    propietario = propietarios_contralor.obtener_propietario(apellido)
    
    return render_template("propietarios.html", Propietario=propietario)
    

@app.route("/eliminar_propietario/<int:id>")
def eliminar_propietario(id):
   
    return redirect("/propietario")


@app.route("/editar_propietario/<int:id>")
def editar_propietario(id):
    
    propietario = propietarios_contralor.obtener_propietario_por_id(id)
  
    return render_template("editar_propietarios.html",Propietario=propietario)


@app.route("/actualizar_propietario", methods=["POST"])
def actualizar_propietario():
       
    nombre = request.form["nombre"].title()
    apellido = request.form["apellido"].title()
    dni = request.form["dni"]
    cuit = request.form["cuit"]
    domicilio = request.form["direccion"].title()
    
    te = request.form["telefono"]
    celular = request.form["celular"]
    correo_elec = request.form["correo_electronico"]
    id = int(request.form["id"])
    propietarios_contralor.actualizar_propietario(
        
       
        nombre,
        apellido,
        dni,
        cuit,
        domicilio,
        te,
        celular,
        correo_elec,
        id    
        )
   
    return redirect("/propietario")


# ---------------------------------------------------------inquilinos-----------------------------------

@app.route("/inquilinos")
def inquilinos(apellido):
     apellido=None
     apellido = request.args.get("apellido") 
     inquilinos=inquilinos_contralor.obtener_inquilino(apellido)

     return render_template("inquilinos.html", Inq=inquilinos)

@app.route("/guardar_inquilinos")
def guard():     
     return render_template("guardar_inquilino.html")

@app.route("/guardar_inquilinos", methods=["POST"])
def guardar_inquilino():
    error=None
    nombre = request.form["nombre"].title()
    apellido = request.form["apellido"].title()
    dni = request.form["dni"]
    cuit = request.form["cuit"].title()
    direccion = request.form["direccion"].title()
    correo_electronico = request.form["correo_electronico"]
    telefono = request.form["telefono"]
    celular = request.form["celular"]
    
    #fecha = request.form["fecha"]
    #fecha_dt = datetime.datetime.strptime(fecha, "%Y-%m-%d")
    
   
    dni1=inquilinos_contralor.select_inquilino_por_dni(dni)
     
    if  (dni1 != None):
        flash('hay un Inquilino registrado!!')
    else:
        inquilinos_contralor.insertar_inquilino(
        nombre,
        apellido,
        dni,
        cuit,
        direccion,
        telefono,
        celular,
        correo_electronico
       
        #fecha
        )
        return redirect (url_for("guardar_inquilino", error=error))

@app.route("/eliminar_inquilino/<int:id>")
def eliminar_inquilino(id):
   
    return redirect("/inquilinos")


@app.route("/editar_inquilino/<int:id>")
def editar_inquilino(id):
    
    inquilino = inquilinos_contralor.obtener_inquilino_por_id(id)
  
    return render_template("editar_inquilino.html",Inquilino=inquilino)


@app.route("/actualizar_inquilino", methods=["POST"])
def actualizar_inquilino():
       
    nombre = request.form["nombre"].title()
    apellido = request.form["apellido"].title()
    dni = request.form["dni"]
    cuit = request.form["cuit"]
    domicilio = request.form["direccion"].title()
    te = request.form["telefono"]
    celular = request.form["celular"]
    correo_elec = request.form["correo_electronico"]
    id = int(request.form["id"])
    inquilinos_contralor.actualizar_inquilino(        
       
        nombre,
        apellido,
        dni,
        cuit,
        domicilio,
        te,
        celular,
        correo_elec,
        id    
        )
   
    return redirect("/inquilinos")


    # -------------------------------------- impuestos------------------------------------------------
   


@app.route("/guardar_impuesto")
def guardar4():
    propiedades = listas.lista_propiedades()

    return render_template("guardar_impuestos.html", Propiedades=propiedades)


@app.route("/guardar_impuesto", methods=["POST"])
def guardar_impuesto():

    id_propiedades = int(request.form["list"])
    abl = int(request.form["abl"])
    aysa = int(request.form["aysa"])
    exp_comunes = int(request.form["exp_comunes"])
    exp_extraordinarias = int(request.form["exp_extraordinarias"])
    seguro = int(request.form["seguro"])
    fecha = request.form["fecha"]
    fecha_dt = datetime.datetime.strptime(fecha, "%Y-%m-%d")
    impuestos_control.insertar_impuestos(
        id_propiedades, abl, aysa, exp_comunes, exp_extraordinarias, seguro, fecha_dt
    )
    return redirect(url_for('guardar_impuesto'))


@app.route("/impuesto")
def impuesto():
    propiedad = request.args.get("list")
    impuesto = impuestos_control.obtener_impuesto(propiedad)
  
    return render_template(
        "impuestos.html", Impuestos=impuesto)


# --------------------------------------------------------contratos---------------------------------------------------
@app.route("/guardar_contrato")
def guardar6():
    propiedades = listas.lista_propiedades()
    propietarios = listas.lista_propietarios()
    inquilinos = listas.lista_inquilinos()
    return render_template(
        "guardar_contratos.html",
        Propiedades=propiedades,
        Propietarios=propietarios,
        Inquilinos=inquilinos,
    )


@app.route("/guardar_contrato", methods=["POST"])
def guardar_contrato():
    if request.method=="POST":
        
       id_propiedades = int(request.form["propiedades"])
       id_propietarios = int(request.form["propietarios"])
       id_inquilinos = int(request.form["inquilinos"])
       fecha = request.form["fecha"]
       fecha_inicio = datetime.datetime.strptime(fecha, "%Y-%m-%d")
       duracion_contrato= int(request.form["duracion"])
       precio_inicial = int(request.form["precio"])
       precio_6meses = int(request.form["precio6"])
       precio_12meses = int(request.form["precio12"])
       precio_18meses = int(request.form["precio18"])
       precio_24meses = int(request.form["precio24"])
       precio_30meses = int(request.form["precio30"])
       honorarios = float(request.form["honorarios"])
    contratos_control.insertar_contrato(
        id_propietarios,
        id_inquilinos,
        id_propiedades,
        fecha_inicio,
        duracion_contrato,
        precio_inicial,
        precio_6meses,
        precio_12meses,
        precio_18meses,
        precio_24meses,
        precio_30meses,
        honorarios,
    )
    return redirect("/guardar_contrato")


@app.route("/contrato")
def contrato():
    
    prop = request.args.get("list")
    contrato = list(contratos_control.obtener_contrato(prop))
    propiedades = listas.lista_propiedades_propietario()
    
    return render_template("contratos.html", Contrato=contrato, Propiedades=propiedades)


@app.route("/eliminar_contrato/<int:id>")
def eliminar_contrato(id):
    contratos_control.eliminar_contrato(id)
 
    return redirect("/contrato")


@app.route("/editar_contrato/<int:id>")
def editar_contrato(id):
    
    contratos = contratos_control.obtener_contrato_por_id(id)
   
    return render_template("editar_contratos.html", Contratos=contratos)


@app.route("/actualizar_contrato", methods=["POST"])
def actualizar_contrato():
   
        id = int(request.form["id"])
        id_propiedades = int(request.form["propiedad"])
        id_propietarios = int(request.form["propietario"])
        id_inquilinos = int(request.form["inquilino"])
        fecha = request.form["fecha"]
        fecha_inicio = datetime.datetime.strptime(fecha, "%Y-%m-%d")
        duracion_contrato= int(request.form["duracion"])
        precio_inicial = int(request.form["precio_ini"])
        precio_6meses = int(request.form["precio_6"])
        precio_12meses = int(request.form["precio_12"])
        precio_18meses = int(request.form["precio_18"])
        precio_24meses = int(request.form["precio_24"])
        precio_30meses = int(request.form["precio_30"])
        honorarios = float(request.form["honorarios"])

        contratos_control.actualizar_contrato(
        id_propietarios,
        id_inquilinos,
        id_propiedades,
        fecha_inicio,
        duracion_contrato,
        precio_inicial,
        precio_6meses,
        precio_12meses,
        precio_18meses,
        precio_24meses,
        precio_30meses,
        honorarios,
        id,
    )

        return redirect("/contrato")


# --------------------------------recibo_alquiler inquilino------------------------------------------

@app.route("/recibo_inquilinos1", methods=["POST", "GET"])
def recibo():

    if request.method == "POST":
        id = int(request.form["inquilino"])
        varios = int(request.form["varios"])
    
        return redirect(url_for("recibo_inquilino", id=id, varios=varios))
    else:
        inquilinos = listas.lista_inquilinos_contratos()
     
        return render_template("recibo_inquilinos1.html", inquilinos=inquilinos)


@app.route('/recibo_inquilino/<id>/<varios>')
def recibo_inquilino(id, varios):
    
    mensaje= recibos_control.locura(id)
    if mensaje == None:
        flash("Debes actulizar el valor del contrato")
    

    id=int(id)
    fecha = None
    saldo = None
    mensualidad1=None
    mensualidad=[]
    saldo_anterior_servicios=None
    saldo_anterior_mensualidad=None
    recibo = recibos_control.Num_recibo()
    inquilinos = listas.lista_inquilinos1(id)
    direccion= recibos_control.direccion(id)
    cuota = recibos_control.Cuotas(id)
    fecha = datetime.datetime.now()
    fecha1=recibos_control.formato_fecha(fecha)
    rango1=int(datetime.datetime.today().month)
    
    if recibos_control.locura(id) is not None:
       
        mensualidad = recibos_control.locura(id)
       
    servicios = recibos_control.Servicios(id)
    if mensualidad1 is None:
       mensualidad1 = meses.meses(id)
      
    if recibos_control.saldo_anterior(id) is not None: 
        
        saldo=recibos_control.saldo_anterior(id)
        saldo_anterior_servicios=saldo[0][0]
        saldo_anterior_mensualidad=saldo[0][1]
    
    
    total=int( int(mensualidad) + int(servicios[0]) +int(servicios[1])+ int(servicios[2])+ int(servicios[4])+
              int(saldo_anterior_servicios)+int(saldo_anterior_mensualidad) +int(varios))
    
     
        
    jrecibo1 = {
            "recibo": str(recibo),
            "meses_adeudados":str(mensualidad1),
            "mensualidad": str(mensualidad),
            "inquilinos": inquilinos[0][0],
            "direccion": direccion[0][0],
            "cuota": cuota[0],
            "fecha": datetime.datetime.now().strftime("%d/%m/%yyyy"),
            "abl": str(servicios[0]),
            "aysa": str(servicios[1]),
            "exp_comunes": str(servicios[2]),
            "seguros": str(servicios[4]),
            "varios": int(varios),
            "saldo_ant_mensualidad": str(saldo_anterior_servicios),
            "saldo_ant_servicios": str(saldo_anterior_mensualidad),
            "total": str(total),}
          
            
    with open("guardar_inq.json","w") as contenido:
      json.dump(jrecibo1,contenido)
                          
    return render_template(
              "recibo_inquilino.html",
              Mensualidad1=mensualidad1,
              Recibo=recibo,
              Inquilinos=inquilinos,
              Cuota=cuota,
              Direccion=direccion,
              Fecha=fecha1,
              Mensualidad=mensualidad,
              Servicios=servicios,
              Saldo_anterior_mensualidad=saldo_anterior_mensualidad,
              Saldo_anterior_servicios= saldo_anterior_servicios,
              Total=total,
              varios=varios,
              )
    
               


@ app.route ('/recibo_inquilino', methods=["POST"])    
def recibo_guardar():
   
            saldo_ant_mensualidad=0
            saldo_pendiente_mensualidad=0
            saldo_pendiente_servicios=0
            pago=0
            with open('guardar_inq.json', 'r') as contenido:
               datos= json.load(contenido)
               recibo= datos['recibo']
               id_inquilino=int(datos['inquilinos'])
               id_propiedad=int(datos['direccion'])
               fecha1=datos['fecha']
               fecha=datetime.datetime.strptime(fecha1, "%d/%m/%yyyy")
               mes_contrat=datos['cuota']
               str_mes=datos['meses_adeudados'] 
               Meses_Adeudados=int(datos['mensualidad'])
               abl=int(datos['abl'])
               aysa=int(datos['aysa'])
               exp_comunes=int(datos['exp_comunes'])
               seguros=int(datos['seguros'])
               varios=int(datos['varios'])
               saldo_ant_mensualidad= int(datos['saldo_ant_mensualidad'])
              # saldo_ant_servicios: int(datos['saldo_ant_servicios'])
               total=int(datos['total'])
               
            if request.method=="POST":
                  pago=int(request.form["pago"])   
           
            #if saldo_pendiente_mensualidad and saldo_pendiente_servicios is None: 
            if pago < (saldo_ant_mensualidad+Meses_Adeudados):
                     saldo_pendiente_mensualidad=(saldo_ant_mensualidad+Meses_Adeudados)-pago
                     saldo_pendiente_servicios=abl+aysa+exp_comunes+seguros+varios
            elif pago> (saldo_ant_mensualidad+Meses_Adeudados):
                     saldo_pendiente_servicios=total-pago
                     saldo_pendiente_mensualidad=0 
            
             
            
            recibos_control.guardar_recibo(recibo,id_inquilino,id_propiedad,fecha,mes_contrat,
                            str_mes,Meses_Adeudados,abl,aysa,exp_comunes,seguros,varios,total,
                            pago, saldo_pendiente_servicios, saldo_pendiente_mensualidad)           
    
            
   
            return redirect(url_for("recibo"))
# ---------------------------------------------------- escritos inquilinos --------------------------------------

@ app.route ('/ver_recibo_inquilinos')
 
def ver_recibo_inquilino(): 
     
     
       apellido = request.args.get ("apellido")
       escrito = contralor_escritos.escrito_inq(apellido)
       ids=None
       for i in escrito:
           ids=i[0]
       
                     
       return render_template ('ver_recibo_inquilino.html', Escritos=escrito, ids=ids)
       
          
        
@ app.route("/recibo_escrito/<ids>")
def recibo_escrito(ids):
    ids= int(ids)
    escritos=contralor_escritos.escrito_inq2(ids)
    letras=None
    fecha1=None
    mes1=None
    ano=None
    mes=None
    ultimo_dia=None
    anos=None
    numero=None
    formato_ultimo_dia_mes=None
   
    
    for i in escritos:
        fecha=i[6]
        fecha1=  recibos_control.formato_fecha(fecha)
        mes1= datetime.datetime.strftime(i[6],'%m')
        ano= datetime.datetime.strftime(i[6],'%y')
        mes=recibos_control.formato_fecha_mes(int(mes1))
        ultimo_dia= calendar.monthrange(int(ano),int(mes1))[1]
        anos= datetime.datetime.strftime(i[6],'%Y')
        numero = i[17]
        formato_ultimo_dia_mes= recibos_control.formato_fecha_vencimiento (i[6])
        letras= numeros_a_letras.numero_a_letras(numero)
       
    
    return render_template ("escrito_inq.html", Escrito=escritos, Letras=letras, Fecha=fecha1, Mes=mes, 
                            Ultimo_dia=ultimo_dia, Formato=formato_ultimo_dia_mes,Anos=anos)
      
# ------------------------------------- RECIBO PROPIETARIO ----------------------------------------------------- 

@app.route("/recibo_propietario", methods=["POST", "GET"])
def recibo_propietario():

    if request.method == "POST":
        id = int(request.form["propietario"])
        return redirect(url_for('recibo_propietario1', id=id))
    
    else:
        propietario = listas.lista_propietarios()
     
        return render_template('recibo_propietarios1.html', propietario=propietario)

                
@app.route ("/recibo_propietario1/<int:id>", methods=["POST", "GET"]) 
def recibo_propietario1(id):
       
       if request.method == "POST":
          id_prop = request.form["propiedad"]
          valores=request.form["varios"]
          
          return redirect(url_for('recibo1', id=id_prop, valores=valores))
       
       else:
           propiedad = listas.lista_propiedades_por_propietario(id)
     
       return render_template('recibos_propietarios2.html', propiedad=propiedad)

@app.route ("/recibo1/<id>/<valores>/", methods=["GET","POST"])    
def recibo1(id,valores):  
          
        id=id
        varios= valores
        if recibos_control_prop.recibo_del_mes(id)!=None: 
           recibo_propietario=recibos_control_prop.get_recibo_propietario(id)
           rec=recibo_propietario
           j= datetime.datetime.now()
           rec["fecha"]=recibos_control.formato_fecha(j)
           with open ('recibo_prop2.json','w') as recibo1:
                json.dump (rec,recibo1)
        
        elif recibos_control_prop.recibo_del_mes(id)==None:
         
                rec1= recibos_control_prop.saldo_anterior_mensualiadad(id)
                rec=recibos_control_prop.suma_pagos_rec_inq(id)
                honor=int(rec['honorarios'])   
                meses= int(rec['meses']) 
                honorarios= int(meses*(honor/100)) 
                j= datetime.datetime.now()
                rec["fecha"]=recibos_control.formato_fecha(j)
                rec["honorarios"]=honorarios
                rec["varios"]= varios
                rec["id_propiedad"]=id
                rec["monto_mensualidad"]= rec1
                 
                with open ('recibo_prop2.json','w') as recibo:
                   json.dump (rec,recibo)

        return render_template('recibo_propietario.html',prop=rec, varios=varios)    
        
            
@app.route("/recibo2", methods=["POST"])
def recibo2(): 
    abl1=None
    aysa1=None
    seg1=None
    
    if request.method=="POST":
        abl1=request.form.get("chekabl")
        aysa1= request.form.get("chekaysa")
        seg1=request.form.get("chekseguro")
    if abl1 is None:
        abl1=0
    if aysa1 is None:
        aysa1=0
    if seg1 is None:
        seg1=0
    
    return redirect(url_for('recibo3',abl1=abl1, aysa1=aysa1, seg1=seg1))

@app.route('/recibo2/<abl1>/<aysa1>/<seg1>')
def recibo3(abl1,aysa1,seg1):
    abl1=abl1
    aysa1= aysa1
    seg1=seg1
    abl=None
    aysa=None
    seg=0
    
    saldo=None
    
    with open('recibo_prop2.json','r') as cont:
        reci=json.load(cont)
      
   
    mensualidad = int(reci["meses"])
   
    if abl1 =='1':
          abl=reci["abl"]
       
    elif abl1 =='0':
          abl=0
         
    if aysa1 =='1':
          aysa=reci["aysa"]
       
    elif aysa1 =='0':
          aysa=0
          
    if seg1 =='1':
        seg=reci['seguros']
          
    elif seg1 =='0':
        seg=0
    
           
    hono= int(reci["honorarios"])
        
    saldo= (mensualidad - hono) + int(reci['varios'])+ int(abl) + int(aysa) + int(seg) + int(reci['exp_ext']) + reci['monto_mensualidad'] 
    
   
    
    id_prop= recibos_control_prop.id_propietario(reci['id_propiedad'])
   
    recibo={'apellido':reci['apellido'],'direccion':reci['direccion'],
            'cuotameses':reci['cuotameses'], 'mes_de_ontrato':reci['mes_de_ontrato'],'meses':reci['meses'], 'abl':
             abl, 'aysa':aysa, 'seguros':seg, 'honorarios': hono,
             'numeroRecibo':reci['numRecibo'], 'exp_ext':reci['exp_ext'],
             'fecha1':reci['fecha'],'valores':reci['varios'], 'saldo':saldo,'id_propiedad':
             reci['id_propiedad'], 'id_propietario':id_prop[0], 'saldo_mensualidad':reci['monto_mensualidad']
             }
   
    
    with open ('recibo_prop2.json','w') as rec:
        r=json.dump (recibo, rec)
    
    return render_template("recibo_propietario_final.html",registro=recibo )
          
@ app.route('/guardar_recibo_prop', methods=["POST"])
def guardar():
    pago=None
    
    if request.method=="POST":
        pago= request.form["pago"]
        with open ('recibo_prop2.json','r') as reci:
            reci= json.load(reci)
               
            if int(pago) <= (int(reci["saldo"])):
                     reci["saldo_mensualidad"]=int(reci["saldo"])-int(pago)
                     
           
            fecha1=datetime.datetime.now().isoformat()
        
        guardar_prop= {'num_recibo': int(reci['numeroRecibo']),'id_propietario':
        int(reci['id_propietario']),'id_propiedad': int(reci['id_propiedad']),
        'fecha':fecha1, 'mes_contrato': int(reci['cuotameses']),'mes_de ontrato':reci['mes_de_ontrato'],'meses': reci['meses'],
        'abl': int(reci['abl']), 'aysa':int(reci['aysa']),'exp_extraor': int(reci['exp_ext']),'seguros': int(reci['seguros']),
        'varios':int(reci['valores']), 'monto_mensual': int(reci['saldo_mensualidad']),'honorarios':int(reci['honorarios']),
        'total':int(reci['saldo']), 'pago':int(pago),
        }
        with open ('guardar_propietario.json','w') as guar:
            gu=json.dump(guardar_prop,guar)  
        
        with open('guardar_propietario.json','r') as re:
            re=json.load(re)
            
        guardar=re.values()
        guardar=list(guardar)
          
                
        g= recibos_control_prop.guardar_rec_prop(guardar)  
                
        
        
    return redirect(url_for('recibo_propietario'))  

@ app.route ('/ver_recibos_propietarios', methods=["POST","GET"])
 
def ver_recibos_propietarios(): 
    id=None
    if request.method=="POST":
         id = int(request.form.get("list"))
    
    propietarios = listas.lista_propietarios()
    
    prop=recibos_control_prop.ver_recibo_propietario(id)
    
    return render_template("recibo_propietario_ver.html", propietarios=propietarios, prop=prop)

@ app.route ('/recibo_escrito_prop/<ids>')
def recibo_escrito_prop(ids):
    ids= int(ids)
    escritos=list(recibos_control_prop.escrito_prop(ids))
    
    letras=None
    fecha1=None
    mes1=None
    ano=None
    mes=None
    ultimo_dia=None
    anos=None
    numero=None
    formato_ultimo_dia_mes=None
    flat_list= itertools.chain(*escritos)  
    
    flat_list1= list(flat_list)
    
    fecha=flat_list1[5]
    fecha1=  recibos_control.formato_fecha(fecha)
    mes1= datetime.datetime.strftime(flat_list1[5],'%m')
    ano= datetime.datetime.strftime(flat_list1[5],'%y')
    mes=recibos_control.formato_fecha_mes(int(mes1))
    ultimo_dia= calendar.monthrange(int(ano),int(mes1))[1]
    anos= datetime.datetime.strftime(flat_list1[5],'%Y')
    numero = flat_list1[17]
    formato_ultimo_dia_mes= recibos_control.formato_fecha_vencimiento (flat_list1[5])
    letras= numeros_a_letras.numero_a_letras(numero)
    #monto_mensualidad=escritos[13]
    print(flat_list1),type(escritos)
    
    return render_template ("escrito_prop.html", Escrito=flat_list1, Letras=letras, Fecha=fecha1, Mes=mes, 
                            Ultimo_dia=ultimo_dia, Formato=formato_ultimo_dia_mes,Anos=anos)
    
    
       
if __name__ == "__main__":

    app.run(host="0.0.0.0",port="80",debug=True)
