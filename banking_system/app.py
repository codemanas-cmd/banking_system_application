from flask import Flask
from config.db import app, db
from routes.user_routes import user_bp
from routes.auth_routes import auth_bp
from routes.transaction_routes import transaction_bp

db.create_all()

app.register_blueprint(user_bp, url_prefix='/api/users')
app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(transaction_bp, url_prefix='/api/transactions')

if __name__ == '__main__':
    app.run(debug=True)
