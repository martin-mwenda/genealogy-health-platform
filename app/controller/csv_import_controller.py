import csv
from flask import request, jsonify
from app.models.family_member import FamilyMember
from app.models.health_record import HealthRecord
from app.models import db
from app.controllers.auth_controller import require_auth

@require_auth
def import_csv(user_id):
    """Handles CSV upload and imports family members and health records."""
    file = request.files['file']
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        if 'FamilyMember' in row:
            new_member = FamilyMember(
                user_id=user_id,
                first_name=row['FirstName'],
                last_name=row['LastName'],
                date_of_birth=row['DateOfBirth'],
                relationship=row['Relationship'],
                gender=row['Gender']
            )
            db.session.add(new_member)
        elif 'HealthRecord' in row:
            new_record = HealthRecord(
                member_id=row['MemberID'],
                condition=row['Condition'],
                date_diagnosed=row['DateDiagnosed'],
                treatment=row['Treatment'],
                risk_factor=row['RiskFactor']
            )
            db.session.add(new_record)

    db.session.commit()
    return jsonify({'message': 'Data imported successfully'}), 201
