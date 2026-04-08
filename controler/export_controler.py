from flask import Blueprint, Response, request
from service.export_service import ExportService

export_bp = Blueprint("export", __name__, url_prefix="/export")
service   = ExportService()


@export_bp.route("/visiteurs/csv", methods=["GET"])
def export_csv():
    search = request.args.get("search")
    departement = request.args.get("departement")
    formation_origine = request.args.get("formationOrigine")
    reorientation = request.args.get("reorientation") == "true"
    situation_particuliere = request.args.get("situationParticuliere") == "true"

    csv_content = service.export_visiteurs_csv(
        search,
        departement,
        formation_origine,
        reorientation,
        situation_particuliere
    )
    return Response(
        csv_content,
        mimetype="text/csv; charset=utf-8",
        headers={
            "Content-Disposition": "attachment; filename=visiteurs_jpo.csv"
        }
    )