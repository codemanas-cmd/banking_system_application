from flask import Blueprint
from controllers.transaction_controller import show_transactions

transaction_bp = Blueprint('transaction', __name__)

transaction_bp.route('/show', methods=['GET'])(show_transactions)
