from flask import Flask, Blueprint, render_template

Lawyer_Network_app = Blueprint('Lawyer_Network', __name__)

@Lawyer_Network_app.route('/')
def index():
	return render_template('home.html')
@Lawyer_Network_app.route('/about')
def about():
	return render_template('about.html')
#creates endpoint for the About webpage 

@Lawyer_Network_app.route('/directory')
def directory():
	return render_template('directory.html')
#creates endpoint for the directory webpage 
@Lawyer_Network_app.route('/lawyer-profile')
def fpProfile():
	return render_template('lawyer-profile.html')

