"""
Authentication Tests
"""
import pytest


class TestAuth:
    """Authentication endpoint tests"""
    
    def test_register_success(self, client):
        """Test successful registration"""
        response = client.post('/api/v1/auth/register', json={
            'username': 'newuser',
            'email': 'new@example.com',
            'password': 'NewPass123!',
            'first_name': 'New',
            'last_name': 'User'
        })
        
        assert response.status_code == 201
        data = response.get_json()
        assert data['message'] == 'User registered successfully'
        assert 'access_token' in data
        assert data['user']['username'] == 'newuser'
    
    def test_register_missing_fields(self, client):
        """Test registration with missing fields"""
        response = client.post('/api/v1/auth/register', json={
            'username': 'testuser'
        })
        
        assert response.status_code == 400
        data = response.get_json()
        assert 'error' in data
    
    def test_register_duplicate_username(self, client):
        """Test registration with duplicate username"""
        # First registration
        client.post('/api/v1/auth/register', json={
            'username': 'duplicate',
            'email': 'first@example.com',
            'password': 'Pass123!'
        })
        
        # Second registration with same username
        response = client.post('/api/v1/auth/register', json={
            'username': 'duplicate',
            'email': 'second@example.com',
            'password': 'Pass123!'
        })
        
        assert response.status_code == 400
        data = response.get_json()
        assert 'already exists' in data['error']
    
    def test_login_success(self, client):
        """Test successful login"""
        # Register first
        client.post('/api/v1/auth/register', json={
            'username': 'loginuser',
            'email': 'login@example.com',
            'password': 'LoginPass123!'
        })
        
        # Login
        response = client.post('/api/v1/auth/login', json={
            'username': 'loginuser',
            'password': 'LoginPass123!'
        })
        
        assert response.status_code == 200
        data = response.get_json()
        assert data['message'] == 'Login successful'
        assert 'access_token' in data
    
    def test_login_invalid_credentials(self, client):
        """Test login with invalid credentials"""
        response = client.post('/api/v1/auth/login', json={
            'username': 'nonexistent',
            'password': 'wrongpass'
        })
        
        assert response.status_code == 401
        data = response.get_json()
        assert 'error' in data
    
    def test_get_current_user(self, client, auth_headers):
        """Test getting current user"""
        response = client.get('/api/v1/auth/me', headers=auth_headers)
        
        assert response.status_code == 200
        data = response.get_json()
        assert 'user' in data
        assert data['user']['username'] == 'testuser'
    
    def test_unauthorized_access(self, client):
        """Test accessing protected endpoint without token"""
        response = client.get('/api/v1/auth/me')
        
        assert response.status_code == 401
