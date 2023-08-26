from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, logout_user

secure_blueprint = Blueprint('secure', __name__, template_folder='templates')

@secure_blueprint.route('/admin',methods=['GET','POST'])
@login_required
def admin_panel():
    header_msg = 'Welcome to the admin panel'
    return render_template('admin_panel.html', header_msg=header_msg)


@secure_blueprint.route('/logout',methods=['GET','POST'])
@login_required
def admin_logout():
    logout_user()
    flash("You are out!!")
    return redirect(url_for('index'))
    
