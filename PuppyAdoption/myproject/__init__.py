import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 	
from flask_migrate import Migrate,MigrateCommand
from flask_script import Command
from flask_login import LoginManager
from flask_login import UserMixin


login_manager=LoginManager()
app=Flask(__name__)

app.config['SECRET_KEY']='mysecretkey'
basedir=os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db=SQLAlchemy(app)
Migrate(app,db)

login_manager.init_app(app)
login_manager.login_view='login'

from myproject.puppies.views import puppies_blueprint
app.register_blueprint(puppies_blueprint,url_prefix='/puppies')

from myproject.owners.views import owners_blueprints
app.register_blueprint(owners_blueprints,url_prefix='/owners')

from myproject.register.views import register_blueprints
app.register_blueprint(register_blueprints,url_prefix='/register')

from myproject.login.views import login_blueprints
app.register_blueprint(login_blueprints,url_prefix='/login')
