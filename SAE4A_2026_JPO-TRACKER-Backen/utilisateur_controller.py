from flask import Blueprint, jsonify
from utilisateur_service import get_utilisateurs_service

utilisateur_bp = Blueprint("utilisateur_bp", __name__)

@utilisateur_bp.route("/utilisateurs", methods=["GET"])
def get_utilisateurs_controller():
    utilisateurs = get_utilisateurs_service()
    return jsonify(utilisateurs)