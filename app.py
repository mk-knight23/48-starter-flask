"""
Flask Starter Entry Point
"""
import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    host = os.getenv('HOST', '0.0.0.0')
    debug = os.getenv('FLASK_DEBUG', '1') == '1'
    app.run(host=host, port=port, debug=debug)
