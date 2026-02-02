"""
Database Models
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .base import TimestampMixin

__all__ = ['db', 'User', 'TimestampMixin']
