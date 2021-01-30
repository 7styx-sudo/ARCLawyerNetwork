from flask import Flask, Blueprint, render_template, request, redirect
from flask import url_for, flash,abort,request,send_from_directory,session
import os
from ARCLawyerNetworkApp import db,app
from ARCLawyerNetworkApp.Users.createProfileForm import AddLawyer
from ARCLawyerNetworkApp.Users.LawyerLogin import LoginForm	
from werkzeug.security import generate_password_hash, check_password_hash
#from flask_login import login_user,login_required,logout_user
#from flask_login import LoginManager

Users_app = Blueprint('Users', __name__)
app.config['SECRET_KEY'] = 'mysecretkey'

#@login_manager.user_loader
#def load_user(user_id):
 #   return User.get(user_id)
'''
@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

'''
@Users_app.route('/login', methods= ['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = Lawfirms.query.filter_by(accountEmail=form.email.data).first()
		
		#if user.check_password(form.password.data) and user is not None:
		#	login_user(user)
		#	flash('Logged in successfully.')
		#	next = request.args.get('next')
		#	if next == None or not next[0]=='/':
		#		next = url_for('lawyer-profile')
		#		return redirect(next)
		session['id'] = user.lawfirm_id
		return redirect(url_for('Lawyer_Network.lawyer-profile'))
	return render_template('login.html', form=form)

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

