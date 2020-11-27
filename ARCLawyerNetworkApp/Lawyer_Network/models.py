from ARCLawyerNetworkApp import db


class lawfirms(db.Model):
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
