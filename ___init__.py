from flask import Flask 

app = Flask(__name__)


from ARCLawyerNetworkApp.Users.views import Users_app
from ARCLawyerNetworkApp.Lawyer_Network.views import Lawyer_Network_app

app.register_blueprint(Users_app)
app.register_blueprint(Lawyer_Network_app)