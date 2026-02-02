"""
Main Blueprint - Serve Frontend and Basic Routes
"""
from flask import Blueprint, jsonify, render_template

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """Serve the React application"""
    return jsonify({
        'message': 'Flask Starter API',
        'version': '1.0.0',
        'docs': '/api/v1/docs'
    })


@main_bp.route('/api')
def api_info():
    """API information"""
    return jsonify({
        'name': 'Flask Starter API',
        'version': '1.0.0',
        'endpoints': {
            'docs': '/api/v1/docs',
            'health': '/health',
            'auth': '/api/v1/auth',
            'api': '/api/v1'
        }
    })
