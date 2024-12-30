from flask import request, jsonify
from models.user import User
from utils.password_utils import check_password
import jwt
import os

def login():
    data = request.get_json()
    user = User.query.filter_by(account_number=data['account_number']).first()
    if not user or not check_password(data['password'], user.password):
        return jsonify({'message': 'Invalid credentials'}), 400

    token = jwt.encode({'id': user.id}, os.getenv('JWT_SECRET'), algorithm='HS256')
    return jsonify({'message': 'Login successful', 'token': token})
