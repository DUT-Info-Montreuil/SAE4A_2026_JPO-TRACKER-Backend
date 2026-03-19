from flask import Blueprint, request, jsonify
from service.visiteur_service import visiteur_service

user_bp = Blueprint("users", __name__, url_prefix="/users")
user_service = visiteur_service()

@user_bp.route("/", methods=["GET"])
def get_all():
    return jsonify(user_service.get_all()), 200

@user_bp.route("/<user_id>", methods=["GET"])
def get_one(user_id):
    user = user_service.get_by_id(user_id)
    if not user:
        return jsonify({"error": "Utilisateur non trouvé"}), 404
    return jsonify(user), 200

@user_bp.route("/", methods=["POST"])
def create():
    data = request.get_json()
    new_id = user_service.create(data)
    return jsonify({"id": new_id}), 201