from flask import request, jsonify
from models.user import User
from config.db import db
from utils.password_utils import hash_password
import random

def add_user():
    data = request.get_json()
    if data['balance'] < 2000:
        return jsonify({'message': 'Minimum balance should be 2000'}), 400

    account_number = str(random.randint(1000000000, 9999999999))
    hashed_password = hash_password(data['password'])

    user = User(
        name=data['name'],
        account_number=account_number,
        dob=data['dob'],
        city=data['city'],
        password=hashed_password,
        balance=data['balance'],
        contact_number=data['contact_number'],
        email=data['email'],
        address=data['address']
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User added', 'account_number': account_number}), 201

def show_users():
    users = User.query.all()
    return jsonify([{
        'name': user.name,
        'account_number': user.account_number,
        'balance': user.balance
    } for user in users])
