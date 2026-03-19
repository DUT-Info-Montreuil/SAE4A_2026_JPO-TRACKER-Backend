from flask import Blueprint, request, jsonify
from service.visiteur_service import visiteur_service

visiteur_bp = Blueprint("visiteurs", __name__, url_prefix="/visiteurs")
service = visiteur_service()


@visiteur_bp.route("/", methods=["GET"])
def get_all():
    """GET /visiteurs/ - Liste résumée de tous les visiteurs"""
    return jsonify(service.get_all()), 200


@visiteur_bp.route("/<visiteur_id>", methods=["GET"])
def get_one(visiteur_id):
    """GET /visiteurs/<id> - Détail complet d'un visiteur"""
    visiteur = service.get_by_id(visiteur_id)
    if not visiteur:
        return jsonify({"error": "Visiteur non trouvé"}), 404
    return jsonify(visiteur), 200


@visiteur_bp.route("/", methods=["POST"])
def create():
    """POST /visiteurs/ - Créer un nouveau visiteur"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Corps de requête manquant"}), 400
    required = ["nom", "prenom", "email"]
    missing = [f for f in required if f not in data]
    if missing:
        return jsonify({"error": f"Champs requis manquants : {missing}"}), 400
    new_id = service.create(data)
    return jsonify({"id": new_id}), 201


@visiteur_bp.route("/<visiteur_id>", methods=["PUT"])
def update(visiteur_id):
    """PUT /visiteurs/<id> - Mettre à jour un visiteur"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Corps de requête manquant"}), 400
    updated = service.update(visiteur_id, data)
    if not updated:
        return jsonify({"error": "Visiteur non trouvé"}), 404
    return jsonify(updated), 200


@visiteur_bp.route("/<visiteur_id>", methods=["DELETE"])
def delete(visiteur_id):
    """DELETE /visiteurs/<id> - Supprimer un visiteur"""
    success = service.delete(visiteur_id)
    if not success:
        return jsonify({"error": "Visiteur non trouvé"}), 404
    return jsonify({"message": "Visiteur supprimé"}), 200
