from flask import Blueprint, render_template, redirect, url_for
from myproject import DB
from myproject.models import Owner
from myproject.owners.forms import AddForm

owners_blueprint = Blueprint('owners', __name__, template_folder='templates/owners')

@owners_blueprint.route('/add',methods=['GET','POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        
        name = form.name.data
        new_owner = Owner(name, 1)
        DB.session.add(new_owner)
        DB.session.commit()
        
        return redirect(url_for('puppies.list'))  ## BlueprintName.FuncName
    return render_template('add_owner.html', form=form)