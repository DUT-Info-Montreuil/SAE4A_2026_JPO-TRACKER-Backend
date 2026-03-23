import csv
import io
from extension import mongo


class ExportService:

    def export_visiteurs_csv(self) -> str:
        visiteurs = mongo.db.visiteurs.find()

        output = io.StringIO()
        writer = csv.writer(output)

        # En-têtes
        writer.writerow([
            "nom", "prenom", "email", "telephone",
            "date_de_naissance", "formation_interessee",
            "type_evenement", "date_visite",
            "etablissement", "ville",
            "immersion_souhaitee", "immersion_statut",
            "consentement_collecte", "consentement_contact",
            "source_saisie", "statut", "annee_campagne", "created_at"
        ])

        for v in visiteurs:
            evenement  = v.get("evenement", {})
            immersion  = v.get("immersion", {})
            rgpd       = v.get("rgpd", {})
            meta       = v.get("meta", {})
            etab       = v.get("établisement_d'origine", {})
            adresse    = v.get("adresse", {})

            date_naissance = v.get("date_de_naissance")
            date_visite    = evenement.get("date_visite")
            created_at     = meta.get("created_at")

            writer.writerow([
                v.get("nom", ""),
                v.get("prenom", ""),
                v.get("email", ""),
                v.get("telephone", ""),
                date_naissance.strftime("%Y-%m-%d") if date_naissance else "",
                v.get("formation_interessee", ""),
                evenement.get("type", ""),
                date_visite.strftime("%Y-%m-%d %H:%M") if date_visite else "",
                etab.get("nom", ""),
                adresse.get("ville", ""),
                immersion.get("souhaite_participer", ""),
                immersion.get("statut", ""),
                rgpd.get("consentement_collecte", ""),
                rgpd.get("consentement_contact", ""),
                meta.get("source_saisie", ""),
                meta.get("statut", ""),
                meta.get("annee_campagne", ""),
                created_at.strftime("%Y-%m-%d %H:%M") if created_at else "",
            ])

        return output.getvalue()