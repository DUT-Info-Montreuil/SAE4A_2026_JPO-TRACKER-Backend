from extension import (mongo)
from bson import ObjectId

class visiteur_service:

    def get_all(self):
        users = mongo.db.utilisateurs.find()
        return

    def get_by_id(self, user_id):
        u = mongo.db.utilisateurs.find_one({"_id": ObjectId(user_id)})
        if not u:
            return None
        return

    def create(self, data):
        result = mongo.db.utilisateurs.insert_one({
            "nom": data["nom"],
            "email": data["email"]
        })
        return str(result.inserted_id)