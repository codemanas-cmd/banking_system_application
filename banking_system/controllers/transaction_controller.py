from flask import request, jsonify
from models.transaction import Transaction

def show_transactions():
    data = request.get_json()
    transactions = Transaction.query.filter_by(account_number=data['account_number']).all()
    return jsonify([{
        'type': t.type,
        'amount': t.amount,
        'date': t.date
    } for t in transactions])
