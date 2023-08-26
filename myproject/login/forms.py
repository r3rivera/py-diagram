from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from myproject.models import UserCredential
from wtforms import ValidationError

class LoginForm(FlaskForm):
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    submit = SubmitField('Login')
    


class RegistrationForm(FlaskForm):
    
    username = StringField('Username: ', validators=[DataRequired()])
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    password = PasswordField('Password: ', validators=[DataRequired(), EqualTo('password_confirm', message='Passwords must match!')])
    password_confirm = PasswordField('Confirm Password: ', validators=[DataRequired()])
    submit = SubmitField('Register')
    
    def check_email(self, field):
        if UserCredential.query.filter_by(email=field.data).first():
            raise ValidationError('Email already exist!')
    
    def check_username(self, field):
        if UserCredential.query.filter_by(username=field.data).first():
            raise ValidationError('Username already exist!')
        
