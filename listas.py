from numpy import iterable
import conec_sql


def lista_propietarios():
    cursor = conec_sql.connection().cursor
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT id_propietarios,concat(apellido,' ',nombre) FROM propietarios order by apellido "
        )
        propietarios = cursor.fetchall()
        print(propietarios)
        return propietarios


def lista_propietarios_por_propiedad(id):
    cursor = conec_sql.connection().cursor
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "select prop.id_propietarios, concat(apellido, ' ', nombre) as nombre\
            from propietarios  as prop inner join propiedades as P on\
            P.propietarios= prop.id_propietarios where P.id_propiedades=(?)",
            (id,),
        )

        propietarios = cursor.fetchall()

        return propietarios


def lista_propiedades():
    cursor = conec_sql.connection().cursor()
    propiedades = None
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT id_propiedades, direccion FROM propiedades_1 order by direccion asc"
        )

        propiedades = cursor.fetchall()
        print(propiedades)

        return propiedades


def lista_propiedades_propietario():
    cursor = conec_sql.connection().cursor()
    propiedades1 = None
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT contrato.id_contratos,prop.direccion FROM contratos1 as contrato\
            INNER join propiedades as prop on prop.id_propiedades=contrato.id_Propiedades\
            order by prop.Dirección"
        )

        propiedades1 = cursor.fetchall()
        print(propiedades1)
        return propiedades1


def lista_propiedades_por_propietario(id):
    cursor = conec_sql.connection().cursor()
    propiedad = None
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT id_propiedades,direccion FROM propiedades_1 WHERE propietario=(%s)",
            (id),
        )

        propiedad = cursor.fetchall()

        return propiedad


def lista_propiedades_por_propiedad(id):
    cursor = conec_sql.connection().cursor()
    propiedad = None
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT id_propiedades,direccion FROM propiedades_1 WHERE id_propiedades=(%s)",
            (id),
        )

        propiedad = cursor.fetchall()

        return propiedad
    
def lista_propiedades_por_nombre_propiedad(id):
    cursor = conec_sql.connection().cursor()
    propiedad = None
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT im.int_impuestos, pro.direccion, im.abl, im.aysa, im.exp_comunes, im.exp_extraordinarias, im.seguro, im.fecha FROM impuestos as im INNER join propiedades_1 as pro on im.id_propiedades=pro.id_propiedades WHERE pro.direccion like '(%s)';",
            ("%" + str(propiedad) + "%"),
        )

        propiedad = cursor.fetchall()

        return propiedad 


def lista_inquilinos():
    cursor = conec_sql.connection().cursor()
    inquilinos = None
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT id_inquilinos, concat(apellido,' ',nombre) FROM inquilinos order by apellido asc"
        )
        inquilinos = cursor.fetchall()

        return inquilinos


def lista_inquilinos_recibo_RecInq(id):
    cursor = conec_sql.connection().cursor()
    inquilinos1 = None
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT re.id_Inquilino, concat(inq.Apellido,' ',inq.Nombre) as inquilino FROM Recibo_Inquilino\
            as re inner join Inquilinos as inq on inq.id_Inquilinos=re.id_Inquilino where inq.Apellido like (?) \
            order by inq.Apellido asc",
            (("%" + str(id) + "%")),
        )
        inquilinos1 = cursor.fetchall()

        return inquilinos1


def lista_inquilinos_contratos():
    cursor = conec_sql.connection().cursor()
    inquilinos = None
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT con.id_Inquilinos, concat(inq.Apellido,' ',inq.Nombre) FROM Contratos1 as con inner\
                join Inquilinos as inq on inq.id_Inquilinos=con.id_Inquilinos order by Apellido asc"
        )
        inquilinos = cursor.fetchall()

        return inquilinos


def lista_inquilinos1(id):
    conec_sql.connection().cursor()
    inquilinos = None
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT id_inquilinos, concat(apellido,' ',nombre) FROM inquilinos where id_inquilinos= (?)",
            (id),
        )

        inquilinos = cursor.fetchall()

        return inquilinos


def lista_buscar_propietarios():
    cursor = conec_sql.connection().cursor()
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT id_propietarios,concat(nombre,' ',apellido) as propietario FROM propietarios where apellido like (%s)",
            ("%" + str(id) + "%"),
        ),

        propietario = cursor.fetchall()
        propietarios = []
        columnNames = [column[0] for column in cursor.description]
        for record in propietario:
            propietarios.append(dict(zip(columnNames, record)))

        return propietarios
