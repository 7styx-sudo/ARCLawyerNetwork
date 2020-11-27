
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db)

from ARCLawyerNetworkApp.Users.views import Users_app
from ARCLawyerNetworkApp.Lawyer_Network.views import Lawyer_Network_app

app.register_blueprint(Users_app)
app.register_blueprint(Lawyer_Network_app)