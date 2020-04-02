from wtforms import SubmitField, BooleanField, StringField, TextField, PasswordField, validators
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length

class RegistrationForm(FlaskForm):
    username = StringField('First Name', [validators.DataRequired(), validators.Length(min=4, max=20)])
    email = StringField('Email Address', [validators.DataRequired(), validators.Email(), validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the Terms of Service and Privacy Notice (updated Jan 22, 2015)',
                              [validators.DataRequired()])
    submit = SubmitField('Submit')

