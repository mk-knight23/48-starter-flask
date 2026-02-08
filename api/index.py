"""
Vercel Serverless Function Handler for Flask App
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app

# Create Flask app
app = create_app()

# Vercel handler
class Handler:
    def __init__(self):
        self.app = app

    def __call__(self, request, response):
        from werkzeug.wrappers import Request as WerkzeugRequest
        from werkzeug.wrappers import Response as WerkzeugResponse

        # Create WSGI request
        werkzeug_request = WerkzeugRequest(request.environ)

        # Get response from Flask
        with app.test_client() as client:
            # Forward the request to Flask test client
            method = request.method
            path = request.path
            query_string = request.query_string.decode('utf-8') if request.query_string else ''
            headers = dict(request.headers)
            data = request.body

            # Make request to Flask
            flask_response = client.open(
                path=path,
                method=method,
                query_string=query_string,
                headers=headers,
                data=data
            )

            # Copy response
            response.status_code = flask_response.status_code
            response.headers.extend(flask_response.headers)
            return flask_response.data

# Create handler instance
handler = Handler()
