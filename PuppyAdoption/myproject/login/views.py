from flask import Blueprint,render_template,redirect,url_for,flash,request,session
from myproject import db
from myproject.models import Login
from myproject.login.forms import LoginForm
from flask_login import login_user,login_required,logout_user
from werkzeug.security import generate_password_hash,check_password_hash
from myproject.models import Users
from flask_login import UserMixin

login_blueprints=Blueprint('login',__name__,template_folder='templates/login')


@login_blueprints.route('/LoginForm',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
    	user=Users.query.filter_by(username=form.username.data).first()

    	if user is not None and user.check_password(form.password.data):
    		login_user(user)
    		flash('Logged in Successfully!')

    		next=request.args.get('next')

    		if next==None or not next[0]=='/':
    			next =url_for ('Welcome')

    		return redirect(next)
    return render_template('login.html',form=form)
