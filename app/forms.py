from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    surname = StringField("surname", validators=[DataRequired()])
    age = StringField("age", validators=[DataRequired()])
    number = StringField("number", validators=[DataRequired()])
    submit = SubmitField("Log in")