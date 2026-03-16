from db import db

def get_utilisateurs_service():
    collection = db["utilisateurs"]
    utilisateurs = collection.find({}, {"_id": 0, "nom": 1, "prenom": 1})
    return list(utilisateurs)