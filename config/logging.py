"""
Centralized logging configuration for Flask application
"""
import os
import logging
from logging.handlers import RotatingFileHandler


def setup_logging(app):
    """Setup logging configuration for the Flask application"""

    # Create logs directory if it doesn't exist
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    # Remove existing handlers to avoid duplicates
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)

    # Create log format
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(message)s'
    formatter = logging.Formatter(log_format)

    # File handler - rotate at 10MB, keep 5 backups
    file_handler = RotatingFileHandler(
        f'{log_dir}/app.log',
        maxBytes=10 * 1024 * 1024,  # 10MB
        backupCount=5,
        encoding='utf-8'
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    root_logger.addHandler(file_handler)

    # Console handler for development
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG if app.debug else logging.INFO)
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)

    # Set up specific loggers
    logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)
    logging.getLogger('sqlalchemy.pool').setLevel(logging.WARNING)
    logging.getLogger('werkzeug').setLevel(logging.INFO)
    logging.getLogger('flask_cors').setLevel(logging.INFO)

    # Log application startup
    app.logger.info(f"Application starting in {'DEBUG' if app.debug else 'PRODUCTION'} mode")


def get_logger(name):
    """Get a logger instance for a specific module"""
    return logging.getLogger(name)