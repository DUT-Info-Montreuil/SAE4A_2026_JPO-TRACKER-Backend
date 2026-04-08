from flask import Blueprint, request, jsonify
from service.auth_service import AuthService
from service.auth_service import admin_required

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")
service = AuthService()


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Corps de requete manquant"}), 400
    mot_de_passe = data.get("mot_de_passe")
    if not mot_de_passe:
        return jsonify({"error": "Mot de passe manquant"}), 400
    token = service.login(mot_de_passe)
    if not token:
        return jsonify({"error": "Mot de passe incorrect"}), 401
    return jsonify({"token": token}), 200


@auth_bp.route("/changer-mot-de-passe", methods=["PUT"])
@admin_required
def changer_mot_de_passe():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Corps de requete manquant"}), 400
    ancien = data.get("ancien_mot_de_passe")
    nouveau = data.get("nouveau_mot_de_passe")
    if not ancien or not nouveau:
        return jsonify({"error": "Champs manquants"}), 400
    resultat = service.changer_mot_de_passe(ancien, nouveau)
    if resultat is False:
        return jsonify({"error": "Ancien mot de passe incorrect"}), 401
    if resultat is None:
        return jsonify({"error": "Admin non trouve"}), 404
    return jsonify({"message": "Mot de passe mis a jour"}), 200