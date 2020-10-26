from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[DataRequired()]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired()]
    )
    submit = SubmitField('Log in')

class RegisterForm(FlaskForm):
    name = StringField(
        'Name',
        validators=[DataRequired()]
    )
    surname = StringField(
        'Surname',
        validators=[DataRequired()]
    )
    username = StringField(
        'Username',
        validators=[DataRequired(), Length(min=5, max=20)]
    )
    mail = StringField(
        'E-Mail',
        validators=[DataRequired()]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired()]
    )
    submit = SubmitField('Register')