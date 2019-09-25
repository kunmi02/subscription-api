from flask import jsonify
from requests.status_codes import codes


HTTP_CODES = codes


def _make_api_response(response_data, http_code, meta=None):

    if meta is not None:
        response_data.update(meta=meta)

    return jsonify(response_data), http_code


def make_failure_response(http_code, message, meta=None):

    response_data = {
        'status': 'FAILURE',
        'error': {
            'code': http_code,
            'message': message
        }
    }

    return _make_api_response(response_data, http_code, meta)


def make_success_response(response_data, http_code=200, meta=None):

    response_data = {
        'status': 'SUCCESS',
        'code': http_code,
        'data': response_data
    }

    return _make_api_response(response_data, http_code, meta)


def make_created_response(response_data, meta=None):

    return make_success_response(response_data, HTTP_CODES.created, meta)


def make_deleted_response():
    return '', HTTP_CODES.no_content

