from flask import Blueprint, render_template, redirect, url_for, flash, abort, request
from flask_login import login_user, login_required, logout_user
from myproject import DB
from myproject.models import UserCredential 
from myproject.login.forms import LoginForm, RegistrationForm


login_blueprint = Blueprint('auth', __name__, template_folder='templates')

@login_blueprint.route('/login',methods=['GET','POST'])
def user_login():
    '''
    Login User
    '''
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = UserCredential.query.filter_by(email = login_form.email.data).first()
        print(type(user))
        if user.is_valid_password(login_form.password.data) and user is not None:
            login_user(user)
            flash('Login is successful!')
            
            next = request.args.get('next')
            
            if next is None or not next[0]=='/':
                next =  url_for('secure.admin_panel')
            return redirect(next)
        
    
    return render_template('login.html', form=login_form)


@login_blueprint.route('/register',methods=['GET','POST'])
def user_register():
    '''
    Register User
    '''
    reguser_form = RegistrationForm()
    if reguser_form.validate_on_submit():
        user = UserCredential(email = reguser_form.email.data, 
                              username=reguser_form.username.data, 
                              password=reguser_form.password.data)
        DB.session.add(user)
        DB.session.commit()
        print('User is registered!')
        flash('User is registered!')
        return redirect(url_for('auth.user_login'))
    
    return render_template('register.html', form=reguser_form)
    