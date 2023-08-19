from flask import Blueprint, render_template, redirect, url_for
from myproject import DB
from myproject.models import Puppy
from myproject.puppies.forms import AddForm, DelForm

puppies_blueprint = Blueprint('puppies', __name__, template_folder='templates/puppies')

@puppies_blueprint.route('/add', methods=['GET', 'POST'])
def add_pup():
    
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data 
        
        #DB Model
        new_pup = Puppy(name)
        DB.session.add(new_pup)
        DB.session.commit()
        return redirect(url_for('puppies.list'))
    
    return render_template('add.html', form=form)


@puppies_blueprint.route('/list')
def list():
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)


@puppies_blueprint.route('/delete/<int:pup_id>', methods=['GET','POST'])
def delete(pup_id):
    #form = DelForm()
    #if form.validate_on_submit():
    pup = Puppy.query.get(pup_id)
    DB.session.delete(pup)
    DB.session.commit()

    return redirect(url_for('puppies.list'))