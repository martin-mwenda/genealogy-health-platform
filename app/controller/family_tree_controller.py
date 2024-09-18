from flask import request, jsonify
from app.models.family_member import FamilyMember
from app.models import db

def get_family_tree():
    """Fetches the family tree for a user by unique ID."""
    user_id = request.args.get('user_id')
    family_members = FamilyMember.query.filter_by(user_id=user_id).all()
    return jsonify([member.serialize() for member in family_members]), 200

def post_family_tree():
    """Adds or updates family tree data for a user."""
    data = request.json
    user_id = data['user_id']
    family_data = data['family_data']

    for member in family_data:
        new_member = FamilyMember(**member, user_id=user_id)
        db.session.add(new_member)

    db.session.commit()
    return jsonify({'message': 'Family tree updated successfully'}), 201

