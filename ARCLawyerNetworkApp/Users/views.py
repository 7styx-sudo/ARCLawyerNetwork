from flask import Flask, Blueprint, render_template, request, redirect, url_for
from flask import url_for
from flask import send_from_directory
from flask import request
import os
from ARCLawyerNetworkApp import db,app

Users_app = Blueprint('Users', __name__)
'''
@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

'''
@Users_app.route('/login', methods= ['GET','POST'])
def login():
	return render_template('login.html')

@Lawyer_Network_app.route('/create-profile', methods= ['GET','POST'])
def create():
	return render_template('create-profile.html')
#creates endpoint for the register webpage 

@Lawyer_Network_app.route('/review-lawyer')
def review():
	return render_template('review-lawyer.html', methods= ['GET','POST'])

