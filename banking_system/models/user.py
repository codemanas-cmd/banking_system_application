from config.db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    account_number = db.Column(db.String(10), unique=True, nullable=False)
    dob = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    balance = db.Column(db.Float, default=2000)
    contact_number = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
