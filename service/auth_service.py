from flask import request, jsonify, current_app
from functools import wraps
from extension import mongo
import bcrypt
import jwt
from datetime import datetime, timezone, timedelta


def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization", "").replace("Bearer ", "")
        if not token:
            return jsonify({"error": "Token manquant"}), 401
        try:
            jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expire"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Token invalide"}), 401
        return f(*args, **kwargs)
    return decorated


class AuthService:
    def _get_admin(self):
        return mongo.db.admin.find_one({"role": "admin"})

    def initialiser(self):
        if not self._get_admin():
            mdp_hash = bcrypt.hashpw("admin123".encode(), bcrypt.gensalt())
            mongo.db.admin.insert_one({
                "role": "admin",
                "mot_de_passe": mdp_hash,
                "meta": {
                    "created_at": datetime.now(timezone.utc),
                    "updated_at": datetime.now(timezone.utc)
                }
            })

    def login(self, mot_de_passe):
        admin = self._get_admin()
        if not admin:
            return None
        if not bcrypt.checkpw(mot_de_passe.encode(), admin["mot_de_passe"]):
            return None
        payload = {
            "role": "admin",
            "exp": datetime.now(timezone.utc) + timedelta(hours=8)
        }
        return jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm="HS256")

    def changer_mot_de_passe(self, ancien_mot_de_passe, nouveau_mot_de_passe):
        admin = self._get_admin()
        if not admin:
            return None
        if not bcrypt.checkpw(ancien_mot_de_passe.encode(), admin["mot_de_passe"]):
            return False
        nouveau_hash = bcrypt.hashpw(nouveau_mot_de_passe.encode(), bcrypt.gensalt())
        mongo.db.admin.update_one(
            {"role": "admin"},
            {"$set": {
                "mot_de_passe": nouveau_hash,
                "meta.updated_at": datetime.now(timezone.utc)
            }}
        )
        return True