from flask import Flask, render_template, request, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField, DateTimeField, RadioField, 
                     SelectField, TextAreaField)
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'key_for_csrf_mitigation'

'''
Form field
'''
class UserForm(FlaskForm):
    firstName = StringField('First Name:', validators=[DataRequired()])
    lastName = StringField("Last Name:", validators=[DataRequired()])
    submit = SubmitField('Submit')
    



@app.errorhandler(404)
def page_not_found(e):
    return render_template("error404.html")


@app.route('/')
def index():
    '''
    index page 
    '''
    return render_template("index.html", welcome_message='Welcome to my page')


@app.route('/signup',  methods=['GET', 'POST'])
def sign_up():
    '''
    Sign up Page
    '''
    
    userForm = UserForm()
    if userForm.validate_on_submit():
        userForm.firstName.data = ''
        
    return render_template("signup.html", signup_message='Please provide your details', userForm=userForm)

@app.route('/home', methods=['GET', 'POST'])
def signup_submit():
    print(request)
    first_name = request.args.get('firstname')
    last_name = request.args.get('lastname')
    
    return render_template("home.html", user = f"{last_name}, {first_name}")


@app.route('/health')
def health():
    '''
    Health page 
    '''
    return '<h1>Running</h1>'


@app.route('/user/<user_id>')
def user(user_id):
    return f"<h1>{user_id}</h1>"





if __name__ == '__main__':
    app.run(debug=True)