from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Email,Length

class Formularios(FlaskForm):
     nombre= StringField ("Nombre",validators=[
          DataRequired(),
          Length(max=25, min=3)
     ])
     correo= StringField ("Correo", validators=[
          DataRequired(),
          Email()
     ])

     telefono= StringField ("Telefono",validators=[
          DataRequired(),
          Length(max=25, min=3)
     ])

     submit= SubmitField('enviar')

     password = PasswordField ("password",validators=[
          DataRequired(),
          Length(min=6, message='Demasiado corto')
                                          ])