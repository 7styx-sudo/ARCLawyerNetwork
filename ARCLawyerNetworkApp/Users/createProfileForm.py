from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, validators, RadioField

class AddLawyer(FlaskForm):
 
	lawfirm = StringField(u'Law Firm Name:',[validators.required()] )
	states = StringField(u'What states are you certified by the Bar to serve in?',[validators.required()])
	website = StringField(u"Law Firm's Website",[validators.required()])
	specialities = StringField(u"What are your firm's immigration specialties?",[validators.required()])
	email = StringField(u'What email should potential clients use to contact you?',[validators.optional()])
	phone = StringField(u'What phone number should potential clients use to contact you?',[validators.required()])
	address = StringField(u"Please list your firm's full main address.", [validators.required()])
	probono = RadioField(u"Will your firm offer pro-bono or low-bono services?", [validators.required()])
	accountEmail = StringField(u"Please list the email you would like to be associated with this profile",[validators.required()])
	password = StringField(u'Password:', [validators.required()])
	confirmPassword = StringField(u'Confirm Password:', [validators.required()])
	notes = StringField(u"Is there anything else you would like potential clients to know?", [validators.optional()])
	submit = SubmitField('Sign Up')
