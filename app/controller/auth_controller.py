from flask import request, jsonify
from app.models.user import User
from flask_bcrypt import Bcrypt
from app.models import db
import jwt
import datetime

bcrypt = Bcrypt()
SECRET_KEY = 'your_secret_key'  # Use environment variable in production

def login():
    """Handles user login and token generation."""
    data = request.json
    user = User.query.filter_by(email=data['email']).first()

    if user and bcrypt.check_password_hash(user.password, data['password']):
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, SECRET_KEY, algorithm='HS256')

        return jsonify({'token': token}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

def signup():
    """Handles new user registration."""
    data = request.json
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(
        email=data['email'],
        password=hashed_password,
        first_name=data['first_name'],
        last_name=data['last_name']
    )
    
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

def verify_token(token):
    """Decodes JWT token and returns user ID."""
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return data['user_id']
    except:
        return None

def require_auth(f):
    """Decorator to protect routes requiring authentication."""
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message': 'Token is missing!'}), 403

        user_id = verify_token(token)
        if user_id is None:
            return jsonify({'message': 'Invalid token!'}), 403

        return f(user_id, *args, **kwargs)
    return wrapper
