from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextField,  validators
from wtforms.validators import DataRequired, Length

class RegistrationForm(FlaskForm):
    username = StringField('Name', [validators.DataRequired(), validators.Length(min=2, max=20)])
    email = StringField('Email', [validators.DataRequired(), validators.Email(), validators.Length(min=6, max=35)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('Confirm Password', message='Passwords must match')
    ])
    confirm_password = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the Terms of Service and Privacy Notice (updated Jan 22, 2015)',
                              [validators.DataRequired()])
    submit = SubmitField('Submit')

