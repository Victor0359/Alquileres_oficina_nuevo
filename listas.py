from numpy import iterable
import conec_sql


def lista_propietarios():
    cursor = conec_sql.connection().cursor
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT id_Propietario,concat(Nombre,' ',Apellido) FROM Propietarios order by Apellido ASC;"
        )
        propietarios = cursor.fetchall()

        return propietarios


def lista_propietarios_por_propiedad(id):
    cursor = conec_sql.connection().cursor
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "select prop.Id_Propietario, concat(Apellido, ' ', Nombre) as nombre\
            from Propietarios  as prop inner join Propiedades as P on\
            P.propietario= prop.Id_Propietario where P.Id_Propiedades=(?)",
            (id,),
        )

        propietarios = cursor.fetchall()

        return propietarios


def lista_propiedades():
    cursor = conec_sql.connection().cursor()
    propiedades = None
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT id_propiedades, Dirección FROM Propiedades order by Dirección asc"
        )

        propiedades = cursor.fetchall()

        return propiedades


def lista_propiedades_propietario():
    cursor = conec_sql.connection().cursor()
    propiedades1 = None
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT contrato.id_Contratos,prop.Dirección FROM contratos1 as contrato\
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
            "SELECT Id_Propiedades,Dirección FROM Propiedades WHERE propietario=(?)",
            (id),
        )

        propiedad = cursor.fetchall()

        return propiedad


def lista_propiedades_por_propiedad(id):
    cursor = conec_sql.connection().cursor()
    propiedad = None
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT Id_Propiedades,Dirección FROM Propiedades WHERE id_propiedades=(?)",
            (id),
        )

        propiedad = cursor.fetchall()

        return propiedad
    
def lista_propiedades_por_nombre_propiedad(propiedad):
    cursor = conec_sql.connection().cursor()
    propiedad = None
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT Id_Propiedades,Dirección,localidad, concat(propie.Nombre, '' ,propie.Apellido)\
             as Propietario FROM Propiedades as pro inner join Propietarios as propie on propie.id_Propietario=\
             pro.propietario WHERE Dirección like('%?%')",
            (id),
        )

        propiedad = cursor.fetchall()

        return propiedad 


def lista_inquilinos():
    cursor = conec_sql.connection().cursor()
    inquilinos = None
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT id_Inquilinos, concat(Apellido,' ',Nombre) FROM Inquilinos Apellido order by Apellido asc"
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
            "SELECT id_Inquilinos, concat(Apellido,' ',Nombre) FROM Inquilinos where id_Inquilinos= (?)",
            (id),
        )

        inquilinos = cursor.fetchall()

        return inquilinos


def lista_buscar_propietarios():
    cursor = conec_sql.connection().cursor()
    with conec_sql.connection().cursor() as cursor:
        cursor.execute(
            "SELECT Id_Propietario,concat(Nombre,' ',Apellido) as propietario FROM Propietarios where Apellido like (?)",
            ("%" + str(id) + "%"),
        ),

        propietario = cursor.fetchall()
        propietarios = []
        columnNames = [column[0] for column in cursor.description]
        for record in propietario:
            propietarios.append(dict(zip(columnNames, record)))

        return propietarios
