from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
from flask_wtf import FlaskForm
from wtforms import (StringField,SubmitField,PasswordField,validators)
from wtforms.validators import DataRequired,Email,EqualTo
from ARCLawyerNetworkApp.Lawyer_Network.models import Lawfirms

class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Log In')

'''	#def validate(self): #this is the method that validates the form
			rv = FlaskForm.validate(self) #checks if the data was input
			if not rv:
				return False #validation didnt pass 

	        #check if the email entered is actually in database
			user = Lawfirms.query.filter_by(accountEmail=self.email.data).first()

			if user: #this will be false if the above query returned nothing
				return True
	            #if it is true this code will run
				if not check_password_hash(user.password, self.password.data): #comparing databse password with form password
					self.password.errors.append("Incorrect email or password")
					return False

				return True
			else:
				self.password.errors.append("Incorrect email or password")
				return False	'''
