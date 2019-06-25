from flask import Blueprint,render_template,redirect,url_for,flash,request
from myproject import db
from myproject.models import Users
from myproject.register.forms import RegisterForm
from flask_login import login_user,login_required,logout_user
from werkzeug.security import generate_password_hash,check_password_hash

register_blueprints=Blueprint('register',__name__,template_folder='templates/register')


@register_blueprints.route('/RegistrationForm',methods=['GET','POST'])
def add_reg():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user=Users(username=form.username.data,email=form.email.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('login.login'))
    return render_template('register.html', form=form)