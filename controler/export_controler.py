from flask import Blueprint, Response, request
from service.export_service import ExportService

export_bp = Blueprint("export", __name__, url_prefix="/export")
service = ExportService()


def _get_filtres():
    return {
        "search": request.args.get("search"),
        "departement": request.args.get("departement"),
        "formation_origine": request.args.get("formationOrigine"),
        "reorientation": request.args.get("reorientation") == "true",
        "situation_particuliere": request.args.get("situationParticuliere") == "true"
    }


@export_bp.route("/visiteurs/csv", methods=["GET"])
def export_csv():
    csv_content = service.export_visiteurs_csv(**_get_filtres())
    return Response(
        csv_content,
        mimetype="text/csv; charset=utf-8",
        headers={
            "Content-Disposition": "attachment; filename=visiteurs_jpo.csv"
        }
    )


@export_bp.route("/visiteurs/emails/csv", methods=["GET"])
def export_emails_csv():
    csv_content = service.export_emails_csv(**_get_filtres())
    return Response(
        csv_content,
        mimetype="text/csv; charset=utf-8",
        headers={
            "Content-Disposition": "attachment; filename=emails_visiteurs.csv"
        }
    )