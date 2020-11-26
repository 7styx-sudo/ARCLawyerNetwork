from flask import Flask, render_template

@ARCnetwork_app.route('/')
def index():
	return render_template("home.html')

@ARCnetwork_app.route('/about')
def about():
	return render_template("about.html')

@ARCnetwork_app.route('/')
def index():
	return render_template("home.html')
