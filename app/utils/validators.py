"""
Input Validators
"""
import re
from flask import request


def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validate_password(password):
    """Validate password strength"""
    if len(password) < 8:
        return False, 'Password must be at least 8 characters'
    if not re.search(r'[A-Z]', password):
        return False, 'Password must contain uppercase letter'
    if not re.search(r'[a-z]', password):
        return False, 'Password must contain lowercase letter'
    if not re.search(r'\d', password):
        return False, 'Password must contain digit'
    return True, ''


def validate_json(required_fields):
    """Decorator to validate JSON input"""
    def decorator(f):
        def wrapper(*args, **kwargs):
            if not request.is_json:
                return {'error': 'Content-Type must be application/json'}, 415
            
            data = request.get_json()
            missing = [field for field in required_fields if field not in data]
            
            if missing:
                return {'error': f'Missing fields: {", ".join(missing)}'}, 400
            
            return f(*args, **kwargs)
        return wrapper
    return decorator
