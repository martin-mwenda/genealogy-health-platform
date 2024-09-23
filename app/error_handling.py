from flask import jsonify

def handle_not_found(error):
    response = {
        'error': 'Not Found',
        'message': 'The requested resource could not be found.'
    }
    return jsonify(response), 404

def handle_internal_server_error(error):
    response = {
        'error': 'Internal Server Error',
        'message': 'An unexpected error occurred on the server.'
    }
    return jsonify(response), 500
