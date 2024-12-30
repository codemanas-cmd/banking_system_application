from flask import Blueprint
from controllers.user_controller import add_user, show_users

user_bp = Blueprint('user', __name__)

user_bp.route('/add', methods=['POST'])(add_user)
user_bp.route('/show', methods=['GET'])(show_users)
