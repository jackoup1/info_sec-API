from flask import Blueprint, request, jsonify
from models import db
from models.product import Product
from utils.security import verify_token

product_bp = Blueprint('product', __name__)

@product_bp.route('/products', methods=['POST'])
@verify_token
def add_product():
    data = request.json
    if not data or 'pname' not in data or 'price' not in data or 'stock' not in data:
        return jsonify({'error': 'Missing fields'}), 400

    new_product = Product(
        pname=data['pname'],
        description=data.get('description', ''),
        price=data['price'],
        stock=data['stock']
    )

    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product added successfully'}), 201

@product_bp.route('/products', methods=['GET'])
@verify_token
def get_products():
    products = Product.query.all()
    return jsonify([{
        'pid': p.pid, 'pname': p.pname, 'description': p.description,
        'price': float(p.price), 'stock': p.stock, 'created_at': p.created_at
    } for p in products])
