from flask import Flask 

app = Flask(__name__)


from ACRLawyerNetworkApp.Users.views import Users_app
from ACRLawyerNetworkApp.Lawyer_Network.views import Lawyer_Network_app

app.register_blueprint(Users_app)
app.register_blueprint(Lawyer_Network_app)