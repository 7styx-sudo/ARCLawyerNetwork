
from ARCLawyerNetworkApp import db


serves = db.Table('serves',
    db.Column('lawfirm_id', db.Integer, db.ForeignKey('lawfirms.lawfirm_id')),
    db.Column('state_id', db.Integer, db.ForeignKey('states.states_id'))
    )

class Lawfirms(db.Model):
    lawfirm_id = db.Column(db.Integer, primary_key=True)
    lawFirmName = db.Column(db.Text)
    state = db.Column(db.Text)
    website = db.Column(db.Text)
    specialities = db.Column(db.Text)
    email = db.Column(db.Text)
    contactLink = db.Column(db.Text)
    genPhone = db.Column(db.Text)
    phone = db.Column(db.Text)
    address = db.Column(db.Text)
    serves = db.relationship('States', secondary=serves, backref= db.backref('statesServed', lazy = 'dynamic') )

    def __init__(self, lawFirmName, state, website, specialities, email, contactLink, genPhone, phone, address):
        self.lawFirmName = lawFirmName
        self.state = state
        self.website = website
        self.specialities = specialities
        self.email = email
        self.contactLink = contactLink
        self.genPhone = genPhone
        self.phone = phone
        self.address = address

    def __repr__(self):
        return f"The lawfirm name is {self.lawFirmName}"

class States(db.Model):
    states_id = db.Column(db.Integer, primary_key=True)
    states = db.Column(db.String(20))

    def __init__(self, states):
        self.states = states

    

    def __repr__(self):
        return f"The state is {self.states}"    