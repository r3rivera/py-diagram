import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

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

Login_Mgr = LoginManager()
Login_Mgr.init_app(app)

## Route the user to the login page (See login/views.py)
Login_Mgr.login_view = 'auth.user_login'


## Needed after DB
from myproject.puppies.views import puppies_blueprint
from myproject.owners.views import owners_blueprint
from myproject.login.views import login_blueprint
from myproject.secured.views import secure_blueprint

app.register_blueprint(login_blueprint, url_prefix='/auth')
app.register_blueprint(owners_blueprint, url_prefix='/owners')
app.register_blueprint(puppies_blueprint, url_prefix='/puppies')
app.register_blueprint(secure_blueprint, url_prefix='/secure')