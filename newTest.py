from ARCLawyerNetworkApp import db,app

from ARCLawyerNetworkApp.Lawyer_Network.models import Lawfirms
#import numpy as np 
import pandas as pd 

#my_Lawfirms = Lawfirms('el paso law2', 'texas', 'www.law.com', 'deportation defense', 'law@law.com', 'law.com/contact', 6105554455, 554433343, ' 101 texas drace, texas')
#db.session.add(my_Lawfirms)
#db.session.commit()

df = pd.read_csv('lawyerDataNew.csv')
#print(df) 
length = list(range(0,len(df.index)))
for index in length:
	lawfirmname = df.iloc[index]["Law Firm Name"]
	state = df.iloc[index]["State Served"]
	website = df.iloc[index]["Website"]
	specialities = df.iloc[index]["Specialities"]
	email = df.iloc[index]["Consultation Email"]
	contactLink = df.iloc[index]["Contact Form Link"]
	genPhone = df.iloc[index][" General Phone Number"]
	phone = df.iloc[index]["Phone Number 1"]
	address = df.iloc[index]["Address 1"]
	my_Lawfirms = Lawfirms(lawfirmname,state, website,specialities,email, contactLink,genPhone, phone, address)
	db.session.add(my_Lawfirms)

db.session.commit()