"""
Rate limiting configuration for Flask application
"""
import os
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask import request


def get_rate_limit_key():
    """Get rate limit key with IP and user authentication"""
    try:
        from flask import request
        if hasattr(request, 'user') and request.user:
            return f"user_{request.user.id}"
        return get_remote_address()
    except RuntimeError:
        # Outside request context
        return "test"


def setup_rate_limiting(app):
    """Setup rate limiting for the application"""

    # Default limits
    default_limits = [
        "200 per day",
        "50 per hour",
        "10 per minute"
    ]

    # Production limits (stricter)
    production_limits = [
        "1000 per day",
        "200 per hour",
        "30 per minute"
    ]

    limits = production_limits if app.config.get('ENV', 'development') == 'production' else default_limits

    limiter = Limiter(
        app=app,
        key_func=get_rate_limit_key,
        default_limits=limits
    )

    return limiter


def get_rate_limit_for_endpoint(endpoint_name):
    """Get custom rate limits for specific endpoints"""
    custom_limits = {
        'api.login': ["5 per minute"],
        'api.register': ["3 per minute"],
        'api.forgot_password': ["3 per minute"],
        'api.health_check': ["1000 per minute"],
        'api.docs': ["100 per minute"]
    }

    return custom_limits.get(endpoint_name, None)