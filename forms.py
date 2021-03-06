from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    ss = StringField()
    username = StringField('Username',
                                  validators=[DataRequired(), Length(min=3, max=14)])
    email = StringField('Email',
                               validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                                    validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    keep_login = BooleanField('Remember me')
    submit = SubmitField('Login')
