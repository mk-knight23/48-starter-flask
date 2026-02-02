"""
Pytest Configuration and Fixtures
"""
import pytest
from app import create_app
from app.models import db
from app.models.user import User


@pytest.fixture
def app():
    """Create application for testing"""
    app = create_app('testing')
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture
def client(app):
    """Create test client"""
    return app.test_client()


@pytest.fixture
def runner(app):
    """Create test CLI runner"""
    return app.test_cli_runner()


@pytest.fixture
def auth_headers(client):
    """Create authenticated user and return headers"""
    # Register user
    client.post('/api/v1/auth/register', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'TestPass123!'
    })
    
    # Login
    response = client.post('/api/v1/auth/login', json={
        'username': 'testuser',
        'password': 'TestPass123!'
    })
    
    token = response.json['access_token']
    return {'Authorization': f'Bearer {token}'}


@pytest.fixture
def admin_headers(client):
    """Create admin user and return headers"""
    # Create admin
    client.post('/api/v1/auth/register', json={
        'username': 'admin',
        'email': 'admin@example.com',
        'password': 'AdminPass123!'
    })
    
    # Make admin
    with client.application.app_context():
        user = User.query.filter_by(username='admin').first()
        user.is_admin = True
        user.save()
    
    # Login
    response = client.post('/api/v1/auth/login', json={
        'username': 'admin',
        'password': 'AdminPass123!'
    })
    
    token = response.json['access_token']
    return {'Authorization': f'Bearer {token}'}
