from ARCLawyerNetworkApp import db


class Lawfirms(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lawFirmName = db.Column(db.Text)
    state = db.Column(db.Text)
    website = db.Column(db.Text)
    specialities = db.Column(db.Text)
    email = db.Column(db.Text)
    contactLink = db.Column(db.Text)
    genPhone = db.Column(db.Integer)
    phone = db.Column(db.Integer)
    address = db.Column(db.Text)

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


serves = db.Table('serves,'
    db.column('lawyer_id', db.Integer, db.ForeignKey('lawyer.lawyer_id')),
    db.column('state_id', db.Integer, db.ForeignKey('states.states_id'))
    )

class Lawyer(db.Model):
    lawyer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    subscriptions = db.relationship('state', secondary=serves, backref= db.backref('statesServed', lazy = dynamic) )

class States(db.Model):
    states_id = db.Column(db.Integer, primary_key=True)
    states = db.Column(db.String(20))