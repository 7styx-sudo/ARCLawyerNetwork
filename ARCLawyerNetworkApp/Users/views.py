from flask import Flask, Blueprint, render_template
from flask import url_for
from flask import send_from_directory
from flask import request
from utility_functions import *
import os

Users_app = Blueprint('Users', __name__)

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@Users_app.route('/login')
def index():
	return render_template('login.html')
@Users_app.route('/register')
def about():
	return render_template('register.html')
#creates endpoint for the register webpage 



