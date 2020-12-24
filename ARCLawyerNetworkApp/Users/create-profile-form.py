from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, URLField

class AddLawyer(FlaskForm):

	lawfirm = StringField('Law Firm Name:',[validators.required()] )
	states = StringField('What states are you certified by the Bar to serve in?',[validators.required()]
	website = URLField("Law Firm's Website",[validators.required()])
	specialities = StringField("What are your firm's immigration specialties?",[validators.required()])
	email = StringField('What email should potential clients use to contact you?',[validators.optional()])
	phone = StringField('What phone number should potential clients use to contact you?',[validators.required()])
	address = StringField("Please list your firm's full main address.", [validators.required()])
	probono = RadioField("Will your firm offer pro-bono or low-bono services?", [validators.required()])
	accountEmail = StringField("Please list the email you would like to be associated with this profile",[validators.required()])
	password = StringField('Password:', [validators.required()])
	confirmPassword = StringField('Confirm Password:', [validators.required()])
