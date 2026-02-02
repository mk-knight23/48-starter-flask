"""
API Endpoint Tests
"""
import pytest


class TestUsersAPI:
    """Users API tests"""
    
    def test_list_users(self, client):
        """Test listing all users"""
        response = client.get('/api/v1/users')
        
        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, list)
    
    def test_get_user(self, client):
        """Test getting specific user"""
        # Create user first
        client.post('/api/v1/auth/register', json={
            'username': 'getuser',
            'email': 'get@example.com',
            'password': 'GetPass123!'
        })
        
        response = client.get('/api/v1/users/1')
        
        assert response.status_code == 200
        data = response.get_json()
        assert data['username'] == 'getuser'
    
    def test_update_user_unauthorized(self, client):
        """Test updating user without authentication"""
        response = client.put('/api/v1/users/1', json={
            'first_name': 'Updated'
        })
        
        assert response.status_code == 401
    
    def test_update_user_success(self, client, auth_headers):
        """Test successful user update"""
        response = client.put('/api/v1/users/1', 
                            headers=auth_headers,
                            json={
                                'first_name': 'Updated',
                                'last_name': 'Name'
                            })
        
        assert response.status_code == 200
        data = response.get_json()
        assert data['first_name'] == 'Updated'


class TestPostsAPI:
    """Posts API tests"""
    
    def test_list_posts(self, client):
        """Test listing all posts"""
        response = client.get('/api/v1/posts')
        
        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, list)
    
    def test_create_post_unauthorized(self, client):
        """Test creating post without authentication"""
        response = client.post('/api/v1/posts', json={
            'title': 'Test Post',
            'content': 'Test content'
        })
        
        assert response.status_code == 401
    
    def test_create_post_success(self, client, auth_headers):
        """Test successful post creation"""
        response = client.post('/api/v1/posts',
                             headers=auth_headers,
                             json={
                                 'title': 'Test Post',
                                 'content': 'This is test content',
                                 'summary': 'Test summary',
                                 'published': True
                             })
        
        assert response.status_code == 201
        data = response.get_json()
        assert data['title'] == 'Test Post'
    
    def test_get_post(self, client, auth_headers):
        """Test getting specific post"""
        # Create post first
        client.post('/api/v1/posts',
                   headers=auth_headers,
                   json={
                       'title': 'Get Test',
                       'content': 'Content'
                   })
        
        response = client.get('/api/v1/posts/1')
        
        assert response.status_code == 200
        data = response.get_json()
        assert data['title'] == 'Get Test'
    
    def test_update_post_unauthorized(self, client):
        """Test updating post without authentication"""
        response = client.put('/api/v1/posts/1', json={
            'title': 'Updated'
        })
        
        assert response.status_code == 401
    
    def test_delete_post_unauthorized(self, client):
        """Test deleting post without authentication"""
        response = client.delete('/api/v1/posts/1')
        
        assert response.status_code == 401


class TestHealth:
    """Health check tests"""
    
    def test_health_check(self, client):
        """Test health endpoint"""
        response = client.get('/health')
        
        assert response.status_code == 200
        data = response.get_json()
        assert data['status'] == 'healthy'
        assert 'version' in data
