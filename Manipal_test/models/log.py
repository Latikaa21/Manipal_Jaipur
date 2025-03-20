from flask import Blueprint, request, jsonify
from app.database import mongo

logs_bp = Blueprint("logs", __name__)

@logs_bp.route("/logs/store", methods=["POST"])
def store_logs():
    data = request.json
    mongo.db.logs.insert_one(data)
    return jsonify({"message": "Log stored successfully"}), 201

@logs_bp.route("/logs", methods=["GET"])
def get_logs():
    logs = list(mongo.db.logs.find({}, {"_id": 0}))
    return jsonify(logs)
