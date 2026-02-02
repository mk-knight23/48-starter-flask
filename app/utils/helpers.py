"""
Helper Functions
"""
from flask import jsonify, make_response


def success_response(data=None, message=None, status=200):
    """Create standardized success response"""
    response = {'success': True}
    
    if data is not None:
        response['data'] = data
    if message:
        response['message'] = message
    
    return make_response(jsonify(response), status)


def error_response(message, status=400, errors=None):
    """Create standardized error response"""
    response = {
        'success': False,
        'error': message
    }
    
    if errors:
        response['errors'] = errors
    
    return make_response(jsonify(response), status)


def paginate_response(query, page=1, per_page=10):
    """Paginate query results"""
    pagination = query.paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )
    
    return {
        'items': [item.to_dict() for item in pagination.items],
        'total': pagination.total,
        'pages': pagination.pages,
        'current_page': page,
        'per_page': per_page,
        'has_next': pagination.has_next,
        'has_prev': pagination.has_prev
    }
