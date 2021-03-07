from flask import Flask, Blueprint, render_template, request, redirect, url_for
from ARCLawyerNetworkApp.Lawyer_Network.models import Lawfirms, States
from ARCLawyerNetworkApp import db,app

from ARCLawyerNetworkApp.Lawyer_Network.forms import Search

Lawyer_Network_app = Blueprint('Lawyer_Network', __name__)

@Lawyer_Network_app.route('/')
def index():
	return render_template('home.html')
	
@Lawyer_Network_app.route('/directory', methods= ['GET','POST'])
def directory():

	currentstate = States.query.get(3)
	if request.method == 'POST':
		lfsearch = request.form["lawfirm"]
		ssearch = request.form["state"]
		statesearch = States.query.filter_by(states= ssearch).first().statesServed

		return render_template('directory.html', statesearch=statesearch)	

	return render_template('directory.html')

@Lawyer_Network_app.route('/about')
def about():
	return render_template('about.html')
#creates endpoint for the About webpage 

@Lawyer_Network_app.route('/lawyer-profile/<lawfirm_id>', methods= ['GET','POST'])

def lprofile(lawfirm_id):
	
	currentlawfirm = Lawfirms.query.filter_by(lawfirm_id= lawfirm_id).first()
	return render_template('lawyer-profile.html', result=currentlawfirm)
	return f"{lfsearch} {ssearch}"

@Lawyer_Network_app.route('/claim-profile')
def claim():
	return render_template('claim-profile.html')


@Lawyer_Network_app.route('/results')
def results():
	return render_template('results.html')