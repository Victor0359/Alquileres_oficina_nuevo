import conec_sql

def escrito_inq(id):
    
    conec_sql.connection().cursor()
    with conec_sql.connection().cursor() as cursor:
        cursor.execute (
            "SELECT top(5)rec.id_Inquilino,rec.id_Recibo_Inquilino, concat(inq.apellido,' ',inq.nombre)  as inquilino,\
                prop.Dirección,prop.localidad,rec.mes_contrat,rec.fecha,rec.Meses_Adeudados,rec.abl,rec.aysa, rec.expensas_comunes,\
                rec.seguros,rec.varios,rec.saldo_pen_servicios,rec.saldo_mes_adeudado, rec.total,rec.pago from Recibo_Inquilino\
				as rec Inner join Propiedades as prop on prop.id_propiedades=rec.id_propiedad inner join Inquilinos as inq on inq.id_inquilinos=\
                rec.id_inquilino where inq.apellido =(?) order by rec.id_Recibo_Inquilino desc " ,
                            (id,),
            )
                    
                        
        datos_recibo=cursor.fetchall()
         
      
        return datos_recibo
    
def escrito_inq2(id):
    
    conec_sql.connection().cursor()
    with conec_sql.connection().cursor() as cursor:
        cursor.execute (
            "SELECT top(5)rec.id_Inquilino,rec.id_Recibo_Inquilino, concat(inq.apellido,' ',inq.nombre)  as inquilino,\
            prop.Dirección,prop.localidad,rec.mes_contrat,rec.fecha,rec.str_mes,rec.Meses_Adeudados,rec.abl,rec.aysa, \
            rec.expensas_comunes, rec.seguros,rec.varios,rec.saldo_pen_servicios,rec.saldo_mes_adeudado, rec.total,\
            rec.pago from Recibo_Inquilino as rec Inner join Propiedades as prop on prop.id_propiedades=rec.id_propiedad\
            inner join Inquilinos as inq on inq.id_inquilinos= rec.id_inquilino where rec.id_Recibo_Inquilino =(?) order\
             by rec.id_Recibo_Inquilino desc " ,
                            (id,),
            )
                    
                        
        datos_recibo=cursor.fetchall()
         
      
        return datos_recibo
    def recibo_prop():
        conec_sql.connection().cursor()
    with conec_sql.connection().cursor() as cursor:
        cursor.execute ("select rec.id_recibo_propietario,concat(pro.Apellido,' ',pro.Nombre) as propietario,\
        prop.Dirección, rec.num_recibo, rec.fecha, rec.mes_contrato, rec.Mensualidad, rec.abl, rec.aysa,\
        rec.exp_extraor, rec.seguros,rec.varios, rec.monto_mensualidad,rec.monto_servicios, rec.total,rec.pago\
        from Recibo_propietario as rec inner join Propiedades as prop on prop.Id_Propiedades=rec.id_propiedad\
        inner join Propietarios as pro on pro.Id_Propietario = rec.id_propietario where rec.id_propiedad=(?)",
        (id,),
        )
        recibo_prop= cursor.fetchall()
        
        return recibo_prop
         
        