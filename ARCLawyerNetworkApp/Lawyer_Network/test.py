from ARCLawyerNetworkApp import db,app

from ARCLawyerNetworkApp.Lawyer_Network.models import Lawfirms

my_Lawfirms = Lawfirms('el paso law', 'texas', 'www.law.com', 'deportation defense', 'law@law.com', 'law.com/contact', 6105554455, 554433343, ' 101 texas drace, texas')

db.session.add(my_Lawfirms)
db.session.commit()
