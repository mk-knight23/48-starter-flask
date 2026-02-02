"""
Base Models with Mixins
"""
from datetime import datetime
from app.models import db


class TimestampMixin:
    """Adds created_at and updated_at timestamps"""
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )


class BaseModel(TimestampMixin):
    """Base model with common fields"""
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    is_active = db.Column(db.Boolean, default=True, nullable=False)

    def save(self):
        """Save to database"""
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        """Delete from database"""
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        """Convert model to dictionary"""
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
        }
