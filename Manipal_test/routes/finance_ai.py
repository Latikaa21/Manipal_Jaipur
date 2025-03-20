from flask import Blueprint, request, jsonify
from app.finance_ai.model import process_finance_query

finance_bp = Blueprint("finance", __name__)

@finance_bp.route("/finance/query", methods=["POST"])
def finance_query():
    data = request.json
    response = process_finance_query(data["query"])
    return jsonify({"response": response})
