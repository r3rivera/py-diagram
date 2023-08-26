
from myproject import DB, Login_Mgr
from flask_bcrypt import Bcrypt
from flask_login import UserMixin

#####################################
###### SQL TABLE ORM ################
#####################################

b_crypt = Bcrypt()


### Use to populate the current_user object
@Login_Mgr.user_loader
def load_user(user_id):
    return UserCredential.query.get(user_id)



class Puppy(DB.Model):
    
    __tablename__ = 'puppies'
    
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.Text)
    owner = DB.relationship('Owner', backref='puppy', uselist=False)
    
    def __init__(self, name):
        self.name = name 
        
    def __repr__(self):
        return f"Puppy name: {self.name}"
    
    
class Owner(DB.Model):
    __tablename__ = 'owners'
    
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.Text)
    puppy_id = DB.Column(DB.Integer, DB.ForeignKey('puppies.id'))
    
    def __init__(self, name, puppy_id):
        self.name = name 
        self.puppy_id = puppy_id
        
    def __repr__(self):
        return f"Owner name: {self.name}"


class UserCredential(DB.Model, UserMixin):
    __tablename__ = 'credentials'
    
    id = DB.Column(DB.Integer, primary_key=True)
    email = DB.Column(DB.String(64), unique=True, index=True)
    username = DB.Column(DB.String(64), unique=True, index=True)
    password_hash = DB.Column(DB.String(128))
    
    def __init__(self, email, username, password):
        self.email = email 
        self.username = username
        self.password_hash = b_crypt.generate_password_hash(password)
        
    def is_valid_password(self, password):
        return b_crypt.check_password_hash(self.password_hash, password)    
        
    def __repr__(self):
        return self.email