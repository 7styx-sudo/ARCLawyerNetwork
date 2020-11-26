from flask import Flask, Blueprint, render_template

Users_app = Blueprint('Users', __name__)

@Users_app.route('/login')
def index():
	return render_template('login.html')
@Users_app.route('/register')
def about():
	return render_template('register.html')
#creates endpoint for the register webpage 



