from flask import Blueprint, request, jsonify
from .services.open_ai import *
main = Blueprint('main', __name__)

@main.route('/query', methods=['POST'])
def handle_query():
    data = request.get_json()
    query = data.get('query')
    print(query)

    if not query:
        return AI(" give an small error 'unable to process query'")

    response = AI(query)

    return jsonify(response)
