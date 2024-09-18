from app.models import db

class FamilyMember(db.Model):
    """Model for storing family member information."""
    __tablename__ = 'family_members'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    relationship = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    date_of_death = db.Column(db.Date, nullable=True)

    def serialize(self):
        """Serializes the family member data to JSON format."""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'date_of_birth': self.date_of_birth.strftime('%Y-%m-%d'),
            'relationship': self.relationship,
            'gender': self.gender,
            'date_of_death': self.date_of_death.strftime('%Y-%m-%d') if self.date_of_death else None
        }

