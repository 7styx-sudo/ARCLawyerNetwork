from flask import Flask, Blueprint, render_template
from ARCLawyerNetworkApp.Lawyer_Network.models import Lawfirms
from ARCLawyerNetworkApp import db,app

Lawyer_Network_app = Blueprint('Lawyer_Network', __name__)
'''
import csv
with open ('Website-Data-Lawyers.csv','r' ) as csv_files:
	csv_reader = csv.DictReader(csv_file)
	for line in csv_DictReader:
		lawFirmName = line[1] 
		state = line[2]
		website = line[3]
		specialities = line[4]
		email = line[5]
		contactLink = link[6]
		genPhone = link[7]
		phone1 = link[8]
		address1 = link[9]'''

	
@Lawyer_Network_app.route('/')
def index():
	#allData = Lawfirms.query.all()
	#return f"{allData}"
	return render_template('home.html')
@Lawyer_Network_app.route('/about')
def about():
	return render_template('about.html')
#creates endpoint for the About webpage 

@Lawyer_Network_app.route('/directory')
def directory():
	return render_template('directory.html')#lawFirmName =lawFirmName, state = state, website = website, specialities = specialities, email = email, contactLink = contactLink, genPhone = genPhone, phone1 = phone1, address1 = address1)
#creates endpoint for the directory webpage 
@Lawyer_Network_app.route('/lawyer-profile')
def lprofile():
	return render_template('lawyer-profile.html')
@Lawyer_Network_app.route('/claim-profile')
def claim():
	return render_template('claim-profile.html')
@Lawyer_Network_app.route('/review-lawyer')
def review():
	return render_template('review-lawyer.html')