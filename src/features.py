"""
Flask Starter Features - Production Ready Add-ons
"""

from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta
import redis

app = Flask(__name__)
CORS(app)
api = Api(app)

# Configuration
SECRET_KEY = "your-secret-key"
REDIS_URL = "redis://localhost:6379/0"

# JWT Functions
def generate_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(days=7)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

# Redis Cache
redis_client = redis.from_url(REDIS_URL, decode_responses=True)

class CacheManager:
    @staticmethod
    def get(key):
        return redis_client.get(key)
    
    @staticmethod
    def set(key, value, ttl=3600):
        redis_client.setex(key, ttl, value)
    
    @staticmethod
    def delete(key):
        redis_client.delete(key)

# API Resources
class AuthResource(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        # Mock authentication
        if username and password:
            token = generate_token(username)
            return {'token': token}, 200
        
        return {'error': 'Invalid credentials'}, 401

api.add_resource(AuthResource, '/api/auth')
