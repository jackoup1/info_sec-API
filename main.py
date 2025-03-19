from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db
from routes.authentication import auth_bp
from routes.user_routes import user_bp
from routes.product_routes import product_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)
app.register_blueprint(product_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True)
