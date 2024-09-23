from app.models import db

class HealthRecord(db.Model):
    """Model for storing health records of family members."""
    __tablename__ = 'health_records'

    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('family_members.id'), nullable=False)
    condition = db.Column(db.String(100), nullable=False)
    date_diagnosed = db.Column(db.Date, nullable=False)
    treatment = db.Column(db.String(255), nullable=True)
    risk_factor = db.Column(db.String(255), nullable=True)

    def serialize(self):
        """Serializes the health record data to JSON format."""
        return {
            'id': self.id,
            'member_id': self.member_id,
            'condition': self.condition,
            'date_diagnosed': self.date_diagnosed.strftime('%Y-%m-%d'),
            'treatment': self.treatment,
            'risk_factor': self.risk_factor
        }
