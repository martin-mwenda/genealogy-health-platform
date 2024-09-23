from app.models import db

class GeneticRiskAssessment(db.Model):
    """Model for storing genetic risk assessments."""
    __tablename__ = 'genetic_risk_assessments'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    risk_score = db.Column(db.Float, nullable=False)
    disease_type = db.Column(db.String(50), nullable=False)
    date_generated = db.Column(db.DateTime, default=db.func.current_timestamp())

    def serialize(self):
        """Serializes genetic risk assessment to JSON format."""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'risk_score': self.risk_score,
            'disease_type': self.disease_type,
            'date_generated': self.date_generated.isoformat()
        }

