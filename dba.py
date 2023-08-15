import os
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy


#Gets the full path of this python file
basedir = os.path.abspath(os.path.dirname(__file__)) 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.app_context().push()

##########################################################

class User(db.Model):
    
    __tablename__ = 'b_user'
    
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    email = db.Column(db.Text)
    
    def __init__(self, name, email):
        self.name = name 
        self.email = email 
        
    def __repr__(self):
        return f"User_Id:{self.user_id}, Name:{self.name}, Email:{self.email}"