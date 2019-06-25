from flask import Blueprint,render_template,redirect,url_for,flash
from myproject import db
from myproject.models import Owner
from myproject.owners.forms import AddOwner

owners_blueprints=Blueprint('owners',__name__,template_folder='templates/owners')


@owners_blueprints.route('/addowner',methods=['GET','POST'])
def add_own():
	form=AddOwner()

	if form.validate_on_submit():
		name=form.name.data
		pup_id=form.pup_id.data

		new_own=Owner(name,pup_id)
		db.session.add(new_own)
		db.session.commit()

		flash('Owner Added Successfully!')
		return redirect(url_for('puppies.list_pup'))
	return render_template('addowner.html',form=form)