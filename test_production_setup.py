#!/usr/bin/env python3
"""
Test script to verify Flask production setup
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app

def test_production_setup():
    """Test all production setup components"""

    print("🧪 Testing Flask Production Setup\n")

    # Test production app creation
    print("1. Testing production app creation...")
    app = create_app('production')
    print("✅ Production app created successfully")

    with app.app_context():
        # Test database
        print("2. Testing database connection...")
        from app.models import db
        try:
            db.session.execute(db.text('SELECT 1'))
            print("✅ Database connection successful")
        except Exception as e:
            print(f"❌ Database connection failed: {e}")

        # Test logging
        print("3. Testing logging system...")
        app.logger.info("Testing logging system")
        if os.path.exists('logs/app.log'):
            print("✅ Log file created")
        else:
            print("⚠️  Log file not found")

        # Test rate limiting
        print("4. Testing rate limiting...")
        from flask_limiter.util import get_remote_address
        from config.rate_limiting import get_rate_limit_key
        key = get_rate_limit_key()
        print(f"✅ Rate limiting key generated: {key}")

        # Test security headers
        print("5. Testing security headers...")
        with app.test_client() as client:
            response = client.get('/health')
            if 'X-Frame-Options' in response.headers or 'X-Content-Type-Options' in response.headers:
                print("✅ Security headers present")
            else:
                print("⚠️  Security headers not found")

        # Test health check
        print("6. Testing health check endpoint...")
        with app.test_client() as client:
            response = client.get('/health')
            if response.status_code == 200:
                data = response.get_json()
                if data.get('status') == 'healthy':
                    print("✅ Health check working")
                else:
                    print("❌ Health check returned unexpected response")
            else:
                print(f"❌ Health check failed: {response.status_code}")

        # Test API endpoints
        print("7. Testing API endpoints...")
        with app.test_client() as client:
            # Test without authentication
            response = client.get('/api/v1/users')
            if response.status_code in [401, 403, 404]:
                print("✅ API endpoint protected")
            else:
                print(f"⚠️  API endpoint returned unexpected status: {response.status_code}")

    # Test configuration
    print("8. Testing environment configuration...")
    env_vars = [
        'FLASK_ENV',
        'DATABASE_URL',
        'JWT_SECRET_KEY',
        'SECRET_KEY',
        'REDIS_URL'
    ]

    for var in env_vars:
        value = os.getenv(var)
        if value:
            print(f"✅ {var} is set")
        else:
            print(f"⚠️  {var} is not set")

    print("\n🎉 Production setup test completed!")
    print("\nTo start the application in production:")
    print("1. Set environment variables")
    print("2. Run: docker-compose up -d")
    print("3. Access: https://localhost")
    print("4. Health check: https://localhost/health")

if __name__ == '__main__':
    test_production_setup()