from extension import mongo
from bson import ObjectId
from datetime import datetime, timezone
from dtos.visiteur_short_dto import VisiteurShortDTO
from dtos.visiteur_long_dto import VisiteurLongDTO


def _map_short(u):
    return VisiteurShortDTO(
        id=str(u["_id"]),
        nom=u.get("nom", ""),
        prenom=u.get("prenom", ""),
        email=u.get("email", ""),
        formation_interessee=u.get("formation_interessee", ""),
        evenement=u.get("evenement", {}),
        statut=u.get("meta", {}).get("statut", "")
    ).to_dict()


def _map_long(u):
    return VisiteurLongDTO({
        "id": str(u["_id"]),
        "nom": u.get("nom", ""),
        "prenom": u.get("prenom", ""),
        "email": u.get("email", ""),
        "telephone": u.get("telephone", ""),
        "date_de_naissance": u.get("date_de_naissance"),
        "formation_origine": u.get("formation_origine", {}),
        "etablissement_origine": u.get("établisement_d'origine", {}),
        "adresse": u.get("adresse", {}),
        "formation_interessee": u.get("formation_interessee", ""),
        "evenement": u.get("evenement", {}),
        "immersion": u.get("immersion", {}),
        "rgpd": u.get("rgpd", {}),
        "meta": u.get("meta", {})
    }).to_dict()


class visiteur_service:

    def get_all(self):
        visiteurs = mongo.db.visiteurs.find()
        return [_map_short(u) for u in visiteurs]

    def get_by_id(self, visiteur_id):
        u = mongo.db.visiteurs.find_one({"_id": ObjectId(visiteur_id)})
        if not u:
            return None
        return _map_long(u)

    def create(self, data):
        now = datetime.now(timezone.utc)
        document = {
            "nom": data["nom"],
            "prenom": data["prenom"],
            "email": data["email"],
            "telephone": data.get("telephone", ""),
            "date_de_naissance": data.get("date_de_naissance"),
            "formation_origine": data.get("formation_origine", {}),
            "établisement_d'origine": data.get("etablissement_origine", {}),
            "adresse": data.get("adresse", {}),
            "formation_interessee": data.get("formation_interessee", ""),
            "evenement": data.get("evenement", {}),
            "immersion": data.get("immersion", {
                "souhaite_participer": False,
                "statut": "non_demande"
            }),
            "rgpd": data.get("rgpd", {
                "information_affichee": False,
                "consentement_collecte": False,
                "consentement_contact": False,
                "date_consentement": now
            }),
            "meta": {
                "source_saisie": data.get("meta", {}).get("source_saisie", ""),
                "annee_campagne": data.get("meta", {}).get("annee_campagne", now.year),
                "statut": "actif",
                "created_at": now,
                "updated_at": now
            }
        }
        result = mongo.db.visiteurs.insert_one(document)
        return str(result.inserted_id)

    def update(self, visiteur_id, data):
        data["meta.updated_at"] = datetime.now(timezone.utc)
        mongo.db.visiteurs.update_one(
            {"_id": ObjectId(visiteur_id)},
            {"$set": data}
        )
        return self.get_by_id(visiteur_id)

    def delete(self, visiteur_id):
        result = mongo.db.visiteurs.delete_one({"_id": ObjectId(visiteur_id)})
        return result.deleted_count > 0
