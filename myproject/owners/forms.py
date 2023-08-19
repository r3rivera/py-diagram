from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    
    name = StringField('Name of Puppy: ')
    submit = SubmitField('Submit Puppy')

class DelForm(FlaskForm):
    id = IntegerField('ID of Puppy: ')
    submit = SubmitField('Remove Puppy')