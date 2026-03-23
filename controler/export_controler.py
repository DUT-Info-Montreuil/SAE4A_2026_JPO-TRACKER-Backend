from flask import Blueprint, Response
from service.export_service import ExportService

export_bp = Blueprint("export", __name__, url_prefix="/export")
service   = ExportService()


@export_bp.route("/visiteurs/csv", methods=["GET"])
def export_csv():
    csv_content = service.export_visiteurs_csv()
    return Response(
        csv_content,
        mimetype="text/csv; charset=utf-8",
        headers={
            "Content-Disposition": "attachment; filename=visiteurs_jpo.csv"
        }
    )