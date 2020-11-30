from ARCLawyerNetworkApp import db,app
from ARCLawyerNetworkApp.Lawyer_Network.models import Lawfirms, States, serves
#import numpy as np 
import pandas as pd 

#my_Lawfirms = Lawfirms('el paso law2', 'texas', 'www.law.com', 'deportation defense', 'law@law.com', 'law.com/contact', 6105554455, 554433343, ' 101 texas drace, texas')
#db.session.add(my_Lawfirms)
#db.session.commit()

#this function parses the states columns and makes association between each state and the lawfirm
def state_association (input,input2):
	stateslist = []
	stateslist1 = input.split(",")#splits states into a list by comma
	for item in stateslist1:
		stateslist.append(item.strip())
	#print(stateslist)

	currentfirm = Lawfirms.query.filter_by(lawFirmName= input2).first()#retriving current lawfirm record from search
	for eachstate in stateslist:
		currentstate = States.query.filter_by(states= eachstate).first()#searches states table for each state in list
		if currentstate != None:
			currentstate.statesServed.append(currentfirm)
	db.session.commit()

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
	genPhone = df.iloc[index]["General Phone"]
	phone = df.iloc[index]["Phone 1"]
	address = df.iloc[index]["Address 1"]
	my_Lawfirms = Lawfirms(lawfirmname,state, website,specialities,email, contactLink,genPhone, phone, address)
	db.session.add(my_Lawfirms)
	db.session.commit()
	state_association(state,lawfirmname)

