from flask import Blueprint, request, jsonify
from service.visiteur_service import VisiteurService
from service.auth_service import admin_required

visiteur_bp = Blueprint("visiteurs", __name__, url_prefix="/visiteurs")
service = VisiteurService()


@visiteur_bp.route("/", methods=["GET"])
@admin_required
def get_all():
    return jsonify(service.get_all()), 200

@visiteur_bp.route("/full", methods=["GET"])
def get_all_full():
    return jsonify(service.get_all_full()), 200

@visiteur_bp.route("/filtrer", methods=["GET"])
@admin_required
def get_filtrer():
    search = request.args.get("search")
    departement = request.args.get("departement")
    formation_origine = request.args.get("formationOrigine")
    reorientation = request.args.get("reorientation") == "true"
    situation_particuliere = request.args.get("situationParticuliere") == "true"
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))
    visiteurs, total = service.get_filtered(
        search,
        departement,
        formation_origine,
        reorientation,
        situation_particuliere,
        page,
        limit
    )
    return jsonify({"visiteurs": visiteurs, "total": total}), 200


@visiteur_bp.route("/<visiteur_id>", methods=["GET"])
@admin_required
def get_one(visiteur_id):
    visiteur = service.get_by_id(visiteur_id)
    if not visiteur:
        return jsonify({"error": "Visiteur non trouvé"}), 404
    return jsonify(visiteur), 200


@visiteur_bp.route("/dept/<dept>", methods=["GET"])
@admin_required
def get_dept(dept):
    return jsonify(service.get_by_dept(dept)), 200


@visiteur_bp.route("/", methods=["POST"])
def create():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Corps de requete manquant"}), 400
    required = [
        "nom",
        "prenom",
        "email",
        "date_de_naissance",
        "situation_particulier",
        "formation_origine",
        "etablissement_origine",
        "adresse",
        "formation_interessee"
    ]
    missing = [f for f in required if f not in data]
    if missing:
        return jsonify({"error": f"Champs requis manquants : {missing}"}), 400
    new_id = service.create(data)
    return jsonify({"id": new_id}), 201


@visiteur_bp.route("/<visiteur_id>", methods=["PUT"])
@admin_required
def update(visiteur_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Corps de requête manquant"}), 400
    updated = service.update(visiteur_id, data)
    if not updated:
        return jsonify({"error": "Visiteur non trouvé"}), 404
    return jsonify(updated), 200


@visiteur_bp.route("/<visiteur_id>", methods=["DELETE"])
@admin_required
def delete(visiteur_id):
    success = service.delete(visiteur_id)
    if not success:
        return jsonify({"error": "Visiteur non trouvé"}), 404
    return jsonify({"message": "Visiteur supprimé"}), 200


@visiteur_bp.route("/", methods=["DELETE"])
@admin_required
def delete_visiteur():
    deleted_count = service.delete_visiteur()
    return jsonify({
        "message": "Visiteurs supprimés",
        "deleted_count": deleted_count
    }), 200
