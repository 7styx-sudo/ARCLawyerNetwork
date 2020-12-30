from flask import Flask, Blueprint, render_template, request, redirect
from flask import url_for
from flask import send_from_directory
from flask import request
import os
from ARCLawyerNetworkApp import db,app
from ARCLawyerNetworkApp.Users.createProfileForm import AddLawyer	
from werkzeug.security import generate_password_hash

Users_app = Blueprint('Users', __name__)
app.config['SECRET_KEY'] = 'mysecretkey'
'''
@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

'''
@Users_app.route('/login', methods= ['GET','POST'])
def login():
	return render_template('login.html')

@Users_app.route('/create-profile', methods= ['GET','POST'])
def create():
	form = AddLawyer()

	if form.validate_on_submit():
		lawfirmName = form.lawfirmName.data
		state = form.state.data
		website = form.website.data
		specialities = form.specialities.data
		email = form.email.data
		genPhone = form.genPhone.data
		address = form.address.data
		probono = form.probono.data
		accountEmail = form.accountEmail.data
		password = generate_password_hash(form.password.data) 
		notes = form.notes.data

		new_lawyer = Lawyer(lawfirmName, state, website, specialities, email, genPhone, address, probono, accountEmail, password, notes)   
		db.session.add(new_lawyer)
		db.session.commit()

		return redirect(url_for('lawyer-profile'))	

	return render_template('create-profile.html', form = form)
#creates endpoint for the register webpage 

@Users_app.route('/review-lawyer')
def review():
	return render_template('review-lawyer.html', methods= ['GET','POST'])

