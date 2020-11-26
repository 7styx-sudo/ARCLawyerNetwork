from flask import Flask, Blueprint, render_template

ARCnetwork_app = Blueprint('', __name__)

@ARCnetwork_app.route('/')
def index():
	return render_template("home.html')
@ARCnetwork_app.route('/about')
def about():
	return render_template('about.html')
#creates endpoint for the About webpage 

@ARCnetwork_app.route('/directory')
def directory():
	return render_template('directory.html')
#creates endpoint for the directory webpage 
@ARCnetwork_app.route('/lawyer-profile')
def fpProfile():
	return render_template('lawyer-profile.html')

