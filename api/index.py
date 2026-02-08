"""
Vercel Serverless Function Handler
"""
import json
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        response = {
            'status': 'healthy',
            'version': 'v1',
            'platform': 'vercel',
            'message': 'Flask Starter API running on Vercel'
        }
        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        self.do_GET()
