
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ARCLawyerNetworkApp import db,app
from ARCLawyerNetworkApp.Lawyer_Network.models import Lawfirms

#db = SQLAlchemy(app)

serves = db.Table('serves',
	db.column('lawyer_id', db.Integer, db.ForeignKey('lawyer.lawyer_id')),
    db.column('state_id', db.Integer, db.ForeignKey('state.state_id'))
    	)
class Lawyer(db.Model):
    lawyer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    subscriptions = db.relationship('state', secondary=serves, backref= db.backref('subscribers', lazy = dynamic) )

class States(db.Model):
    states_id = db.Column(db.Integer, primary_key=True)
    states = db.Column(db.String(20))
