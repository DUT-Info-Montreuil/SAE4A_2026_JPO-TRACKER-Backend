from extension import mongo
from bson import ObjectId

class visiteur_service:

    def get_all(self):
        users = mongo.db.utilisateurs.find()
        return [
            {
                "id": str(u["_id"]),
                "nom": u.get("nom", ""),
                "prenom": u.get("prenom", ""),
                "email": u.get("email", "")
            }
            for u in users
        ]

    def get_by_id(self, user_id):
        u = mongo.db.utilisateurs.find_one({"_id": ObjectId(user_id)})
        if not u:
            return None
        return {
            "id": str(u["_id"]),
            "nom": u.get("nom", ""),
            "prenom": u.get("prenom", ""),
            "email": u.get("email", ""),
            "bac": u.get("bac", ""),
            "departement": u.get("departement", "")
        }

    def create(self, data):
        result = mongo.db.utilisateurs.insert_one({
            "nom": data["nom"],
            "prenom": data.get("prenom", ""),
            "email": data["email"],
            "bac": data.get("bac", ""),
            "departement": data.get("departement", "")
        })
        return str(result.inserted_id)

    def delete(self, user_id):
        result = mongo.db.utilisateurs.delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count > 0
