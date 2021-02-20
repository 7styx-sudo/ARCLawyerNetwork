from flask import Flask, Blueprint, render_template, request, redirect, url_for
from ARCLawyerNetworkApp.Lawyer_Network.models import Lawfirms, States
from ARCLawyerNetworkApp import db,app
from flask_login import login_user,login_required,logout_user

Lawyer_Network_app = Blueprint('Lawyer_Network', __name__)

@Lawyer_Network_app.route('/')
def index():
	return render_template('home.html')
	
@Lawyer_Network_app.route('/directory', methods= ['GET','POST'])
def directory():
	#allData = Lawfirms.query.all()
	#return f"{allData}"

	#currentstate = States.query.filter_by(states= "Texas").first_or_404()
	#for x in currentstate:
		#return f"{x.states}"
	currentstate = States.query.get(3)
	#return f"{currentstate}"
	#test = currentstate.stateServed()
	#return f'{test}' 
	if request.method == 'POST':
		lfsearch = request.form["lawfirm"]
		ssearch = request.form["state"]
		#currentstate = States.query.filter_by(states= eachstate).first()
		statesearch = States.query.filter_by(states= ssearch).first().statesServed
		#statesearch = statesearch.statesServed
		#return redirect(url_for('Lawyer_Network.results', statesearch=statesearch))
		return render_template('directory.html', statesearch=statesearch)
		

	return render_template('directory.html')
@Lawyer_Network_app.route('/about')
def about():
	return render_template('about.html')
#creates endpoint for the About webpage 

@Lawyer_Network_app.route('/lawyer-profile/<lawfirm_id>', methods= ['GET','POST'])
@login_required
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