from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    name = StringField(
        'User name',
        validators=[DataRequired()]
    )
    surname = StringField(
        'User surname',
        validators=[DataRequired()]
    )
    username = StringField(
        'User username',
        validators=[DataRequired()]
    )
    mail = StringField(
        'User mail',
        validators=[DataRequired()]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired()]
    )
    submit = SubmitField('Log in')