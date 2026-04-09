from flask import request, jsonify, current_app
from functools import wraps
from extension import mongo
import bcrypt
import jwt
import os
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

    def login(self, mot_de_passe):
        admin = current_app.config["ADMIN_PASSWORD_HASH"]
        if not admin:
            return None
        if not bcrypt.checkpw(mot_de_passe.encode(), admin.encode()):
            return None
        payload = {
            "role": "admin",
            "exp": datetime.now(timezone.utc) + timedelta(hours=8)
        }
        return jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm="HS256")

    def changer_mot_de_passe(self, ancien_mot_de_passe, nouveau_mot_de_passe):
        admin = current_app.config["ADMIN_PASSWORD_HASH"]
        if not admin:
            return None
        if not bcrypt.checkpw(ancien_mot_de_passe.encode(), admin.encode()):
            return False
        nouveau_hash = bcrypt.hashpw(nouveau_mot_de_passe.encode(), bcrypt.gensalt()).decode()
        env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
        with open(env_path, "r") as f:
            lignes = f.readlines()
        ligne_trouvee = False
        nouvelles_lignes = []
        for ligne in lignes:
            if ligne.startswith("ADMIN_PASSWORD_HASH="):
                nouvelles_lignes.append(f"ADMIN_PASSWORD_HASH={nouveau_hash}\n")
                ligne_trouvee = True
            else:
                nouvelles_lignes.append(ligne)
        if not ligne_trouvee:
            nouvelles_lignes.append(f"ADMIN_PASSWORD_HASH={nouveau_hash}\n")
        with open(env_path, "w") as f:
            f.writelines(nouvelles_lignes)
        current_app.config["ADMIN_PASSWORD_HASH"] = nouveau_hash
        return True