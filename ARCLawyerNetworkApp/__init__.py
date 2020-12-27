
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__,template_folder='./templates',static_folder='./static')


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:emily@localhost/ARCdb'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:nurudeen@localhost/ARCdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db)

from ARCLawyerNetworkApp.Users.views import Users_app
from ARCLawyerNetworkApp.Lawyer_Network.views import Lawyer_Network_app

app.register_blueprint(Users_app)
app.register_blueprint(Lawyer_Network_app)