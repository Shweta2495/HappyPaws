from myproject import app,db
from flask import render_template,redirect,request,url_for,flash
from flask_login import login_user,login_required,logout_user
from myproject.models import Users
from myproject.login.forms import LoginForm
from myproject.register.forms import RegisterForm
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin


@app.route('/')
def index():
	return render_template('home.html')

@app.route('/logout')
@login_required
def logout():
	logout_user()
	flash("You logged out!")
	return render_template('home.html')


@app.route('/Welcome')
@login_required
def Welcome():
	return render_template('home.html')

if __name__ == '__main__':
	db.create_all()
	app.run(debug=True)