from flask import Blueprint
from app.controllers import family_tree_controller, health_records_controller, genetic_risk_controller, user_controller

api = Blueprint('api', __name__)

# Family Tree Routes
api.add_url_rule('/api/family-tree', view_func=family_tree_controller.get_family_tree, methods=['GET'])
api.add_url_rule('/api/family-tree', view_func=family_tree_controller.post_family_tree, methods=['POST'])

# Health Records Routes
api.add_url_rule('/api/health-records', view_func=health_records_controller.get_health_records, methods=['GET'])
api.add_url_rule('/api/health-records', view_func=health_records_controller.post_health_record, methods=['POST'])

# Genetic Risk Routes
api.add_url_rule('/api/genetic-risk', view_func=genetic_risk_controller.get_genetic_risk, methods=['GET'])
api.add_url_rule('/api/genetic-risk', view_func=genetic_risk_controller.post_genetic_risk, methods=['POST'])

# User Routes
api.add_url_rule('/api/user', view_func=user_controller.get_user, methods=['GET'])
api.add_url_rule('/api/user', view_func=user_controller.post_user, methods=['POST'])

