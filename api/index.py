"""
Vercel Serverless Function Handler for Flask App
"""
import sys
import os
import json

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Simple health check handler for Vercel
def handler(request, response):
    """Simple handler for Vercel serverless functions"""
    response.status_code = 200
    response.headers['Content-Type'] = 'application/json'
    return json.dumps({
        'status': 'healthy',
        'version': 'v1',
        'platform': 'vercel',
        'message': 'Flask Starter API running on Vercel'
    })
