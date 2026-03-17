from flask import Blueprint, request, jsonify
from services.impls.AuthServiceImpl import AuthServiceImpl

auth_bp = Blueprint("auth", __name__)

auth_service = AuthServiceImpl()

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    result = auth_service.register(data)
    return jsonify(result), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    result = auth_service.login(data)
    return jsonify(result), 200