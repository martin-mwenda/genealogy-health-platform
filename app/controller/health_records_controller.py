from flask import request, jsonify
from app.models.health_record import HealthRecord
from app.models import db
from app.controllers.auth_controller import require_auth

@require_auth
def get_health_records(user_id):
    """Retrieves health records for a user and their family members."""
    health_records = HealthRecord.query.filter_by(user_id=user_id).all()
    return jsonify([record.serialize() for record in health_records]), 200

@require_auth
def post_health_record(user_id):
    """Adds or updates health records for a user."""
    data = request.json
    new_record = HealthRecord(
        member_id=data['member_id'],
        condition=data['condition'],
        date_diagnosed=data['date_diagnosed'],
        treatment=data['treatment'],
        risk_factor=data['risk_factor']
    )

    db.session.add(new_record)
    db.session.commit()
    return jsonify({'message': 'Health record added successfully'}), 201
