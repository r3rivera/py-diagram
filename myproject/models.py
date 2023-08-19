
from myproject import DB


#####################################
###### SQL TABLE ORM ################
#####################################

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

#####################################
####### VIEW FUNCTIONS - HTML FORMS #
#####################################