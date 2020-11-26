from flask import Flask, Blueprint, render_template

ARCnetwork_app = Blueprint('', __name__)

@ARCnetwork_app.route('/login')
def index():
	return render_template('login.html')
@ARCnetwork_app.route('/register')
def about():
	return render_template('register.html')
#creates endpoint for the register webpage 



