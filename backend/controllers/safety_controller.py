from flask import jsonify
from backend.services.safety_service import calculate_safety

def get_safety_score(data):

    result = calculate_safety(data)

    return jsonify(result)