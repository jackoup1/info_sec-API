from flask import Blueprint, request, jsonify
from models import db
from models.user import User
from utils.security import verify_token

user_bp = Blueprint('user', __name__)

@user_bp.route('/users/<int:id>', methods=['PUT'])
@verify_token
def update_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.json
    if 'name' in data:
        user.name = data['name']
    if 'username' in data:
        user.username = data['username']

    db.session.commit()
    return jsonify({'message': 'User updated successfully'})
