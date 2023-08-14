from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField, DateTimeField, RadioField, 
                     SelectField, TextAreaField)
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key_for_csrf_mitigation'

class InfoForm(FlaskForm):
    breed = StringField('What Breed are ')
    neutered = BooleanField('Have the dog been neutered? ')
    mood = RadioField("What is dog's mood: ", choices=[('mood_one', 'Scared'), ('mood_two', 'Excited')])
    food_choices = SelectField('Favorite Food: ', choices=[('chicken', 'Chicken Food'), ('beef', 'Beef Food'),('tuna', 'Tuna Food')])
    submitBtn = SubmitField('Submit')    


@app.errorhandler(404)
def page_not_found(e):
    '''
    Error not found page 
    '''
    return render_template("error404.html")

@app.route('/', methods=['GET', 'POST'])
def main_func():
    '''
    Breed Form Page 
    '''
    infoForm = InfoForm()
    if infoForm.validate_on_submit():
        flash('Flashing')
                
        session['breed'] = infoForm.breed.data
        session['neutered'] = infoForm.neutered.data 
        session['mood'] = infoForm.mood.data
        session['food'] = infoForm.food_choices.data

        return redirect(url_for('breed_response'))
    return render_template("main.html", infoForm=infoForm)
    
@app.route('/breed')
def breed_response():
    '''
    Breed Response
    '''
    return render_template("main_response.html")

if __name__ == '__main__':
    app.run(debug=True)