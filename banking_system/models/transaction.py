from config.db import db

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_number = db.Column(db.String(10), nullable=False)
    type = db.Column(db.String(10), nullable=False)  # credit, debit, transfer
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=db.func.current_timestamp())
