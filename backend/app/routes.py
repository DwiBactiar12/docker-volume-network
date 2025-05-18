from flask import Blueprint, request, jsonify
from .models import Item
from .db import db

routes = Blueprint("routes", __name__)

@routes.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    item = Item(name=data['name'])
    db.session.add(item)
    db.session.commit()
    return jsonify({'id': item.id, 'name': item.name}), 201

@routes.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([{'id': item.id, 'name': item.name} for item in items])

@routes.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    item = Item.query.get_or_404(item_id)
    item.name = data['name']
    db.session.commit()
    return jsonify({'id': item.id, 'name': item.name})

@routes.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Item deleted'})
