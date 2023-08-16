import os 
from forms import AddForm, DelForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'app_secret'

#####################################
###### SQL DBA SECTION ##############
#####################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DB = SQLAlchemy(app)
app.app_context().push()
Migrate(app, DB)

#####################################
###### SQL TABLE ORM ################
#####################################

class Puppy(DB.Model):
    
    __tablename__ = 'puppies'
    
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.Text)
    
    def __init__(self, name):
        self.name = name 
        
    def __repr__(self):
        return f"Puppy name: {self.name}"
    

#####################################
####### VIEW FUNCTIONS - HTML FORMS #
#####################################

@app.route('/')
def index():
    welcome_message = 'Hello and Welcome!'
    return render_template('home.html',welcome_message=welcome_message)


@app.route('/add', methods=['GET', 'POST'])
def add_pup():
    
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data 
        
        #DB Model
        new_pup = Puppy(name)
        DB.session.add(new_pup)
        DB.session.commit()
        return redirect(url_for('list_pup'))
    
    return render_template('add.html', form=form)


@app.route('/list')
def list_pup():
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)


@app.route('/delete/<int:pup_id>', methods=['GET','POST'])
def del_pup(pup_id):
    #form = DelForm()
    #if form.validate_on_submit():
    pup = Puppy.query.get(pup_id)
    DB.session.delete(pup)
    DB.session.commit()

    return redirect(url_for('list_pup'))



if __name__ == '__main__':
    app.run(debug=True)
