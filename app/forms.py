from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class AddUserForms(FlaskForm):
    name = StringField('User name', validators=[DataRequired()])
    surname = StringField('User surname', validators=[DataRequired()])
    age = IntegerField('User age', validators=[DataRequired()])
    address = TextField('User address', validators=[DataRequired()])
    submit = SubmitField("Save")
