from flask import Blueprint, request, jsonify
from models import db
from models.user import User
from utils.security import generate_token

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    if not data or not all(k in data for k in ['name', 'username', 'password']):
        return jsonify({'error': 'Missing fields'}), 400

    user = User.query.filter_by(username=data['username']).first()
    if user:
        return jsonify({'error': 'Username already exists'}), 409

    new_user = User(name=data['name'], username=data['username'])
    new_user.set_password(data['password'])

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()

    if user and user.check_password(data['password']):
        token = generate_token(user.username)
        return jsonify({'token': token})

    return jsonify({'error': 'Invalid credentials'}), 401
